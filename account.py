from card import Card
from typing import List
from card_factory import CardFactory
from account_manager import AccountManager

class Account:
    def __init__(self, name: str, password: str, factory: CardFactory, account_manager: AccountManager):
        self.name = name
        self.password = password
        self.factory = factory
        self.account_manager = account_manager
        
        self.is_logged_in = False
        self.deckList: List[List[Card]] = []

    def set_decklist(self, raw_deck_data: List[List[str]]):
        self.deckList = []
        
        for deck in raw_deck_data:
            self.deckList = self.account_manager.get_decklist_for_account(self.name)

    def get_decklist(self) -> List[List[Card]]:
        return self.deckList
    
    def login(self, password: str) -> bool:
        if self.password == password:
            self.is_logged_in = True
            return True
        return False
    
    def logout(self):
        self.is_logged_in = False
    

