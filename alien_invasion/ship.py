import pygame

class Ship():
    """Класс управления кораблем"""
    def __init__(self, ai_game_screen):
        """Инициализирует корабль и задает его начальную позицию"""
        self.screen = ai_game_screen
        self.screen_rect = ai_game_screen.get_rect()

        # Загружает изображение корабля и получает прямоугольник
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        # Каждый новый корабль появляется у нижнего края экрана
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """ Рисует корабль в текущей позиции """
        self.screen.blit(self.image, self.rect)
