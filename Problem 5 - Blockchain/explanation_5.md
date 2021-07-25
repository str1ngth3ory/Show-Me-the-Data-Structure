### Problem 5 - Blockchain

As suggested in the problem statement, a linked list is used to implement the block chain data structure. However, instead of storing one data, the node is storing timestamp, data, its hash value, and the hash value of the previous node. And in order to obtain a unique hash value, both the time stamp string and the data string are encoded together.

In the blockchain class, both the head and tail nodes are tracked to avoid traversing through the entire linked list when adding new block of data.

**Time Complexity:** the time complexity of adding a new block is O(1) because tail node can be easily accessed.

The space complexity of each block is as follow:
timestamp - 32 bytes
data - m bytes
hash value - 32 bytes
next pointer = 1 byte
Total = m + 97 bytes

The blockchain class just adds multiple of blocks and two more pointers. Therefore,

**Space Complexity:** the space complexity of block chain is O(n(m+97) + 2) or O(n x m) where n is number of blocks and m is the length of the data string. If we ignore the length of each datablock (limited data), then the time complexity is O(n) where n is the number of blocks.

Note: In calculating space complexity, the following memory value is assumed:
  * pointer - 1 byte
  * bool, char - 1 byte  
  * int(32) - 4 bytes
