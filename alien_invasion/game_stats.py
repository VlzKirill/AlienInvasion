import os.path

class GameStats():
    """ Отслеживание статистики для игры"""
    def __init__(self, ai_game):
        """ Инициализирует статистику"""
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False
        self.high_score = self.check_saved_high_score()

    def reset_stats(self):
        """ Инициализирует статистику, меняющуюся в ходе игры"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def check_saved_high_score(self):
        highscore_filename = 'high_score.txt'
        check_file = os.path.exists(highscore_filename)
        if not check_file:
            return 0
        else:
            with open(highscore_filename) as file_object:
                saved_high_score = file_object.read().strip()
            return int(saved_high_score)