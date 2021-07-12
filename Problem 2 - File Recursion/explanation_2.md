### Problem 2 - File Recursion

Recursion is used to keep searching for the next directory if available. I think it's essentially a post-order DFS of a tree in which each directory is a node. The search result for each node is returned after all of its sub-nodes (sub-directories) are searched. Each node is traversed one time, and therefore the time complexity is O(n).

**Time Complexity:** O(n)

A list is used to store the paths for all the files that end with the suffix. Therefore, the space complexity is O(n).

**Space Complexity:** O(n)
