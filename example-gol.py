from pgtemplate import *
import pygame
import random
import time

LINECOLOR = (20, 20, 20)
ALIVECOLOR = (0, 255, 0)
ROWS = 10
COLS = 10

UPDATEAFTER = 1


class Cell(object):

    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.alive = False
        self.future = None


class GOL(BaseGame):

    def __init__(self):
        BaseGame.__init__(self)
        self.runner.caption = 'Game Of Life'
        self.runner.screensize = 800, 600
        self.cellmap = [[] for x in range(ROWS)]
        for r in range(ROWS):
            self.cellmap[r] = [[] for x in range(COLS)]
            for c in range(COLS):
                cell = Cell(r, c)
                cell.alive = random.randint(0, 100) < 30
                self.cellmap[r][c] = cell
        self.last_update = time.time()

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.clearnext = True

    def draw_grid(self, screen):
        screen_width, screen_height = screen.get_width(), screen.get_height()
        cell_width = screen_width / COLS
        cell_height = screen_height / ROWS
        stroke_width = 2
        for x in range(COLS):
            xpos = (x + 1) * cell_width
            pygame.draw.line(
                screen, LINECOLOR, (xpos, 0), (xpos, screen_height), stroke_width)

        for y in range(ROWS):
            ypos = (y + 1) * cell_height
            pygame.draw.line(
                screen, LINECOLOR, (0, ypos), (screen_width, ypos), stroke_width)

    def get_cell_rect(self, screen, row, col):
        """return """
        screen_width, screen_height = screen.get_width(), screen.get_height()
        cell_width = screen_width / COLS
        cell_height = screen_height / ROWS
        x1, y1 = cell_width * col, cell_height * row,
        return x1, y1, cell_width, cell_height

    def update_game_state(self):
        now = time.time()
        if now - self.last_update < UPDATEAFTER:
            return
        self.last_update = now
        print "update game state"

        for r in range(ROWS):
            for c in range(COLS):
                cell = self.cellmap[r][c]
                cell.future = None
                neighbours_alive = 0
                for othercell_row in [-1, 0, 1]:
                    for othercell_col in [-1, 0, 1]:
                        if othercell_row == 0 and othercell_col == 0:
                            continue
                        if self.get_alive(r + othercell_row, c + othercell_col):
                            neighbours_alive += 1

                if cell.alive:
                    if neighbours_alive < 2 or neighbours_alive > 3:
                        cell.future = False
                else:
                    if neighbours_alive == 3:
                        cell.future = True

        for r in range(ROWS):
            for c in range(COLS):
                cell = self.cellmap[r][c]
                if cell.future != None:
                    cell.alive = cell.future
                    print "cell row=%s col=%s alive=%s" % (r, c, cell.alive)

    def get_alive(self, row, col):
        try:
            return self.cellmap[row][col].alive
        except IndexError:
            return False

    def draw(self, screen):
        screen.fill((0, 0, 0),)
        for r in range(ROWS):
            for c in range(COLS):
                if self.get_alive(r, c):
                    pygame.draw.rect(
                        screen, ALIVECOLOR, self.get_cell_rect(screen, r, c))

        self.draw_grid(screen)


if __name__ == '__main__':
    game = GOL()
    game.start()
