# LRU CACHE IMPLEMENTATION
class Node:
    def __init__(self, value, key):
      self.value = value
      self.key = key
      self.next = None
      self.previous = None

class DoublyLinkedList:
    def __init__(self):
      self.head = None
      self.tail = None

    def append(self, value, key):
    #Function to append value to the DoublyLinkedList and return the address of the appended node
      if(self.head is None):
        self.head = Node(value, key)
        self.tail = self.head
      else:
        self.tail.next = Node(value, key)
        self.tail.next.previous = self.tail
        self.tail = self.tail.next
      return self.tail

    def remove_retrieve(self, address):
      node = address
      node_val = node.value
      node_key = node.key

      if(node == self.head):
        self.head = self.head.next
      elif (node == self.tail):
        self.tail.previous.next = None
        self.tail = self.tail.previous
      else:
        node.previous.next = node.next
        node.next.previous = node.previous
      return node_val, node_key

    def head_removal(self):
      if(self.head is None):
        self.head = None
        return None
      else:
        val = self.head.value
        key = self.head.key
        self.head.next.previous = None
        self.head = self.head.next
        return val, key

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables

        self.hash_dict = {}

        if(type(capacity) is not int):
            raise ValueError('Invalid input for LRU Cache size')
        elif(capacity <= 0):
            raise ValueError('Invalid input for LRU Cache size')
        else:
            self.capacity = capacity

        #Variable to keep track of capacity
        self.cache_counter = 0

        #Doubly linked list to store values that correspond to keys
        self.linked_list_cache = DoublyLinkedList()

        pass

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if(key in self.hash_dict):
          value, key = self.linked_list_cache.remove_retrieve(self.hash_dict[key])
          self.hash_dict.pop(key)
          self.cache_counter -= 1
          #Since the value has been retrieved, the node needs to go to be set to front of doubly Linked list
          self.set(key, value)
          #Return value corresponding to the key
          return value
        else:
          return -1
        pass

    def remove(self):
        #Remove the LRU element from cache, which is the head of the DoublyLinkedList
        removed_val, removed_key = self.linked_list_cache.head_removal()
        self.hash_dict.pop(removed_key)
        self.cache_counter -= 1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.

        if (self.cache_counter + 1 <= self.capacity):
            node_address = self.linked_list_cache.append(value, key)
            self.hash_dict[key] = node_address
            self.cache_counter += 1
        else:
            self.remove()
            node_address = self.linked_list_cache.append(value, key)
            self.hash_dict[key] = node_address
            self.cache_counter = self.capacity

# Test Case 1

try:
    our_cache = LRU_Cache(5)
except ValueError:
    print("Please revisit your input for cache size")
else:
    our_cache.set(1, 1);
    our_cache.set(2, 2);
    our_cache.set(3, 3);
    our_cache.set(4, 4);

    print(our_cache.get(1))       # returns 1
    print(our_cache.get(2))       # returns 2
    print(our_cache.get(9))     # returns -1 because 9 is not present in the cache

    our_cache.set(5, 5)
    our_cache.set(6, 6)

    print(our_cache.get(3))     # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

    print('----END------OF-------TEST-------CASE------')
# Test Case 2
try:
    our_cache_2 = LRU_Cache("haha")
except ValueError:
    print("Please revisit your input for cache size")
else:
    our_cache_2.set(1, 10);
    our_cache_2.set(2, 30);

    print(our_cache_2.get(1))   #should return 10
    print(our_cache_2.get(3))   #should return -1

    our_cache_2.set(3, None)
    our_cache_2.set(4, 85)

    print(our_cache_2.get(3)) #should return None

    print('----END------OF-------TEST-------CASE------')

try:
    our_cache_3 = LRU_Cache(0)
except ValueError:
    print("Please revisit your input for cache size")
else:
    our_cache_3.set(1, 10)
    our_cache_3.set(2, 20)

    print(our_cache_3.get(1))

    print('----END------OF-------TEST-------CASE------')
