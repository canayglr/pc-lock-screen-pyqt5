from PyQt5.QtWidgets import*
from login_python import Ui_MainWindow
from arayuz import arayz
from PyQt5 import QtCore
import time
import sys

class MainPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.lineEdit.setEchoMode(QLineEdit.Password)
        self.arayuz= arayz()
        self.ui.lineEdit.returnPressed.connect(self.process)
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
        self.showFullScreen()
    def closeEvent(self, event):
        event.ignore()
    def process(self):
        encrypted_message = ''  
 
        alphabet=['a','b' ,'c' , 'd', 'e', 'f', 'g' ,'h' ,'i' ,'j','k' ,'l' ,'m' ,'n' ,
            'o' ,'p' ,'r' ,'s' ,'t' ,'u' ,'v', 'y' ,'z']
        received_text = self.ui.lineEdit.text()
        for i in received_text:          
            
            if i not in alphabet:
                encrypted_message += i          #alfabenin içinde değilse, boşluk veya yıldız gibi
                                    #bir karakterdir onun için mesajımıza ekledik.
            else:
                encrypted_message += alphabet[(alphabet.index(i)+3) % len(alphabet)]
        with open("password.txt", "r", encoding="utf-8") as f:
            sifre=f.read()
        if (encrypted_message==sifre):
            self.aktar()
        else:
            self.ui.label_2.setText("Sifre Hatali")
            self.ui.lineEdit.clear()

    def aktar(self):
        self.arayuz.showFullScreen()
        self.hide()
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    sys.exit(app.exec_())