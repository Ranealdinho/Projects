import pygame 
from settings import *
from tile import *
from player import *

class Level:
    def __init__(self):

        # get display surface
        self.display_surface = pygame.display.get_surface()

        # sprite group setup
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()

        # sprite setup
        self.create_map()

    def create_map(self):
        for row_index,row in enumerate(WORLD_MAP):
            for col_index,col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'x':
                    Tile((x,y),[self.visible_sprites])
                if col == 'p':
                    self.player = Player((x,y),[self.visible_sprites])

    def run(self):
        # # run the entire game
        self.visible_sprites.draw(self.display_surface)
        # self.visible_sprites.update()

        # update and draw the game
        pass