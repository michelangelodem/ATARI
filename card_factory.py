from CardEffects.card_effect import CardEffect
from card_repository import CardRepository
from card import Card

class CardFactory:
    def __init__(self, repository: CardRepository):
        self.repository = repository
        
    def create_card(self, name: str) -> Card:
        card_data = self.repository.find_card_by_name(name)
        if not card_data:
            raise ValueError(f"Card with name '{name}' not found in repository.")
        
        effect = None
        if 'effect' in card_data:
            effect = CardEffect(card_data['effect']['description'])
        
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
