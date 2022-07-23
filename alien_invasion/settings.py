class Settings:
    """ Класс для хранения всех настроек игры Alien Invasion"""

    def __init__(self):
        """Инициализирует настройки игры"""
        # Параметры экрана
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.alien_speed = 0.1
        self.fleet_drop_speed = 20
        #fleet_direction 1: движение вправо, -1: движение влево
        self.fleet_direction = 1

        # Настройки корабля
        self.ship_speed = 0.5
        self.ship_limit = 3

        # Параметры снаряда (пули)
        self.bullet_speed = 1.5
        self.bullet_width = 3000
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Темп ускорения игры
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """ Инициализирует настройки, изменяющиеся в ходе игры"""
        self.ship_speed = 0.5
        self.bullet_speed = 1.5
        self.alien_speed = 0.1

        # fleet_direction=1 означает движение вправо, -1 -влево
        self.fleet_direction = 1

    def increase_speed(self):
        """ Увеличивает настройки скорости"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale