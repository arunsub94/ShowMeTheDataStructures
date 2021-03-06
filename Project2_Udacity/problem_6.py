# UNION AND INTERSECTION OF LINKED LISTS
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

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
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    # Your Solution Here
    ll1_node = llist_1.head
    unionList = LinkedList()
    elementSet = set()
    while ll1_node:
        if (ll1_node.value not in elementSet):
            elementSet.add(ll1_node.value)
            unionList.append(ll1_node.value)
        ll1_node = ll1_node.next

    ll2_node = llist_2.head
    while ll2_node:
        if (ll2_node.value not in elementSet):
            elementSet.add(ll2_node.value)
            unionList.append(ll2_node.value)
        ll2_node = ll2_node.next

    return unionList

    pass

def intersection(llist_1, llist_2):
    # Your Solution Here
    intersectionList = LinkedList()
    ll1_node = llist_1.head
    ll2_node = llist_2.head
    elementSet = set()
    intersectionSet = set()
    while ll1_node:
      if(ll1_node.value not in elementSet):
          elementSet.add(ll1_node.value)
      ll1_node = ll1_node.next

    while ll2_node:
      if (ll2_node.value in elementSet and ll2_node.value not in intersectionSet):
          intersectionList.append(ll2_node.value)
          intersectionSet.add(ll2_node.value)
          elementSet.add(ll2_node.value)
      ll2_node = ll2_node.next

    return intersectionList
    pass


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
# output: 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 21 -> 32 -> 9 -> 1 -> 11 ->

print (intersection(linked_list_1,linked_list_2))
#output : 6 -> 4 -> 21 ->

print('----END------OF-------TEST-------CASE------')


# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [6,6,6,6,6,7,7,7,8,8,8]
element_2 = [0,0,0,0,0,5,5,5,5,6,6,6]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
#output : 6 -> 7 -> 8 -> 0 -> 5 ->
print (intersection(linked_list_3,linked_list_4))
#output: 6 ->
print('----END------OF-------TEST-------CASE------')

# Test case 3

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = [None]
element_2 = [3, 3, 3, 3, 3, 3, None]

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print (union(linked_list_5,linked_list_6))
#output: None -> 3 ->
print (intersection(linked_list_5,linked_list_6))
#output: None ->
print('----END------OF-------TEST-------CASE------')


"""
RUN TIME ANALYSIS

In both of my union and intersection functions, I have employed a while loop to iterate through each list (O(n)) and
a search operation on a set, which is O(1) on average due to the fact that sets are implemented as hash tables, and O(n) in the worst case.
This holds good for iterating through both linked lists and so, for the functions it's a time complexity of O(n + 1) explicitly on average,
and O(2n) worst-case but for all intents and practical purposes, the runtime of the function is O(n). This holds good for both functions.
"""
