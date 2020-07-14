UNION AND INTERSECTION OF LINKED LISTS

In both of my union and intersection functions, I have employed a while loop to iterate through each list (O(n)) and
a search operation on a set, which is O(1) on average due to the fact that sets are implemented as hash tables, and O(n) in the worst case.
This holds good for iterating through both linked lists and so, for the functions it's a time complexity of O(n + 1) explicitly on average,
and O(2n) worst-case but for all intents and practical purposes, the runtime of the function is O(n). This holds good for both functions.
