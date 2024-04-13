from sky_api import SkyAccount
from login_handler import LoginHandler
from rich import print
# import pyperclip

def get_user_credentials():
    login_type = {
        '1': 'Nintendo',
        '2': 'Lua Code',
        '3': 'Google Code',
        '4': 'Steam',
        '5': 'Huawei',
        '6': 'Facebook',
        '7': 'Sony'
    }

    print('''
    Login Methods:
    -----------------------      
        1. Nintendo
        2. Lua Code
        3. Google Code
        4. Steam
        5. Huawei
        6. Facebook
        7. Playstation
''')

    login_method = input("Select a login method (1 - 7): ")

    if login_method not in login_type:
        print("Invalid login method. Please select 1 - 7.")
        return None, None
    elif login_method == '2':
        lua_code = input("Enter Lua code: ")
        login_handler = LoginHandler(login_method)
        user_id, session = login_handler.lua_handler(lua_code)
    else:
        print(f"Copy this link to your clipboard: https://live.radiance.thatgamecompany.com/account/auth/oauth_signin?type={login_type[login_method]}&token=")
        code = input("Enter the code: ")
        print(code)

        login_handler = LoginHandler(login_method)
        user_id, session = login_handler.login(code)
    
    print(user_id,session)
    return user_id, session


def execute_user_option(option, sky_account):
    if option == 1:
        # Test get_all_friends
        friend_uuids = sky_account.get_all_friends()
        print("All Friends UUIDs:", friend_uuids)
    elif option == 2:
        # Test get_all_blocked_friends
        blocked_friend_uuids = sky_account.get_all_blocked_friends()
        print("All Blocked Friends UUIDs:", blocked_friend_uuids)
    elif option == 3:
        # Test set_all_friends_blocked
        set_block = True  # Set to False if you want to unblock
        sky_account.set_all_friends_blocked(set_block)
        print("All friends blocked successfully!")
    elif option == 4:
        # Test set_all_blocked_friends_unblocked
        sky_account.set_all_blocked_friends_unblocked()
        print("All blocked friends unblocked successfully!")
    elif option == 5:
        # Test set_all_blocked_friends_unblocked
        sky_account.get_iap_list()
    else:
        print("Invalid option. Please select a valid option.")

# Get user credentials dynamically
user_id_input, session_input = get_user_credentials()

def features():
    if user_id_input and session_input:
        sky_account = SkyAccount(user_id_input, session_input)

        # Prompt user for action
        print("Options:")
        print("1. Get all friends")
        print("2. Get all blocked friends")
        print("3. Block all friends")
        print("4. Unblock all blocked friends")
        print("5. List iap")

        selected_option = int(input("Select an option (1-5): "))

        # Execute the selected option
        execute_user_option(selected_option, sky_account)
        features()

features()