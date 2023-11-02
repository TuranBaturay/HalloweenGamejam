import batFramework as bf
import pygame

GRAVITY = 10

class Player(bf.AnimatedSprite):
    def __init__(self)->None:
        super().__init__((16,16))
        self.actions = bf.ActionContainer(
            bf.Action("up").add_key_control(pygame.K_UP).set_holding(),
            bf.Action("down").add_key_control(pygame.K_DOWN).set_holding(),
            bf.Action("up").add_key_control(pygame.K_UP).set_holding(),
            bf.Action("down").add_key_control(pygame.K_DOWN).set_holding(),
        )
        self.speed : float = 20.0

        self.add_animState(
            "idle","assets/animations/player/idle.png",(16,16), [20,20]
        )
        self.set_animState("idle")

    def do_process_actions(self,event):
        self.actions.process_event(event)
        
    def do_reset_actions(self):
        self.actions.reset()
    
    def do_update(self,dt:float)->None:
        self.velocity.y += GRAVITY
        if self.actions.is_active("up"):
            self.velocity.x -= self.speed * dt
            self.set_flipX(True)
        if self.actions.is_active("down"):
            self.velocity.x += self.speed * dt
            self.set_flipX(False)

        self.move_by_velocity()
        self.velocity *= 0.65
        if self.rect.bottom >100 : self.set_y(100-self.rect.h)
