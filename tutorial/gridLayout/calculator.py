from PySide6.QtWidgets import QWidget, QGridLayout,QSizePolicy, QPushButton, QLineEdit, QHBoxLayout, QVBoxLayout
class MainCalculator(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Calculator: Grid Layout setup")

        # calculator 

        # calculator part
        valueNumberINput = QLineEdit()

        v_layout = QVBoxLayout()
        v_layout.addWidget(valueNumberINput)

        button_1 = QPushButton('1')
        button_2 = QPushButton('2')
        button_3 = QPushButton('3')
        button_4 = QPushButton('4')
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
        grid_layout_1.addWidget(button_4, 1,0)
        grid_layout_1.addWidget(button_5, 1,1)
        grid_layout_1.addWidget(button_6, 1,2)
        grid_layout_1.addWidget(button_7, 2,0)
        grid_layout_1.addWidget(button_8, 2,1)
        grid_layout_1.addWidget(button_9, 2,2)


        grid_layout_2 = QGridLayout()

        multiplyBtn = QPushButton("*")

        divisionBtn = QPushButton("/")
        modulusBtn = QPushButton("%")
        addBtn = QPushButton("+")
        subtractBtn = QPushButton("-")
        equalsBtn = QPushButton("=")
        exponentBtn = QPushButton("exp")
        pieBtn = QPushButton("π")

 
        # wide 2 columns 4 row   || values are : row | column
        grid_layout_2.addWidget(addBtn,0,0)    
        grid_layout_2.addWidget(subtractBtn,1,0) 
        grid_layout_2.addWidget(multiplyBtn,2,0)
        # grid_layout_2.addWidget(multiplyBtn,,0, 0,1)    

        # 1 row with 4 columns
        grid_layout_3 = QGridLayout()
        grid_layout_3.addWidget(pieBtn,0,1 )
        grid_layout_3.addWidget(exponentBtn, 0,2)
        grid_layout_3.addWidget(equalsBtn, 0,3, 0,2)

        h_layout = QHBoxLayout()
        h_layout.addLayout(grid_layout_1)
        h_layout.addLayout(grid_layout_2)


        v_layout.addLayout(h_layout)
        v_layout.addLayout(grid_layout_3)

        self.setLayout(v_layout)

        
