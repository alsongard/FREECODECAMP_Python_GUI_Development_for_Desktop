# shows multiple user interface for which you can toggle the interfaces

from PySide6.QtWidgets import QWidget, QPushButton, QTabWidget, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QListWidget

class TabViewWindow(QWidget):
    def __init__(self):
        super().__init__()

        tab_widget = QTabWidget()

        widget_form = QWidget() # create your own QWidget for which you can display something 
        # user_name_label = QLabel("Full Name") # labell for fullname
        first_name_label = QLabel("First Name")
        middle_name_label = QLabel("Middle Name")
        last_name_label = QLabel("Last Name")
        self.middle_name_input = QLineEdit()
        self.first_name_input = QLineEdit()
        self.last_name_input = QLineEdit()
        # user_name_input = QLineEdit() # input for user input 

        # add signal & slot
        self.first_name_input.editingFinished.connect(self.getFirstText)
        self.middle_name_input.editingFinished.connect(self.getMiddleText)
        self.last_name_input.editingFinished.connect(self.getLastText)



        formLayout = QVBoxLayout() # form layout that will hod user label and user_input
        formLayout.addWidget(first_name_label) # add label
        formLayout.addWidget(self.first_name_input) 
        formLayout.addWidget(middle_name_label)
        formLayout.addWidget(self.middle_name_input)
        formLayout.addWidget(last_name_label)
        formLayout.addWidget(self.last_name_input)

        # button for entering username
        okBtn = QPushButton("Ok")
        cancelBtn = QPushButton("Cancel")

        # signal to the buttons
        okBtn.clicked.connect(self.displayOnFinished)

        # add button Layout
        buttonLayout = QHBoxLayout() # create a horizontal layout for buttons 
        buttonLayout.addWidget(okBtn) # add button in horizontal
        buttonLayout.addWidget(cancelBtn) # add button in horizontal


        formLayout.addLayout(buttonLayout)

        widget_form.setLayout(formLayout)



        # second QWidget for holding QListWidget
        secondQwidget  = QWidget()

        # listWidget
        self.userListWidget = QListWidget()
        self.userListWidget.addItem("Earth")
        self.userListWidget.addItems(["Mercury", "Venus", "Mars", "Jupiter", "Jupiter", "Saturn", "Uranus"])

        # add label and input for getting user input

        newItemLabel = QLabel("Enter name of new Item")
        self.newItemInputLine = QLineEdit()

        # add buttons for adding and removing
        addItemBtn = QPushButton("Add Item")
        dltItemBtn = QPushButton("Delete Item")


        addItemBtn.clicked.connect(self.addItemToList)
        dltItemBtn.clicked.connect(self.removeItemFromList)
        # for the display set : listWidget first
        # set label&lineEdit and buttons in singleLayout
        # the buttons set HorizontalLayout

        # verticalLayout
        v_container = QVBoxLayout()
        v_container.addWidget(self.userListWidget)
        v_container.addWidget(newItemLabel)
        v_container.addWidget(self.newItemInputLine)

        # horLayout
        listButtonLayout = QHBoxLayout()
        listButtonLayout.addWidget(addItemBtn)
        listButtonLayout.addWidget(dltItemBtn)

        v_container.addLayout(listButtonLayout)
        
        
        secondQwidget.setLayout(v_container)


        tab_widget.addTab(widget_form, "Information")
        tab_widget.addTab(secondQwidget, "List Information")


        # set final/Window view
        app_vert_layout = QVBoxLayout()
        app_vert_layout.addWidget(tab_widget)

        self.setLayout(app_vert_layout)

    def displayOnFinished(self):
        print(f"User full Name : {self.first_name_input.text()} {self.middle_name_input.text()} {self.last_name_input.text()}")

    def getFirstText(self):
        print(self.first_name_input.text())
        return self.first_name_input.text()
    
    def getMiddleText(self):
        print(self.middle_name_input.text())
        return self.middle_name_input.text()
    
    def getLastText(self):
        text = self.last_name_input.text()
        print(self.last_name_input.text())
        return self.last_name_input.text()
    

    def addItemToList(self):
        new_item = self.newItemInputLine.text()
        self.userListWidget.addItem(new_item)

    def removeItemFromList(self):
        for item in self.userListWidget.selectedItems():
            self.userListWidget.takeItem(self.userListWidget.row(item))
        
