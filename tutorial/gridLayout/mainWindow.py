from PySide6.QtWidgets import QWidget, QSizePolicy ,QGridLayout,QSizePolicy, QPushButton, QLineEdit, QHBoxLayout, QVBoxLayout


class MainWindowWidget(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Grid Layout setup")



        button_1 = QPushButton('1')
        button_2 = QPushButton('2')
        button_3 = QPushButton('3')
        button_4 = QPushButton('4')
        button_4.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        button_5 = QPushButton('5')
        button_6 = QPushButton('6')
        button_7 = QPushButton('7')
        button_8 = QPushButton('8')
        button_9 = QPushButton('9')

        grid_layout_1 =  QGridLayout() # create an instance of the layout
        """
        To add widget to each layout do:
        grid_layout.addWidget(button, row_value, column_value)
        the row_value specify the row upon which the button will be and so does the column
        e.g grid_layout.addWidget(button_1, 0, 0) row 0 column 0

        for span: to span a widget component in multiple rows or columns
        grid_layout.addWidget(button_1, 0, 0, 1, 0) 
        span to the next row: row 1, but same column 0
        """
        # design for calculator 3 columns 0, 1, 2 ||  rows 3 
        grid_layout_1.addWidget(button_1, 0,0) 
        grid_layout_1.addWidget(button_2, 0,1)
        grid_layout_1.addWidget(button_3, 0,2)
        grid_layout_1.addWidget(button_4, 1,0, 2,1)
        grid_layout_1.addWidget(button_5, 1,1)
        grid_layout_1.addWidget(button_6, 1,2)
        # grid_layout_1.addWidget(button_7, 2,0) # space will be taken by button 4
        grid_layout_1.addWidget(button_8, 2,1)
        grid_layout_1.addWidget(button_9, 2,2)

        self.setLayout(grid_layout_1)


