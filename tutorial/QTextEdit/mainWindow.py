from PySide6.QtWidgets import QWidget, QTextEdit, QVBoxLayout, QHBoxLayout, QPushButton

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("MousePad")
        self.multiTextEdit = QTextEdit()
        v_layout = QVBoxLayout()
        h_layout = QHBoxLayout()


        copyBtn = QPushButton("Copy")
        copyBtn.clicked.connect(self.multiTextEdit.copy)
        cutBtn = QPushButton("Cut")
        cutBtn.clicked.connect(self.multiTextEdit.cut)
        PasteBtn = QPushButton("Paste")
        PasteBtn.clicked.connect(self.multiTextEdit.paste)
        undoBtn = QPushButton("Undo")
        undoBtn.clicked.connect(self.multiTextEdit.undo)
        redoBtn = QPushButton("Redo")
        redoBtn.clicked.connect(self.multiTextEdit.redo)

        saveBtn = QPushButton("Save")
        saveBtn.clicked.connect(self.copyText)


        h_layout.addWidget(copyBtn)
        h_layout.addWidget(cutBtn)
        h_layout.addWidget(PasteBtn)
        h_layout.addWidget(undoBtn)
        h_layout.addWidget(redoBtn)
        h_layout.addWidget(saveBtn)

        EnterBtn = QPushButton("Enter")

        v_layout.addLayout(h_layout)
        v_layout.addWidget(self.multiTextEdit)
        v_layout.addWidget(EnterBtn)

        self.setLayout(v_layout)

    def copyText(self):
        copiedText = self.multiTextEdit.copy



    