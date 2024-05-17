import os
from typing import Dict, List
from ..utils.ignore_rule import parse_gitignore, is_gitignored


def get_files_in_directory(directory, should_ignore=True, ignore_file_path=None):
    """
    获取指定目录下所有文件，排除.gitignore中列出的文件
    """

    file_list = []
    ignore_file_path = (
        ignore_file_path
        if ignore_file_path is not None
        else os.path.join(".", ".gitignore")
    )
    gitignore_rules = parse_gitignore(ignore_file_path)
    print(ignore_file_path)

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            # 检查文件路径是否匹配.gitignore中的规则
            if should_ignore:
                if not is_gitignored(file_path, gitignore_rules):
                    file_list.append(file_path)
            else:
                file_list.append(file_path)
    return file_list


# Example usage 获取当前所有排出掉 gitignore 中的文件
# current_directory = "."  # 当前目录
# files = get_files_in_directory(current_directory)
# print(files)


def get_directory_structure(path) -> Dict[str, Dict[str, List[str]]]:
    """
    获取指定路径下的目录结构
    :param path: 路径
    :return: 目录结构
    """
    directory_structure = {}
    for root, dirs, files in os.walk(path):
        directory_structure[root] = {"dirs": dirs, "files": files}
    return directory_structure


def get_directory_folder_list(path) -> List[str]:
    """
    获取指定路径下的目录结构
    :param path: 路径
    :return: 目录结构
    """
    directory_structure = get_directory_structure(path)
    absolute_path = list(directory_structure.keys())[0]
    return directory_structure[absolute_path]["dirs"]


def get_directory_file_list(path) -> List[str]:
    """
    获取指定路径下的目录结构
    :param path: 路径
    :return: 目录结构
    """
    directory_structure = get_directory_structure(path)
    absolute_path = list(directory_structure.keys())[0]
    return directory_structure[absolute_path]["files"]
