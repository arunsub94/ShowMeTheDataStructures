
FILE RECURSION PROBLEM

This problem required a recursive approach due to the fact that directories could contain directories/files
and as we go deeper into a directory, you would end up with potentially more directory/file choices.

A directory can have sub-directories and sub-directories can have files. As a consequence,
due to the depth of recursion, each directory has a sub-directory and files within each
sub-directory. Let's take an example as shown below.

directory
  sub_dir_1
    file_1.c
    file_2.c
  sub_dir_2
    file_3.c
    file_4.c

In the above example, the function find_files() is recursively called three times. The first time,
[sub_dir1, sub_dir2] are returned and then the two files in each sub_dir are returned.
This results in a total of 6 items being returned which happens to be n, the input into the function.
Hence, the time complexity of this recursive function is O(n), having taken into account the depth of recursion.

The array being used to store is O(n) space complexity.
