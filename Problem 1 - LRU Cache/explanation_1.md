### Problem 1 - Least Recently Used Cache

Doubly linked list and dictionary are used in conjunction to achieve O(1) time complexity.
* Doubly linked list is used to track the order of access to each data entry and allow for easy insertion of data.
* Dictionary is used to access data entry with constant time complexity.
Both key and value are stored in each node to allow constant time access to each data entry.

**Time Complexity:** O(1)

The space complexity of a doubly linked node of [key, value] is 4 + 1 + 1 = 6. The LRU_cache class = 6n + 1 + 1 + 4 + 4 = 6n + 10. The space complexity of the LRU_cache class is O(n).  

**Space Complexity:** O(n)

Note:  
* When the same key occurs, the old value is replaced by the new value.  
* In calculating space complexity, the following memory value is assumed:
  * pointer - 1 byte
  * bool, char - 1 byte  
  * int(32) - 4 bytes
