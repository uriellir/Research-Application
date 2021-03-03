# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LocalExplaining.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(664, 283)
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        Form.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("brainPic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtLocal = QtWidgets.QLabel(Form)
        self.txtLocal.setGeometry(QtCore.QRect(220, 20, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.txtLocal.setFont(font)
        self.txtLocal.setObjectName("txtLocal")
        self.LblDegree = QtWidgets.QLabel(Form)
        self.LblDegree.setGeometry(QtCore.QRect(30, 110, 581, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.LblDegree.setFont(font)
        self.LblDegree.setObjectName("LblDegree")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(110, 40, 401, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.txtLocal_2 = QtWidgets.QLabel(Form)
        self.txtLocal_2.setGeometry(QtCore.QRect(30, 60, 561, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.txtLocal_2.setFont(font)
        self.txtLocal_2.setObjectName("txtLocal_2")
        self.LblEfficiency = QtWidgets.QLabel(Form)
        self.LblEfficiency.setGeometry(QtCore.QRect(30, 160, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.LblEfficiency.setFont(font)
        self.LblEfficiency.setObjectName("LblEfficiency")
        self.LblEff = QtWidgets.QLabel(Form)
        self.LblEff.setGeometry(QtCore.QRect(160, 170, 501, 71))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.LblEff.setFont(font)
        self.LblEff.setObjectName("LblEff")
        self.LblDegExp = QtWidgets.QLabel(Form)
        self.LblDegExp.setGeometry(QtCore.QRect(110, 120, 401, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.LblDegExp.setFont(font)
        self.LblDegExp.setObjectName("LblDegExp")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Local Parameters Explaining"))
        self.txtLocal.setText(_translate("Form", "Local Parameters Explaining"))
        self.LblDegree.setText(_translate("Form", "1. Degree -"))
        self.txtLocal_2.setText(_translate("Form", "•  Local Parameters - one value for each node/edge. \n"
"\n"
" Local Parameters of graph:"))
        self.LblEfficiency.setText(_translate("Form", "2. Local efficiency – "))
        self.LblEff.setText(_translate("Form", "The local efficiency quantifies a network\'s resistance to failure on a small scale. \n"
"\n"
"That is the local efficiency of a node i characterizes how well information is exchanged\n"
"\n"
"by its neighbors when it is removed."))
        self.LblDegExp.setText(_translate("Form", "The vertex degree for a vertex v is the number of edges incident to v."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
