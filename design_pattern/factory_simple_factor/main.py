

class RoleFactor:
    def __init__(self, name):
        self.name = name
        self.hp = hp
        self.mp = mp

    def show_information(self):
        print("name: {}\nhp:{}\nmp:{}".format(self.name, self.hp, self.mp))


class Archer(RoleFactor):
    def __init__(self, name):
        self.name = name
        self.hp = 50
        self.mp = 50


class Warrior(RoleFactor):
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.mp = 10


class RoleHandler:
    def __init__(self, career, name):
        self.career = career
        self.name = name
        pass

    def create_role(self):
        if self.career == "archer":
            return Archer(self.name)
        if self.career == "warrior":
            return Warrior(self.name)

        # Add new career here
        # if career == "Priest":
        #     return Priest(name)

        return None


if __name__ == '__main__':
    john = RoleHandler("warrior", "john").create_role()
    john.show_information()
    may = RoleHandler("archer", "may").create_role()
    may.show_information()
