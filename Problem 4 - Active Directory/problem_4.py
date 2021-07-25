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


def is_user_in_group(user, group, output=False):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """

    if user in group.users:
        return True

    for sub_group in group.groups:
        if output:
            break
        else:
            output = is_user_in_group(user, sub_group, output)

    return output


# construct an active directory for test cases
super_group = Group("super_group")
group_1 = Group("group_1")
group_2 = Group("group_2")
sub_group_1 = Group("sub_group_1")
sub_group_2 = Group("sub_group_2")
sub_group_3 = Group("sub_group_3")
sub_group_4 = Group("sub_group_4")

user_1 = "user_1"
user_2 = "user_2"
user_3 = "user_3"
user_4 = "user_4"
user_5 = "user_5"
user_6 = "user_6"
user_7 = "user_7"
user_8 = "user_8"

super_group.add_user(user_1)

super_group.add_group(group_1)
super_group.add_group(group_2)

group_1.add_group(sub_group_1)
group_1.add_group(sub_group_2)
group_2.add_group(sub_group_3)
group_2.add_group(sub_group_4)

super_group.add_user(user_1)
group_1.add_user(user_2)
group_2.add_user(user_3)
sub_group_1.add_user(user_4)
sub_group_2.add_user(user_5)
sub_group_3.add_user(user_6)
sub_group_4.add_user(user_7)

# Test Case 1 - User not in the group
print('Test Case 1 - Is user_8 in super_group? ')
print('Answer:', is_user_in_group(user_8, super_group)) # return False

# Test Case 2 - Search a lower group for a higher group user_1
print('Test Case 2 - Is user_1 in group_2? ')
print('Answer:', is_user_in_group(user_1, group_2)) # return False

# Test Case 3 - Search a user in the grupp
print('Test Case 3 - Search users in each group level')
print('Is user_1 in super_group?')
print(is_user_in_group(user_1, super_group))  # return True
print('Is user_2 in group_1?')
print(is_user_in_group(user_2, group_1))  # return True
print('Is user_7 in super_group?')
print(is_user_in_group(user_7, super_group))  # return True

# Test Case 4 - empty group
empty_group = Group('empty_group')
print('Is user in the empty_group?')
print(is_user_in_group('user', empty_group))
