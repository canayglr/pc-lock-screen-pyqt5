from PyQt5.QtWidgets import *
from proje_python import Ui_MainWindow
import time
import os

class arayz(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.suresiz.clicked.connect(self.close)
        self.ui.otuz.clicked.connect(self.yarimsaat)
        self.ui.bir.clicked.connect(self.birsaat)
    def yarimsaat(self):
        os.system("shutdown /s /t 1800")
        box = QMessageBox()
        box.setIcon(QMessageBox.Information)
        box.setWindowTitle("Bilgilendirme")
        box.setText("Yarım Saat Süreniz Başlamıştır")
        box.setStandardButtons(QMessageBox.Ok)
        box.exec_()
        self.close()
    def birsaat(self):
        os.system("shutdown /s /t 3600")
        box = QMessageBox()
        box.setIcon(QMessageBox.Information)
        box.setWindowTitle("Bilgilendirme")
        box.setText("Bir Saat Süreniz Başlamıştır")
        box.setStandardButtons(QMessageBox.Ok)
        box.exec_()
        self.close()