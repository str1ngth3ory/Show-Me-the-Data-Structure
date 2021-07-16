import sys
import heapq


class Node(object):

    def __init__(self, freq, character=None):
        self.freq = freq
        self.character = character
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


class Huffman(object):

    def __init__(self):
        self.freq_dict = dict()
        self.huffman_root = None  # to store the Huffman Tree
        self.char_to_bin_dict = dict()

    def encoding(self, data):
        '''
        Call this method to encode input starting
        Input: a string to be encoded_data
        Regurn: the binary codes
        '''
        # raise error if input is invalid
        if data is None or data == '':
            raise ValueError('NoneType Input')

        # generate Huffman Tree and binary code table
        self.generate_binary_table(data)

        # convert characters to binary codes
        binary_code = ''
        for char in data:
            binary_code = binary_code + self.char_to_bin_dict[char]
        return binary_code

    def decoding(self, data):
        '''
        Call this method to decode the binary code
        (Huffman Tree is stored in the object, no need to input)
        Input: binary codes
        Return: decoded string
        '''
        # raise error if huffman tree hasn't been established
        if self.huffman_root is None:
            raise ValueError('Huffman Tree not exist')

        string = ''
        return self._decoding(data, self.huffman_root, 0, string)

    def generate_binary_table(self, data):
        '''
        A function to generate dictionary of character to binary code
        Input: the string to be encoded
        '''
        # generate character frequency dictionary
        self.freq_dict = dict()
        for char in data:
            if char in self.freq_dict:
                self.freq_dict[char] += 1
            else:
                self.freq_dict[char] = 1

        # form a min heap
        h = []
        for key, value in self.freq_dict.items():
            heapq.heappush(h, Node(value, key))
        if len(h) == 1:
            self.huffman_root = Node(h[0].freq)
            self.huffman_root.left = h[0]
        else:
            # call the function to generate the Huffman Tree
            self.huffman_root = self._huffman_tree(h)
        # use the tree to generate binary code for each character
        code = ''
        self._generate_bins(self.huffman_root, code)

    # define a recursive function to form a Huffman Tree & return the root
    def _huffman_tree(self, heap_arr):
        '''
        A private recursive function for establishing the Huffman Tree
        Input: min-heap of characters and their frequencies
        Return: root of the Huffman Tree
        '''
        # base case which returns the last/root node
        if len(heap_arr) == 1:
            return heap_arr[0]

        # pop the two smallest nodes in the min-heap, merge them
        # and push them back into the heap. return the updated heap.
        min_heap_1 = heapq.heappop(heap_arr)
        min_heap_2 = heapq.heappop(heap_arr)
        new_node = Node(min_heap_1.freq + min_heap_2.freq)
        new_node.left = min_heap_1
        new_node.right = min_heap_2
        heapq.heappush(heap_arr, new_node)
        return self._huffman_tree(heap_arr)

    def _generate_bins(self, node, code):
        '''
        A private recursive function to help find binary codes for each
        character
        '''

        # base case - record the traversed path with respect ot the character
        if not node.left and not node.right:
            self.char_to_bin_dict[node.character] = code
        else:
            # traverse all possible paths to find codes for each charater
            if node.left:
                self._generate_bins(node.left, code+'0')
            if node.right:
                self._generate_bins(node.right, code+'1')

    def _decoding(self, data, node, idx, string):
        '''
        A private recursive function for decoding
        Input:  data - binary codes
                node - starting node
                idx  - index of binary code that's being used to traverse the
                       Huffman Tree
                string - a string to store the decoded information
        Return  decoded string
        '''

        # base case - return character if traverse to the leaf node
        if not node.left and not node.right:
            string = string + node.character
            # restart from root for the next binary code
            if idx <= len(data)-1:
                return self._decoding(data, self.huffman_root, idx, string)
            # reach the end of the binary code
            else:
                return string
        # traverse left or right based on the binary code
        elif data[idx] == '0':
            return self._decoding(data, node.left, idx+1, string)
        elif data[idx] == '1':
            return self._decoding(data, node.right, idx+1, string)


if __name__ == "__main__":
    huffman = Huffman()

    test_case_1 = 'AAA'  # single character input
    test_case_2 = 'The bird is the word'  # multi-characters input
    test_case_3 = ''  # empty input

    print('Test Case 1')
    encoded_data = huffman.encoding(test_case_1)
    decoded_data = huffman.decoding(encoded_data)
    print(f'String to be encoded: {test_case_1}')
    print(f'Encoded data: {encoded_data}')
    print(f'Decoded data: {decoded_data}\n')

    print('Test Case 2')
    print("The size of the data is: {}".format(sys.getsizeof(test_case_2)))
    print("The content of the data is: {}\n".format(test_case_2))

    encoded_data = huffman.encoding(test_case_2)

    print("The size of the encoded data is: {}".format(sys.getsizeof(
                                            int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman.decoding(encoded_data)

    print("The size of the decoded data is: {}".format(sys.getsizeof(
                                            decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

    print('Test Case 3')
    print(f'String to be encoded: {test_case_3}')
    encoded_data = huffman.encoding(test_case_3)
