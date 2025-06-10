from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QSizePolicy ,QHBoxLayout, QLineEdit, QLabel

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()


        v_layout = QVBoxLayout()
        h_layout_2 = QHBoxLayout()
        h_layout_1 = QHBoxLayout()


        user_label = QLabel("Username: ")


        # to alter the size of the QLineEdit we use setSizePolicy(horizontalPolicy, verticalPolicy) QSizePolicy.Policy.Expanding || QSizePolicy.Policy.Fixed
        line_edit = QLineEdit()
        line_edit.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

        button_later = QPushButton("Remind me later")
        button_ok = QPushButton("Ok")
        button_cancel = QPushButton("Cancel")
        
        # add to h_layout_1
        h_layout_1.addWidget(user_label)
        h_layout_1.addWidget(line_edit)

        # add to h_layout_2
        h_layout_2.addWidget(button_later, 1)  # default stretch is 1
        h_layout_2.addWidget(button_ok, 1) # default stretch : 1
        h_layout_2.addWidget(button_cancel,2) # stretch set to 2


        v_layout.addLayout(h_layout_1)
        v_layout.addLayout(h_layout_2)

        self.setLayout(v_layout)
        

