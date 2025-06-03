from PySide6.QtWidgets import QPushButton, QWidget, QVBoxLayout, QHBoxLayout


class RocketWidget(QWidget):
    def __init__(self):
        super().__init__()

        button1 = QPushButton('button1')
        button2 = QPushButton('button2')

        button1.setCheckable(True)
        button2.setCheckable(True)


        button1.clicked.connect(self.buttonFunc)
        button2.clicked.connect(self.buttonFunc)

        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(button1)
        buttonLayout.addWidget(button2)

        self.setLayout(buttonLayout)


    def buttonFunc(self,checked=True):
        print(f"Button is clicked value: {checked}")



"""
so we use self to access the attributes of the class
in buttonFunc() we use for: when creating an instance of RocketWidget, we specify that in thegiven instance access buttonFunc()

In Python, when defining methods of a class, the first parameter is conventionally named `self`.
It represents the instance of the class. Without it, we wouldn't have access to the instance's attributes and methods.
In the context of the connection:
`button1.clicked.connect(self.buttonFunc)`
- We are telling the button: when you are clicked, call the method `buttonFunc` of this `RocketWidget` instance.
"""
