from typing import Tuple, List
import re


def generate_test_file_from_file(test_file_path: str, program_file_path: str):
    functions = get_functions(program_file_path)
    create_function_test_file(functions, test_file_path)


def get_functions(file_path: str) -> List[Tuple[str, str]]:
    functions = []
    with open(file_path, "r") as file:
        for line in file:
            match = re.search("def (.*)\((.*)\):", line)
            if match:
                functions.append((match.group(1), match.group(2)))
    return functions


def create_function_test_file(functions: List[Tuple[str, str]], file_path: str):
    with open(file_path, "w") as file:
        file.write("# Auto-generated pytest file\n")
        for function in functions:
            file.write("\n")
            class_name = "".join([x.capitalize() for x in function[0].split("_")])
            file.write("class Test{}:\n".format(class_name))
            file.write("    def test_{}(self):\n".format(function[0]))
            file.write("        fail()\n")