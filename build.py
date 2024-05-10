"""
This module contains a script to clean the dist directory and build the project using poetry.
"""

import os
import shutil
import subprocess


def main():
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


if __name__ == "__main__":
    main()
