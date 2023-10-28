import batFramework as bf
import code.player as Player

class GameScene(bf.Scene):
    def __init__(self): 
        super().__init__("game")
        self.set_clear_color("gray20")
        
    def do_when_added(self):
        self.root.add_child(bf.Button(
            "<",
            lambda : self.manager.set_scene("title")
        ))
        d = bf.Debugger()
        d.add_dynamic_data("FPS",lambda : str(round(self.manager.get_fps())))
        self.root.add_child(d)
