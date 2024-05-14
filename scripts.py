"""
This script contains the functions that are used to build and clean the project.
"""

import argparse
import os
import shutil
import subprocess


def build():
    """
    This function checks if the dist directory exists and deletes it.
    Then, it runs the 'poetry build' command.
    """
    try:
        if os.path.exists("dist/"):
            shutil.rmtree("dist/")
        subprocess.run(["poetry", "build"], check=True)
    except (FileNotFoundError, subprocess.CalledProcessError) as e:
        print(f"An error occurred: {e}")


def run_command(command, check=True, capture_output=True, text=True):
    """
    This function runs a command with subprocess. Run and returns the result.
    """
    try:
        result = subprocess.run(
            command,
            capture_output=capture_output,
            text=text,
            check=check,
        )
        return result
    except subprocess.CalledProcessError as e:
        print(f"{command[2]} exited with status {e.returncode}. There might be issues.")
        return None


def clean(auto_fix=True):
    """
    This function cleans the project using isort, black, flake8, pylint, and mypy.
    If auto_fix is True, isort and black will automatically fix problems.
    """
    parser = argparse.ArgumentParser(description="Clean a Python project.")
    parser.add_argument(
        "path", help="The path of the project to clean.", default="AniLinkPy", nargs="?"
    )
    parser.add_argument(
        "--no-fix", help="Do not automatically fix problems.", action="store_true"
    )
    args = parser.parse_args()

    path = args.path
    auto_fix = not args.no_fix

    print("Running isort...")
    isort_command = ["poetry", "run", "isort", path]
    if not auto_fix:
        isort_command.append("--check")
    result = run_command(isort_command)
    if result and result.stdout:
        print(result.stdout)
    else:
        print("isort found no problems.")

    print("\nRunning black...")
    black_command = ["poetry", "run", "black", path]
    if not auto_fix:
        black_command.append("--check")
    result = run_command(black_command)
    if result and result.stdout:
        print(result.stdout)
    else:
        print("black found no problems.")

    print("\nRunning flake8...")
    result = run_command(["poetry", "run", "flake8", path])
    if result and result.stdout:
        print(result.stdout)
    else:
        print("flake8 found no problems.")

    print("\nRunning pylint...")
    result = run_command(["poetry", "run", "pylint", path])
    if result and result.stdout:
        print(result.stdout)
    else:
        print("pylint found no problems.")

    print("\nRunning mypy...")
    result = run_command(
        [
            "poetry",
            "run",
            "mypy",
            "--install-types",
            "--non-interactive",
            path,
        ]
    )
    if result and result.stdout:
        print(result.stdout)
    else:
        print("mypy found no problems.")
