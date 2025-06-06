from PySide6.QtWidgets import QApplication, QMainWindow
import sys
from mainWindow import MainWindowApp
from mainWidget import MainWidget

app = QApplication(sys.argv)

window = MainWidget()

window.show()
exit_code = app.exec()
sys.exit(exit_code)