from PySide6.QtWidgets import QApplication
from rocketWidget import RocketWidget
import sys

app = QApplication()
window  = RocketWidget()
window.show()
exit_code = app.exec()
sys.exit(exit_code)