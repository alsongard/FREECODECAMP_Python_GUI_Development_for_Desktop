from PySide6.QtWidgets import QWidget, QListWidget, QPushButton, QAbstractItemView, QVBoxLayout, QHBoxLayout


class ListWidgetWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QListWidget Introduction and Practise")
        verticalLayout = QVBoxLayout()
        self.myListWidget =QListWidget()
        self.myListWidget.setSelectionMode(QAbstractItemView.MultiSelection)
        self.myListWidget.addItem("One")
        self.myListWidget.addItems(["Jupiter", "Earth"])
        self.myListWidget.currentItemChanged.connect(self.current_item_changed)
        self.myListWidget.currentTextChanged.connect(self.current_text_changed)


        # add to box layout the following buttons
        button_hor_layout = QHBoxLayout()
        button_add_item = QPushButton("Add  Item")
        button_add_item.clicked.connect(self.add_item)

        button_delete_item = QPushButton("Delete Item")
        button_delete_item.clicked.connect(self.delete_item)

        button_item_count = QPushButton("Item Count")
        button_item_count.clicked.connect(self.item_count)

        button_selected_items = QPushButton("Selected Items")
        button_selected_items.clicked.connect(self.select_items)

        button_hor_layout.addWidget(button_item_count)
        button_hor_layout.addWidget(button_selected_items)
        button_hor_layout.addWidget(button_add_item)
        button_hor_layout.addWidget(button_delete_item)

        verticalLayout.addWidget(self.myListWidget)
        verticalLayout.addLayout(button_hor_layout)
        self.setLayout(verticalLayout)

    def current_item_changed(self, item):
        print(f"Current Item: {item.text()}")

    def current_text_changed(self, text):
        print(f"Current Text changed : ${text}")
    
    def add_item(self):
        self.myListWidget.addItem("Pluto")

    def item_count(self):
        print(f"List widget count is : {self.myListWidget.count()}")
        return self.myListWidget.count()

    def delete_item(self):
        self.myListWidget.takeItem(self.myListWidget.currentRow())

    def select_items(self):
        selectedList = self.myListWidget.selectedItems()
        for item in selectedList:
            print(f"Item selected : {item.text()}")