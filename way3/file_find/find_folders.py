from typing import List
import os
from way3.utils.ignore_rule import parse_gitignore, is_gitignored


def find_folders_by_name(
    directory: str, search_string: str, should_ignore=True, ignore_file_path=None
) -> List[str]:
    """
    寻找某个路径下，文件夹包含某个字符串的所有文件夹列表
    """
    matching_folders = []

    ignore_file_path = (
        ignore_file_path
        if ignore_file_path is not None
        else os.path.join(".", ".gitignore")
    )
    gitignore_rules = parse_gitignore(ignore_file_path)

    for root, dirs, files in os.walk(directory):
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            # 检查文件夹路径是否匹配.gitignore中的规则
            if should_ignore:
                if (
                    not is_gitignored(dir_path, gitignore_rules)
                    and search_string in dir
                ):
                    matching_folders.append(dir_path)
            else:
                if search_string in dir:
                    matching_folders.append(dir_path)

    return matching_folders
