import batFramework as bf
import pygame
import scenes

bf.init(
    (360,240),
    resource_path = "data",
    flags=pygame.SCALED,
    window_title="Game",
    default_font = "fonts/p2p.ttf",
    default_text_size=8
)

bf.Manager(
    scenes.TitleScene(),
    scenes.GameScene(),
).run()

