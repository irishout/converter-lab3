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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Converter()
    window.show()
    sys.exit(app.exec())
    