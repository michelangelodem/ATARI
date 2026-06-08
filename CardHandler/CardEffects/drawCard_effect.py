from ATARI.CardHandler.CardEffects.card_effect import CardEffect

class DrawCardEffect(CardEffect):
    def __init__(self, description = "Draw a card from your deck."):
        self.description = description

    def trigger(self, game_state, user_player, opponent_player) override:
        print(f"{user_player.name} activates effect: {self.description}")
        user_player.draw_card()