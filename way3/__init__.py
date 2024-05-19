name = "way3"

# File OP
from .file_op.create_file import create_file as create_file  # noqa: E402
from .file_op.create_file import add_to_file_end as add_to_file_end  # noqa: E402
from .file_op.create_file import delete_file as delete_file  # noqa: E402
from .file_op.edit import insert_to_file as insert_to_file  # noqa: E402
from .file_op.edit import modify_line as modify_line  # noqa: E402
from .file_op.edit import delete_line as delete_line  # noqa: E402
from .file_op.edit import replace_string_in_line as replace_string_in_line  # noqa: E402
from .file_op.edit import replace_string_in_file as replace_string_in_file  # noqa: E402


# File Find
from .file_find.current_dir import get_current_dir as get_current_dir  # noqa: E402
from .file_find.traverse_files_from_folder import parse_gitignore as parse_gitignore  # noqa: E402
from .file_find.traverse_files_from_folder import is_gitignored as is_gitignored  # noqa: E402
from .file_find.traverse_files_from_folder import (  # noqa: E402
    get_files_in_directory as get_files_in_directory,
)
from .file_find.traverse_files_from_folder import (  # noqa: E402
    get_directory_structure as get_directory_structure,
)
from .file_find.traverse_files_from_folder import (  # noqa: E402
    get_directory_folder_list as get_directory_folder_list,
)
from .file_find.traverse_files_from_folder import (  # noqa: E402
    get_directory_file_list as get_directory_file_list,
)

# Folder OP
from .folder_op.create_folder import create_directory as create_directory  # noqa: E402
from .folder_op.create_folder import rename_directory as rename_directory  # noqa: E402
from .folder_op.create_folder import delete_directory as delete_directory  # noqa: E402

## read file
from .file_op.read import read_file as read_file  # noqa: E402
from .file_op.read import read_line as read_line  # noqa: E402
