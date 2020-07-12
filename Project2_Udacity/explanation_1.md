
LRU CACHE IMPLEMENTATION

For this problem, I have chosen to employ a doubly Linked List to keep track
of the LRU Cache. The choice of data structure was motivated by the following reasons:

    1. The data structure needs to keep track of the order in which the LRU cache
    elements are added/accessed.

    2. The data structure needs to be dynamically modified to reflect most used and least
    used elements in the cache.

In light of these considerations, the doubly linked list was employed. It also helps
that since it is a linked list, removal/retrieval operations are O(1) time complexity.

A dictionary was used to keep track of "active" keys in the dictionary. Again, this was motivated by efficiency with retrieval/search operations taking O(1) time complexity with the dictionary. Hence, the time complexity
of the LRU Cache operations can be said to be O(1).

In terms of space complexity, the doubly linked list is O(n) and the dictionary is also O(n).
Hence, the space complexity is O(n).
