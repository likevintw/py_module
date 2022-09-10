

class Controller:
    def __init__(self): pass
    def up(self, handler): pass
    def down(self, handler): pass


class LG(Controller):
    def __init__(self): pass
    def up(self): ControllerLG().up_LG()
    def down(self): ControllerLG().down_LG()


class SONY(Controller):
    def __init__(self): pass
    def up(self): ControllerSONY().up_SONY()
    def down(self): ControllerSONY().down_SONY()


class ControllerLG:
    def __init__(self): pass
    def up_LG(self): print("up_LG")
    def down_LG(self): print("down_LG")


class ControllerSONY:
    def __init__(self): pass
    def up_SONY(self): print("up_SONY")
    def down_SONY(self): print("down_SONY")


class ControllerBridge:
    def __init__(self): pass
    def up(self, handler): handler.up()
    def down(self, handler): handler.down()


if __name__ == '__main__':
    controller = ControllerBridge()
    controller.up(LG())
    controller.up(SONY())
