import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLineEdit, QTextBrowser, QMessageBox, QSpacerItem, QSizePolicy
)
from PySide6.QtCore import Qt
from .register import registerWindow
from page.page import JanelaVazia
import bcrypt
import mysql.connector


class loginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()
    
    def setupUI(self):

        self.label = QLabel(self)
        self.label.setFixedSize(500,500)
        self.label.setStyleSheet(
            "background-color: #121414;" \
            " border: 2px solid white;" \
            " border-radius: 30px;" \
            " color: white;"
            )
        
        #CENTRALIZANDO LABEL
        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)
        
        self.main_layout = QVBoxLayout(self.centralwidget)
        self.main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.content_layout = QVBoxLayout()
        self.content_layout.setSpacing(20)
        self.content_layout.setContentsMargins(0, 20, 0, 0)
        self.content_layout.setContentsMargins(20, 20, 0, 0)
        self.content_layout.addSpacerItem(QSpacerItem(20, 10))


        # TÍTULO DE LOGIN
        self.fonte_title = QTextBrowser()
        self.fonte_title.setText("<font size='20'><b>LOGIN</b></font>")
        self.fonte_title.setStyleSheet(
            'background-color: transparent;'
            ' color: white;'
            ' border: None;'
        )
        self.fonte_title.setMaximumHeight(50)

        self.content_layout.addWidget(self.fonte_title, alignment=Qt.AlignmentFlag.AlignLeft)
        self.content_layout.setContentsMargins(20, 20, 0, 0)

        # Espaço entre título e campos
        self.content_layout.addSpacerItem(QSpacerItem(20, 50))

        # USUÁRIO
        self.fonte_user = QLineEdit()
        self.fonte_user.setPlaceholderText("ㅤDigite o nome de usuário")
        self.fonte_user.setMaxLength(12)
        self.fonte_user.setStyleSheet(
            'background-color: #121414;'
            ' color: white;'
            ' border: 2px solid white;'
            ' border-radius: 18px;'
        )
        self.fonte_user.setFixedHeight(41)
        self.fonte_user.setFixedWidth(270)

        # SENHA
        self.fonte_password = QLineEdit()
        self.fonte_password.setPlaceholderText("ㅤDigite a senha")
        self.fonte_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.fonte_password.setMaxLength(12)
        self.fonte_password.setStyleSheet(
            'background-color: #121414;'
            ' color: white;'
            ' border: 2px solid white;'
            ' border-radius: 18px;'
        )
        self.fonte_password.setFixedHeight(41)
        self.fonte_password.setFixedWidth(270)

        self.content_layout.addWidget(self.fonte_user, alignment=Qt.AlignmentFlag.AlignLeft)
        self.content_layout.addSpacerItem(QSpacerItem(10,10))
        self.content_layout.addWidget(self.fonte_password, alignment=Qt.AlignmentFlag.AlignLeft)
        self.content_layout.addSpacerItem(QSpacerItem(10, 10))

        # BOTÃO ENTRAR
        self.button = QPushButton("Entrar")
        self.button.setStyleSheet(
            'background-color: #121414;'
            ' font-weight: bold;'
            ' color: white;'
            ' border: 2px solid white;'
            ' border-radius: 18px;'
        )
        self.button.setFixedHeight(41)
        self.button.setFixedWidth(270)
        self.button.clicked.connect(self.login)

        # BOTÃO REGISTRO
        self.button_register = QPushButton("Registre-se")
        self.button_register.setStyleSheet(
            'background-color: transparent;'
            ' color: white;'
            ' font-weight: bold;'
            ' border: none;'
        )
        self.button_register.setFixedHeight(30)
        self.button_register.setFixedWidth(100)
        self.button_register.clicked.connect(self.showregisterpage)
        
        register_layout = QHBoxLayout()
        register_layout.setContentsMargins(0, 0, 0, 0)
        register_layout.addSpacerItem(QSpacerItem(0, 0))
        register_layout.addWidget(self.button_register, alignment=Qt.AlignmentFlag.AlignLeft)

        self.content_layout.addLayout(register_layout)
        self.content_layout.addWidget(self.button, alignment=Qt.AlignmentFlag.AlignLeft)

        
        self.content_layout.addSpacerItem(QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding))

        wrapper_layout = QVBoxLayout()
        wrapper_layout.addLayout(self.content_layout)

    
        self.label.setLayout(wrapper_layout)
        self.main_layout.addWidget(self.label, alignment=Qt.AlignmentFlag.AlignCenter)
        
        # CONFIG DA JANELA
        self.setWindowTitle("Login")
        self.setMinimumSize(800, 600)
        self.resize(1280, 720)
        self.setStyleSheet(
            "background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, \
            stop: 0 #0d0d23, stop: 1 #121414);"
        )

        # BANCO DE DADOS
        self.conexao = mysql.connector.connect(
            host="localhost",
            username="", #COLOQUE O NOME DE USUARIO DO SERVIDOR MYSQL
            password="", #COLOQUE A SENHA(SE TIVER)
            database="" #COLOQUE O NOME DO SEU BANCO DE DADOS
        )
        self.cursor = self.conexao.cursor()
    
    #FUNÇÃO PARA ABRIR A TELA DE REGISTRO
    def showregisterpage(self):
        self.register = registerWindow()
        self.register.show()
        self.close()
    
    #FUNÇÃO PARA ABRIR A JANELA
    def loginok(self):
        self.janela = JanelaVazia()
        self.janela.setupWINDOW()
        
    #FUNÇÃO PARA PROCURAR USUÁRIO   
    def founduser(self, login_name):
        comandos = "SELECT * FROM sua_table WHERE nome = %s" #COLOQUE A TABLE DO SEU BANCO DE DADOS E O VALOR QUE REPRESENTE O NOME DE USUÁRIO
        valores = (login_name,)
        self.cursor.execute(comandos, valores)
        return self.cursor.fetchone()
    
    #CONFIGURANDO PROCESSO DE LOGIN

    def login(self):
        user = self.fonte_user.text()
        senha = self.fonte_password.text()
        resultado = self.founduser(user)

        if not user or not senha:
            QMessageBox.warning(self, "ERRO!", "CAMPO VAZIO!")
            return

        if resultado is None:
            QMessageBox.warning(self, "ERRO!", "USUÁRIO OU SENHA INCORRETOS!")
            return

        senha_hash = resultado[2].encode('utf8')

        if bcrypt.checkpw(senha.encode('utf8'), senha_hash):
            QMessageBox.information(self, "SUCESSO!", "LOGIN BEM SUCEDIDO!")
            self.loginok()
            self.close()
        else:
            QMessageBox.warning(self, "ERRO!", "USUÁRIO OU SENHA INCORRETOS!")


app = QApplication(sys.argv)
window = loginWindow()
window.show()
sys.exit(app.exec())
