from typing import List
from card import Card
from account import Account

class Player:
    def __init__(self, account: Account, HP_MAX_SCORE: int):
        self.account = account
        self.score = HP_MAX_SCORE
        self.HP_UPPER_LIMIT = 10 * HP_MAX_SCORE

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
        if 0 <= deck_index < len(self.account.get_decklist()):
            self.deck = self.account.get_decklist()[deck_index]
        else:
            raise ValueError("Invalid deck index")

    def draw_card(self):
        if self.deck:
            card = self.deck.pop(0)
            self.hand.append(card)
        else:
            raise Exception("Deck is empty, cannot draw a card.")
        
    