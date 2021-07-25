### Problem 4 - Active Directory

A recursive call of the function is used to search sub-directory if user is not found in the current directory. The recursive call will stop if user is found. Time complexity is O(n) because all the directories are accessed in the function.

**Time Complexity:** O(n)

The space complexity is 1 for each recursive call since only a bool variable is stored in each function call.  

**Space Complexity:** Therefore, the total complexity is O(n) where n is the number of sub-directories (or recursive calls).
