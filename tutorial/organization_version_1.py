from  PySide6.QtWidgets  import QApplication, QMainWindow, QPushButton
import sys

class Button(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Welcome")
        button = QPushButton()
        button.setText('PressMe')
        self.setCentralWidget(button)


app = QApplication()
window = Button()
window.show()
app.exec()

