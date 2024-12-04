
import random

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def __get__(self, instance, owner):
        print(f"INSTANCE: {instance}, OWNER: {owner}")
        return int(random.random() * self.sides)


class Game:
    def __init__(self):
        self.x = 8
        # self.d6 = 8  # print(g.d6)  # g.__dict__['d6']

    d6 = Die()
    d10 = Die(10)


if __name__ == "__main__":
    print(Game.d6)  # --> Game.__dict__['d6'].__get__(None, Game)
    print(Game.d10)

    g = Game()
    print(g.d6)  # {g.__dict__['d6'] | type(g).__dict__['d6']}.__get__(g, type(g))

    print(g.__dict__)
    g.d6 = 5  # --> non-data descriptor overriden by instance dictionary
    print(g.d6)

    # entries in instance dictionary
       # data descriptor > instance dictionary > non-data descriptor

