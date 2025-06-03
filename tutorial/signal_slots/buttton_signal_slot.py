from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys

app = QApplication()
window = QMainWindow()

def buttonFunc(data):
    print(f"The button was pressed : {data}")
    
button = QPushButton()
button.setCheckable(True)
button.setText("Clicked")

button.clicked.connect(buttonFunc)
window.setCentralWidget(button)
window.show()

exit_code = app.exec()
sys.exit(exit_code)
