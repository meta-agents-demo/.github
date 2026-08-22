import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ValidateBaselineTests(unittest.TestCase):
    def run_validator(self, root: Path) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(root / 'scripts/validate_baseline.py'), str(root)],
            text=True,
            capture_output=True,
            check=False,
        )

    def test_current_repository_passes(self) -> None:
        result = self.run_validator(ROOT)
        self.assertEqual(result.returncode, 0, result.stderr or result.stdout)

    def test_every_checkout_must_disable_credential_persistence(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            candidate = Path(temporary_directory) / 'repository'
            shutil.copytree(
                ROOT,
                candidate,
                ignore=shutil.ignore_patterns('.git', '__pycache__'),
            )
            workflow = candidate / '.github/workflows/credential-regression.yml'
            workflow.write_text(
                '''name: credential regression
on: pull_request
permissions:
  contents: read
jobs:
  verify:
    runs-on: ubuntu-latest
    timeout-minutes: 5
    steps:
      - uses: actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1
        with:
          persist-credentials: false
      - uses: actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1
''',
                encoding='utf-8',
            )

            result = self.run_validator(candidate)

            self.assertNotEqual(result.returncode, 0)
            self.assertIn(
                'checkout credentials persist in .github/workflows/credential-regression.yml:13',
                result.stderr,
            )


if __name__ == '__main__':
    unittest.main()
