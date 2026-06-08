class CardEffect:
    def __init__(self, description: str):
        self.description = description

    def trigger(self, game_state, user_player, opponent_player):
        """Override this method to define what the card actually does."""
        pass