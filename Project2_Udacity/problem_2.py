# FILE RECURSION PROBLEM

import os.path

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
    pathList = []
    #Updated code here
    if(not os.path.isdir(path) and not os.path.isfile(path)):
        return "Sorry, file path does not exist! Try again."

    dir_contents = os.listdir(path)

    for element in dir_contents:
      el_path = os.path.join(path, element)

      if(os.path.isfile(el_path)):
        if(el_path.endswith(suffix)):
          pathList.append(el_path)

      if(os.path.isdir(el_path)):
        new_list = find_files(suffix, el_path)
        if new_list:
          pathList += new_list

    return pathList


#NOTE: I have used the local directory of the file mentioned in the description to test this function
print(find_files(".c",r"C:\Users\aruns\Downloads\testdir"))

#Included test case where file path does not exist
print(find_files(".c",r"C:\Users\aruns\Downloads\testdir23"))
