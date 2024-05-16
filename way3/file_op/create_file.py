import os
import logging
from typing import Union


def create_file(
    file_name: str,
    content: str,
    file_path: Union[str, os.PathLike] = ".",
    force_rewrite: bool = True,
) -> tuple[bool, str]:
    if file_name.startswith(os.sep):
        file_path = file_name
    else:
        file_path = os.path.join(file_path, file_name)

    if not force_rewrite and os.path.exists(file_path):
        logging.warning("File already exists: " + file_path)
        return False, f"Failure, File already exists: {file_path}"

    with open(file_path, "w") as file:
        file.write(content)

    return True, os.path.abspath(file_path)


def add_to_file_end(
    file_name: str,
    content: str,
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

    with open(file_path, "a") as file:
        file.write(content)

    return True, {os.path.abspath(file_path)}


def delete_file(
    file_name: str, file_path: Union[str, os.PathLike] = "."
) -> tuple[bool, str]:
    if file_name.startswith(os.sep):
        file_path = file_name
    else:
        file_path = os.path.join(file_path, file_name)

    if os.path.exists(file_path):
        os.remove(file_path)
        return True, {os.path.abspath(file_path)}
    else:
        logging.warning("File does not exist: " + file_path)
        return False, f"Failure, File does not exist: {file_path}"
