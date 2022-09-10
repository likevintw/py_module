

class MagicWater:
    def __init__(self):
        self.name = None
        self.hp = None
        self.mp = None

    def drink_water(self, hp, mp):
        print("drink {}".format(self.name))
        print("{}+{}".format(self.hp, self.mp))
        return hp, mp


class WhiteWater:
    def drink_water(self, hp, mp):
        self.name = "White"
        self.hp = 80
        self.mp = 0
        print("drink {}".format(self.name))
        print("{}+{}".format(self.hp, self.mp))
        print("")
        return hp+self.hp, mp+self.mp


class BlueWater:
    def drink_water(self, hp, mp):
        self.name = "Blue"
        self.hp = 0
        self.mp = 20
        print("drink {}".format(self.name))
        print("{}+{}".format(self.hp, self.mp))
        print("")
        return hp+self.hp, mp+self.mp


class Role:
    def __init__(self, name):
        self.name = name
        self.hp = 1
        self.mp = 0

    def drink_water(self, water):
        self.hp, self.mp = water.drink_water(self.hp, self.mp)

    def show_hp_mp(self):
        print("name: ", self.name)
        print("hp: ", self.hp)
        print("mp: ", self.mp)
        print("")


if __name__ == '__main__':
    bule_water = BlueWater()
    #
    john = Role("john")
    john.show_hp_mp()
    #
    john.drink_water(bule_water)
    john.show_hp_mp()
    #
    white_water = WhiteWater()
    #
    john.drink_water(white_water)
    john.show_hp_mp()
