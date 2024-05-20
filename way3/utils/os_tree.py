import os


def tree(
    directory,
    prefix="",
    show_hidden=False,
    max_depth=None,
    full_path=False,
    sort_by_size=False,
    show_permissions=False,
    current_depth=0,
):
    # 先获取目录中的所有文件和文件夹
    entries = os.listdir(directory)

    if not show_hidden:
        entries = [entry for entry in entries if not entry.startswith(".")]

    if sort_by_size:
        entries.sort(key=lambda entry: os.path.getsize(os.path.join(directory, entry)))
    else:
        entries.sort()

    files = []
    dirs = []
    for entry in entries:
        full_path_entry = os.path.join(directory, entry)
        if os.path.isdir(full_path_entry):
            dirs.append(entry)
        else:
            files.append(entry)

    def format_entry(entry, path):
        if full_path:
            entry = path
        if show_permissions:
            entry = f"{oct(os.stat(path).st_mode)[-3:]} {entry}"
        return entry

    # 打印当前目录下的文件
    for file in files:
        file_path = os.path.join(directory, file)
        print(prefix + "|-- " + format_entry(file, file_path))

    # 递归打印子目录
    if max_depth is None or current_depth < max_depth:
        for i, dir in enumerate(dirs):
            dir_path = os.path.join(directory, dir)
            print(prefix + "|-- " + format_entry(dir, dir_path))
            new_prefix = prefix + "|   " if i < len(dirs) - 1 else prefix + "    "
            tree(
                dir_path,
                new_prefix,
                show_hidden,
                max_depth,
                full_path,
                sort_by_size,
                show_permissions,
                current_depth + 1,
            )


# 使用示例
# tree(
#     "./way3",
#     show_hidden=True,
#     max_depth=2,
#     full_path=False,
#     sort_by_size=True,
#     show_permissions=False,
# )
