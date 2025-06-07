from PySide6.QtWidgets import QApplication

import sys

from mainWindow import MainWindow

app = QApplication()
window = MainWindow()
window.show()
exit_code = app.exec()

sys.exit(exit_code)