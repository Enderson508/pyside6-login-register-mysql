import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLineEdit, QTextBrowser, QMessageBox, QSpacerItem, QSizePolicy
)
from PySide6.QtCore import Qt, QRect
import bcrypt
import mysql.connector

class registerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUII()

    
    def setupUII(self):
        
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
        
        #TITULO DE REGISTRO
        self.fonte_title = QTextBrowser(self)
        self.fonte_title.setText(
            "<font size = '20'><b>REGISTER</b><font>"
            )
        self.fonte_title.setStyleSheet(
            'background-color: transparent;' \
            ' color: white;' \
            ' border: None;'
            )
        self.fonte_title.setFixedSize(250,100)
        self.content_layout.addWidget(self.fonte_title, alignment=Qt.AlignmentFlag.AlignLeft)
        self.content_layout.addSpacerItem(QSpacerItem(10, 10))
        
        
        #AREAS DE DIGITAÇÃO
        self.fonte_user = QLineEdit(self)
       
        self.fonte_user.setObjectName(u"lineEdit")
        self.fonte_user.setFixedSize(250, 41)
        self.fonte_user.setPlaceholderText("ㅤDigite o nome de usuário")
        self.fonte_user.setMaxLength(12)
        self.fonte_user.setStyleSheet(
            'background-color: #121414;' \
            ' color: white; border: 2px solid white;' \
            ' border-radius: 18px;'
            )
        
        self.content_layout.addWidget(self.fonte_user, alignment=Qt.AlignmentFlag.AlignLeft)
        self.content_layout.addSpacerItem(QSpacerItem(20, 20))
        
       
        #SENHAS
        
        self.fonte_senha = QLineEdit(self)
        self.fonte_senha.setObjectName(u"lineEdit")
        self.fonte_senha.setFixedSize(250, 41)
        self.fonte_senha.setPlaceholderText("ㅤDigite a senha que você deseja")
        self.fonte_senha.setEchoMode(QLineEdit.EchoMode.Password)
        self.fonte_senha.setMaxLength(12)
        self.fonte_senha.setStyleSheet(
            'background-color: #121414;' \
            ' color: white; border:' \
            ' 2px solid white;' \
            ' border-radius: 18px;')
        self.content_layout.addWidget(self.fonte_senha, alignment=Qt.AlignmentFlag.AlignLeft)
        self.content_layout.addSpacerItem(QSpacerItem(5, 5))
        
        

        self.fonte_senha_confirm = QLineEdit(self)
        self.fonte_senha_confirm.setObjectName(u"lineEdit")
        self.fonte_senha_confirm.setFixedSize(250, 42)
        self.fonte_senha_confirm.setPlaceholderText("ㅤConfirme sua senha")
        self.fonte_senha_confirm.setEchoMode(QLineEdit.EchoMode.Password)
        self.fonte_senha_confirm.setMaxLength(12)
        self.fonte_senha_confirm.setStyleSheet(
            'background-color: #121414;' \
            ' color: white;' \
            ' border: 2px solid white;' \
            ' border-radius: 18px;'
            )
        self.content_layout.addWidget(self.fonte_senha_confirm, alignment=Qt.AlignmentFlag.AlignLeft)
        self.content_layout.addSpacerItem(QSpacerItem(10, 10))
              
        
    
        

        #BOTÃO DE ENTRAR
        self.button = QPushButton(self)
        self.button.setText("Registrar")
        self.button.setFixedSize(200, 41)
        self.button.setStyleSheet(
            'background-color: #121414;' \
            ' font-weight: bold;' \
            ' color: white;' \
            ' border: 2px solid white;' \
            ' border-radius: 18px;'
            )
        self.button.clicked.connect(self.register)
        
        self.content_layout.addWidget(self.button, alignment=Qt.AlignmentFlag.AlignLeft)
        self.content_layout.addSpacerItem(QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding))
        
        self.wrapper = QVBoxLayout()
        self.wrapper.addLayout(self.content_layout)
        
        self.label.setLayout(self.wrapper)
        
        self.main_layout.addWidget(self.label, alignment=Qt.AlignmentFlag.AlignCenter)


 
        #CONFIGURAÇÃO DA JANELA
        self.setWindowTitle("Register")
        self.setMinimumSize(800, 600)
        self.resize(1280, 720)
        self.show() 
        self.setStyleSheet(
            "background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, \
            stop: 0 #0d0d23,\
            stop: 1 #121414);"
            )
        


        #SERVIDOR MYSQL

        self.conexao = mysql.connector.connect(
            host = "localhost",
            username = "", #COLOQUE O NOME DE USUARIO DO SERVIDOR MYSQL
            password = "", #COLOQUE A SENHA(SE TIVER)
            database = "" #COLOQUE O NOME DO SEU BANCO DE DADOS
        )
        self.cursor = self.conexao.cursor(buffered=True)

    #INSERIR VALORES NO BANCO DE DADOS
    def registeruser(self, user_name, user_senha):
        senha_hash = bcrypt.hashpw(user_senha.encode('utf-8'), bcrypt.gensalt())
        comandos = "INSERT INTO sua_table(dado_user, dado_password) VALUES (%s, %s)" #COLOQUE A SUA TABLE E DENTRO DO PARÊNTESES COLOQUE OS VALORES QUE REPRESENTAM O NOME E A SENHA DE USUÁRIO
        valores =   (user_name, senha_hash) 
        self.cursor.execute(comandos, valores)
        self.conexao.commit()
        
    #PROCURA VALORES NO BANCO DE DADOS
    def founduser(self, user):
        comandos = "SELECT * FROM sua_table WHERE nome = %s" #COLOQUE A TABLE DO SEU BANCO DE DADOS E O VALOR QUE REPRESENTE O NOME DE USUÁRIO
        valores = (user,)
        self.cursor.execute(comandos, valores)
        return self.cursor.fetchone() is not None
        
        

    #ABRIR A TELA DE LOGIN
    def registerok(self):
        from .logar import loginWindow
        self.windowregister = loginWindow()
        self.windowregister.show()
        self.close()  


    #CONFIGURANDO ÁREA DE REGISTRO
    def register(self):
        user = self.fonte_user.text()
        senha = self.fonte_senha.text() 

        if user == "" or senha == "" or self.fonte_senha_confirm.text() == "":
            QMessageBox.warning(self, "ERRO!", "CAMPO VAZIO!")
            return
        

        if self.fonte_senha.text() != self.fonte_senha_confirm.text():
            QMessageBox.warning(self,"ERRO!", "SENHAS DIFERENTES!")
            return

        if self.founduser(user):
            QMessageBox.warning(self, "ERRO!", "NOME DE USUÁRIO JÁ EXISTE!")
            return 
        
        self.registeruser(user, senha)
        QMessageBox.information(self,
             "SUCESSO!", 
             "USUÁRIO CADASTRADO COM SEUCESSO!"
             ) 
        self.registerok()  
        

  


  
      
            
            
if __name__ == "__main__":
    app = QApplication([])
    window = registerWindow()
    window.show()
    app.exec() 


