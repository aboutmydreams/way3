from typing import List
import os
from way3.utils.ignore_rule import parse_gitignore, is_gitignored


def find_files_by_name(
    search_string: str, directory=".", should_ignore=True, ignore_file_path=None
) -> List[str]:
    """
    寻找某个路径下，文件名包含某个字符串的所有文件名绝对路径列表
    """
    matching_files = []

    ignore_file_path = (
        ignore_file_path
        if ignore_file_path is not None
        else os.path.join(".", ".gitignore")
    )
    gitignore_rules = parse_gitignore(ignore_file_path)

    for root, dirs, files in os.walk(directory):
        for file in files:
            if search_string in file:
                file_path = os.path.join(root, file)
                # 检查文件路径是否匹配.gitignore中的规则
                if should_ignore:
                    if not is_gitignored(file_path, gitignore_rules):
                        matching_files.append(file_path)
                else:
                    matching_files.append(file_path)

    return matching_files
