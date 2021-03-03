# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ConditionExplaining.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(642, 230)
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        Form.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("brainPic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtCompare = QtWidgets.QLabel(Form)
        self.txtCompare.setGeometry(QtCore.QRect(250, 20, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.txtCompare.setFont(font)
        self.txtCompare.setObjectName("txtCompare")
        self.LblSelect = QtWidgets.QLabel(Form)
        self.LblSelect.setGeometry(QtCore.QRect(40, 70, 581, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.LblSelect.setFont(font)
        self.LblSelect.setObjectName("LblSelect")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(110, 40, 401, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.LblSelect_2 = QtWidgets.QLabel(Form)
        self.LblSelect_2.setGeometry(QtCore.QRect(40, 150, 561, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.LblSelect_2.setFont(font)
        self.LblSelect_2.setObjectName("LblSelect_2")
        self.LblSelect_3 = QtWidgets.QLabel(Form)
        self.LblSelect_3.setGeometry(QtCore.QRect(40, 110, 591, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.LblSelect_3.setFont(font)
        self.LblSelect_3.setObjectName("LblSelect_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Condition Explaning"))
        self.txtCompare.setText(_translate("Form", "Condition Explaining"))
        self.LblSelect.setText(_translate("Form", "1. Alone –  the subject performs free movements when his back is directed to the researcher."))
        self.LblSelect_2.setText(_translate("Form", "3. Synchronized – the subject is asked to follow the research assistant movements."))
        self.LblSelect_3.setText(_translate("Form", "2. Spontaneous – the subject makes free movements when he is facing the research assistant."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
