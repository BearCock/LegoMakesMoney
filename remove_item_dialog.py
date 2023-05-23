from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtGui import QFont


class RemoveDialog(QMessageBox):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("LegoMakesMoney - odstranit položku?")
        self.setText("Opravdu si přejete odstranit označenou položku?")
        self.setIcon(QMessageBox.Icon.Warning)

        font_size = QFont()
        font_size.setPointSize(10)
        self.setFont(font_size)

        self.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        self.setDefaultButton(QMessageBox.StandardButton.No)

        yes_button = self.button(QMessageBox.StandardButton.Yes)
        no_button = self.button(QMessageBox.StandardButton.No)
        yes_button.setText("Ano")
        no_button.setText("Ne")

        style_sheet_red = """
            }
        QMessageBox QPushButton {
            background-color: #e31717;
            }
                     """

        style_sheet_green = """
                    }
                QMessageBox QPushButton {
                    background-color: #25e317;
                    }
                             """

        style_sheet = """
        QMessageBox {
            background-color: #343640;
            color: #cdcdd3;
        }
        QMessageBox QLabel {
            color: #cdcdd3;
        }
        """

        self.setStyleSheet(style_sheet)
        yes_button.setStyleSheet(style_sheet_red)
        no_button.setStyleSheet(style_sheet_green)