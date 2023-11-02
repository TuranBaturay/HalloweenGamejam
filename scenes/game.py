import batFramework as bf
import code
from typing import Self
import pygame
from code.meter import Meter

class GameScene(bf.Scene):
    def __init__(self): 
        super().__init__("game")
        self.set_clear_color("gray20")
        self.player = code.Player()
        self.add_world_entity(self.player.set_center(*self.hud_camera.get_center()))
        self.camera.set_follow_dynamic_point(lambda : self.player.rect.center)
        self.meter = Meter().add_constraint(bf.ConstraintAnchorTopRight()).set_border_radius(10)
        self.root.add_child(self.meter)
        self.add_action(
            bf.Action("more").add_key_control(pygame.K_RIGHT),
            bf.Action("less").add_key_control(pygame.K_LEFT)
        )

        self.add_world_entity(bf.Frame(200,100).set_position(0,100))

    def do_when_added(self):
        self.root.add_child(bf.Button(
            "<",
            lambda : self.manager.set_scene("title")
        ))
        d = bf.Debugger()
        d.add_dynamic_data("FPS",lambda : str(round(self.manager.get_fps())))
        self.root.add_child(d)
        # bf.EasingAnimation("test",bf.Easing.EASE_IN_OUT,1000,end_callback = lambda  : self.meter.set_value(0 if self.meter.get_value()!=0 else 100),loop=True).start()

    def do_handle_event(self,event)->None:
        if self.actions.is_active("more"):
            self.meter.change_by(10)
        if self.actions.is_active("less"):
            self.meter.change_by(-10)
