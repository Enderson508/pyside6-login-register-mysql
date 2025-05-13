import sys
from PySide6.QtWidgets import QApplication, QMainWindow

class JanelaVazia(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupWINDOW()
    def setupWINDOW(self):
        self.setWindowTitle("Bem-Vindo(a)")
        self.showMaximized()


if __name__ == "__main__":
        app = QApplication([])
        janela = JanelaVazia()
        janela.showMaximized()
        janela.setWindowTitle("Bem-Vindo")
        sys.exit(app.exec())
