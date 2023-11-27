import sys

from PySide6.QtWidgets import QMainWindow, QApplication

from ui.py.mainwindow import Ui_MainWindow
from ui.user.phone_setting_user import PhoneSettingWindow
from ui.user.search_phone_user import SearchPhoneWidget

VERSION = '1.2.0'
DEV_fullname = 'Andrey Ageev'
email_DEV = ' a.ageev@finist.ru'


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.stacked_widget = self.ui.stackedWidget
        self.phone_setting_window = None
        self.search_phone = None
        self.ui.pushButton_2.clicked.connect(self.on_button_phone_setting)
        self.ui.pushButton_7.clicked.connect(self.on_button_search_phones)
        self.on_button_phone_setting()

        self.ui.label_6.setText(f'version {VERSION} ||| dev: {DEV_fullname}, support: {email_DEV}')

    def on_button_phone_setting(self):
        if self.phone_setting_window is None:
            self.phone_setting_window = PhoneSettingWindow()
            self.stacked_widget.addWidget(self.phone_setting_window)
            self.stacked_widget.setCurrentWidget(self.phone_setting_window)
        else:
            self.stacked_widget.setCurrentWidget(self.phone_setting_window)

    def on_button_search_phones(self):
        if self.search_phone is None:
            self.search_phone = SearchPhoneWidget()
            self.stacked_widget.addWidget(self.search_phone)
            self.stacked_widget.setCurrentWidget(self.search_phone)
        else:
            self.stacked_widget.setCurrentWidget(self.search_phone)


def start_ui():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    start_ui()
