
from window import Ui_MainWindow
# Категории исключений
class LogicError(Exception):

    def negative_value(self, category):
        return f'Вы не можете конвертировать отрицательные значения в категории "{category}"'

    def zero_kelvin_unit_1(self):
        return '0 по Кельвину - это абсолют!'
    
    def zero_kelvin_unit_2(self):
        return 'Такие температуры невозможны (0 по Кельвину)'

    
