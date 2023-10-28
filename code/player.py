import batFramework as bf
import pygame

class Player(bf.AnimatedSprite):
    def __init__(self):
        super().__init__((32,32))
        self.surface.fill("red")
        self.actions = bf.ActionContainer(
            bf.Action("up").add_key_control(pygame.K_UP).set_holding(),
            bf.Action("down").add_key_control(pygame.K_DOWN).set_holding(),
            bf.Action("left").add_key_control(pygame.K_LEFT).set_holding(),
            bf.Action("right").add_key_control(pygame.K_RIGHT).set_holding(),
        )
        self.speed : float = 100.0

    def do_update(self,dt:float)->None:
        self.velocity.x = self.speed *(
            int(self.actions.get("right").is_active()) - int(self.actions.get("left").is_active())
        )
        self.move_by_velocity()
