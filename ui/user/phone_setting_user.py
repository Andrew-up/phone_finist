import sys

from PySide6.QtCore import Slot
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import  QApplication, QWidget

from ui.py.phone_setting import Ui_Form
from utils.setting_GXP1620 import PhoneGXP1620SettingThread
from utils.validator import check_url, check_sip, check_password

TEXT_VALID = "color: rgb(0, 128, 43);"
TEXT_NOT_VALID = "color: rgb(255, 0, 0);"




class PhoneSettingWindow(QWidget):
    def __init__(self, parent=None):
        super(PhoneSettingWindow, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.process_setting = False
        self.thread_GXP1620 = PhoneGXP1620SettingThread()
        self.thread_GXP1620.button_enable.connect(self.button_enabled)
        self.thread_GXP1620.status_operation.connect(self.send_message_to_logging_window)
        self.thread_GXP1620.status_operation_error.connect(self.send_message_error)
        self.thread_GXP1620.setting_end.connect(self.send_message_end_setting)

        self.ui.pushButton.clicked.connect(self.startSettingGXP1620)
        self.set_not_visible_checkbox()
        self.setWindowIcon(QIcon('../../logo.ico'))

        self.ui.ip_phone_line_edit.textChanged.connect(self.ip_valid)
        self.ui.sip_user_line_edit.textChanged.connect(self.sip_valid)
        self.ui.sip_password_line_edit.textChanged.connect(self.password_valid)
        self.form_validator()

    def form_validator(self):
        form_valid = True
        if not check_url(self.ui.ip_phone_line_edit.text()):
            form_valid = False
        if not check_sip(self.ui.sip_user_line_edit.text()):
            form_valid = False
        if not check_password(self.ui.sip_password_line_edit.text()):
            form_valid = False
        if self.process_setting:
            form_valid = False
        self.ui.pushButton.setEnabled(form_valid)

    def sip_valid(self):
        if check_sip(self.ui.sip_user_line_edit.text()):
            self.ui.sip_user_line_edit.setStyleSheet(TEXT_VALID)
        else:
            self.ui.sip_user_line_edit.setStyleSheet(TEXT_NOT_VALID)
        self.form_validator()

    def password_valid(self):
        if check_password(self.ui.sip_password_line_edit.text()):
            self.ui.sip_password_line_edit.setStyleSheet(TEXT_VALID)
        else:
            self.ui.sip_password_line_edit.setStyleSheet(TEXT_NOT_VALID)
        self.form_validator()

    def ip_valid(self):
        if check_url(self.ui.ip_phone_line_edit.text()):
            self.ui.ip_phone_line_edit.setStyleSheet(TEXT_VALID)
        else:
            self.ui.ip_phone_line_edit.setStyleSheet(TEXT_NOT_VALID)
        self.form_validator()

    def set_not_visible_checkbox(self):
        self.ui.ip_phone_line_edit.setText('')
        self.ui.sip_user_line_edit.setText('')
        self.ui.sip_password_line_edit.setText('')
        self.ui.web_pass_line_edit.setText('admin')
        self.ui.loading_label.setVisible(False)
        self.ui.reset_phone_check_box.setChecked(False)
        self.ui.checkBox_2.setText('Быстрая настройка')
        self.ui.checkBox_2.setChecked(True)
        self.ui.checkBox_2.setEnabled(True)
        # self.ui.checkBox_2.setVisible(False)
        self.ui.checkBox_3.setVisible(False)
        self.ui.checkBox_4.setVisible(False)
        self.ui.checkBox_5.setVisible(False)
        self.ui.checkBox_6.setVisible(False)
        self.ui.checkBox_7.setVisible(False)
        self.ui.checkBox_8.setVisible(False)
        self.ui.checkBox_9.setVisible(False)
        self.ui.checkBox_10.setVisible(False)

        self.ui.radioButton.setText('GXP1610/ GXP1620/ GXP1625/ GXP1628/ GXP2140/')
        self.ui.radioButton.setChecked(True)
        self.ui.radioButton.setEnabled(True)

        self.ui.radioButton_2.setVisible(False)
        self.ui.radioButton_3.setVisible(False)

    def startSettingGXP1620(self):
        link = self.ui.ip_phone_line_edit.text()
        if not link.startswith('http'):
            link = 'http://' + link + '/'
        if self.ui.reset_phone_check_box.isChecked():
            self.thread_GXP1620.set_reset_phone(True)
        else:
            self.thread_GXP1620.set_reset_phone(False)

        if self.ui.checkBox_2.isChecked():
            self.thread_GXP1620.set_fast_setting(True)
        else:
            self.thread_GXP1620.set_fast_setting(False)

        self.thread_GXP1620.set_url_phone(link)
        self.thread_GXP1620.set_login_web(self.ui.web_login_line_edit.text())
        self.thread_GXP1620.set_password_web(self.ui.web_pass_line_edit.text())
        self.thread_GXP1620.set_sip_user_id(self.ui.sip_user_line_edit.text())
        self.thread_GXP1620.set_sip_user_password(self.ui.sip_password_line_edit.text())
        self.thread_GXP1620.start()

    @Slot(bool)
    def button_enabled(self, btn_enable):
        self.ui.pushButton.setEnabled(btn_enable)
        self.process_setting = not btn_enable

    @Slot(str)
    def send_message_to_logging_window(self, message):
        self.ui.logging_progress_text_edit.append(f'<span style="color:#000000";>{message}</span>')

    @Slot(str)
    def send_message_end_setting(self, message):
        self.ui.logging_progress_text_edit.append(f'<span style="color:#0f8a5b";>{message}</span>')

    @Slot(str)
    def send_message_error(self, message):
        self.ui.logging_progress_text_edit.append(f'<span style="color:#ad2a21";>{message}</span>')


def start_ui():
    app = QApplication(sys.argv)
    window = PhoneSettingWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    start_ui()
