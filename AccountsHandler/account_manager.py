import json
from typing import List
import os    

class AccountManager:
    def __init__(self, accounts_file: str):
        self.accounts_file = accounts_file
        self.accounts_data = self._load_accounts()


    def _load_accounts(self):
        if not os.path.exists(self.accounts_file):
            return {}
        with open(self.accounts_file, 'r') as f:
            return json.load(f)
        
    def get_decklist_for_account(self, account_name: str) -> List[dict[str, int]]:
        return self.accounts_data.get(account_name, {}).get('decklist', [])