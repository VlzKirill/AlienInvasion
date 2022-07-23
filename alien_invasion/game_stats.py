class GameStats():
    """ Отслеживание статистики для игры"""
    def __init__(self, ai_game):
        """ Инициализирует статистику"""
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        """ Инициализирует статистику, меняющуюся в ходе игры"""
        self.ships_left = self.settings.ship_limit