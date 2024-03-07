from sky_api import SkyAccount
from login_handler import LoginHandler
from rich import print

def get_user_credentials():
    print("Login methods:")
    print("1. Nintendo")
    print("2. Lua Code")

    login_method = input("Select a login method (1 or 2): ")

    if login_method == "1":
        nintendo_id = input("Enter Nintendo player code: ")

        login_handler = LoginHandler(login_method)
        user_id, session = login_handler.login_nintendo(nintendo_id)
    elif login_method == "2":
        lua_code = input("Enter Lua code: ")
        login_handler = LoginHandler(login_method)
        user_id, session = login_handler.lua_handler(lua_code)
    else:
        print("Invalid login method. Please select 1 or 2.")
        return None, None

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

        selected_option = int(input("Select an option (1-4): "))

        # Execute the selected option
        execute_user_option(selected_option, sky_account)
        features()

features()