class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
            return

        # check for duplicate, if found, do not append value
        node = self.head
        while node:
            if value == node.value:
                return
            node = node.next

        self.tail.next = Node(value)
        self.tail = self.tail.next

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(llist_1, llist_2):
    # create a copy of linked list 1 - union list
    ulist = LinkedList()
    u_set = set()

    # add values from both lists to the set and exclude duplicates
    node = llist_1.head
    while node:
        u_set.add(node.value)
        node = node.next

    node = llist_2.head
    while node:
        u_set.add(node.value)
        node = node.next

    # convert the set into a linked list and return the linked list
    for value in u_set:
        ulist.append(value)

    if ulist.head:
        return ulist
    else:
        return None


def intersection(llist_1, llist_2):
    # create a copy of linked list 1 - union list
    ilist = LinkedList()
    set_1 = set()
    i_set = set()

    # add values from both lists to the set and exclude duplicates
    node = llist_1.head
    while node:
        set_1.add(node.value)
        node = node.next

    node = llist_2.head
    while node:
        if node.value in set_1:
            i_set.add(node.value)
        node = node.next

    # convert the set into a linked list and return the linked list
    for value in i_set:
        ilist.append(value)

    if ilist.head:
        return ilist
    else:
        return None


# Test case 1
# For union: return [3,2,4,35,6,65,21,32,9,1,11]
# For intersection: return [6,4,21]

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print('Test Case 1')
print('Union:', union(linked_list_1, linked_list_2))
print('Intersection:', intersection(linked_list_1, linked_list_2))

# Test case 2
# For union: return [3,2,4,35,6,65,23,1,7,8,9,11,21]
# For intersection: return None

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print('\nTest Case 2')
print('Union:', union(linked_list_3, linked_list_4))
print('Intersection:', intersection(linked_list_3, linked_list_4))

# Test case 3 - Empty data
# Return None for both union and intersection

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print('\nTest Case 3')
print('Union:', union(linked_list_5, linked_list_6))
print('Intersection:', intersection(linked_list_5, linked_list_6))

# Test case 4 - One set empty
# Return the non-empty list for union and None for intersection

linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

element_1 = [1, 3, 6, 23, 35]
element_2 = []

for i in element_1:
    linked_list_7.append(i)

for i in element_2:
    linked_list_8.append(i)

print('\nTest Case 3')
print('Union:', union(linked_list_7, linked_list_8))
print('Intersection:', intersection(linked_list_7, linked_list_8))
