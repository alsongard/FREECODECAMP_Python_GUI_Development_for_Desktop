from PySide6.QtWidgets import QMainWindow, QWidget, QPushButton, QMessageBox, QHBoxLayout
from PySide6.QtGui import QAction, QIcon
from mainWidget import MainWidget

class MainWindowApp(QMainWindow):
    def __init__(self, app):
        super().__init__()

        self.app = app
    # create menuBarObject which is empty
        menuBarObject = self.menuBar()


        # add menuBarBars to menuBarObject
        fileMenuBarBar = menuBarObject.addMenu("&File")
        editMenuBarBar = menuBarObject.addMenu("&Edit")
        viewMenuBarBar  = menuBarObject.addMenu("&View")
        goMenuBarBar = menuBarObject.addMenu("&Go")
        bookMarkMenuBarBar = menuBarObject.addMenu("&Bookmars")
        helpMenuBarBar =  menuBarObject.addMenu("&Help")

        
        newTabfileMenuBarBarBar = fileMenuBarBar.addAction("New Tab")
        newTabfileMenuBarBarBar.setShortcut("Ctrl+T")
        newTabfileMenuBarBarBar.triggered.connect(self.newTabfileMenu)

        newWindowfileMenuBarBarBar = fileMenuBarBar.addAction("New Window")
        newWindowfileMenuBarBarBar.setShortcut("Ctrl+N")
        newWindowfileMenuBarBarBar.triggered.connect(self.newWindowfileMenu)

        createFolderfileMenuBarBarBar = fileMenuBarBar.addAction("Create Folder")
        createFolderfileMenuBarBarBar.setShortcut("Shift+Ctrl+N")
        createFolderfileMenuBarBarBar.triggered.connect(self.createFolderfileMenu)

        openTermialfileMenuBarBarBar = fileMenuBarBar.addAction("Open Terminal Here")
        openTermialfileMenuBarBarBar.setShortcut("F4")

        closeWindowfileMenuBarBarBar = fileMenuBarBar.addAction("Close Window")
        closeWindowfileMenuBarBarBar.setShortcut("Ctrl+Q")
        closeWindowfileMenuBarBarBar.triggered.connect(self.CloseApp)



    def newTabfileMenu(self):
        print("creating a new tab")

    def newWindowfileMenu(self):
        print("creating a new window")
    
    def createFolderfileMenu(self):
        print("creatin a new folder")
    
    def CloseApp(self):
        self.app.exit()

# create folder(Shift + Ctrl +N)
# create documents
# Open terminal here
# Open as root


"""
Static MessageBox methods
# can be:
# critical - question -information -warning -about

#
def button_cliked_critical(self):
    response = QMessageBox.critical(self, "Message Title", "Critical Message!", QMessageBox.ok | QMessageBox.Cancel )
    if response == QMessageBox.ok:
        print("something usefull")
    else:
        print("not useful")
"""