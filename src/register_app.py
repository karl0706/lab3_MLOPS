# application, where users need to register. They need to fill in their username, email and password.
import re

def get_email_from_input():
    """ Contains '@' and '.' """
    email = input("Tell me your email: ")

    if ("@" not in email or "." not in email):
        print('Email is not valid.')
    else:
        return email
    
def get_user_name_from_input():
    """ Not empty string. No spaces. """
    username = input("Create your user name: ").strip()

    if not username:
        print('Please you need to give your username')
    elif " " in username:
        print('Please No space inside')
    else :
        return username

def get_password_from_input():
    """ 
    Password needs to be at least 8 characters long with
    at least one number, one special character and one letter.
    """
    mdp = input("Create your password: ").strip()

    if len (mdp) < 8: 
        print('Please you need to have at least 8 character')
    elif not re.search(r"[A-Za-z]", mdp):
        print("Error: Password must contain at least one letter.")
    elif not re.search(r"[0-9]", mdp):
        print("Error: Password must contain at least one number.")
    elif not re.search(r"[!@#$%^&*(),.?\":{}|<>]", mdp):
        print("Error: Password must contain at least one special character.")
    else:
        return mdp