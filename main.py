import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTableWidgetItem,
    QTreeWidgetItem,
    QPushButton,
    QMessageBox,
)
from PyQt6.QtCore import QDateTime, Qt
from PyQt6.QtGui import QStandardItemModel, QStandardItem

from window import Ui_MainWindow

class Converter(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #физ величины для каждый категории
        self.units_dict = {
            'Длина': ['Миллиметры','Сантиметры', 'Метры', 'Километры'],
            'Масса': ['Миллраммы', 'Граммы', 'Килограммы', 'Тонны'],
            'Температура': ['Цельсии', 'Кельвины', 'Фаренгейты'],
            'Скорость': ['м/c', 'км/ч'],
            'Площадь': ['мм^2', 'см^2', 'м^2', 'км^2'],
            'Объем': ['мм^3', 'см^3', 'м^3', 'км^3'],
            'Время': ['Миллисекунды', 'Секунды', 'Минуты', 'Часы']
        }
        
        self.setup_connections()
        self.update_units()

    def setup_connections(self):
        #подключение сигналов нажатия
        self.ui.category_combo.currentTextChanged.connect(self.update_units)
        self.ui.swap_units_btn.clicked.connect(self.swap_units)
        self.ui.swap_currency_btn.clicked.connect(self.swap_currency_units)
        
    def update_units(self, category=None):
        if category is None:
            category = self.ui.category_combo.currentText()

        self.ui.from_unit_combo.clear()
        self.ui.to_unit_combo.clear()
        
        units = self.units_dict.get(category, [])
        
        self.ui.from_unit_combo.addItems(units)
        self.ui.to_unit_combo.addItems(units)

        if units:
            self.ui.from_unit_combo.setCurrentIndex(0) 
            self.ui.to_unit_combo.setCurrentIndex(1)

    def swap_units(self):
        first_unit_index = self.ui.from_unit_combo.currentIndex()
        second_unit_index = self.ui.to_unit_combo.currentIndex()
        self.ui.from_unit_combo.setCurrentIndex(second_unit_index) 
        self.ui.to_unit_combo.setCurrentIndex(first_unit_index)

    def swap_currency_units(self):
        first_unit_index = self.ui.from_currency_combo.currentIndex()
        second_unit_index = self.ui.to_currency_combo.currentIndex()
        self.ui.from_currency_combo.setCurrentIndex(second_unit_index) 
        self.ui.to_currency_combo.setCurrentIndex(first_unit_index)    




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Converter()
    window.show()
    sys.exit(app.exec())
    