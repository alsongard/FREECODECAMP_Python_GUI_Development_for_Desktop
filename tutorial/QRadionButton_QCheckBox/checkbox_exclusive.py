from PySide6.QtWidgets import QWidget, QPushButton, QCheckBox, QGroupBox, QHBoxLayout, QVBoxLayout, QButtonGroup

class CheckBoxExclusive(QWidget):
    def __init__(self):
        super().__init__()


        # start setting the groupBox
        beverage = QGroupBox("Select Beverage")

        coffee = QCheckBox("coffee")
        tea = QCheckBox("tea")
        juice = QCheckBox("Juice")

        coffee.setChecked(True)

        beverageExclusiveButtons = QButtonGroup(self)
        beverageExclusiveButtons.addButton(coffee)
        beverageExclusiveButtons.addButton(tea)
        beverageExclusiveButtons.addButton(juice)
        beverageExclusiveButtons.setExclusive(True) # ensures that only 1 button is checked (default when using QButtonGroup())

        # add a Vertical layout for the checkbox
        v_layout = QVBoxLayout()
        v_layout.addWidget(coffee)
        v_layout.addWidget(tea)
        v_layout.addWidget(juice)

        beverage.setLayout(v_layout)

        # create layout for the window
        h_layout = QHBoxLayout()
        h_layout.addWidget(beverage)

        self.setLayout(h_layout)
