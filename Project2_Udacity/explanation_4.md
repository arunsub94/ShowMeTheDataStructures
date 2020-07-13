
ACTIVE DIRECTORY: USER NAME CHECKING

The recursive function of this problem could in the worst case have to explore
the entire depth going all the way to the last sub-group. To illustrate with an example,

PARENT
USER14
  CHILD1  
    SUBCHILD1
      USER1
      USER2
    SUBCHILD2
      USER3
  CHILD2
    SUBCHILD3
      USER4
    SUBCHILD4
      USER5
    SUBCHILD5
      USER6
  CHILD3
  USER12  
    SUBCHILD6
      USER7
    SUBCHILD7
      USER8
      USER9
    SUBCHILD8
      USER10
    SUBCHILD9
      USER11
  CHILD4
    SUBCHILD10
      USER13
      USER15

In the above example of the active directory, the user could be in any level of group and within any group.
The function is_user_in_group() would begin with group parent, and then recursively be called 4 times for each child, then will be called 10 times for each sub_child and then 15 times foe each user. This results in a total of 30 items to be iterated through to check if user is present or not, in the worst case.

Hence, in the worst case, the function would end up checking all items. Hence, the time complexity would be O(n) where n is the total number of items(all sub-groups and users). In terms of space complexity, since a list of users is employed at each
level the space complexity is O(n).
