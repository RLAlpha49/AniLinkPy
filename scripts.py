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
    This function cleans the project using isort, black, and pylint.
    """
    result = subprocess.run(["python", "-m", "isort", "--check", "--diff", "AniLinkPy"], capture_output=True, text=True)
    if result.stdout:
        print(result.stdout)
    else:
        print("isort found no problems.")

    subprocess.run(["python", "-m", "black", "AniLinkPy"], check=True)
    try:
        subprocess.run(["python", "-m", "pylint", "AniLinkPy"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"pylint exited with status {e.returncode}. There might be linting errors.")
