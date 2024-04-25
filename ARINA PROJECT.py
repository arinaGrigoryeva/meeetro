import sys
import sqlite3

from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QCheckBox, QLineEdit
from PyQt5.QtWidgets import QPushButton, QListWidget, QTextEdit, QLCDNumber, QInputDialog


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('zxc.ui', self)
        self.setWindowTitle('Геометрические фигуры')
        self.treygolnik.clicked.connect(self.func)
        self.romb.clicked.connect(self.func_2)
        self.trapeciya.clicked.connect(self.func_3)
        self.parallelogramm.clicked.connect(self.func_4)
        self.test.clicked.connect(self.func_21)
        self.next.clicked.connect(self.func_6)
        self.reyting.clicked.connect(self.reyting_func)
        self.nazad.clicked.connect(self.back)
        self.rezult.clicked.connect(self.rez)
        self.le = QLineEdit(self)
        self.le.move(130, 22)

        self.le.hide()
        self.label.hide()
        self.label_3.hide()
        self.label_2.hide()
        self.label_4.hide()
        self.label_5.hide()
        self.label_6.hide()
        self.label_7.hide()
        self.label_8.hide()
        self.label_9.hide()
        self.label_10.hide()
        self.label_11.hide()
        self.label_12.hide()
        self.label_13.hide()
        self.label_14.hide()
        self.label_15.hide()
        self.label_16.hide()
        self.label_17.hide()
        self.label_18.hide()
        self.label_37.hide()

        self.nazad.hide()
        self.reyting.hide()
        self.next.hide()
        self.rezult.hide()
        self.lineEdit.hide()
        self.reyting_tab.hide()

        self.label_36.hide()
        self.label_31.hide()
        self.label_32.hide()
        self.label_33.hide()
        self.label_34.hide()
        self.label_35.hide()
        self.label_25.hide()
        self.label_26.hide()
        self.label_27.hide()
        self.label_28.hide()
        self.label_29.hide()
        self.label_30.hide()

        self.label_19.hide()
        self.label_20.hide()
        self.label_21.hide()
        self.label_22.hide()
        self.label_23.hide()
        self.label_24.hide()
        self.checkBox.hide()
        self.checkBox_13.hide()
        self.checkBox_2.hide()
        self.checkBox_12.hide()
        self.checkBox_5.hide()
        self.checkBox_6.hide()
        self.checkBox_3.hide()
        self.checkBox_8.hide()
        self.checkBox_9.hide()
        self.checkBox_11.hide()
        self.checkBox_4.hide()
        self.checkBox_10.hide()

        self.lcdNumber.hide()

    def func_21(self):
        name1, ok_pressed = QInputDialog.getText(self, "Введите имя",
                                                 "Как тебя зовут?")
        if ok_pressed:
            self.le.setText(str(name1))
            self.nazad.show()
            self.label_3.hide()
            self.label_15.hide()
            self.label_16.hide()
            self.label_17.hide()
            self.label_12.hide()
            self.label_13.hide()
            self.label_14.hide()
            self.label_2.hide()
            self.label_7.hide()
            self.label_8.hide()
            self.label_9.hide()
            self.label_10.hide()
            self.label_11.hide()
            self.label.hide()
            self.label_4.hide()
            self.label_5.hide()
            self.label_6.hide()
            self.label_37.hide()
            self.next.hide()
            self.test.hide()
            self.lineEdit.hide()
            self.label_19.show()
            self.label_20.show()
            self.label_21.show()
            self.label_22.show()
            self.label_23.show()
            self.label_24.show()
            self.checkBox.show()
            self.checkBox_13.show()
            self.checkBox_2.show()
            self.checkBox_12.show()
            self.checkBox_6.show()
            self.checkBox_5.show()
            self.checkBox_3.show()
            self.checkBox_8.show()
            self.checkBox_9.show()
            self.checkBox_11.show()
            self.checkBox_4.show()
            self.checkBox_10.show()
            self.lcdNumber.show()
            self.treygolnik.hide()
            self.romb.hide()
            self.trapeciya.hide()
            self.parallelogramm.hide()
            self.checkBox_13.stateChanged.connect(self.point)
            self.checkBox_12.stateChanged.connect(self.point_2)
            self.checkBox_5.stateChanged.connect(self.point_3)
            self.checkBox_3.stateChanged.connect(self.point_4)
            self.checkBox_11.stateChanged.connect(self.point_5)
            self.checkBox_4.stateChanged.connect(self.point_6)
            self.checkBox.stateChanged.connect(self.point_7)
            self.checkBox_2.stateChanged.connect(self.point_8)
            self.checkBox_6.stateChanged.connect(self.point_9)
            self.checkBox_8.stateChanged.connect(self.point_10)
            self.checkBox_9.stateChanged.connect(self.point_11)
            self.checkBox_10.stateChanged.connect(self.point_12)
            self.rezult.show()

    def func(self):
        self.label.hide()
        self.label_2.show()
        self.label_6.show()
        self.label_5.show()
        self.label_4.show()
        self.label_7.hide()
        self.label_8.hide()
        self.label_9.hide()
        self.label_15.hide()
        self.label_16.hide()
        self.label_17.hide()
        self.label_18.hide()
        self.label_10.hide()
        self.label_11.hide()
        self.label_12.hide()
        self.label_13.hide()
        self.label_14.hide()

    def func_2(self):
        self.label_2.hide()
        self.label_6.hide()
        self.label_5.hide()
        self.label_4.hide()
        self.label_12.hide()
        self.label_13.hide()
        self.label_14.hide()
        self.label_15.hide()
        self.label_16.hide()
        self.label_17.hide()
        self.label_18.hide()

        self.label.show()
        self.label_7.show()
        self.label_8.show()
        self.label_9.show()
        self.label_10.show()
        self.label_11.show()

    def func_3(self):
        self.label_2.hide()
        self.label_6.hide()
        self.label_5.hide()
        self.label_4.hide()
        self.label.hide()
        self.label_7.hide()
        self.label_8.hide()
        self.label_9.hide()
        self.label_10.hide()
        self.label_11.hide()
        self.label_15.hide()
        self.label_16.hide()
        self.label_17.hide()
        self.label_18.hide()

        self.label_13.show()
        self.label_14.show()
        self.label_12.show()

    def func_4(self):
        self.label_2.hide()
        self.label_6.hide()
        self.label_5.hide()
        self.label_4.hide()
        self.label.hide()
        self.label_7.hide()
        self.label_8.hide()
        self.label_10.hide()
        self.label_11.hide()
        self.label_13.hide()
        self.label_14.hide()
        self.label_12.hide()

        self.label_15.show()
        self.label_16.show()
        self.label_17.show()
        self.label_18.show()
        self.label_9.show()

    def func_5(self):
        self.test.hide()
        self.label_37.show()
        self.nazad.show()
        self.treygolnik.hide()
        self.romb.hide()
        self.trapeciya.hide()
        self.parallelogramm.hide()
        self.label.hide()
        self.label_2.hide()
        self.label_3.hide()
        self.label_6.hide()
        self.label_5.hide()
        self.label_4.hide()
        self.label_7.hide()
        self.label_8.hide()
        self.label_9.hide()
        self.label_10.hide()
        self.label_11.hide()
        self.label_13.hide()
        self.label_14.hide()
        self.label_12.hide()
        self.label_15.hide()
        self.label_16.hide()
        self.label_17.hide()
        self.label_18.hide()
        self.next.show()
        self.lineEdit.show()

    def func_6(self):
        self.label_37.hide()
        self.next.hide()
        self.test.hide()
        self.lineEdit.hide()
        self.label_19.show()
        self.label_20.show()
        self.label_21.show()
        self.label_22.show()
        self.label_23.show()
        self.label_24.show()
        self.checkBox.show()
        self.checkBox_13.show()
        self.checkBox_2.show()
        self.checkBox_12.show()
        self.checkBox_6.show()
        self.checkBox_5.show()
        self.checkBox_3.show()
        self.checkBox_8.show()
        self.checkBox_9.show()
        self.checkBox_11.show()
        self.checkBox_4.show()
        self.checkBox_10.show()
        self.lcdNumber.show()
        self.checkBox_13.stateChanged.connect(self.point)
        self.checkBox_12.stateChanged.connect(self.point_2)
        self.checkBox_5.stateChanged.connect(self.point_3)
        self.checkBox_3.stateChanged.connect(self.point_4)
        self.checkBox_11.stateChanged.connect(self.point_5)
        self.checkBox_4.stateChanged.connect(self.point_6)
        self.checkBox.stateChanged.connect(self.point_7)
        self.checkBox_2.stateChanged.connect(self.point_8)
        self.checkBox_6.stateChanged.connect(self.point_9)
        self.checkBox_8.stateChanged.connect(self.point_10)
        self.checkBox_9.stateChanged.connect(self.point_11)
        self.checkBox_10.stateChanged.connect(self.point_12)
        self.rezult.show()

    a = 0

    def back(self):
        self.label.hide()
        self.label_2.show()
        self.label_6.show()
        self.label_5.show()
        self.label_4.show()
        self.label_7.hide()
        self.label_8.hide()
        self.label_9.hide()
        self.label_10.hide()
        self.label_11.hide()
        self.label_12.hide()
        self.label_13.hide()
        self.label_14.hide()
        self.label_15.hide()
        self.label_16.hide()
        self.label_17.hide()
        self.label_18.hide()
        self.label_3.show()
        self.label_37.hide()
        self.treygolnik.show()
        self.romb.show()
        self.trapeciya.show()
        self.parallelogramm.show()
        self.test.show()
        self.reyting.hide()
        self.next.hide()

        self.nazad.hide()
        self.rezult.hide()
        self.lineEdit.hide()
        self.reyting_tab.hide()
        self.lineEdit.hide()

        self.label_36.hide()
        self.label_31.hide()
        self.label_32.hide()
        self.label_33.hide()
        self.label_34.hide()
        self.label_35.hide()
        self.label_25.hide()
        self.label_26.hide()
        self.label_27.hide()
        self.label_28.hide()
        self.label_29.hide()
        self.label_30.hide()

        self.label_19.hide()
        self.label_20.hide()
        self.label_21.hide()
        self.label_22.hide()
        self.label_23.hide()
        self.label_24.hide()
        self.checkBox.hide()
        self.checkBox_13.hide()
        self.checkBox_2.hide()
        self.checkBox_12.hide()
        self.checkBox_5.hide()
        self.checkBox_6.hide()
        self.checkBox_3.hide()
        self.checkBox_8.hide()
        self.checkBox_9.hide()
        self.checkBox_11.hide()
        self.checkBox_4.hide()
        self.checkBox_10.hide()
        self.lcdNumber.hide()
        if self.checkBox.isChecked():
            self.checkBox.toggle()
        if self.checkBox_13.isChecked():
            self.checkBox_13.toggle()
        if self.checkBox_2.isChecked():
            self.checkBox_2.toggle()
        if self.checkBox_12.isChecked():
            self.checkBox_12.toggle()
        if self.checkBox_5.isChecked():
            self.checkBox_5.toggle()
        if self.checkBox_6.isChecked():
            self.checkBox_6.toggle()
        if self.checkBox_3.isChecked():
            self.checkBox_3.toggle()
        if self.checkBox_8.isChecked():
            self.checkBox_8.toggle()
        if self.checkBox_9.isChecked():
            self.checkBox_9.toggle()
        if self.checkBox_11.isChecked():
            self.checkBox_11.toggle()
        if self.checkBox_4.isChecked():
            self.checkBox_4.toggle()
        if self.checkBox_10.isChecked():
            self.checkBox_10.toggle()
        self.lcdNumber.display(str(0))

    def point_7(self, state):
        if state == Qt.Checked:
            self.label_25.show()

    def point_8(self, state):
        if state == Qt.Checked:
            self.label_26.show()

    def point_9(self, state):
        if state == Qt.Checked:
            self.label_27.show()

    def point_10(self, state):
        if state == Qt.Checked:
            self.label_28.show()

    def point_11(self, state):
        if state == Qt.Checked:
            self.label_29.show()

    def point_12(self, state):
        if state == Qt.Checked:
            self.label_30.show()

    def point(self, state):
        global a
        if state == Qt.Checked:
            self.label_36.show()
            self.a += 1

    def point_2(self, state):
        global a
        if state == Qt.Checked:
            self.label_31.show()
            self.a += 1

    def point_3(self, state):
        global a
        if state == Qt.Checked:
            self.label_32.show()
            self.a += 1

    def point_4(self, state):
        global a
        if state == Qt.Checked:
            self.label_33.show()
            self.a += 1

    def point_5(self, state):
        global a
        if state == Qt.Checked:
            self.label_34.show()
            self.a += 1

    def point_6(self, state):
        global a
        if state == Qt.Checked:
            self.label_35.show()
            self.a += 1

    def rez(self):
        self.lcdNumber.display(str(self.a))
        self.reyting.show()

    def reyting_func(self):
        global name1
        self.reyting.hide()
        self.reyting_tab.show()
        self.lcdNumber.hide()
        self.rezult.hide()
        self.label_36.hide()
        self.label_31.hide()
        self.label_32.hide()
        self.label_33.hide()
        self.label_34.hide()
        self.label_35.hide()
        self.label_25.hide()
        self.label_26.hide()
        self.label_27.hide()
        self.label_28.hide()
        self.label_29.hide()
        self.label_30.hide()

        self.label_19.hide()
        self.label_20.hide()
        self.label_21.hide()
        self.label_22.hide()
        self.label_23.hide()
        self.label_24.hide()
        self.checkBox.hide()
        self.checkBox_13.hide()
        self.checkBox_2.hide()
        self.checkBox_12.hide()
        self.checkBox_5.hide()
        self.checkBox_6.hide()
        self.checkBox_3.hide()
        self.checkBox_8.hide()
        self.checkBox_9.hide()
        self.checkBox_11.hide()
        self.checkBox_4.hide()
        self.checkBox_10.hide()

        name = str(self.le.text())
        score = str(self.a)
        conn = sqlite3.connect('ag.db')
        c = conn.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS ag(names TEXT, '
                  'scores TEXT)')

        c.execute('INSERT INTO ag(names, scores) VALUES (?, ?)', (name, score))
        c.execute("SELECT * FROM ag ORDER BY scores DESC")
        conn.commit()

        c.close()
        conn.close()

        conn = sqlite3.connect('ag.db')
        c = conn.cursor()
        tab = 'SELECT * FROM ag LIMIT 50'
        self.reyting_tab.setRowCount(50)
        tablerow = 0
        for row in c.execute(tab):
            self.reyting_tab.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.reyting_tab.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            tablerow += 1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
