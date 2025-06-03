from PySide6.QtWidgets import QApplication
from button_holder import Button
import sys # sys module for getting command line arguments passed to the script file: usefull for settings

app = QApplication()
window  = Button() # button inherits everything from QMainWindow() hence we can use it's instace to create window
window.show()
exit_code =app.exec()
sys.exit(exit_code)