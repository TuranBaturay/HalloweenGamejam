import batFramework as bf
import pygame

GRAVITY = 50
GROUND_Y = 200
class Player(bf.AnimatedSprite):
    def __init__(self)->None:
        super().__init__((16,16))
        self.actions = bf.ActionContainer(
            bf.Action("up").add_key_control(pygame.K_UP).set_holding(),
        )
        self.speed : float = 20.0
        self.jump_force:float = 0
        self.jump_force_max:float = 400
        self.on_ground :bool = False
        self.ended_jump : bool = False
        self.started_jump : bool = False
        self.add_animState(
            "idle","assets/animations/player/idle.png",(64,64), [3, 2, 1, 1, 3, 4, 4, 3, 1, 1, 3, 4, 4]
        )
        self.set_animState("idle")

    def do_process_actions(self,event):
        self.actions.process_event(event)
        
    def do_reset_actions(self):
        self.actions.reset()

    
    def do_update(self,dt:float)->None:
        if self.actions.is_active("up"):
            if self.on_ground and not self.started_jump:
                self.on_ground = False
                self.jump_force = self.jump_force_max
                self.started_jump = True
                self.ended_jump = False
            if self.started_jump and not self.ended_jump:#already airborne
                self.velocity.y -= self.jump_force * dt
                self.jump_force*=0.7
                if round(self.jump_force,1) < 0.1:
                    self.ended_jump = True
                    self.started_jump = False
        else:
            self.ended_jump = True
            self.started_jump = False
            self.velocity.y += GRAVITY*dt
        if self.ended_jump:
            self.velocity.y += GRAVITY*dt
        # not pressing up

        self.move_by_velocity()
        if self.rect.bottom >GROUND_Y :
            self.set_y(GROUND_Y-self.rect.h)
            self.on_ground = True
            self.velocity.y = 0
        self.velocity *= 0.65
