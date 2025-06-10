from PySide6.QtWidgets import QApplication
from mainWindow import MainWindowCheckBox
from checkbox_exclusive import CheckBoxExclusive
import sys

app = QApplication()

window = MainWindowCheckBox()

# window = CheckBoxExclusive()
window.show()

exit_code = app.exec()

sys.exit(exit_code)
