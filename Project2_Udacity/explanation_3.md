HUFFMAN CODING IMPLEMENTATION

For the encoding part of the implementation, I have chosen to employ a
minheap as a proxy for a priority queue using Python's heapq. The insert, delete and
remove operations on a min heap have a worst case complexity of O(logn) and so,
this is the most efficient choice of data structure for the encoding process. The
while loop to pop the elements from the heap & reinsert into tree are O(n). Hence, the
encoding algorithm will have a time complexity of O(nlogn).

The recursive function to traverse from root to leaf and encode is of time
complexity O(n). The decoding function would also have a time complexity of
O(nlogn) since there are n iterations in the while loop, with each iteration taking
O(logn) to traverse the heap tree.

The worst case space complexity for the heap is O(n). 
