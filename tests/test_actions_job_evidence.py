import unittest

from scripts.classify_actions_job import classify_job


class ActionsJobEvidenceTests(unittest.TestCase):
    def test_zero_step_failure_is_runner_admission_not_code_failure(self) -> None:
        result = classify_job(
            {"id": 1, "name": "private-ci", "conclusion": "failure", "steps": None}
        )
        self.assertEqual(result["classification"], "runner_admission_failure")
        self.assertEqual(result["executedSteps"], 0)
        self.assertFalse(result["codeFailureProven"])

    def test_executed_failure_is_a_workflow_failure(self) -> None:
        result = classify_job(
            {
                "id": 2,
                "name": "ci",
                "conclusion": "failure",
                "steps": [
                    {"name": "Set up job", "conclusion": "success"},
                    {"name": "cargo test", "conclusion": "failure"},
                ],
            }
        )
        self.assertEqual(result["classification"], "workflow_failure")
        self.assertEqual(result["executedSteps"], 2)
        self.assertTrue(result["codeFailureProven"])

    def test_success_requires_real_step_evidence(self) -> None:
        with self.assertRaises(ValueError):
            classify_job({"id": 3, "name": "ci", "conclusion": "success", "steps": []})

        result = classify_job(
            {
                "id": 4,
                "name": "ci",
                "conclusion": "success",
                "steps": [{"name": "tests", "conclusion": "success"}],
            }
        )
        self.assertEqual(result["classification"], "success")
        self.assertFalse(result["codeFailureProven"])


if __name__ == "__main__":
    unittest.main()
