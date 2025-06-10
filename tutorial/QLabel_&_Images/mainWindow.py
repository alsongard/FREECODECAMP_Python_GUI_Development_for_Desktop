from PySide6.QtWidgets import QLabel, QWidget, QPushButton, QVBoxLayout
from PySide6.QtGui import QPixmap


class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QLabem with Images")

        image_label = QLabel()
        image_label.setPixmap(QPixmap("../images/backiee-19212-landscape.jpg"))

        v_layout = QVBoxLayout()
        v_layout.addWidget(image_label)
        enterBtn =QPushButton("Enter")
        v_layout.addWidget(enterBtn)
        self.setLayout(v_layout)
