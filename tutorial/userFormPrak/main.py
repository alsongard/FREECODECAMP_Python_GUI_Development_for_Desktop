from PySide6.QtWidgets import QApplication
from mainWidget import MainWidget
import sys

app = QApplication()
window = MainWidget()
window.show()
exit_code = app.exec()

sys.exit(exit_code)
