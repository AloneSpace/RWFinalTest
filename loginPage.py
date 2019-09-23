import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi

class LoginPage(QDialog):
    def __init__(self):
        super(LoginPage,self).__init__()
        loadUi("loaderUI/loginUI.ui",self)
        self.setWindowTitle('Rittiyawannalai Final Test')
        self.submitButton.clicked.connect(self.on_submit)

    def on_submit(self):
        self.close()
        my_dialog = QDialog(self)
        my_dialog.setWindowTitle("ยินต้อนรับคุณ กรัณย์ภัทร พรหมวิสุทธิ์ ("+ self.user_field.text() + ")")
        my_dialog.setWindowModality(Qt.ApplicationModal)
        my_dialog.setFixedHeight(200)
        my_dialog.setFixedWidth(400)
        my_dialog.exec_()

    # def on_submitTest(self):
    #
    # def on_cancelTest(self):


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = LoginPage()
    widget.show()
    sys.exit(app.exec_())