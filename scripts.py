"""
This script contains the functions that are used to build and clean the project.
"""

import argparse
import os
import shutil
import subprocess
import sys


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


def run_command(command, capture_output=True, text=True, check=False):
    """
    This function runs a command and returns the result.
    :param command:
    :param capture_output:
    :param text:
    :param check:
    :return result:
    """
    result = subprocess.run(
        command,
        capture_output=capture_output,
        text=text,
        check=check,
    )
    if result.returncode != 0:
        print(f"{command[2]} exited with status {result.returncode}.")
        if result.stderr:
            print(f"{result.stderr}")
        return result
    return result


def run_and_handle_command(command, auto_fix):
    """
    This function runs a command and handles the result.
    :param command:
    :param auto_fix:
    :return result:
    """
    if not auto_fix:
        if "check" in command:
            command.append("--fix")
        else:
            command.append("--check")
    result = run_command(command)
    if result and result.stdout:
        print(result.stdout)
    if result and result.returncode != 0:
        return result
    return None


def clean():
    """
    This function cleans a Python project. It runs ruff and mypy.
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

    errors = []

    print("Running ruff...")
    error = run_and_handle_command(["poetry", "run", "ruff", "check", path], auto_fix)
    if error:
        errors.append(error)
    error = run_and_handle_command(["poetry", "run", "ruff", "format", path], auto_fix)
    if error:
        errors.append(error)

    print("\nRunning mypy...")
    error = run_and_handle_command(
        [
            "poetry",
            "run",
            "mypy",
            "--install-types",
            "--non-interactive",
            path,
        ],
        auto_fix,
    )
    if error:
        errors.append(error)

    if errors:
        print("\nErrors occurred during the cleaning process:")
        for error in errors:
            print(
                f"Command '{' '.join(error.args)}' returned non-zero exit status {error.returncode}."
            )
        sys.exit(errors[0].returncode)
