"""A web application wants to ensure that users are authenticated before accessing 
sensitive functions. Create a decorator that checks whether the user is logged in before 
allowing access to a function."""


is_logged_in = False                                # False = user is not logged in

def login_required(func):                           # receives the original function
    def wrapper():                                  # this runs instead of the original function
        if is_logged_in:
            func()                                  # logged in -> run the original function
        else:
            print("Please login first")             # not logged in -> block it
    return wrapper

@login_required                                     # applies the decorator to view_account
def view_account():
    print("Showing account details")

view_account()                                      # not logged in -> blocked
is_logged_in = True                                 # user logs in now
view_account()                                      # allowed
