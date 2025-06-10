from PySide6.QtWidgets import QWidget, QApplication
import sys
from mainWindow import MainWidget
app = QApplication()
window = MainWidget()
window.show()
exit_code = app.exec()
sys.exit(exit_code)