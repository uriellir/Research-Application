# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ConditionComparison.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(522, 353)
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        Form.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("brainPic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.txtCompare = QtWidgets.QLabel(Form)
        self.txtCompare.setGeometry(QtCore.QRect(160, 20, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.txtCompare.setFont(font)
        self.txtCompare.setObjectName("txtCompare")
        self.BrainPic_3 = QtWidgets.QLabel(Form)
        self.BrainPic_3.setGeometry(QtCore.QRect(430, 10, 81, 81))
        self.BrainPic_3.setText("")
        self.BrainPic_3.setPixmap(QtGui.QPixmap("logo2.png"))
        self.BrainPic_3.setObjectName("BrainPic_3")
        self.LblSelect = QtWidgets.QLabel(Form)
        self.LblSelect.setGeometry(QtCore.QRect(60, 60, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.LblSelect.setFont(font)
        self.LblSelect.setObjectName("LblSelect")
        self.labelCond = QtWidgets.QLabel(Form)
        self.labelCond.setGeometry(QtCore.QRect(60, 150, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.labelCond.setFont(font)
        self.labelCond.setObjectName("labelCond")
        self.CBoxPatient = QtWidgets.QComboBox(Form)
        self.CBoxPatient.setGeometry(QtCore.QRect(170, 60, 151, 22))
        self.CBoxPatient.setObjectName("CBoxPatient")
        self.labelRes = QtWidgets.QLabel(Form)
        self.labelRes.setGeometry(QtCore.QRect(270, 150, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.labelRes.setFont(font)
        self.labelRes.setObjectName("labelRes")
        self.labelRES = QtWidgets.QLabel(Form)
        self.labelRES.setGeometry(QtCore.QRect(270, 180, 291, 81))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.labelRES.setFont(font)
        self.labelRES.setStyleSheet("\n"
"color: rgb(255, 0, 0);\n"
"")
        self.labelRES.setObjectName("labelRES")
        self.labelTitle = QtWidgets.QLabel(Form)
        self.labelTitle.setGeometry(QtCore.QRect(80, 180, 121, 81))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.labelTitle.setFont(font)
        self.labelTitle.setObjectName("labelTitle")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(50, 130, 401, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.BtnConExp = QtWidgets.QPushButton(Form)
        self.BtnConExp.setGeometry(QtCore.QRect(80, 280, 151, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BtnConExp.sizePolicy().hasHeightForWidth())
        self.BtnConExp.setSizePolicy(sizePolicy)
        self.BtnConExp.setSizeIncrement(QtCore.QSize(0, 0))
        self.BtnConExp.setBaseSize(QtCore.QSize(10, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.BtnConExp.setFont(font)
        self.BtnConExp.setStyleSheet("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 50px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.55, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.50, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.BtnConExp.setAutoDefault(True)
        self.BtnConExp.setDefault(True)
        self.BtnConExp.setObjectName("BtnConExp")
        self.BtnBack = QtWidgets.QPushButton(Form)
        self.BtnBack.setGeometry(QtCore.QRect(410, 290, 61, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BtnBack.sizePolicy().hasHeightForWidth())
        self.BtnBack.setSizePolicy(sizePolicy)
        self.BtnBack.setSizeIncrement(QtCore.QSize(0, 0))
        self.BtnBack.setBaseSize(QtCore.QSize(10, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.BtnBack.setFont(font)
        self.BtnBack.setStyleSheet("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 50px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.55, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.50, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.BtnBack.setAutoDefault(True)
        self.BtnBack.setDefault(True)
        self.BtnBack.setObjectName("BtnBack")
        self.labelGrp = QtWidgets.QLabel(Form)
        self.labelGrp.setGeometry(QtCore.QRect(60, 90, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.labelGrp.setFont(font)
        self.labelGrp.setObjectName("labelGrp")
        self.labelRes_2 = QtWidgets.QLabel(Form)
        self.labelRes_2.setGeometry(QtCore.QRect(60, 110, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.labelRes_2.setFont(font)
        self.labelRes_2.setObjectName("labelRes_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Condition Comparison"))
        self.txtCompare.setText(_translate("Form", "Compare between Condition"))
        self.LblSelect.setText(_translate("Form", "Select a patient:"))
        self.labelCond.setText(_translate("Form", "Conditions:"))
        self.labelRes.setText(_translate("Form", "Results:"))
        self.labelRES.setText(_translate("Form", "of   1.000\n"
"\n"
"of   1.000\n"
"\n"
"of   1.000"))
        self.labelTitle.setText(_translate("Form", ">> Alone:\n"
"\n"
">> Spontaneous:\n"
"\n"
">> Synchronized:"))
        self.BtnConExp.setText(_translate("Form", "Conditions Explaining"))
        self.BtnBack.setText(_translate("Form", "Back"))
        self.labelGrp.setText(_translate("Form", "Group"))
        self.labelRes_2.setText(_translate("Form", "Research"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
