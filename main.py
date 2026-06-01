import os
import sys

path_to_accounts = os.path.join(os.path.dirname(__file__), 'Accounts.json')
sys.path.append(os.path.dirname(__file__))

from account_manager import AccountManager

def main():
    print(path_to_accounts)
    account_manager = AccountManager(path_to_accounts)
    decklists = account_manager.get_decklist_for_account("Name")     
    print(decklists)

if __name__ == "__main__":
    main()