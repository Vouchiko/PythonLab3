import os

from PyQt6 import QtCore, QtWidgets
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget, QLabel, QRadioButton
from PyQt6.QtWidgets import QMessageBox

from task1 import run1
from task2 import run2
from task3 import run3
from task5 import Iterator1


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
        Lab_3.setWindowTitle(_translate("Lab_3", "Python Lab3"))
        self.Task1.setText(_translate("Lab_3", "Task1(Создать аннотацию)"))
        self.Task2.setText(_translate("Lab_3", "Task2(Создать аннотацию)"))
        self.Task3.setText(_translate("Lab_3", "Task3(Создать аннотацию)"))
        self.Image_work.setText(_translate("Lab_3", "Работа с изображениями"))
        self.Path_to_dataset.setText(_translate("Lab_3", "Выбрать путь"))

        self.Path_to_dataset.clicked.connect(self.get_folder)
        self.Task1.clicked.connect(self.task1)
        self.Task2.clicked.connect(self.task2)
        self.Task3.clicked.connect(self.task3)
        self.Image_work.clicked.connect(self.openDialog)

    # task 1
    def get_folder(self):
        self.folder = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder')
        try:
            os.chdir(self.folder)
            print(self.folder)
        except:
            error = QMessageBox()
            error.setWindowTitle("Error")
            error.setText("Папка не выбрана")
            error.setIcon(self, QMessageBox.warning)
            error.StandardButton(QMessageBox.close())
            error.exec()

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

    def openDialog(self):
        dialog = Dialog(self)
        dialog.exec()


class Dialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)
        self.__iterator = Iterator1("/Users/vouchiko/Desktop/Lab3", "Brown Bear", "dataset")
        self.__pixmap = QPixmap('.jpg')
        self.resize(800, 700)
        self.verticalLayout = QtWidgets.QGridLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setGeometry(QtCore.QRect(130, 230, 115, 30))
        self.verticalLayout.setSpacing(10)
        self.setLayout(self.verticalLayout)
        self.setGeometry(300, 300, 350, 300)

        self.pushButton_3 = QtWidgets.QPushButton(self)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setGeometry(QtCore.QRect(270, 90, 100, 32))

        self.verticalLayout.addWidget(self.pushButton)
        self.setWindowTitle("Изображения")
        self.pushButton.setText("Следующее")
        self.pushButton.clicked.connect(self.__nextButton)
        self.pushButton_3.setText("Выйти")
        self.pushButton_3.clicked.connect(self.btnClosed)
        self.verticalLayout.addWidget(self.pushButton_3)

        pixmap = QPixmap("/Users/vouchiko/Desktop/Lab3/dataset/brown bear/0000.jpg").scaledToWidth(600).scaledToHeight(
            400)
        self.__lable = QLabel(self)

        self.__lable.setPixmap(pixmap)

        self.verticalLayout.addWidget(self.__lable)

        self.radioButton_1 = QRadioButton('brown bear')
        self.radioButton_1.setChecked(True)
        self.radioButton_1.setAccessibleName("brown bear")
        self.radio_button_2 = QRadioButton('polar bear')
        self.radioButton_1.setAccessibleName("polar bear")
        self.verticalLayout.addWidget(self.radioButton_1)
        self.verticalLayout.addWidget(self.radio_button_2)
        self.radioButton_1.clicked.connect(self.buttonClicked)
        self.radio_button_2.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        sender = self.sender()
        if sender.text() == 'brown bear':
            self.__iterator.setName(sender.text())
            self.__iterator.getName()
        elif sender.text() == 'polar bear':
            self.__iterator.setName(sender.text())
            self.__iterator.getName()

    def __nextButton(self, ) -> None:
        try:
            tmp = os.path.join(os.path.join(self.__iterator.dataset, self.__iterator.path, self.__iterator.name),
                               self.__iterator.__next__())
            print(tmp)
            self.__pixmap = QPixmap(f"{tmp}").scaledToWidth(600).scaledToHeight(400)
            self.__lable.setPixmap(self.__pixmap)
            print(tmp)
        except:
            error1 = QMessageBox()
            error1.setWindowTitle("Ошибка")
            error1.setText("Закончились картинки")

    def btnClosed(self):
        self.close()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Lab_3()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
