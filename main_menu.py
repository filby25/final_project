import pygame

class MainMenu:
    """class to provide a menu with multiple play options"""

    def __init__(self, position, message, fontsize = 120):
        pygame.init()

        self.text_color = (60,210,40)
        self.bg_color = (34,52,32)
        self.font = pygame.font.SysFont('Futura', fontsize, True, False)
        self.img = self.font.render(message, True, self.text_color, self.bg_color)
        self.text_rect = self.img.get_rect()
        self.text_rect.center = position

    def display(self, screen):
        screen.fill((32,43,54))
        screen.blit(self.img, self.text_rect)