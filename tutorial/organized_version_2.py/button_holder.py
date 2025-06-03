from PySide6.QtWidgets import QMainWindow, QPushButton

class Button(QMainWindow):
    def __init__(self):
        super().__init__()

        # set up window: window = QMainWindow() || window = QWidget() 
        # the above will not happen as Button() inherits from QMainWindow() base class
       
        self.setWindowTitle("Hello World")
        # set up button
        button = QPushButton()
        button.setText("Hello World")
        self.setCentralWidget(button)