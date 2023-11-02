import batFramework as bf
import pygame
from typing import Self

class Meter(bf.Frame):
    def __init__(self,width:float=100,height:float=30,min_value:float=0,max_value:float=100,value:float|None=None,animation:bf.EasingAnimation=None)->None:
        self.value = value if value else min_value  
        self.max_value = max_value
        self.min_value = min_value
        self.animation_start_value:float = 0
        self.animation_target_value:float = 0

        if animation is None:
            self.animation = bf.EasingAnimation(
                easing_function = bf.Easing.LINEAR,
                duration=300,
                update_callback=self.animation_update,reusable=True
                )
        else:
            self.animation = animation

        self._meter_color = "red"
                
        super().__init__(width,height)
        self.set_outline_width(2)
        self.set_outline_color("white")
        self.set_color("black")

    def get_bounding_box(self):
        yield from super().get_bounding_box()
        yield pygame.FRect(*self.rect.topleft,self.rect.w*self.get_proportion(),self.rect.h).inflate(-1,-1)

    def animation_update(self,progression:float):
        delta = (self.animation_target_value - self.animation_start_value) * progression
        self._set_value_internal(self.animation_start_value + delta)
        
    def set_meter_color(self,color)->Self:
        self._meter_color = color
        self.build()
        return self

    def change_by(self,value:float)->None:
        self.set_value(min(max(self.value + value,self.min_value),self.max_value))
        
    def set_value(self,value:float)->None:
        if value < self.min_value or value > self.max_value: return
        # self.animation.end()
        self.animation_start_value = self.value
        self.animation_target_value = value
        self.animation.start()

    def _set_value_internal(self,value:float)->None:
        self.value = value
        self.build()

    def get_value(self)->float:
        return self.value

    def get_proportion(self) -> float:
        if self.max_value == self.min_value:
            return 0.0  # Handle the case where min_value is equal to max_value
        return (self.value - self.min_value) / (self.max_value - self.min_value)

    def _build_shape(self)->None:
        self.surface.fill(self._color)
        self.surface.fill(self._meter_color,(0,0,self.rect.w * self.get_proportion(),self.rect.h))

    def _build_rounded_shape(self)->None:
        self.surface.fill((0,0,0,0))
        pygame.draw.rect(
            self.surface,
            self._color,
            (0,0,*self.rect.size),
            0,
            *self._border_radius
        )
        if self.get_proportion()<0.05 : return
        r = self.rect.copy()
        r.midleft = self.rect.move(-self.rect.x,-self.rect.y).midleft
        r.w = self.rect.w * self.get_proportion()
        pygame.draw.rect(
            self.surface,
            self._meter_color,
            r,
            0,
            *self._border_radius
        )

