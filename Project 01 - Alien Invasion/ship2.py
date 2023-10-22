import pygame


class Ship:
    def __init__(self, pp_game):
        self.screen = pp_game.screen
        self.screen_rect = pp_game.screen.get_rect()

        self.image = pygame.image.load('images/KidRock.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)
