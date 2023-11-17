# To check for duplicated images within a list of folders, you can follow these general steps using Python:
#
# Gather a list of image files in each folder.
# Compute a unique identifier (like a hash) for each image.
# Compare the identifiers to find duplicates.
# Here's a basic Python script that achieves this using the os and hashlib libraries:

import os
import hashlib


def hash_file(file_path):
    # Function to hash a file using SHA-256
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while True:
            data = f.read(65536)  # Read file in chunks to conserve memory
            if not data:
                break
            hasher.update(data)
    return hasher.hexdigest()


def find_duplicates(root_folder):
    # Dictionary to store hashes and corresponding file paths
    hash_dict = {}
    duplicates = []

    for folder_name, subfolders, files in os.walk(root_folder):
        for file_name in files:
            file_path = os.path.join(folder_name, file_name)
            file_hash = hash_file(file_path)
            if file_hash in hash_dict:
                duplicates.append((file_path, hash_dict[file_hash]))
            else:
                hash_dict[file_hash] = file_path

    return duplicates


def find_duplicates_in_directory(folders_to_check, find_or_delete):
    # Replace 'path_to_folders' with the path to your folders containing images

    duplicate_images = find_duplicates(folders_to_check)

    if duplicate_images:
        print("Duplicate images found:")
        for dup in duplicate_images:
            print(f"Duplicate 1: {dup[0]}\n"
                  f"Duplicate 2: {dup[1]}")
            # this removes the first duplicate it finds , uncomment if you want to delete it
            if find_or_delete == 'delete':
                delete_duplicate(dup[0])

    else:
        print("No duplicate images found.")


def delete_duplicate(file_to_delete):
    os.remove(file_to_delete)


def update_filenames(directory_path):
    # Check if the given path is a directory
    if not os.path.isdir(directory_path):
        print(f"The path '{directory_path}' is not a valid directory.")
        return

    # Get a list of all files in the directory
    files = os.listdir(directory_path)

    # Iterate through each file and update the name
    for index, file_name in enumerate(files):
        original_path = os.path.join(directory_path, file_name)

        # Check if the file is a regular file (not a directory)
        if os.path.isfile(original_path):
            # Extract the file extension (if any)
            root, extension = os.path.splitext(file_name)

            # Create the new file name by appending "updated" to the original name
            new_file_name = f"242424242_{index}{index}{extension}"

            # Create  the new file path
            new_path = os.path.join(directory_path, new_file_name)

            # Rename the file
            os.rename(original_path, new_path)
            print(f"Renamed: {file_name} -> {new_file_name}")


# delete duplicates in a given directory
find_duplicates_in_directory('./dataset/plank', 'delete')
# Example usage:
# directory_path = "./dataset/downdog"
# update_filenames(directory_path)
