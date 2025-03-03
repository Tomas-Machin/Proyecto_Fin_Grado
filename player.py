class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.chips = 1000  # Cantidad inicial de fichas

    def bet(self, amount):
        if amount > self.chips:
            raise ValueError("No tienes suficientes fichas.")
        self.chips -= amount
        return amount

    def receive_card(self, card):
        self.hand.append(card)
