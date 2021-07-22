### Problem 5 - Blockchain

**Time Complexity:**

As specified in the problem statement, linked lists are used to implement the union and intersection functions. Assuming duplicate value should be excluded in the list, each time a value is to be added to the list, we need to traverse down the list for duplicate. Therefore, the time complexity of the append method is O(n).

To find the union, each node in list 2 is check against every node in list 1. Therefore, the time complexity of the union function is O(m x n) where m is the number of elements in list 1 and n is the number of elements in list 2.

Similarly for the intersection function, each node in list 2 is compared with every node in list 1 to find shared values in both lists. Therefore, the time complexity of the intersection function is also O(m x n) where m is the number of elements in list 1 and n is the number of elements in list 2.

**Space Complexity:**

Each node has a value and a pointer: 4 + 1 bytes

The space complexity of the function is proportional to how many element in the union or intersection. For worst case:
Union: O(5 x (m + n)) or O(m + n)
Intersection: O(5 x min(m, n)) or O(min(m, n))
where m is the number of elements in list 1 and n is the number of elements in list 2.


Note: In calculating space complexity, the following memory value is assumed:
  * pointer - 1 byte
  * bool, char - 1 byte  
  * int(32) - 4 bytes
