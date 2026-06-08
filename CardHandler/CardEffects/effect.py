from ATARI.AccountsHandler.player import Player 

class Effect:
    def __init__(self, action_type: str, description: str):
        self.action_type = action_type 
        self.description = description  

    def activate(self, game_engine, current_player : Player, opponent_player : Player):
        """
        Override this method in child classes to execute 
        the unique logic for this specific effect type.
        """
        raise NotImplementedError("Subclasses must implement the activate method!")
    
class HealEffect(Effect):
    def __init__(self, amount: int = 1):
        super().__init__(action_type="HEAL", description=f"Heal {amount} points.")
        self.amount = amount

    def activate(self, game_engine, current_player: Player, opponent_player: Player):
        current_player.heal(self.amount)

class DrawEffect(Effect):
    def __init__(self, amount: int = 1):
        super().__init__(action_type="DRAW", description=f"Draw {amount} cards.")
        self.amount = amount

    def activate(self, game_engine, current_player: Player, opponent_player: Player):
        for _ in range(self.amount):
            current_player.draw_card()