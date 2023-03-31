from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

Form, Window = uic.loadUiType("radio-online.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()
def on_click_1():
    print("Click!!!")
form.pushButton.clicked.connect(on_click_1)
app.exec()
