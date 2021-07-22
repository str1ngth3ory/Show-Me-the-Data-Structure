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
    node = llist_1.head
    while node:
        ulist.append(node.value)
        node = node.next

    # check every node in list 2 against every node in the list 1
    # if list 2 node not in list 1, append it to the union list
    node_2 = llist_2.head
    while node_2:
        node_1 = llist_1.head
        while node_1:
            if node_2.value == node_1.value:
                break
            node_1 = node_1.next
        if node_1 is None:
            ulist.append(node_2.value)
        node_2 = node_2.next

    if ulist.head:
        return ulist
    else:
        return None


def intersection(llist_1, llist_2):
    # create a copy of linked list 1 - intersection list
    ilist = LinkedList()

    # check every node in list 2 against every node in the list 1
    # if list 2 node is in list 1, append it to the intersection list
    node_2 = llist_2.head
    while node_2:
        node_1 = llist_1.head
        while node_1:
            if node_2.value == node_1.value:
                ilist.append(node_2.value)
                break
            node_1 = node_1.next
        node_2 = node_2.next

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
