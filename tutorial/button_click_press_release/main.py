from PySide6.QtWidgets import QApplication
import sys
from mainWindow import MainWidgetApp

app = QApplication(sys.argv)
window = MainWidgetApp()


window.show()

exit_code = app.exec()

sys.exit(exit_code)