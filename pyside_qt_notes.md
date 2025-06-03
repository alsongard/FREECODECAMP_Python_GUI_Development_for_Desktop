Use Qt widgets API for developing desktop applications(cross platform)
Use QML language for developing widgets for android and embeded systems.

QT can be used in:
- GUI
- network
- threading
- databases
- others utitilities


```python

from PySide6.QtWidgets import QApplication, QWidget
```
``QApplication``: this the core class that manages the applications control flow, main setting and the event loop. In every PySide6 GUI application, it is required to have the QApplication.*(core class, handling eventloops, control flow and main settings)*

``QWidget``:
The Qwidget is the base class for all user interface objects. Used to create main window for an applications

```python
app  = QApplication(sys.argv)
```
why pass ``sys.argv`` to ``QApplication``
QApplication can sometimes take arguments for the application settings. Qt-specific arguments (like `-style` for setting the application style). We pass `sys.argv` to allow such arguments to be processed by Qt.
The line creates a QApplication object that will be used to manage the applicatoin event loop


creating the main window:
```python
window = QWidget()
```
The above code is used to create the main window for the application. By default the window is empty window.Remember from above QWidget is used to create a window for the application and a class all the user interface objects

Display the window:
```python
window.show()
```

```python
app.exec()
```
app.exec()` starts the application's event loop. The event loop is an infinite loop that waits for user interactions (like mouse clicks, key presses) and system events, and then dispatches them to the appropriate widgets.

### **using QMainWindow()**
the ``QMainWindow()`` class is used to center the main components for the Window.
Example:
```python
from PySide6.QtWidgets import QMainWindow, QPushButton
class Button(QMainWindow): # inherit everything from QMainWindow: instance of button same to window = QMainWindow()
    def __init__(self):
        super().__init__
        self.setWindowTitle("Some Title")
        button = QPushButton()
        button.setText("Python GUI")

        self.setCentralWidget(button)

# main.py file
from PySide6.QtWidget import QApplication
from button_holder import Button
app = QApplication() # set main window
window = Button()
window.show()
exit_code = app.exec()
sys.exit(exit_code)
```


Signal and Slots
Example:
```python
button = QPushButton()
button.clicked.connect(buttonClickedFunc)
# buttonObject. clicked==slot connect ==signal
```

```python
def buttonClickFunc(data):
    print(f"Button is clicked : {data}")
button.setCheckable(True) # this makes the button checkable, the value true is used in this case
                          # the value: True can toggle by clicking the button

# set up a signal on the button which is clicked and then add a slot which is connect
button.clicked.connect(buttonClickFunc)
```


### **Using Widgets and Layouts Basics**


### **QMainWindow**
- Menu
- ToolBars
- StatusBars
- Actions


**QMainWindow**
```python


```

**QIcon**
To set an icon we use QIcon() class from  ``PySide6.QtGui import QIcon()``.
Syntax: ``QIcon(path_to_file_icon)``
Example:
```python
class AppMainWindow(QtMainWindow):
    def__init__(self, app):
        super().__init__()

        self.app = app
        self.setWindowTitle("SomeName")
        self.setWindowIcon(QIcon("assets/images/pen_icon.png"))
```




1. menus
To add a menu bar to the main window, you use the menuBar() method of the QMainWindow:The menuBar() method returns a QMenuBar object. If a QMenuBar object doesn’t exist, the menuBar() will create a new  QMenuBar object before returning it. Otherwise, it returns the existing QMenuBar object.
```python
menuBarObject = self.menuBar()
```
