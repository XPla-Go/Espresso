import random
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QPushButton, QTableWidgetItem
import sqlite3


class Nim(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        con = sqlite3.connect("coffee.sqlite")
        cur = con.cursor()
        self.labels = ["ID", "название сорта", "степень обжарки", "молотый/в зернах", "описание вкуса", "цена", "объем упаковки"]
        result = cur.execute("""SELECT * FROM coffee""").fetchall()
        for elem in result:
            print(elem)
        self.setCentralWidget(self.tableWidget)
        self.tableWidget.setColumnCount(len(self.labels))
        self.tableWidget.setHorizontalHeaderLabels(self.labels)
        con.close()
        for index, elem in enumerate(result):
            row = self.tableWidget.rowCount()
            self.tableWidget.setRowCount(row + 1)
            for i, j in enumerate(elem):
                self.tableWidget.setItem(row, i, QTableWidgetItem(str(j)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Nim()
    ex.show()
    sys.exit(app.exec())