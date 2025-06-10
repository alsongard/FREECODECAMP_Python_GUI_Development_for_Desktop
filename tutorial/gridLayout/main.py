from PySide6.QtWidgets import QApplication
import sys
from mainWindow  import MainWindowWidget
from calculator import MainCalculator
app = QApplication()
# window = MainWindowWidget()
window = MainCalculator()
window.show()
exit_code = app.exec()
sys.exit(exit_code)