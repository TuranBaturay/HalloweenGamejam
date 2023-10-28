import batFramework as bf

class TitleScene(bf.Scene):

    def __init__(self): 
        super().__init__("title")

    def do_when_added(self):
        layout = bf.Column(gap = 10,shrink=True)
        c = bf.Container(
            layout,
            bf.Button("PLAY",lambda :self.manager.set_scene("game")),
            bf.Button("QUIT")
        ).add_constraint(bf.ConstraintCenter())
        self.root.add_child(c)
        d = bf.Debugger()
        d.add_dynamic_data("FPS",lambda : str(round(self.manager.get_fps())))
        self.root.add_child(d)
