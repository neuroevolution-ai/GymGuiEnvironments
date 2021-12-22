import importlib.resources
from typing import List

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QGridLayout

from gym_gui_environments.pyside_gui_environments.src.utils.utils import load_ui


UI_FILES_BASE_PATH = importlib.resources.files("gym_gui_environments.pyside_gui_environments.src.utils")


class MissingContentDialog(QDialog):

    def __init__(self, warning_text: str, content: List[str], **kwargs):
        super().__init__(**kwargs)

        self.setWindowFlag(Qt.FramelessWindowHint, True)

        self.dialog = load_ui(UI_FILES_BASE_PATH.joinpath("missing_content_dialog.ui").__str__())
        self.layout = QGridLayout()
        self.layout.addWidget(self.dialog, 1, 1)
        self.setLayout(self.layout)
        self.setModal(True)

        self.dialog.text_label.setText(warning_text)

        self.dialog.content_combobox.clear()
        self.dialog.content_combobox.addItems(content)

        self.dialog.close_button.clicked.connect(self.close)

        self.currently_shown_widgets = [
            self.dialog.content_combobox,
            self.dialog.close_button
        ]


class WarningDialog(QDialog):

    def __init__(self, warning_text: str, **kwargs):
        super().__init__(**kwargs)

        self.setWindowFlag(Qt.FramelessWindowHint, True)

        self.dialog = load_ui(UI_FILES_BASE_PATH.joinpath("warning_dialog.ui").__str__())
        self.layout = QGridLayout()
        self.layout.addWidget(self.dialog, 1, 1)
        self.setLayout(self.layout)
        self.setModal(True)

        self.dialog.text_label.setText(warning_text)

        self.dialog.close_button.clicked.connect(self.close)

        self.currently_shown_widgets = [
            self.dialog.close_button
        ]


class ConfirmationDialog(QDialog):

    def __init__(self, confirmation_text: str, **kwargs):
        super().__init__(**kwargs)

        self.setWindowFlag(Qt.FramelessWindowHint, True)

        self.dialog = load_ui(UI_FILES_BASE_PATH.joinpath("confirmation_dialog.ui").__str__())
        self.layout = QGridLayout()
        self.layout.addWidget(self.dialog, 1, 1)
        self.setLayout(self.layout)
        self.setModal(True)

        self.dialog.text_label.setText(confirmation_text)

        self.dialog.accept_button.clicked.connect(self.close)
        self.dialog.decline_button.clicked.connect(self.close)

        self.currently_shown_widgets = [
            self.dialog.accept_button,
            self.dialog.decline_button
        ]
