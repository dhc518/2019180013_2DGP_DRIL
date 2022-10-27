class Player:
    name = 'Player'

    def __init__(self):
        self.x = 100


    def where(self):
        print(self.x)


player = Player()
player.where()

print(Player.name)
print(player.name)

Player.where(player)