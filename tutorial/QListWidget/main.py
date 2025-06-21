from PySide6.QtWidgets import QApplication, QWidget

from listWidget import ListWidgetWindow;
import sys
app = QApplication()

window = ListWidgetWindow()
window.show()
exit_code = app.exec()
sys.exit(exit_code)