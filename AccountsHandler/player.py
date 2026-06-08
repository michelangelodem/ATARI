from typing import List
from ATARI.CardHandler.card import Card
from ATARI.AccountsHandler.account import Account
from ATARI.CardHandler.card_factory import CardFactory
 
class Player:
    def __init__(self, factory: CardFactory, account: Account, HP_MAX_SCORE: int):
        self.account = account
        self.score = HP_MAX_SCORE
        self.HP_UPPER_LIMIT = 10 * HP_MAX_SCORE
        self.factory = factory

        self.deck: List[Card] = []
        self.hand: List[Card] = []
        self.graveyard: List[Card] = []
        self.field: List[Card] = []
        self.discard_pile: List[Card] = []


    def __str__(self):
        return f"{self.account.name}: {self.score} points"
    
    def take_damage(self, damage: int):
        self.score -= damage
        if self.score < 0:
            self.score = 0

    def heal(self, heal_amount: int):
        self.score += heal_amount
        if self.score > self.HP_UPPER_LIMIT:
            self.score = self.HP_UPPER_LIMIT

    def choose_deck(self, deck_index: int):
        decklists : List[dict[str, int]] = self.account.get_decklist()
        
        if 0 <= deck_index < len(decklists):
            chosen_dict = decklists[deck_index]
            self.deck = self.factory.create_match_deck(chosen_dict)
        else:
            raise ValueError("Invalid deck index")

    def draw_card(self):
        if self.deck:
            card = self.deck.pop(0)
            self.hand.append(card)
        else:
            raise Exception("Deck is empty, cannot draw a card.")
        
    