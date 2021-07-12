
class Node(object):
# Define a doubly linked list node to help track the 'recency'

    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.hash_map = {}
        # Track the first and last node to help achieve O(1) order modification
        self.head = None
        self.last = None
        self.num_entries = 0
        self.capacity = capacity

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.hash_map:
            # If cache hit happens at the head, move the second item to the head,
            # and move the head to the end and return the value
            if self.head == self.hash_map[key]:
                self.head = self.head.next
                self.head.prev = None
                self.last.next = self.hash_map[key]
                self.hash_map[key].next = None
                self.hash_map[key].prev = self.last
                self.last = self.hash_map[key]
            # If cache hit happens at the last element, return the value
            elif self.last == self.hash_map[key]:
                pass
            # Otherwise, move the hit item to the end and connect the next item to the previous item. Then return the value
            else:
                self.hash_map[key].prev.next = self.hash_map[key].next
                self.hash_map[key].next.prev = self.hash_map[key].prev
                self.last.next = self.hash_map[key]
                self.hash_map[key].prev = self.last
                self.last = self.hash_map[key]
            return self.hash_map[key].value[1]
        else:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.

        # initial entry
        if self.num_entries == 0:
            self.hash_map[key] = Node([key, value])
            self.head = self.hash_map[key]
            self.last = self.hash_map[key]
            self.num_entries += 1
        # After initial entry - if key exists, replace the old node, and make it the last node
        # if key doesn't exist, add key value pairs (check if data structure has reached max capacity)
        else:
            if key in self.hash_map:
                if self.head == self.hash_map[key]:
                    self.head = self.head.next
                elif self.last == self.hash_map[key]:
                    self.last = self.last.prev
                else:
                    self.hash_map[key].prev.next = self.hash_map[key].next
                    self.hash_map[key].next.prev = self.hash_map[key].prev
                self.hash_map[key] = Node([key, value])
                self.last.next = self.hash_map[key]
                self.hash_map[key].prev = self.last
                self.last = self.hash_map[key]
            else:
                if self.num_entries >= self.capacity:
                    self.hash_map.pop(self.head.value[0])
                    self.head = self.head.next
                else:
                    self.num_entries += 1
                self.hash_map[key] = Node([key, value])
                self.hash_map[key].prev = self.last
                self.last.next = self.hash_map[key]
                self.last = self.hash_map[key]

    # Define the print statement display helper funciton to show the order of nodes
    def __repr__(self):
        output = []
        node = self.head
        while node:
            output.append(node.value[1])
            node = node.next
        return f'{output}'



our_cache = LRU_Cache(5)

# Test case 1 - 0 data entry
print(our_cache.get(1))     # return -1

# Test case 2 - less than 5 entries,
our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);

print(our_cache.get(1))     # returns 1
print(our_cache.get(2))     # returns 2
print(our_cache.get(9))     # returns -1 because 9 is not present in the cache

# Test case 3 - more than 5 entries
our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3))     # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

our_cache.set(7, 7)
our_cache.set(8, 8)

print(our_cache.get(4))     # returns -1 because the cache reached it's capacity and 4 was the least recently used entry
print(our_cache.get(1))     # returns -1 because the cache reached it's capacity and 1 was the least recently used entry
print(our_cache.get(2))     # returns 2
