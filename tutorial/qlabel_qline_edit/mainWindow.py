from PySide6.QtWidgets  import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout

class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QLIne and QLabel")
        label = QLabel("Fullname: ")
        self.line_edit = QLineEdit()
        # QLineEdit() signal->Connect
        self.line_edit.cursorPositionChanged.connect(self.cursor_position_changed)
        self.line_edit.editingFinished.connect(self.editFinished)
        self.line_edit.selectionChanged.connect(self.selectedTextonLideEdit)

        

        button = QPushButton("Enter")
        button.clicked.connect(self.statement_print)
        self.label1 = QLabel("SignIn")

        h_layout = QHBoxLayout()
        h_layout.addWidget(label)
        h_layout.addWidget(self.line_edit)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(button)
        v_layout.addWidget(self.label1)

        self.setLayout(v_layout)

    def statement_print(self):
        print(f"Text data is : {self.line_edit.text()}")
        # change text of QLabel
        self.label1.setText(self.line_edit.text())

    def cursor_position_changed(self,old,new):
        print(f"The position is  old: {old}, new: {new}")
    
    def editFinished(self):
        print("user Just pressed enter on LineEdit")

    def selectedTextonLideEdit(self):
        print(f"Selected text is : {self.line_edit.selectedText()}")