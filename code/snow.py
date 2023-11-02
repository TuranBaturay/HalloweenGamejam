import batFramework as bf

import pygame


class SnowParticle(bf.Particle):
    def __init__(
        self,
        start_pos,
        start_vel,
    ):
        super().__init__(start_pos,start_vel,duration=1000,color="white",size=(8,8))


    def update(self,dt):
        super().update(dt)
        
