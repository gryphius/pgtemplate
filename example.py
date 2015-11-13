from pgtemplate import *
import pygame
import random

class PGameExample(BaseGame):
    def __init__(self):
        BaseGame.__init__(self)
        self.runner.caption='DrawLines'
        self.runner.screensize = 800,600

        self.clearnext = False

    def handle_event(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.clearnext = True


    def draw(self,screen):
        if self.clearnext:
            screen.fill((0,0,0),)
            self.clearnext= False
        color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        width,height = self.runner.screensize
        startpos = (random.randint(0,width),random.randint(0,height))
        endpos = (random.randint(0,width),random.randint(0,height))
        pygame.draw.line(screen,color, startpos,endpos,5)


if __name__=='__main__':
    game = PGameExample()
    game.start()


