import batFramework as bf
from gameConst import GameConstants as gconst

class Defaults:
    @staticmethod
    def init():
        # Load tileset
        bf.utils.load_tileset("assets/tilesets/tileset.png", "tileset", gconst.TILE_SIZE)
