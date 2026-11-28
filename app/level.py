#
# Draw out dungeon level 
#
import pygame

class Level:

    def __init__(self, width, height, screen):
        self.width = width
        self.height = height
        self.tiles = []
        for i in range(0,height):
            row = []
            for j in range(0,width):
                row.append('X')
            self.tiles.append(row)
        self.screen = screen
        self.tile_img=pygame.image.load('assets/tile2.png')

    def set_tile(self, x_pos, y_pos, tile_type):
        self.tiles[y_pos][x_pos] = tile_type

    def draw(self):
        for row in self.tiles:
            for x_pos in range(0,self.width):
                for y_pos in range(0,self.height):
                    # Initializing Color
                    color = (48, 141, 70)
                    # Drawing Rectangle
                    x_offset = x_pos * 32
                    y_offset = y_pos * 32
                    self.screen.blit(self.tile_img,(x_offset, y_offset))
                
