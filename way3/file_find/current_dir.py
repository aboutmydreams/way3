import os


def get_current_dir(instance=__file__):
    return os.path.dirname(os.path.abspath(instance))
