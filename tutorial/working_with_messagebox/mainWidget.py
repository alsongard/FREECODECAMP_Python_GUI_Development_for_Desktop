from PySide6.QtWidgets import QMainWindow, QWidget, QPushButton, QMessageBox, QHBoxLayout
from PySide6.QtGui import QAction, QIcon

class MainWidget(QWidget):
    def __init__(self):
        super().__init__() # access all methods/vars from QWidget

        # setup layout
        horizontal_layout = QHBoxLayout()

        # buttons
        exitAlert = QPushButton("Exit Alert")
        informationBtn = QPushButton("Information")
        criticalBtn = QPushButton("Critical")
        warningBtn = QPushButton("Warning")
        questionBtn = QPushButton("Question")


        # clicked.connect || signal.slot
        exitAlert.clicked.connect(self.button_clicked_hard) # button clicked hard
        criticalBtn.clicked.connect(self.button_clicked_critical) # button clicked critical function
        informationBtn.clicked.connect(self.button_clicked_information) # button clicked information function
        warningBtn.clicked.connect(self.button_clicked_question) # button clicked warning
        questionBtn.clicked.connect(self.button_clicked_question)

        # add button to layout
        horizontal_layout.addWidget(exitAlert)
        horizontal_layout.addWidget(informationBtn)
        horizontal_layout.addWidget(criticalBtn)
        horizontal_layout.addWidget(warningBtn)


        # set layout
        self.setLayout(horizontal_layout)


    # hard way
    def button_clicked_hard(self):
        messageObject = QMessageBox()
        # set msgBox size
        messageObject.setMinimumSize(700, 200)
        # set windowTitle
        messageObject.setWindowTitle("Read!!!")
        # setting Texxt
        messageObject.setText("something happened")
        # setting INformativeText
        messageObject.setInformativeText("Do you want to proceed?")
        #seting icon
        messageObject.setIcon(QMessageBox.Icon.Critical)  # Use setIcon() with enum
        # Set standard buttons
        messageObject.setStandardButtons(
            QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel  # Use enum values, not hex
        )
        # Set default button
        messageObject.setDefaultButton(QMessageBox.StandardButton.Ok)  # Correct method name

        ret = messageObject.exec()
        if ret == QMessageBox.StandardButton.Ok:
            print("YOu choose well")
        else:
            print("You choose parially better")
   
    def button_clicked_critical(self):
        messageBoxResponse = QMessageBox().critical(
            self,
            "Critical",
            "Are your sure you would like to Proceed? ",
            QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel,
            QMessageBox.StandardButton.Ok
            )
        if messageBoxResponse == QMessageBox.StandardButton.Ok:
            print("Proceeding with the given changes")
        else:
            print("Resetting to default factory")

    def button_clicked_information(self):
        msgBoxResponse = QMessageBox.information(
            self,
            "Information Share",
            "Would you like this information to be accessed by public users",
            QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel,
            QMessageBox.StandardButton.Ok
            )
        if msgBoxResponse == QMessageBox.StandardButton.Ok:
            print("This information would be availabe to users")
        else:
            print("Information will not be shared to other users")

    def button_clicked_warning(self):
        responseMsgBox = QMessageBox.warning(
            self,
            "Warning!",
            "Do not proceed as this files are used by SystemmD",
            QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel,
            QMessageBox.StandardButton.Cancel
        )
        if responseMsgBox == QMessageBox.StandardButton.Ok:
            print("Deleting the files selected")
        else:
            print("Delete Operation cancelled")

    def button_clicked_question(self):
        responseMsgBox = QMessageBox.question(
            self,
            "Question",
            "Would you like to continue with the update?",
            QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel,
            QMessageBox.StandardButton.Ok
        )
        if responseMsgBox == QMessageBox.StandardButton.Ok:
            print("Upgrading and Restarting the system")
        else:
            print("Not upgrading packages kali-desktop-themes, vscode, spotify-client...")

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