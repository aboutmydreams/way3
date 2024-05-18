import os
import shutil


def create_directory(directory_name):
    directory_path = os.path.join(os.getcwd(), directory_name)
    if not os.path.exists(directory_path):
        os.mkdir(directory_path)
        print(f"Directory '{directory_name}' has been created.")
        return directory_path
    else:
        print(f"Directory '{directory_name}' already exists.")
        return f"Directory '{directory_name}' already exists."


def rename_directory(original_name, new_name):
    original_path = os.path.join(os.getcwd(), original_name)
    new_path = os.path.join(os.getcwd(), new_name)
    if os.path.exists(original_path):
        try:
            shutil.move(original_path, new_path)
            print(f"Directory '{original_name}' has been renamed to '{new_name}'.")
            return new_path
        except shutil.Error as e:
            print(f"Error: {e}")
            return f"Error: {e}"
    else:
        print(f"Directory '{original_name}' does not exist.")
        return f"Directory '{original_name}' does not exist."

    # Add a check to handle the case where the new directory name already exists
    if os.path.exists(new_path):
        print(f"Directory '{new_name}' already exists.")
        return f"Directory '{new_name}' already exists."


def delete_directory(directory_name):
    directory_path = os.path.join(os.getcwd(), directory_name)
    if os.path.exists(directory_path):
        shutil.rmtree(directory_path)
        print(f"Directory '{directory_name}' has been deleted.")
        return directory_path
    else:
        print(f"Directory '{directory_name}' does not exist.")
        return f"Directory '{directory_name}' does not exist."


# Call the functions
# print(create_directory("example"))
# print(rename_directory("example", "new_example"))
# print(delete_directory("new_example"))
