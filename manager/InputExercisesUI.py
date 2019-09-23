import sys
import os
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi

class InputUI(QDialog):
    def __init__(self):
        super(InputUI,self).__init__()
        current_dir = os.path.abspath(os.path.dirname(__file__))
        parent_dir = os.path.abspath(current_dir + "/../")
        loadUi(parent_dir + "/loaderUI/inputExercises.ui",self)
        self.setWindowTitle('Rittiyawannalai Final Test')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = InputUI()
    widget.show()
    sys.exit(app.exec_())