from typing import List, Optional

from ATARI.CardHandler.CardEffects.effect import Effect

class Card:
    def __init__(self, name: str, attack: int, defense: int, effect: Optional[List[Effect]] = None):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.effect = effect
        self.is_summoned = False
        self._summon()

    def __str__(self):
        return f"Card({self.name}, {self.attack}, {self.defense})"

    def _summon(self):
        self.is_summoned = True
        print("Card summoned:", self)

    def activate_effect(self, game_state, user_player, opponent_player):
        if not self.is_summoned:
            raise Exception("Card must be summoned before it can take action.")
        print("Took action with card:", self)
        if self.effect:
            for effect in self.effect:
                effect.activate(game_state, user_player, opponent_player)

    def take_damage(self, damage: int):
        self.defense -= damage
        print(f"{self.name} takes {damage} damage, remaining defense: {self.defense}")
        if self.defense <= 0:
            self.destroy()

    def destroy(self):
        print(f"{self.name} is destroyed!")
        self.is_summoned = False

    
    