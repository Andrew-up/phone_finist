# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'phone_setting.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QRadioButton,
    QSizePolicy, QTextEdit, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(421, 475)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.radioButton_3 = QRadioButton(Form)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setChecked(True)

        self.horizontalLayout_4.addWidget(self.radioButton_3)

        self.radioButton_2 = QRadioButton(Form)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setEnabled(False)

        self.horizontalLayout_4.addWidget(self.radioButton_2)

        self.radioButton = QRadioButton(Form)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setEnabled(False)

        self.horizontalLayout_4.addWidget(self.radioButton)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.web_login_line_edit = QLineEdit(Form)
        self.web_login_line_edit.setObjectName(u"web_login_line_edit")

        self.horizontalLayout_5.addWidget(self.web_login_line_edit)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.label_4)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, -1)
        self.web_pass_line_edit = QLineEdit(Form)
        self.web_pass_line_edit.setObjectName(u"web_pass_line_edit")

        self.horizontalLayout_6.addWidget(self.web_pass_line_edit)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)

        self.horizontalLayout_6.addWidget(self.label_5)


        self.verticalLayout_5.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.ip_phone_line_edit = QLineEdit(Form)
        self.ip_phone_line_edit.setObjectName(u"ip_phone_line_edit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ip_phone_line_edit.sizePolicy().hasHeightForWidth())
        self.ip_phone_line_edit.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.ip_phone_line_edit)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.label_3)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.sip_user_line_edit = QLineEdit(Form)
        self.sip_user_line_edit.setObjectName(u"sip_user_line_edit")
        sizePolicy1.setHeightForWidth(self.sip_user_line_edit.sizePolicy().hasHeightForWidth())
        self.sip_user_line_edit.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.sip_user_line_edit)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.label)


        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.sip_password_line_edit = QLineEdit(Form)
        self.sip_password_line_edit.setObjectName(u"sip_password_line_edit")

        self.horizontalLayout_2.addWidget(self.sip_password_line_edit)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.label_2)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, 0, -1, -1)
        self.checkBox_9 = QCheckBox(Form)
        self.checkBox_9.setObjectName(u"checkBox_9")
        self.checkBox_9.setEnabled(False)

        self.gridLayout.addWidget(self.checkBox_9, 3, 0, 1, 1)

        self.checkBox_5 = QCheckBox(Form)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setEnabled(False)

        self.gridLayout.addWidget(self.checkBox_5, 1, 1, 1, 1)

        self.checkBox_2 = QCheckBox(Form)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setEnabled(False)

        self.gridLayout.addWidget(self.checkBox_2, 1, 0, 1, 1)

        self.checkBox_10 = QCheckBox(Form)
        self.checkBox_10.setObjectName(u"checkBox_10")
        self.checkBox_10.setEnabled(False)

        self.gridLayout.addWidget(self.checkBox_10, 4, 0, 1, 1)

        self.checkBox_6 = QCheckBox(Form)
        self.checkBox_6.setObjectName(u"checkBox_6")
        self.checkBox_6.setEnabled(False)

        self.gridLayout.addWidget(self.checkBox_6, 3, 1, 1, 1)

        self.reset_phone_check_box = QCheckBox(Form)
        self.reset_phone_check_box.setObjectName(u"reset_phone_check_box")
        self.reset_phone_check_box.setChecked(True)

        self.gridLayout.addWidget(self.reset_phone_check_box, 0, 0, 1, 1)

        self.checkBox_8 = QCheckBox(Form)
        self.checkBox_8.setObjectName(u"checkBox_8")
        self.checkBox_8.setEnabled(False)

        self.gridLayout.addWidget(self.checkBox_8, 4, 1, 1, 1)

        self.checkBox_3 = QCheckBox(Form)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setEnabled(False)

        self.gridLayout.addWidget(self.checkBox_3, 2, 0, 1, 1)

        self.checkBox_7 = QCheckBox(Form)
        self.checkBox_7.setObjectName(u"checkBox_7")
        self.checkBox_7.setEnabled(False)

        self.gridLayout.addWidget(self.checkBox_7, 0, 1, 1, 1)

        self.checkBox_4 = QCheckBox(Form)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setEnabled(False)

        self.gridLayout.addWidget(self.checkBox_4, 2, 1, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_5.addWidget(self.pushButton)

        self.loading_label = QLabel(Form)
        self.loading_label.setObjectName(u"loading_label")

        self.verticalLayout_5.addWidget(self.loading_label)

        self.logging_progress_text_edit = QTextEdit(Form)
        self.logging_progress_text_edit.setObjectName(u"logging_progress_text_edit")
        self.logging_progress_text_edit.setEnabled(True)
        self.logging_progress_text_edit.setReadOnly(True)

        self.verticalLayout_5.addWidget(self.logging_progress_text_edit)


        self.verticalLayout.addLayout(self.verticalLayout_5)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.radioButton_3.setText(QCoreApplication.translate("Form", u"GXP1620", None))
        self.radioButton_2.setText(QCoreApplication.translate("Form", u"GXP280", None))
        self.radioButton.setText(QCoreApplication.translate("Form", u"GXP2140", None))
        self.web_login_line_edit.setText(QCoreApplication.translate("Form", u"admin", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"WEB LOGIN", None))
        self.web_pass_line_edit.setText(QCoreApplication.translate("Form", u"admin", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"WEB PASSWORD", None))
        self.ip_phone_line_edit.setText(QCoreApplication.translate("Form", u"192.168.36.141", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"IP PHONE", None))
        self.sip_user_line_edit.setText(QCoreApplication.translate("Form", u"256", None))
        self.label.setText(QCoreApplication.translate("Form", u"SIP USER", None))
        self.sip_password_line_edit.setText(QCoreApplication.translate("Form", u"CXL5qjsFcWe6", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"SIP PASSWORD", None))
        self.checkBox_9.setText(QCoreApplication.translate("Form", u"CheckBox", None))
        self.checkBox_5.setText(QCoreApplication.translate("Form", u"CheckBox", None))
        self.checkBox_2.setText(QCoreApplication.translate("Form", u"CheckBox", None))
        self.checkBox_10.setText(QCoreApplication.translate("Form", u"CheckBox", None))
        self.checkBox_6.setText(QCoreApplication.translate("Form", u"CheckBox", None))
        self.reset_phone_check_box.setText(QCoreApplication.translate("Form", u"\u0421\u0431\u0440\u043e\u0441 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430", None))
        self.checkBox_8.setText(QCoreApplication.translate("Form", u"CheckBox", None))
        self.checkBox_3.setText(QCoreApplication.translate("Form", u"CheckBox", None))
        self.checkBox_7.setText(QCoreApplication.translate("Form", u"CheckBox", None))
        self.checkBox_4.setText(QCoreApplication.translate("Form", u"CheckBox", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.loading_label.setText(QCoreApplication.translate("Form", u"loading...", None))
    # retranslateUi

