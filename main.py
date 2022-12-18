import sys
import os

from PyQt6 import QtCore, QtWidgets
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget, QLabel, QRadioButton
from PyQt6.QtWidgets import QMessageBox

from task1 import run1
from task2 import run2
from task3 import run3


class Ui_Lab_3(QWidget):
    def setupUi(self, Lab_3):
        Lab_3.setObjectName("Lab_3")
        Lab_3.resize(500, 460)
        self.folder = None
        Lab_3.setStyleSheet("border-left-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(Lab_3)
        self.centralwidget.setObjectName("centralwidget")
        self.Task1 = QtWidgets.QPushButton(self.centralwidget)
        self.Task1.setGeometry(QtCore.QRect(0, 210, 200, 100))
        self.Task1.setStyleSheet("background-color: rgb(116, 255, 216);\n"
                                 "background-color: rgb(255, 251, 211);\n"
                                 "color: rgb(0, 0, 0);")

        self.Task1.setObjectName("Task1")
        self.Task2 = QtWidgets.QPushButton(self.centralwidget)
        self.Task2.setGeometry(QtCore.QRect(300, 210, 200, 100))
        self.Task2.setStyleSheet("background-color: rgb(255, 251, 211);\n"
                                 "color: rgb(0, 0, 0);")
        self.Task2.setObjectName("Task2")
        self.Task3 = QtWidgets.QPushButton(self.centralwidget)
        self.Task3.setGeometry(QtCore.QRect(0, 310, 200, 100))
        self.Task3.setStyleSheet("background-color: rgb(116, 255, 216);\n"
                                 "background-color: rgb(255, 251, 211);\n"
                                 "color: rgb(0, 0, 0);")
        self.Task3.setObjectName("Task3")
        self.Image_work = QtWidgets.QPushButton(self.centralwidget)
        self.Image_work.setGeometry(QtCore.QRect(300, 310, 200, 100))
        self.Image_work.setStyleSheet("background-color: rgb(255, 251, 211);\n"
                                      "color: rgb(0, 0, 0);")
        self.Image_work.setObjectName("Image_work")
        self.Path_to_dataset = QtWidgets.QPushButton(self.centralwidget)
        self.Path_to_dataset.setGeometry(QtCore.QRect(200, 260, 100, 100))
        self.Path_to_dataset.setStyleSheet("background-color: rgb(255, 203, 168);\n"
                                           "color: rgb(0, 0, 0);")
        self.Path_to_dataset.setObjectName("Path_to_dataset")
        Lab_3.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Lab_3)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.menubar.setObjectName("menubar")
        Lab_3.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Lab_3)
        self.statusbar.setObjectName("statusbar")
        Lab_3.setStatusBar(self.statusbar)
        self.retranslateUi(Lab_3)
        QtCore.QMetaObject.connectSlotsByName(Lab_3)

    def retranslateUi(self, Lab_3):
        _translate = QtCore.QCoreApplication.translate
        Lab_3.setWindowTitle(_translate("Lab_3", "MainWindow"))
        self.Task1.setText(_translate("Lab_3", "Task1(Создать аннотацию)"))
        self.Task2.setText(_translate("Lab_3", "Task2(Создать аннотацию)"))
        self.Task3.setText(_translate("Lab_3", "Task3(Создать аннотацию)"))
        self.Image_work.setText(_translate("Lab_3", "Работа с изображениями"))
        self.Path_to_dataset.setText(_translate("Lab_3", "Выбрать путь"))

        self.Path_to_dataset.clicked.connect(self.get_folder)
        self.Task1.clicked.connect(self.task1)
        self.Task2.clicked.connect(self.task2)
        self.Task3.clicked.connect(self.task3)

    def get_folder(self):
        self.folder = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder')
        os.chdir(self.folder)
        print(self.folder)


    def task1(self):
        run1(self.folder, 'polar bear', 'annotation Polar Bear')
        run1(self.folder, 'brown bear', 'annotation Brown Bear')
        complete = QMessageBox()
        complete.setWindowTitle("OK")
        complete.setText("Выполнено")
        complete.exec()

    def task2(self):
        run2(self.folder, "datasetTask1", "Annotation")
        complete = QMessageBox()
        complete.setWindowTitle("OK")
        complete.setText("Выполнено")
        complete.exec()

    def task3(self):
        run3(self.folder, 'annotation.csv', 'datasetcopy2')
        complete = QMessageBox()
        complete.setWindowTitle("OK")
        complete.setText("Выполнено")
        complete.exec()


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Lab_3()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
