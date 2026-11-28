#
# Class for the Hero
#
import pygame, math

class Hero():

    def __init__(self, xpos, ypos, screen):
        self.xpos = xpos
        self.ypos = ypos
        self.speed = 0
        self.angle = 0
        self.screen = screen
        self.hero_img=pygame.image.load('assets/arrow.png')
        self.speed = 0.1

    def move(self, rotation, speed):

        self.speed = 0.1 * speed
        self.angle += rotation * 0.1

        x_dif = self.speed * math.sin(math.radians(self.angle))
        y_dif = self.speed * math.cos(math.radians(self.angle))

        self.xpos += x_dif
        self.ypos += y_dif

    def draw(self):
        rotated_image = pygame.transform.rotate(self.hero_img,self.angle)
        # get width/height of image
        ht = rotated_image.get_height()
        wd = rotated_image.get_width()

        dx = self.xpos - (wd/2)
        dy = self.ypos - (ht/2)

        self.screen.blit(rotated_image, (dx, dy))
