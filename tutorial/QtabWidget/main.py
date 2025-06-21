from PySide6.QtWidgets import QApplication
import sys
from tabWidgetWindow import TabViewWindow
app = QApplication()
window  = TabViewWindow()
window.show()
exit_code = app.exec()
sys.exit(exit_code)