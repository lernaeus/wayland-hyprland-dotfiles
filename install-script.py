import os

def create_symlink(source_path, symlink_path):
    if not os.path.exists(symlink_path):
        os.symlink(source_path, symlink_path)
        print(f"Created symlink: {symlink_path} -> {source_path}")
    else:
        print(f"Symlink already exists: {symlink_path} -> {source_path}, skipping...")

def create_symlinks(source_dir, config_dir):
    folders_in_repo = []
    files_in_repo = []

    # Iterate through files in repo and check if they're a file or a folder
    for element in os.listdir(source_dir):
        element_path = os.path.join(source_dir, element)

        if os.path.isdir(element_path):
            folders_in_repo.append(element)
        elif os.path.isfile(element_path):
            files_in_repo.append(element)

    print([folder for folder in folders_in_repo])
    print([file for file in files_in_repo])

    # Create symlinks for each folder in repo
    for dir_name in folders_in_repo:
        source_folder_path = os.path.join(source_dir, dir_name)
        symlink_path = os.path.join(config_dir, dir_name)

        create_symlink(source_folder_path, symlink_path)

    for file_name in files_in_repo:
        source_file_path = os.path.join(source_dir, file_name)
        symlink_path = os.path.join(config_dir, file_name)

        create_symlink(source_file_path, symlink_path)

source_directory = os.path.join(os.getcwd(), '.config')
config_directory = os.path.expanduser("~/.config")

# create_symlinks(source_directory, config_directory)

print(source_directory, config_directory)