### Problem 6 - Union and Intersection

**Time Complexity:**

As specified in the problem statement, linked lists are used to implement the union and intersection functions. Assuming that duplicate value should be excluded from the list, each time a value is to be added to the list, we need to traverse down the list to search for duplicate. Therefore, the time complexity of the append method is O(n).

To find the union, all the elements in both lists are visited and unique values are stored in a set. Since set is a hashmap data structure, the time to check if an element is in a set is O(1). The total time complexity of the union function is O(m+n) where m and n are the sizes of each list. In the end, conversion of the set which contains the result into a linked list will take O(k) where k is the number of elements in the intersection, k <= m + n. The overall time complexity of the union function is O(m+n).

Similarly for the intersection function, the unique elements in list 1 is first stored in a set, which takes O(n) where n is the number of elements in list 1. Then each of the elements in list 2 is checked against the set for identical values, and each check against the set is O(1); in total, it takes O(m) where m is the number of elements in list 2. In the end, conversion of the set which contains the result into a linked list will take O(k) where k is the number of elements in the intersection. The overall time complexity of the function is O(n+m) assuming k is a limited value.

**Space Complexity:**

Each node has a value and a pointer: 4 + 1 bytes

m is the number of elements in list 1 and n is the number of elements in list 2
Union: O(5 x (m + n) x 2 + 4 x (m + n)) for linked list 1 and 2 + linked list union + the set which stores the union. Overall, the space complexity is O(14(m + n)); for the worst case O(n).
Intersection: O(5 x (m + n) + 4m + 4(min(m,n)) + 5(min(m,n))) for linked list 1 and 2 + the set which stores unique value in list 1 + the set which stores the intersection + the linked list for intersection. Overall, the space complexity is O(9m + 5n + 9min(m,n)); or for the worst case, O(n).

Note: In calculating space complexity, the following memory value is assumed:
  * pointer - 1 byte
  * bool, char - 1 byte  
  * int(32) - 4 bytes
