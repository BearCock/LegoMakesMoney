from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtGui import QFont


class InfoDialog(QMessageBox):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("LegoMakesMoney")
        self.setText("              Data uložena                            ")
        self.addButton(QMessageBox.StandardButton.Ok)
        self.setIcon(QMessageBox.Icon.Information)

        style_sheet = """
        QMessageBox {
            background-color: #343640;
            color: #cdcdd3;
        }
        QMessageBox QLabel {
            color: #cdcdd3;
        }
        QMessageBox QPushButton {
            background-color: #25e317;
        }
        """

        self.setStyleSheet(style_sheet)

        font_size = QFont()
        font_size.setPointSize(10)
        self.setFont(font_size)