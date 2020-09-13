# ################################################################# #
# Active Directory - Add Users / Modify Users / Remove Users
#
#
#
#
#  ################################################################ #

import active_directory


server_name = '*****'
domain_name = '*****'
user_name = '*****'
password = '*****'


def menu_options():
    print("""\nActive Directory\n
    - Modify/Create/Remove Users from Active Directory Windows/Microsoft. 
        Find A User [0]
        Add a User [1]
        Find a computer [2]
        Show types of a group [3]
        List the groups a user is in [4]
    \n
    
    """)


def list_all_groups():
    for group in active_directory.search(objectClass='group'):
        print(group.cn)


def add_new_user():
    for group in active_directory.search(objectClass='group'):
        user_add = input("What username  do you want to add to the AD: ")


def find_a_user():
    print("INFO: Looking up user in Active Directory ")
    user = input("What user are you trying to lookup: ")
    user_find = active_directory.find_user(user)
    print(user_find)


def list_all_users():
    for user in active_directory.search("objectCategory='Person'", "objectClass='User'"):
        print(user)


def list_domain_controller_ad():
    print("INFO: Printing the list of the domain controllers for the active domain: ")


def show_members_of_group():
    me = active_directory.find_user()
    for group in me.memberOf:
        print("Members of group", group.cn)
        for group_member in group.member:
            print("   ", group_member)


def show_the_types_of_groups():
    me = active_directory.find_user()
    for group in me.memberOf:
        print("Group types for", group.cn, ":", ", ".join (group.groupType))


def list_domain_controllers_active_domain():
    for master in active_directory.root().masterBy:
        print (master.Parent.dNSHostName)


menu_options()
