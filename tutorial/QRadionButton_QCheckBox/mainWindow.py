from PySide6.QtWidgets import QWidget, QVBoxLayout, QGroupBox, QHBoxLayout, QCheckBox, QRadioButton, QButtonGroup

class MainWindowCheckBox(QWidget):
    def __init__(self):
        super().__init__()


        self.setWindowTitle("QCheckBox and QRadio Buttons")

        # checkBoxes: operating system
        os =  QGroupBox("Choose Operating System")

        windows = QCheckBox("Windows")
        windows.toggled.connect(self.onWindows)

        linux = QCheckBox("Linux")
        linux.toggled.connect(self.onLInux)

        mac = QCheckBox("Mac")
        mac.toggled.connect(self.onMac)


        # add the above widgets to a given layout
        v_layout_1 = QVBoxLayout()
        v_layout_1.addWidget(windows)
        v_layout_1.addWidget(linux)
        v_layout_1.addWidget(mac)

        os.setLayout(v_layout_1)

        # checkbox with exclusive set to True(only select one option)
        # new groupbox for code editors
        codeEditors = QGroupBox("Select code editor")

        # create checkbox
        vsCode = QCheckBox("visual studio code")
        subLimeTxt = QCheckBox("Sublime Tex")
        vsCordium = QCheckBox("VS Cordium")


        codeButtonGroup = QButtonGroup(self) # create button group instance
        # add checkBox to button group : remeber the QButtonGroup() adds exclusivity by default 
        codeButtonGroup.addButton(vsCode)
        codeButtonGroup.addButton(subLimeTxt)
        codeButtonGroup.addButton(vsCordium)
        codeButtonGroup.setExclusive(True)


        # add this to v_layout
        v_layout = QVBoxLayout()
        v_layout.addWidget(vsCode)
        v_layout.addWidget(subLimeTxt)
        v_layout.addWidget(vsCordium)
        # to to QGroupBox() object
        codeEditors.setLayout(v_layout)

        # new GroupBox : QGroupBox()
        programmingLangBox = QGroupBox("Programming Language")
        pyrdBtn = QRadioButton("Python")
        tyrdBtn = QRadioButton("TypeScript")
        jsrdBtn = QRadioButton("Javascript")

        # set layout : vertical
        program_v_layout = QVBoxLayout()
        program_v_layout.addWidget(pyrdBtn)
        program_v_layout.addWidget(tyrdBtn)
        program_v_layout.addWidget(jsrdBtn)

        programmingLangBox.setLayout(program_v_layout)

        # set layout for the first and Secod QBoxLayout()
        h_layout = QHBoxLayout()
        h_layout.addWidget(os)
        h_layout.addWidget(codeEditors)


        # layout for the application : vertical
        v_app_layout = QVBoxLayout()
        v_app_layout.addLayout(h_layout)
        v_app_layout.addWidget(programmingLangBox)


        self.setLayout(v_app_layout)
    


    def onLInux(self):
        print(f"User is using Linux Operating System")
    
    def onWindows(self):
        print(f"User is using Windows Operating System")

    def onMac(self):
        print(f"User is using Mac Operating System")