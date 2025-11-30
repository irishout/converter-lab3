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

from coefficients_and_categorys import units_dict
from converter_logic import Physical_operations, Currency_operations
from exeptions import *

class Converter(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #физ величины для каждый категории
        self.units_dict = units_dict
        
        self.setup_connections()
        self.update_units()
        self.currency_operator = Currency_operations()
        

    def setup_connections(self):
        #подключение сигналов нажатия
        self.ui.category_combo.currentTextChanged.connect(self.update_units)
        self.ui.swap_units_btn.clicked.connect(self.swap_units)
        self.ui.swap_currency_btn.clicked.connect(self.swap_currency_units)

        self.ui.convert_btn.clicked.connect(self.convert_physical_units)
        self.ui.from_value_edit.returnPressed.connect(self.convert_physical_units)

        self.ui.convert_currency_btn.clicked.connect(self.convert_currency_units)
        
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

        if self.ui.from_value_edit.text():
            tmp = self.ui.from_value_edit.text()
            self.ui.from_value_edit.setText(self.ui.to_value_edit.text())
            self.ui.to_value_edit.setText(tmp)
            self.convert_physical_units()

    def swap_currency_units(self):
        first_unit_index = self.ui.from_currency_combo.currentIndex()
        second_unit_index = self.ui.to_currency_combo.currentIndex()
        self.ui.from_currency_combo.setCurrentIndex(second_unit_index) 
        self.ui.to_currency_combo.setCurrentIndex(first_unit_index)
        

    def convert_physical_units(self):
        self.ui.label_8.setText('')
        operator = Physical_operations()
        category = self.ui.category_combo.currentText()
        unit_1 = self.ui.from_unit_combo.currentText()
        unit_2 = self.ui.to_unit_combo.currentText()
        value = self.ui.from_value_edit.text()

        if ',' in value:                        #Проверка на запись дробного числа через ","
            value = value.replace(',', '.')
        try:
            float_value = float(value)
            edited_value = operator.convert_physical(category, unit_1, unit_2, float_value)
        except:
            self.ui.label_8.setText('Произошла ошибка: введите значение')
            self.ui.to_value_edit.setText('')
            return None            
        
        #Исключения
        exceptions = LogicError()
        messege = None
        if float(value) < 0 and category != 'Температура': #отрицательное значение
            messege = exceptions.negative_value(category)

        elif unit_1 == 'Кельвины' and float(value) < 0: #0 по кельвину
            messege = exceptions.zero_kelvin_unit_1()
        
        elif unit_2 == 'Кельвины' and edited_value < 0: #0 по кельвину
            messege = exceptions.zero_kelvin_unit_2()

        if messege:
            self.ui.label_8.setText(messege)
            self.ui.to_value_edit.setText('')
            return None           
                    
        self.ui.to_value_edit.setText(str(edited_value))

    def convert_currency_units(self):
        self.ui.label_7.setText('')
        unit_1 = self.ui.from_currency_combo.currentText()
        unit_2 = self.ui.to_currency_combo.currentText()
        value = self.ui.from_currency_edit.text()
        edited_value = self.currency_operator.convert_currency(unit_1, unit_2, float(value))
        self.ui.to_currency_edit.setText(str(edited_value))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Converter()
    window.show()
    sys.exit(app.exec())
    