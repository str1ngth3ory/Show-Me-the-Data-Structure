### Problem 1 - Least Recently Used Cache

* Doubly linked list and dictionary are used in conjunction to achieve O(1) time complexity.
    * Doubly linked list is used to track the order of access to each data entry and allow for easy insertion of data.
    * Dictionary is used to access data entry with constant time complexity.
* Both key and value are stored in each node to allow constant time access to each data entry.
* **Note:** When the same key occurs, the old value is replaced by the new value.
