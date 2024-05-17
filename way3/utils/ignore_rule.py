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
