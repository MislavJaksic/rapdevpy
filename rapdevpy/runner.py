"""
    rapdevpy.py
    ------------------

    This is a library. It does not have a Runner.

    :copyrgiht: 2019 MislavJaksic
    :license: MIT License
"""
import sys

from rapdevpy import pytest_gen


def main(args):
    """main() will be run if you run this script directly"""
    test_file_path = "test_test.py"
    program_file_path = "E:/GreatRepository/Publishing/GitHubRepositories/Selenium-Tutorial/selenium_tutorial/helper/eve_wiki/eve_wiki_helper.py"
    pytest_gen.generate_test_file_from_file(test_file_path, program_file_path)

def run():
    """Entry point for the runnable script."""
    sys.exit(main(sys.argv[1:]))


if __name__ == "__main__":
    """main calls run()."""
    run()
