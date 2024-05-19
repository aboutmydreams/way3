from typing import Union, NamedTuple
import os
import logging


class FileInfo(NamedTuple):
    content: str
    length: int
    lines: int
    file_type: str


def read_file(file_name: str, file_path: Union[str, os.PathLike] = ".") -> FileInfo:
    if file_name.startswith(os.sep):
        file_path = file_name
    else:
        file_path = os.path.join(file_path, file_name)

    if not os.path.exists(file_path):
        logging.warning("File does not exist: " + file_path)
        return FileInfo(content="", length=0, lines=0, file_type="")

    with open(file_path, "r") as file:
        content = file.read()
        length = len(content)
        lines = content.count("\n") + 1
        file_type = os.path.splitext(file_path)[1]

    return FileInfo(content=content, length=length, lines=lines, file_type=file_type)


def read_line(
    file_name: str, line_number: int, file_path: Union[str, os.PathLike] = "."
) -> str:
    if file_name.startswith(os.sep):
        file_path = file_name
    else:
        file_path = os.path.join(file_path, file_name)

    if not os.path.exists(file_path):
        logging.warning("File does not exist: " + file_path)
        return ""

    with open(file_path, "r") as file:
        for _ in range(line_number - 1):
            file.readline()
        return file.readline()
