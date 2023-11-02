import batFramework as bf

class Room(bf.Entity):
    def __init__(self,data):
        super().__init__()
        self.load(data)
    def load(self,data):
        pass


class Level(bf.Entity):
    def __init__(self):
        super().__init__(no_surface=True)
        self.room = Room({})
