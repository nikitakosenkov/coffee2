import sqlite3
import sys

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QWidget


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(798, 586)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(30, 20, 221, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 70, 221, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(320, 70, 61, 31))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(300, 80, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(70, 220, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(70, 260, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(70, 300, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(70, 340, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(70, 380, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(70, 420, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 220, 181, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(200, 260, 181, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(200, 300, 181, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(200, 340, 181, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(Form)
        self.lineEdit_6.setGeometry(QtCore.QRect(200, 380, 181, 31))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(Form)
        self.lineEdit_7.setGeometry(QtCore.QRect(200, 420, 181, 31))
        self.lineEdit_7.setObjectName("lineEdit_7")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "добавить"))
        self.pushButton_2.setText(_translate("Form", "изменить"))
        self.label.setText(_translate("Form", "id"))
        self.label_2.setText(_translate("Form", "название"))
        self.label_3.setText(_translate("Form", "степень прожарки"))
        self.label_4.setText(_translate("Form", "зерно/молотый"))
        self.label_5.setText(_translate("Form", "описание"))
        self.label_6.setText(_translate("Form", "цена"))
        self.label_7.setText(_translate("Form", "объем"))


class Ui_MainWindow(object):
    def setupUi(self, coffee):
        coffee.setObjectName("coffee")
        coffee.resize(884, 620)
        self.tableWidget = QtWidgets.QTableWidget(coffee)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 871, 421))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.pushButton = QtWidgets.QPushButton(coffee)
        self.pushButton.setGeometry(QtCore.QRect(10, 440, 871, 171))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(coffee)
        QtCore.QMetaObject.connectSlotsByName(coffee)

    def retranslateUi(self, coffee):
        _translate = QtCore.QCoreApplication.translate
        coffee.setWindowTitle(_translate("coffee", "Form"))
        self.pushButton.setText(_translate("coffee", "ADD or EDIT"))


class Sec(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.chn)
        self.pushButton_2.clicked.connect(self.ad)

    def chn(self):
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        qqq = cur.execute("""INSERT INTO sorts
        VALUES
        ( ? , ? , ? , ? , ? , ? , ? )""",
                          (1, self.lineEdit_2.text(), self.lineEdit_3.text(), self.lineEdit_4.text(),
                           self.lineEdit_5.text(), int(self.lineEdit_6.text()), int(self.lineEdit_7.text())))
        con.commit()
        cur.close()

    def ad(self):
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        cur.execute(f"""UPDATE sorts
                        SET title = {self.lineEdit_2.text()}, fry = {self.lineEdit_3.text()}, 
                        molotyi zerno = {self.lineEdit_4.text()}, description = {self.lineEdit_5.text()}, 
                        price = {int(self.lineEdit_6.text())}, amount = {int(self.lineEdit_7.text())}
                        WHERE id = {int(self.lineEdit)}""")


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.win = Sec()
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        q = cur.execute("SELECT * FROM sorts").fetchall()
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(['id', 'title', 'fry', 'molotyi zerno',
                                                    'description', 'price', 'amount'])
        self.tableWidget.setRowCount(0)
        for i, row in enumerate(list(q)):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(list(row)):
                elem = str(elem)
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(elem))
        self.tableWidget.resizeColumnsToContents()
        self.pushButton.clicked.connect(self.win.show)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
