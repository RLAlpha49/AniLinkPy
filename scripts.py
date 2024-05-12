"""
    This script contains the functions that are used to build and clean the project.
"""

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


def clean():
    """
    This function cleans the project using isort, black, flake8, pylint, and mypy.
    """
    print("Running isort...")
    result = subprocess.run(
        ["poetry", "run", "isort", "AniLinkPy"],
        capture_output=True,
        text=True,
    )
    if result.stdout:
        print(result.stdout)
    else:
        print("isort found no problems.")

    print("\nRunning black...")
    result = subprocess.run(["poetry", "run", "black", "AniLinkPy"], check=True)
    if result.stdout:
        print(result.stdout)
    else:
        print("black found no problems.")

    try:
        print("\nRunning flake8...")
        result = subprocess.run(["poetry", "run", "flake8", "AniLinkPy"], check=True)
        if result.stdout:
            print(result.stdout)
        else:
            print("flake8 found no problems.")
    except subprocess.CalledProcessError as e:
        print(
            f"flake8 exited with status {e.returncode}. There might be style issues."
        )

    try:
        print("\nRunning pylint...")
        result = subprocess.run(["poetry", "run", "pylint", "AniLinkPy"], check=True)
        if result.stdout:
            print(result.stdout)
        else:
            print("pylint found no problems.")
    except subprocess.CalledProcessError as e:
        print(
            f"pylint exited with status {e.returncode}. There might be linting errors."
        )

    try:
        print("\nRunning mypy...")
        result = subprocess.run(
            [
                "poetry",
                "run",
                "mypy",
                "--install-types",
                "--non-interactive",
                "AniLinkPy",
            ],
            check=True,
        )
        if result.stdout:
            print(result.stdout)
        else:
            print("mypy found no problems.")
    except subprocess.CalledProcessError as e:
        print(
            f"mypy exited with status {e.returncode}. There might be type inconsistencies."
        )
