from PySide6.QtWidgets import QLabel, QWidget, QLineEdit, QHBoxLayout, QPushButton, QVBoxLayout, QMainWindow

class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        first_name_label = QLabel("First Name: ")
        middle_name_label = QLabel("Middle Name")
        last_name_label = QLabel("Last Name: ")
        email_label = QLabel("Email..")

        self.first_name_lineEdit = QLineEdit()
        self.middle_name_lineEdit = QLineEdit()
        self.last_name_lineEdit = QLineEdit()
        self.email_lineEdit = QLineEdit()

        # layout1
        horLayout_1 = QHBoxLayout()
        horLayout_1.addWidget(first_name_label)
        horLayout_1.addWidget(self.first_name_lineEdit)

        horLayout_2 = QHBoxLayout()
        horLayout_2.addWidget(middle_name_label)
        horLayout_2.addWidget(self.middle_name_lineEdit)

        horLayout_3 = QHBoxLayout()
        horLayout_3.addWidget(last_name_label)
        horLayout_3.addWidget(self.last_name_lineEdit)

        horLayout_4 = QHBoxLayout()
        horLayout_4.addWidget(email_label)
        horLayout_4.addWidget(self.email_lineEdit)


        vLayout = QVBoxLayout()
        vLayout.addLayout(horLayout_1)
        vLayout.addLayout(horLayout_2)
        vLayout.addLayout(horLayout_3)
        vLayout.addLayout(horLayout_4)

        enterBtn = QPushButton("enterBtn")
        enterBtn.clicked.connect(self.displayNames)
        self.userName = QLabel("")

        vLayout.addWidget(enterBtn)
        vLayout.addWidget(self.userName)
        self.setLayout(vLayout)


    def displayNames(self):
        print(f"userName is {self.first_name_lineEdit.text()} {self.middle_name_lineEdit.text()} {self.last_name_lineEdit.text()} {self.email_lineEdit.text()}")
        userName = f"{self.first_name_lineEdit.text()} {self.middle_name_lineEdit.text()} {self.last_name_lineEdit.text()}"
        self.userName.setText(f"Welcome back {self.first_name_lineEdit.text()}")

        