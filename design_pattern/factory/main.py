

class Ball:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def show_information(self):
        print("name: ", self.name)
        print("color: ", self.color)


class Redball(Ball):
    def __init__(self):
        self.name = "redball"
        self.color = "red"


class Blueball(Ball):
    def __init__(self):
        self.name = "redball"
        self.color = "red"

class BallFactory:
    def __init__(self): pass

    def create_ball(self):
        return None

class RedballFactory(BallFactory):
    def __init__(self): pass

    def create_ball(self):
        return Redball()


class BlueballFactory(BallFactory):
    def __init__(self): pass

    def create_ball(self):
        return Redball()


if __name__ == '__main__':
    ball_1 = RedballFactory().create_ball()
    ball_2 = BlueballFactory().create_ball()
    ball_1.show_information()
    ball_2.show_information()
