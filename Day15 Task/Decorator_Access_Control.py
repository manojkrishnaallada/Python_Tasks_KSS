#Decorator-based Access Control 
"""Scenario: 
Restrict access to certain functions. 
Task: 
● Create a decorator to check user role 
● Use condition inside decorator 
● Apply decorator to multiple functions 
● Store roles in a dictionary"""

# roles stored in dictionary
roles = {"alice": "admin", "bob": "user"}
 
 
# decorator to check role
def admin_only(func):
    def wrapper(user):
        if roles[user] == "admin":           # condition inside decorator
            func(user)
        else:
            print(user, "- access denied")
    return wrapper
 
 
# decorator applied to multiple functions
@admin_only
def delete_data(user):
    print(user, "deleted data")
 
 
@admin_only
def add_data(user):
    print(user, "added data")
 
 
delete_data("alice")
delete_data("bob")
add_data("alice")
add_data("bob")
