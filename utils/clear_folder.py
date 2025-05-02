import os

def clear_previous_files(directory="internal_policy"):
    """
    Deletes all files in the given directory to remove previous uploads.
    """
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)
            print(f"Deleted: {filename}")