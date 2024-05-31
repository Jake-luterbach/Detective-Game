class Player:
    def __init__(self, locationX, locationY):
        self.locationX = locationX
        self.locationY = locationY

    def movement(self):
        self.locationX += 1
        self.locationY += 1

playerObject = Player(0, 0)

playerObject.movement()