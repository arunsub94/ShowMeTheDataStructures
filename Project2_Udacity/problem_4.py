# ACTIVE DIRECTORY: USER NAME CHECKING

class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """

    if(group is None):
      return False

    userList = group.get_users()

    if user in userList:
      return True

    subgroupList = group.get_groups()

    for subgroup in subgroupList:
      return is_user_in_group(user, subgroup)

print(is_user_in_group("sub_child_user_2", child)) #should return False

print('----END------OF-------TEST-------CASE------')

child_user = "child_user"
child.add_user("child_user")

print(is_user_in_group(child_user, parent)) #should return True
print(is_user_in_group(child_user, child))  #should return True
print(is_user_in_group(child_user, sub_child)) #should return False

print('----END------OF-------TEST-------CASE------')

super_parent = Group("super parent")
super_parent.add_group(parent)

sub_child_user_2 = "sub_child_user_2"
sub_child.add_user(sub_child_user_2)

print(is_user_in_group(sub_child_user_2, super_parent)) #should return True

print('----END------OF-------TEST-------CASE------')
