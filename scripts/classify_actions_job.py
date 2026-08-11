#!/usr/bin/env python3
"""Classify GitHub Actions job evidence without confusing runner admission with code failure."""

from __future__ import annotations

import json
import sys
from typing import Any


VALID_CONCLUSIONS = {
    "success",
    "failure",
    "cancelled",
    "skipped",
    "neutral",
    "timed_out",
    "action_required",
    "stale",
    "startup_failure",
}


def classify_job(job: Any) -> dict[str, Any]:
    if not isinstance(job, dict):
        raise ValueError("job evidence must be a JSON object")

    conclusion = job.get("conclusion")
    if conclusion not in VALID_CONCLUSIONS:
        raise ValueError(f"unsupported or missing conclusion: {conclusion!r}")

    steps = job.get("steps")
    if isinstance(steps, list) and any(not isinstance(step, dict) for step in steps):
        raise ValueError("every step must be an object")
    if conclusion == "success":
        if not isinstance(steps, list) or not steps:
            raise ValueError("successful jobs must contain executed step evidence")
        classification = "success"
    elif steps is None or steps == []:
        classification = "runner_admission_failure"
    else:
        if not isinstance(steps, list):
            raise ValueError("steps must be a list, null, or omitted")
        failed_steps = [
            step.get("name", "<unnamed>")
            for step in steps
            if step.get("conclusion") in {"failure", "timed_out", "cancelled"}
        ]
        classification = "workflow_failure" if failed_steps else "non_test_terminal"

    executed_steps = 0 if not isinstance(steps, list) else sum(
        1 for step in steps if step.get("conclusion") not in {None, "skipped"}
    )

    return {
        "schema": "meta-agents.actions-job-evidence.v1",
        "jobId": job.get("id"),
        "name": job.get("name"),
        "conclusion": conclusion,
        "executedSteps": executed_steps,
        "classification": classification,
        "codeFailureProven": classification == "workflow_failure",
    }


def main() -> int:
    try:
        payload = json.load(sys.stdin)
        result = classify_job(payload)
    except (ValueError, json.JSONDecodeError, TypeError) as error:
        print(f"classify-actions-job: {error}", file=sys.stderr)
        return 2

    json.dump(result, sys.stdout, sort_keys=True, separators=(",", ":"))
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
