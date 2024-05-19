import os
import logging
from typing import Union


def insert_to_file(
    file_name: str,
    content: str,
    line_number: int = 0,
    file_path: Union[str, os.PathLike] = ".",
    create_if_not_exist: bool = True,
) -> tuple[bool, str]:
    if file_name.startswith(os.sep):
        file_path = file_name
    else:
        file_path = os.path.join(file_path, file_name)

    if not create_if_not_exist and not os.path.exists(file_path):
        logging.warning("File does not exist: " + file_path)
        return False, f"Failure, File does not exist: {file_path}"

    with open(file_path, "r") as file:
        lines = file.readlines()

    if line_number < 0:
        line_number += len(lines) + 1

    lines.insert(line_number, content + "\n")

    with open(file_path, "w") as file:
        file.writelines(lines)

    return True, os.path.abspath(file_path)


def modify_line(
    file_name: str,
    content: str,
    line_number: int,
    file_path: Union[str, os.PathLike] = ".",
) -> tuple[bool, str]:
    if file_name.startswith(os.sep):
        file_path = file_name
    else:
        file_path = os.path.join(file_path, file_name)

    if not os.path.exists(file_path):
        logging.warning("File does not exist: " + file_path)
        return False, f"Failure, File does not exist: {file_path}"

    with open(file_path, "r") as file:
        lines = file.readlines()

    if line_number < 0:
        line_number += len(lines)

    if abs(line_number) > len(lines):
        logging.warning("Line number exceeds the number of lines in the file.")
        return False, "Failure, Line number exceeds the number of lines in the file."

    lines[line_number] = content + "\n"

    with open(file_path, "w") as file:
        file.writelines(lines)

    return True, os.path.abspath(file_path)


def delete_line(
    file_name: str,
    line_number: int,
    file_path: Union[str, os.PathLike] = ".",
) -> tuple[bool, str]:
    if file_name.startswith(os.sep):
        file_path = file_name
    else:
        file_path = os.path.join(file_path, file_name)

    if not os.path.exists(file_path):
        logging.warning("File does not exist: " + file_path)
        return False, f"Failure, File does not exist: {file_path}"

    with open(file_path, "r") as file:
        lines = file.readlines()

    if line_number < 0:
        line_number += len(lines)

    if abs(line_number) > len(lines):
        logging.warning("Line number exceeds the number of lines in the file.")
        return False, "Failure, Line number exceeds the number of lines in the file."

    del lines[line_number]

    with open(file_path, "w") as file:
        file.writelines(lines)

    return True, os.path.abspath(file_path)


def replace_string_in_file(
    file_name: str,
    old_string: str,
    new_string: str,
    file_path: Union[str, os.PathLike] = ".",
) -> tuple[bool, str]:
    if file_name.startswith(os.sep):
        file_path = file_name
    else:
        file_path = os.path.join(file_path, file_name)

    if not os.path.exists(file_path):
        logging.warning("File does not exist: " + file_path)
        return False, f"Failure, File does not exist: {file_path}"

    with open(file_path, "r") as file:
        file_content = file.read()

    file_content = file_content.replace(old_string, new_string)

    with open(file_path, "w") as file:
        file.write(file_content)

    return True, os.path.abspath(file_path)


def replace_string_in_line(
    file_name: str,
    line_number: int,
    old_string: str,
    new_string: str,
    file_path: Union[str, os.PathLike] = ".",
) -> tuple[bool, str]:
    if file_name.startswith(os.sep):
        file_path = file_name
    else:
        file_path = os.path.join(file_path, file_name)

    if not os.path.exists(file_path):
        logging.warning("File does not exist: " + file_path)
        return False, f"Failure, File does not exist: {file_path}"

    with open(file_path, "r") as file:
        lines = file.readlines()

    if line_number < 0:
        line_number += len(lines)

    if abs(line_number) > len(lines):
        logging.warning("Line number exceeds the number of lines in the file.")
        return False, "Failure, Line number exceeds the number of lines in the file."

    lines[line_number] = lines[line_number].replace(old_string, new_string)

    with open(file_path, "w") as file:
        file.writelines(lines)

    return True, os.path.abspath(file_path)
