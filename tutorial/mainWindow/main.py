from PySide6.QtWidgets import QApplication
from mainWindow import ApplicationMainwindow
import sys

app = QApplication()

window = ApplicationMainwindow(app)
window.show()

exit_code = app.exec()
sys.exit(exit_code)