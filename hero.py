#
# Class for the Hero
#
import pygame

class Hero():

    def __init__(self, xpos, ypos, screen):
        self.xpos = xpos
        self.ypos = ypos
        self.screen = screen
        self.hero_img=pygame.image.load('assets/hero.png')
        self.speed = 0.1

    def move(self, xdir, ydir):
        self.xpos += xdir * self.speed
        self.ypos += ydir * self.speed

    def draw(self):
        self.screen.blit(self.hero_img,(self.xpos, self.ypos))

