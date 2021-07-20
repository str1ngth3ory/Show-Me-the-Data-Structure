import hashlib
import time
from datetime import datetime, timezone


class Block(object):

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None

    def calc_hash(self):
        sha = hashlib.sha256()
        # encode both data and timestamp to get unique hash
        hash_str = (self.data + self.timestamp).encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()


class Blockchain(object):

    def __init__(self):
        self.head = None
        self.tail = None  # track the end of linked list for O(1) access

    def add_block(self, data):

        if data is None or data == '':
            raise ValueError('Empty data entered')

        dt_ts = datetime.fromtimestamp(time.time(), tz=timezone.utc)
        if self.head is None:
            self.head = Block(str(dt_ts), data, 0)
            self.tail = self.head
        else:
            self.tail.next = Block(str(dt_ts), data, self.tail.hash)
            self.tail = self.tail.next

    def to_list(self):
        node = self.head
        data_list = list()
        hash_list = list()
        while node:
            data_list.append(node.data)
            hash_list.append(node.hash)
            node = node.next
        return data_list, hash_list


b = Blockchain()

print('Test Case 1 - add three different data block')
# print three different hash values
b.add_block('data_1')
b.add_block('data_2')
b.add_block('data_3')
data_list, hash_list = b.to_list()
for i in range(len(data_list)):
    print(f'{data_list[i]}')
    print(f'{hash_list[i]}')

print('\n\nTest Case 2 - add two data blocks with the same data')
# print two different hash values
c = Blockchain()
c.add_block('data')
c.add_block('data')
data_list, hash_list = c.to_list()
for i in range(len(data_list)):
    print(f'{data_list[i]}')
    print(f'{hash_list[i]}')

print('\n\nTest Case 3 - empty data')
# raise ValueError
b.add_block(None)
