class UserNotFoundError(Exception):
    """Raise the exception when user not found."""
    def __init__(self, message=None, errors=None):
        #Calling the base class constructor with the parameter it needs
        super().__init__(message)
        # New for your custom code
        self.errors = errors

# Returning None by default
def get_user_from_db(id):
    pass
#Decided to synthesize one instead!
#return XUSER(f"XUSER_{id}_FIRST", f"XUSER_{id}_LAST", id % 100)
#return { "first_name" : f"XUSER_{id}_FIRST", "last_name" : f"XUSER_{id}_LAST", "age" : id % 100 }

def get_user_info(user_id):
    """Get user information from DB."""
    user = get_user_from_db(user_id)
    if not user:
        raise UserNotFoundError(f"No user found of this id: {user_id}")

user_id = 897867
get_user_info(user_id)

""" 
OUTPUT:
Traceback (most recent call last):
  File "custom_exception.py", line 23, in <module>
    get_user_info(user_id)
  File "custom_exception.py", line 20, in get_user_info
    raise UserNotFoundError(f"No user found of this id: {user_id}")
__main__.UserNotFoundError: No user found of this id: 897867
"""
