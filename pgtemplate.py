import pygame
WHITE = (255, 255, 255)

class PGRunner(object):
    def __init__(self,event_callback=None, gamelogic_callback=None, draw_callback=None):
        self.caption = 'mygame'
        self.screensize = (700,500)
        self.fps=60
        self.screen = None
        self.event_callback = event_callback
        self.gamelogic_callback = gamelogic_callback
        self.draw_callback = draw_callback

        self.done = False
        self.fpsclock = pygame.time.Clock()

    def start(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.screensize)
        pygame.display.set_caption(self.caption)

        while not self.done:
            # --- Main event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
                    continue
                if self.event_callback:
                    self.event_callback(event)

            if self.gamelogic_callback:
                self.gamelogic_callback()
            if self.draw_callback:
                self.draw_callback(self.screen)

            pygame.display.flip()

            # --- Limit to 60 frames per second
            self.fpsclock.tick(self.fps)
        pygame.quit()



class BaseGame(object):
    def __init__(self):
        self.runner = PGRunner(event_callback=self.handle_event, gamelogic_callback=self.update_game_state, draw_callback=self.draw)

    def start(self):
        self.runner.start()

    def handle_event(self,event):
        pass

    def update_game_state(self):
        pass

    def draw(self,screen):
        pass

if __name__=='__main__':
    pass