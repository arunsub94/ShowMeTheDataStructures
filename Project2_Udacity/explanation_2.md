
FILE RECURSION PROBLEM

This problem required a recursive approach due to the fact that directories could contain directories/files
and as we go deeper into a directory, you would end up with potentially more directory/file choices.

Since recursion has been employed, the time complexity would be O(n) since it would be iteratively called as
many times as there are sub-directories. Also, the for loop that iterates through all files/directories in a sub-directory
is also O(n). Hence, the overall time complexity is O(n).

The array being used to store is O(n) space complexity. 
