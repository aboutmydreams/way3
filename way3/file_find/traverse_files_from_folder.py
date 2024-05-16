import os
import fnmatch


def parse_gitignore(
    gitignore_path=".gitignore", ignored_files=[".git/", ".venv/", ".github/"]
):
    """
    解析 .gitignore 文件，返回忽略规则列表
    """

    if os.path.exists(gitignore_path):
        with open(gitignore_path, "r") as gitignore_file:
            for line in gitignore_file:
                line = line.strip()
                if line and not line.startswith("#"):
                    ignored_files.append(line)
    return ignored_files


def is_gitignored(file_path, gitignore_rules):
    """
    Check if a file path is ignored according to the given gitignore rules.

    Args:
        file_path (str): The absolute path to the file.
        gitignore_rules (list): List of gitignore rules.

    Returns:
        bool: True if the file is ignored, False otherwise.
    """
    for rule in gitignore_rules:
        # Handle comments and empty lines
        if not rule or rule.startswith("#"):
            continue
        # Handle negated rules
        negated = False
        if rule.startswith("!"):
            negated = True
            rule = rule[1:]

        # Check if the file matches the rule
        if fnmatch.fnmatch(file_path, rule):
            return not negated
        if rule in str(file_path):
            return not negated

    return False


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
