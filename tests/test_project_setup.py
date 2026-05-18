import os
import shutil
import subprocess
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def test_python_command_points_to_virtual_environment():
    virtual_env = os.environ.get("VIRTUAL_ENV")

    assert virtual_env, "Run tests from the project virtual environment."

    expected_python = Path(virtual_env).resolve()
    python_on_path = shutil.which("python")

    assert python_on_path, "python must be available on PATH."
    assert expected_python in Path(python_on_path).resolve().parents
    assert expected_python in Path(sys.executable).resolve().parents


def test_git_status_runs_without_errors():
    result = subprocess.run(
        ["git", "status", "--short"],
        cwd=PROJECT_ROOT,
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, result.stderr
