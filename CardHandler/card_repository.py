import json
from typing import List

class CardRepository:
    def __init__(self, file_path):
        self.file_path = file_path
        self.cards = self.load_cards()

    def load_cards(self):
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_cards(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.cards, file, indent=4)

    def add_card(self, card):
        self.cards.append(card)
        self.save_cards()

    def get_all_cards(self):
        return self.cards

    def find_card_by_name(self, name):
        for card in self.cards:
            if card['name'] == name:
                return card
        return None