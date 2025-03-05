class Player:
    def __init__(self, name, tokens=0):
        self.name = name
        self.tokens = tokens

    def add_tokens(self, amount):
        self.tokens += amount

    def trade_tokens(self, other_player, amount):
        if self.tokens >= amount:
            self.tokens -= amount
            other_player.add_tokens(amount)
            print(f"{self.name} traded {amount} tokens with {other_player.name}")
        else:
            print(f"{self.name} doesn't have enough tokens")

if __name__ == "__main__":
    player1 = Player("Alice", 100)
    player2 = Player("Bob", 50)

    player1.trade_tokens(player2, 30)
    print(f"Alice's tokens: {player1.tokens}")
    print(f"Bob's tokens: {player2.tokens}")
