### Problem 3 - Huffman Coding

In my solution, linked list with binary tree, hashmap(python dictionary), and min-heap are used. Min-heap is implemented using the python heapq library. The Huffman tree is implemented using linked list which store two information items: character and frequency of character.
###### Time complexity analysis of the process by steps:
1. Store the frequency of each character in a dictionary: traversing all character one time, O(n)
2. Forming the Huffman Tree:
  * Whenever pushing or popping items from the min-heap, the heap list needs to be heapified(O(n)). Time complexity for these operations is O(n)*k where k is the number of push/pop needed in the process. However, the number of push/pop,k, and the number of unique character, n, are both limited. The overall time complexity can be viewed as constant, O(1) for small number of characters and O(n) for large number of unique characters.
  * When building the Huffman Tree with linked list, the time complexity is O(n-1), equivalently O(n), where n is the number of unique characters. Again, the number of unique characters is limited. For small number of unique characters, it's constant O(1).
  * When generating the binary code table (against unique characters), all nodes are traversed one time to get to all the leaf nodes. And character to binary code data is stored in a python dictionary. The time complexity of this process is O(n) where n is the number of unique characters.
  However, again the number of characters is limited
3. Conversion of each character to code using the dictionary: the time complexity is O(n) where n is the total number of all characters.
4. For decoding, it requires the search of leaf node in the Huffman Tree (a binary tree) for each 0 or 1 in the binary code string, O(n). Search operation in binary tree has a time complexity of O(m) (O(2m-1)) where n is the total number of leaf nodes (unique characters). The time complexity for decoding is O(n*O(m)). For a small number of unique characters, O(m) can be viewed as a constant time complexity. Therefore, O(n)

Therefore:

**Summary of Time Complexity:**  
Assuming we are dealing with limited characters in the ASCII table.
* For encoding, it is O(n) where n is the number of all characters in the string.
* For decoding, it is O(n) where n is the number of all 0/1 in the binary code string.

###### Space complexity:

* The space complexity of a Node object is O(4 + 1 + 1 + 1) = O(7). A Huffman Tree has 2k - 1 nodes where k is the number of unique characters (leaf nodes). Therefore, the space complexity of a Huffman Tree is O(7(2k-1)).
* There are two dictionaries in the Huffman class, each has a space complexity of O((1 + 4)k) or O(5k) where k is the number of unique characters.
* The min-heap contains nodes which are already counted in the Huffman Tree.

Therefore, the total space complexity of the data structure is O(14k-7 + 5k) or O(k) where k is the number of unique characters.

Note: In calculating space complexity, the following memory value is assumed:
  * pointer - 1 byte
  * bool, char - 1 byte  
  * int(32) - 4 bytes
