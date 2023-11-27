# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'search_phones.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QTextEdit, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(444, 505)
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.checkbox_Novosibirsk = QCheckBox(self.groupBox)
        self.checkbox_Novosibirsk.setObjectName(u"checkbox_Novosibirsk")

        self.gridLayout.addWidget(self.checkbox_Novosibirsk, 0, 1, 1, 1)

        self.checkbox_Krasnodar = QCheckBox(self.groupBox)
        self.checkbox_Krasnodar.setObjectName(u"checkbox_Krasnodar")

        self.gridLayout.addWidget(self.checkbox_Krasnodar, 4, 0, 1, 1)

        self.checkbox_VelikiyNovgorod = QCheckBox(self.groupBox)
        self.checkbox_VelikiyNovgorod.setObjectName(u"checkbox_VelikiyNovgorod")
        self.checkbox_VelikiyNovgorod.setEnabled(False)

        self.gridLayout.addWidget(self.checkbox_VelikiyNovgorod, 4, 1, 1, 1)

        self.checkbox_voronezh = QCheckBox(self.groupBox)
        self.checkbox_voronezh.setObjectName(u"checkbox_voronezh")

        self.gridLayout.addWidget(self.checkbox_voronezh, 5, 0, 1, 1)

        self.checkbox_Razan = QCheckBox(self.groupBox)
        self.checkbox_Razan.setObjectName(u"checkbox_Razan")

        self.gridLayout.addWidget(self.checkbox_Razan, 1, 1, 1, 1)

        self.checkbox_Kazan = QCheckBox(self.groupBox)
        self.checkbox_Kazan.setObjectName(u"checkbox_Kazan")
        self.checkbox_Kazan.setEnabled(False)

        self.gridLayout.addWidget(self.checkbox_Kazan, 3, 1, 1, 1)

        self.checkbox_moscow = QCheckBox(self.groupBox)
        self.checkbox_moscow.setObjectName(u"checkbox_moscow")

        self.gridLayout.addWidget(self.checkbox_moscow, 0, 0, 1, 1)

        self.checkbox_Stavropol = QCheckBox(self.groupBox)
        self.checkbox_Stavropol.setObjectName(u"checkbox_Stavropol")

        self.gridLayout.addWidget(self.checkbox_Stavropol, 5, 1, 1, 1)

        self.checkbox_NN = QCheckBox(self.groupBox)
        self.checkbox_NN.setObjectName(u"checkbox_NN")

        self.gridLayout.addWidget(self.checkbox_NN, 3, 0, 1, 1)

        self.checkbox_spb = QCheckBox(self.groupBox)
        self.checkbox_spb.setObjectName(u"checkbox_spb")

        self.gridLayout.addWidget(self.checkbox_spb, 1, 0, 1, 1)

        self.checkbox_Tambov = QCheckBox(self.groupBox)
        self.checkbox_Tambov.setObjectName(u"checkbox_Tambov")

        self.gridLayout.addWidget(self.checkbox_Tambov, 6, 0, 1, 1)

        self.checkbox_Ekb = QCheckBox(self.groupBox)
        self.checkbox_Ekb.setObjectName(u"checkbox_Ekb")
        self.checkbox_Ekb.setEnabled(False)

        self.gridLayout.addWidget(self.checkbox_Ekb, 6, 1, 1, 1)

        self.checkbox_all_city = QCheckBox(self.groupBox)
        self.checkbox_all_city.setObjectName(u"checkbox_all_city")

        self.gridLayout.addWidget(self.checkbox_all_city, 6, 2, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_2.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_2.addWidget(self.pushButton_2)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.label_current_city = QLabel(Form)
        self.label_current_city.setObjectName(u"label_current_city")

        self.verticalLayout_4.addWidget(self.label_current_city)


        self.verticalLayout_3.addLayout(self.verticalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)

        self.current_number = QLabel(Form)
        self.current_number.setObjectName(u"current_number")

        self.horizontalLayout.addWidget(self.current_number)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.total_number = QLabel(Form)
        self.total_number.setObjectName(u"total_number")

        self.horizontalLayout.addWidget(self.total_number)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.label_search_count = QLabel(Form)
        self.label_search_count.setObjectName(u"label_search_count")

        self.horizontalLayout_2.addWidget(self.label_search_count)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.textEdit = QTextEdit(Form)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy1)

        self.verticalLayout_3.addWidget(self.textEdit)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"GroupBox", None))
        self.checkbox_Novosibirsk.setText(QCoreApplication.translate("Form", u"\u041d\u043e\u0432\u043e\u0441\u0438\u0431\u0438\u0440\u0441\u043a", None))
        self.checkbox_Krasnodar.setText(QCoreApplication.translate("Form", u"\u041a\u0440\u0430\u0441\u043d\u043e\u0434\u0430\u0440", None))
        self.checkbox_VelikiyNovgorod.setText(QCoreApplication.translate("Form", u"\u0412\u0435\u043b\u0438\u043a\u0438\u0439 \u041d\u043e\u0432\u0433\u043e\u0440\u043e\u0434", None))
        self.checkbox_voronezh.setText(QCoreApplication.translate("Form", u"\u0412\u043e\u0440\u043e\u043d\u0435\u0436", None))
        self.checkbox_Razan.setText(QCoreApplication.translate("Form", u"\u0420\u044f\u0437\u0430\u043d\u044c", None))
        self.checkbox_Kazan.setText(QCoreApplication.translate("Form", u"\u041a\u0430\u0437\u0430\u043d\u044c", None))
        self.checkbox_moscow.setText(QCoreApplication.translate("Form", u"\u041c\u043e\u0441\u043a\u0432\u0430", None))
        self.checkbox_Stavropol.setText(QCoreApplication.translate("Form", u"\u0421\u0442\u0430\u0432\u0440\u043e\u043f\u043e\u043b\u044c", None))
        self.checkbox_NN.setText(QCoreApplication.translate("Form", u"\u041d\u0438\u0436\u043d\u0438\u0439 \u043d\u043e\u0432\u0433\u043e\u0440\u043e\u0434", None))
        self.checkbox_spb.setText(QCoreApplication.translate("Form", u"\u0421\u0430\u043d\u043a\u0442-\u041f\u0435\u0442\u0435\u0440\u0431\u0443\u0440\u0433", None))
        self.checkbox_Tambov.setText(QCoreApplication.translate("Form", u"\u0422\u0430\u043c\u0431\u043e\u0432", None))
        self.checkbox_Ekb.setText(QCoreApplication.translate("Form", u"\u0415\u043a\u0430\u0442\u0435\u0440\u0438\u043d\u0431\u0443\u0440\u0433", None))
        self.checkbox_all_city.setText(QCoreApplication.translate("Form", u"\u0412\u0441\u0435 \u0433\u043e\u0440\u043e\u0434\u0430", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u043f\u0430\u043f\u043a\u0443 \u0434\u043b\u044f \u044d\u043a\u0441\u043f\u043e\u0440\u0442\u0430", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0447\u0430\u0442\u044c \u0441\u043a\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.label_current_city.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u041f\u0440\u043e\u0441\u043a\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u043e:", None))
        self.current_number.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"/", None))
        self.total_number.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0439\u0434\u0435\u043d\u043e \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u043e\u0432:", None))
        self.label_search_count.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi

