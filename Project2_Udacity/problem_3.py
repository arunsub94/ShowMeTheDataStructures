# HUFFMAN CODING IMPLEMENTATION

import heapq
import sys

def determine_frequency(message):
    """ Function to determine the frequency of each character in a string message
        INPUT: message (str)
        OUTPUT: dictionary containing the frequency of each character
    """

    freq_dict = dict({})
    for character in message:
        if (character in freq_dict):
            freq_dict[character] += 1
        else:
            freq_dict[character] = 1

    return freq_dict

def build_priority_queue(freq_dict):
    """ Function to build priority queue using a min heap data structure
        INPUT: Dictionary containing frequencies of each character in message
        OUTPUT: Priority Queue (heapq)
    """
    #Create a lit and populate the heap
    heap_pq = []
    for key, value in freq_dict.items():
        heapNode = Node(key, value)
        heapq.heappush(heap_pq, heapNode)

    return heap_pq

class Node:
    def __init__(self, character, frequency):
        self.char = character
        self.freq = frequency
        self.left = None
        self.right = None

    def set_value(self, character, frequency):
        self.char = character
        self.freq = frequency

    def get_value(self):
        return [self.freq, self.char]

    def set_left_child(self, node):
        self.left = node

    def set_right_child(self, node):
        self.right = node

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def has_left_child(self):
        if self.left is not None:
            return True
        else:
            return False

    def has_right_child(self):
        if self.right is not None:
            return True
        else:
            return False

    def __gt__(self, other):
        return (self.freq > other.freq)

    def __lt__(self, other):
        return (self.freq < other.freq)

    def __eq__(self, other):
        return (self.freq == other.freq)

    def __repr__(self):
        return str(self.char) + str(" | ") + str(self.freq)

class huffman_tree:
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def set_root(self, node):
        self.root = node

def encoder(root):

    #Traverse tree from root to leaf to generate encoding for each character
    root_node = root
    #Dictionary to assign encoding for each character
    encode_arr = []
    encoded_dict = traverse_root2leaf(root_node, encode_arr, 0, {})
    return encoded_dict

def traverse_root2leaf(root_node, encode_arr, index, encodeDict):

    if (root_node.has_left_child()):
        encode_arr.insert(index, '0')
        traverse_root2leaf(root_node.get_left_child(), encode_arr, index + 1, encodeDict)

    if(root_node.has_right_child()):
        encode_arr.insert(index, '1')
        traverse_root2leaf(root_node.get_right_child(), encode_arr, index + 1, encodeDict)

    if(not root_node.has_left_child() and not root_node.has_right_child()):
        [freq, char] = root_node.get_value()
        str_out = ''
        for character in encode_arr[:index]:
            str_out += character
        encodeDict[char] = str_out

    return encodeDict

def huffman_encoding(message):

    test_heap = build_priority_queue(determine_frequency(message))
    h_tree = huffman_tree()

    if(len(test_heap) == 1):
        h_tree.set_root(heapq.heappop(test_heap))
        [freq, char] = h_tree.get_root().get_value()
        encoded_str = ''
        for i in range(0, freq+1):
            encoded_str += '1'

        return encoded_str, h_tree

    #Building the Huffman Tree
    while (len(test_heap) != 1):

        #Pop the elements with lowest frequency
        node_1 = heapq.heappop(test_heap)
        node_2 = heapq.heappop(test_heap)

        #Compute the sum of frequencies of both elements
        [freq1, char1] = node_1.get_value()
        [freq2, char2] = node_2.get_value()
        new_freq = freq1 + freq2

        #Create a new node with the new frequency along with children
        new_node = Node('dummy', new_freq)

        #Assign children to the new node
        new_node.set_left_child(node_1)
        new_node.set_right_child(node_2)

        #Push the new frequency into the heap while maintaining heap invariance
        heapq.heappush(test_heap, new_node)

    h_tree.set_root(heapq.heappop(test_heap))

    #DFS traversal to generate encoding
    encoding_key = encoder(h_tree.get_root())

    encoded_str = ''

    for char in message:
        encoded_str += encoding_key[char]

    return encoded_str, h_tree

def huffman_decoding(encoded_message, tree):

    root_node = tree.get_root()

    decoded_str = ''
    encoded_index = 0
    encode_length = len(encoded_message)

    if(not root_node.has_left_child() and not root_node.has_right_child()):
        [freq, char] = root_node.get_value()
        for chr in encoded_message:
            decoded_str += char
        return decoded_str

    while(encoded_index < encode_length):
        [char, index] = traverse2decode(root_node, encoded_message, encoded_index)
        decoded_str += char
        encoded_index = index

    return decoded_str

def traverse2decode(node, message, index):

    #Base Case
    if(not node.has_left_child() and not node.has_right_child()):
        [freq, char] = node.get_value()
        return [char, index]

    if(message[index] == '0'):
        [char, out_index] = traverse2decode(node.get_left_child(), message, index + 1)
    if(message[index] == '1'):
        [char, out_index] = traverse2decode(node.get_right_child(), message, index + 1)

    return [char, out_index]


#TEST CASE 1
if __name__ == "__main__":
    codes = {}

    a_great_sentence = "        "

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    #should return 111111111

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the decoded data is: {}\n".format(decoded_data))
    #should return "        "

#TEST CASE 2
if __name__ == "__main__":
    codes = {}

    a_great_sentence = "aaaaaaaaaaaaaaaa"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    #should return  1111111111111111
    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the decoded data is: {}\n".format(decoded_data))
    #should return "aaaaaaaaaaaaaaaa"

#TEST CASE 3
if __name__ == "__main__":
    codes = {}

    a_great_sentence = "2456777_ADE"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    #should return 1100010110101110101000111100001111

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the decoded data is: {}\n".format(decoded_data))
    #should return 2456777_ADE
