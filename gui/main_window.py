# main_window.py
from PySide6.QtWidgets import QApplication, QMainWindow, QListWidget, QPushButton, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Gerenciador de Senhas")
        self.resize(400, 300)

        # Lista de senhas
        self.password_list = QListWidget()

        # Botões
        self.add_button = QPushButton("Adicionar Senha")
        self.view_button = QPushButton("Visualizar Senha")
        self.delete_button = QPushButton("Excluir Senha")

        # Layout principal
        layout = QVBoxLayout()
        layout.addWidget(self.password_list)
        layout.addWidget(self.add_button)
        layout.addWidget(self.view_button)
        layout.addWidget(self.delete_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
