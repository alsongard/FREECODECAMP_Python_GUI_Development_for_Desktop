from PySide6.QtWidgets import QApplication, QSlider, QMainWindow
import sys
from PySide6.QtCore import Qt


def respond_to_slider_change(data):
    print(f"Slider moved to: {data} ")

app = QApplication()

window = QMainWindow()
slider = QSlider(Qt.Orientation.Horizontal) # by default it is vertical : slider
slider.setMinimum(1)
slider.setMaximum(100)
slider.setValue(25)

# component.signal.slot|connect

slider.valueChanged.connect(respond_to_slider_change)

window.setCentralWidget(slider)
window.show()

exit_code = app.exec()
sys.exit(exit_code)