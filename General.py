import sys

from PySide6.QtWidgets import QApplication, QMainWindow

import buttons
import main
from design import Ui_mainWindow

class Password(QMainWindow):
    def __init__(self):
        super(Password, self).__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)

        self.connect_slider_to_spinbox()
        self.set_password()

    def connect_slider_to_spinbox(self) -> None:
        self.ui.pas_len.valueChanged.connect(self.ui.spinBox.setValue)
        self.ui.spinBox.valueChanged.connect(self.ui.pas_len.setValue)
        self.ui.spinBox.valueChanged.connect(self.set_password)
        self.ui.low_case.clicked.connect(self.set_password)
        self.ui.up_case.clicked.connect(self.set_password)
        self.ui.digits.clicked.connect(self.set_password)
        self.ui.spec.clicked.connect(self.set_password)
        self.ui.generate.clicked.connect(self.set_password)
        self.ui.reload.clicked.connect(self.set_password)
        self.ui.copy.clicked.connect(self.copy_pas)



    def get_character(self) -> str:
        chars = ''
        for btn in buttons.Characters:
            if getattr(self.ui, btn.name).isChecked():
                chars += btn.value
        return chars

    def copy_pas(self) -> None:
        QApplication.clipboard().setText(self.ui.password.text())


    def set_password(self) -> None:
        try:
            self.ui.password.setText(
                main.create_pas(len=self.ui.pas_len.value(), characters=self.get_character())
            )
        except IndexError:
            self.ui.password.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Password()
    window.show()
    sys.exit(app.exec())
