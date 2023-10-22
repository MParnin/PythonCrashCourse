import sys

import pygame


class PracticeProblem:

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Practice Problem 12-1")
        self.bg_color = (0, 0, 255)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)

            pygame.display.flip()


if __name__ == '__main__':
    pp = PracticeProblem()
    pp.run_game()
