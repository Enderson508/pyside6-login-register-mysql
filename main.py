import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFrame
from PySide6.QtCore import Qt
from PySide6.QtGui import QScreen
from login.logar import loginWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__(self)

        self.login = loginWindow()
        self.login.setupUI()
        
        



    

app = QApplication([])
window = MainWindow()
window.show()
app.exec() 


