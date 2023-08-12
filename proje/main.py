from PyQt5.QtWidgets import QApplication
from login import MainPage

app = QApplication([])
window=MainPage()
window.show()
app.exec_()