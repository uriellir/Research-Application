# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GlobalExplaining.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(664, 275)
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        Form.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("brainPic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtGlobal = QtWidgets.QLabel(Form)
        self.txtGlobal.setGeometry(QtCore.QRect(220, 20, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.txtGlobal.setFont(font)
        self.txtGlobal.setObjectName("txtGlobal")
        self.Lbllenght = QtWidgets.QLabel(Form)
        self.Lbllenght.setGeometry(QtCore.QRect(30, 110, 581, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Lbllenght.setFont(font)
        self.Lbllenght.setObjectName("Lbllenght")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(110, 40, 401, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.txtGlob = QtWidgets.QLabel(Form)
        self.txtGlob.setGeometry(QtCore.QRect(30, 60, 561, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.txtGlob.setFont(font)
        self.txtGlob.setObjectName("txtGlob")
        self.LblDens = QtWidgets.QLabel(Form)
        self.LblDens.setGeometry(QtCore.QRect(30, 180, 591, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.LblDens.setFont(font)
        self.LblDens.setObjectName("LblDens")
        self.LblDensExp = QtWidgets.QLabel(Form)
        self.LblDensExp.setGeometry(QtCore.QRect(130, 190, 501, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.LblDensExp.setFont(font)
        self.LblDensExp.setObjectName("LblDensExp")
        self.LblltngthExp = QtWidgets.QLabel(Form)
        self.LblltngthExp.setGeometry(QtCore.QRect(250, 120, 401, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.LblltngthExp.setFont(font)
        self.LblltngthExp.setObjectName("LblltngthExp")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Global Parameters Explaining"))
        self.txtGlobal.setText(_translate("Form", "Global Parameters Explaining"))
        self.Lbllenght.setText(_translate("Form", "1. Avarage Shortest path length -"))
        self.txtGlob.setText(_translate("Form", "•  Global Parameters - one value for the whole network. \n"
"\n"
" Global Parameters of graph:"))
        self.LblDens.setText(_translate("Form", "2. Density – "))
        self.LblDensExp.setText(_translate("Form", "The density of a graph G = (V,E) measures how many edges are in set E compared to the\n"
"\n"
" maximum possible number of edges between vertices in set V."))
        self.LblltngthExp.setText(_translate("Form", " Using the reachability matrix to represent shortest path for each pair. \n"
"\n"
"That describes whether paths (reachable) connect pairs of electrodes."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
