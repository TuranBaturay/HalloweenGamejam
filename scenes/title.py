import batFramework as bf

class TitleScene(bf.Scene):

    def __init__(self): 
        super().__init__("title")

    def do_when_added(self):
        layout = bf.Column(gap = 10,shrink=True).set_child_constraints(bf.ConstraintPercentageWidth(1))
        c = bf.Container(
            layout,
            bf.Button("PLAY",lambda :self.manager.set_scene("game")).set_autoresize(False),
            bf.Button("QUIT",self.manager.stop).set_autoresize(False)
        ).add_constraint(bf.ConstraintCenter())
        self.root.add_child(c)
        d = bf.Debugger()
        d.add_dynamic_data("FPS",lambda : str(round(self.manager.get_fps())))
        self.root.add_child(d)
