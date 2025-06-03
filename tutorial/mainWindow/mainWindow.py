from PySide6.QtWidgets import QMainWindow, QPushButton
from PySide6.QtGui import QIcon

class ApplicationMainwindow(QMainWindow):
    def __init__(self, app):
        super().__init__()

        self.app = app # declare an app member
        self.setWindowTitle("QMainWindow Tutorial")
        self.setWindowIcon(QIcon("../assets/images/pen_image_1.png"))
        
        # to add a menuBar to the mainWindow we use menuBar() method from QMainWindow
        # it will create a QMenuBar object. if QMenuBar object exist it uses the existing
        # object otherwise return a new QMenuBar object

        menuBarObject = self.menuBar()

        # by default the menuBarObject is empty, to add a menu we use addMenu() method
        file_menu = menuBarObject.addMenu("&File")
        edit_menu = menuBarObject.addMenu("&Edit")
        help_menu = menuBarObject.addMenu("&Help")

        # add items to a menu we use addAction() method from QAction class subItem in File MenuBarObject
        new_action = file_menu.addAction('&New')
        save_action = file_menu.addAction('&Save')
        quit_action = file_menu.addAction("&Quit")

        quit_action.triggered.connect(self.quit_app)
        save_action.triggered.connect(self.save_file)
        new_action.triggered.connect(self.save_file)


        # edit_menu menu items
        edit_menu.addAction("Edit")
        edit_menu.addAction("Copy")
        edit_menu.addAction("Cut")
        edit_menu.addAction("Pase")
        edit_menu.addAction("Undo")
        edit_menu.addAction("Redo")

    def quit_app(self):
        self.app.quit()
        
    def new_file(self):
        print("new file")

    def save_file(self):
        print("save file")


"""
so to create a menuBar, we use menuBar() method from the QMainWindow()
```
menuBarObject = self.MenuBar()
# menuBarObject is empty to add menu we use addMenu() function and assign a value to it
file_menu = menuBarObject.addMenu('&File')
edit_menu = menuBarObject.addMenu('&Edit')
view_menu = menuBarObject.addMenu('&View')
"""