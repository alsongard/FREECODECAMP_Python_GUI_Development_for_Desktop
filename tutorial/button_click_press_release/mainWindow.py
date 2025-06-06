from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton


class MainWidgetApp(QWidget):
    def __init__(self):
        super().__init__() # inherits every method from QWidget

        vLayout = QVBoxLayout()

        button1 = QPushButton("Click")

        button1.clicked.connect(self.clickedBtn)
        button1.pressed.connect(self.pressedBtn)
        button1.released.connect(self.releasedBtn)


        vLayout.addWidget(button1)

        self.setLayout(vLayout)

    def clickedBtn(self):
        print("Button is clicked")

    def pressedBtn(self):
        print("Button is pressed")

    def releasedBtn(self):
        print("Button is released")