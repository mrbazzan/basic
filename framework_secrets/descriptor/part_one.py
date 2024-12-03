
import random

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def __get__(self, instance, owner):
        print(instance, owner)
        return int(random.random() * self.sides)


class Game:
    d6 = Die()
    d10 = Die(10)


if __name__ == "__main__":
    print(Game.d6)
    print(Game.d10)

    game = Game()
    print(game.d6)

