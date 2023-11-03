import batFramework as bf
import code
from typing import Self
import pygame
from code.meter import Meter
GROUND_Y = 200

class GameScene(bf.Scene):
    def __init__(self): 
        super().__init__("game")
        self.set_clear_color((0,0,0,180))
        self.bg1 = bf.Image("assets/images/background.png").set_y(self.camera.get_center()[1]-150)
        self.bg2 = bf.Image("assets/images/background.png").set_y(self.camera.get_center()[1]-150)
        self.bg2.set_x(self.bg1.rect.right)
        self.add_world_entity(self.bg1,self.bg2)

        
        self.player = code.Player()
        self.add_world_entity(self.player.set_center(*self.hud_camera.get_center()))
        self.camera.set_follow_dynamic_point(lambda : self.player.rect.move(0,-80).center)
        # self.meter = Meter().add_constraint(bf.ConstraintAnchorTopRight()).set_border_radius(10)
        # self.root.add_child(self.meter)

        
        self.add_action(
            bf.Action("more").add_key_control(pygame.K_RIGHT),
            bf.Action("less").add_key_control(pygame.K_LEFT)
        )

        self.add_world_entity(bf.Frame(200,100).set_position(0,100))

        self.duck = bf.AnimatedSprite()
        self.duck.add_animState(
            "run",
            "assets/animations/duck/run.png",
            (256,256),
            [1, 3, 5, 6, 3, 4, 1, 3, 5, 3, 6, 3, 4]
            
        )
        self.duck.set_animState("run")
        self.add_world_entity(self.duck)
        self.duck.set_y(GROUND_Y -self.duck.rect.h)
        
    def do_when_added(self):
        # self.root.add_child(bf.Button(
        #     "<",
        #     lambda : self.manager.set_scene("title")
        # ))
        d = bf.Debugger()
        d.add_dynamic_data("FPS",lambda : str(round(self.manager.get_fps())))
        self.root.add_child(d)
        # bf.EasingAnimation("test",bf.Easing.EASE_IN_OUT,1000,end_callback = lambda  : self.meter.set_value(0 if self.meter.get_value()!=0 else 100),loop=True).start()


    def do_update(self,dt):
        self.bg1.set_x(self.bg1.rect.x - int(100 * dt))
        self.bg2.set_x(self.bg2.rect.x - int(100 * dt))
        if self.bg1.rect.right < self.camera.rect.left : 
            self.bg1.set_x(self.camera.rect.right)
        if self.bg2.rect.right < self.camera.rect.left : 
            self.bg2.set_x(self.camera.rect.right)
