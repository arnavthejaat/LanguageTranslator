from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import googletrans
from googletrans import Translator


# Window Class
class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle("Translator")
        self.initUI()
        self.translator = Translator()
        self.trans_lang = ""

    def initUI(self):
        #self.textbox = QtWidgets.QLineEdit(self)
        #self.textbox.move(50, 100)

        self.button = QtWidgets.QPushButton(self)
        self.button.setText("Translate")
        self.button.clicked.connect(self.clicked)
        self.button.move(200, 100)

        self.translatedText = QtWidgets.QLineEdit(self)
        self.translatedText.move(300, 100)

        self.userInput = QtWidgets.QLineEdit(self)
        self.userInput.move(100, 100)

    def clicked(self):
        self.trans_lang = self.translator.translate(str(self.userInput.text()), src="auto", dest="en").text
        self.translatedText.setText(str(self.trans_lang))
        self.update()

    def update(self):
        self.translatedText.adjustSize()

# Window function

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()
