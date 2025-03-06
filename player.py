class Player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand
        self.chips = 1000  # Cantidad inicial de fichas
        self.position = None

    def bet(self, amount):
        if amount > self.chips:
            raise ValueError("No tienes suficientes fichas.")
        self.chips -= amount
        return amount

