import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if not os.path.isdir(path):
        return None

    list_files = []

    # Walk through each item in the directory
    for item in os.listdir(path):

        # if item is a file, check if it has the suffix
        temp_path = os.path.join(path, item)

        if os.path.isfile(temp_path):
            if temp_path.endswith(suffix):
                list_files.append(temp_path)

        # if item is a sub-directory, check if the sub-directory contains file
        # with the suffix
        elif os.path.isdir(temp_path):
            list_files = list_files + find_files(suffix, temp_path)

    return list_files


# # Test case 1 - invalid file path
test_case_1 = ['.c', './invalid_filepath']
print(find_files(*test_case_1))  # return None

# Test case 2 - empty folder
test_case_2 = ['.c', './test_case_2']
print(find_files(*test_case_2))  # return empty list

# Test case 3 - typical folder (the folder provided in the problem statement)
test_case_3 = ['.c', './test_case']
print(find_files(*test_case_3))  # return the four files that end with '.c'

# Test case 4 - file not found
test_case_3 = ['.exe', './test_case']
print(find_files(*test_case_3))  # return empty list
