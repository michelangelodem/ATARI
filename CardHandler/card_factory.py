from ATARI.CardHandler.CardEffects.effect import Effect
from ATARI.CardHandler.CardEffects.effect_parser import parse_effect
from ATARI.CardHandler.card_repository import CardRepository
from ATARI.CardHandler.card import Card

class CardFactory:
    def __init__(self, repository: CardRepository):
        self.repository = repository

    def create_card(self, name: str) -> Card:
        card_data = self.repository.find_card_by_name(name)
        if not card_data:
            raise ValueError(f"Card with name '{name}' not found in repository.")
        
        effect : list[Effect] = None
        if 'effect' in card_data:
            effect = parse_effect(card_data['effect'])
        
        return Card(
            name=card_data['name'],
            attack=card_data['attack'],
            defense=card_data['defense'],
            effect=effect
        )
    
    def create_match_deck(self, card_dict: dict[str, int]) -> list[Card]:
        deck = []
        for name in card_dict.keys():
            count = card_dict[name]
            for _ in range(count):
                deck.append(self.create_card(name))
        return deck
