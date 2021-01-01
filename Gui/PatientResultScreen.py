# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PatientResultScreen.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from Patient import Patient


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(836, 569)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("brainPic.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        Form.setWindowIcon(icon)
        self.txtPatient = QtWidgets.QLabel(Form)
        self.txtPatient.setGeometry(QtCore.QRect(70, 30, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.txtPatient.setFont(font)
        self.txtPatient.setObjectName("txtPatient")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(70, 50, 241, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.BrainPic = QtWidgets.QLabel(Form)
        self.BrainPic.setGeometry(QtCore.QRect(10, 20, 41, 41))
        self.BrainPic.setText("")
        self.BrainPic.setPixmap(QtGui.QPixmap("user3.png"))
        self.BrainPic.setObjectName("BrainPic")
        self.txtGlobal = QtWidgets.QLabel(Form)
        self.txtGlobal.setGeometry(QtCore.QRect(60, 110, 211, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.txtGlobal.setFont(font)
        self.txtGlobal.setObjectName("txtGlobal")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(40, 140, 271, 61))
        self.listWidget.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.listWidget.setLineWidth(3)
        self.listWidget.setMidLineWidth(3)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.txtLocal = QtWidgets.QLabel(Form)
        self.txtLocal.setGeometry(QtCore.QRect(60, 300, 211, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.txtLocal.setFont(font)
        self.txtLocal.setObjectName("txtLocal")
        self.txtEloctrode = QtWidgets.QLabel(Form)
        self.txtEloctrode.setGeometry(QtCore.QRect(70, 330, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.txtEloctrode.setFont(font)
        self.txtEloctrode.setObjectName("txtEloctrode")
        self.listWidget_2 = QtWidgets.QListWidget(Form)
        self.listWidget_2.setGeometry(QtCore.QRect(40, 370, 271, 61))
        self.listWidget_2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.listWidget_2.setLineWidth(3)
        self.listWidget_2.setMidLineWidth(3)
        self.listWidget_2.setObjectName("listWidget_2")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        self.buttonBox = QtWidgets.QDialogButtonBox(Form)
        self.buttonBox.setGeometry(QtCore.QRect(50, 500, 41, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.buttonBox.setFont(font)
        self.buttonBox.setStyleSheet("QPushButton {\n"
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
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.BtnGlobal = QtWidgets.QPushButton(Form)
        self.BtnGlobal.setGeometry(QtCore.QRect(80, 210, 191, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BtnGlobal.sizePolicy().hasHeightForWidth())
        self.BtnGlobal.setSizePolicy(sizePolicy)
        self.BtnGlobal.setSizeIncrement(QtCore.QSize(0, 0))
        self.BtnGlobal.setBaseSize(QtCore.QSize(10, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.BtnGlobal.setFont(font)
        self.BtnGlobal.setStyleSheet("QPushButton {\n"
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
        self.BtnGlobal.setAutoDefault(True)
        self.BtnGlobal.setDefault(True)
        self.BtnGlobal.setObjectName("BtnGlobal")
        self.txtBrain = QtWidgets.QLabel(Form)
        self.txtBrain.setGeometry(QtCore.QRect(480, 70, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.txtBrain.setFont(font)
        self.txtBrain.setObjectName("txtBrain")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(260, 160, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label.setFont(font)
        self.label.setStyleSheet("\n"
"color: rgb(0, 0, 0);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(260, 170, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);\n"
"color: rgb(0, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(260, 370, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 0, 0);\n"
"color: rgb(0, 0, 0);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(260, 380, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(0, 0, 0);\n"
"color: rgb(0, 0, 0);")
        self.label_4.setObjectName("label_4")
        self.BrainPic_3 = QtWidgets.QLabel(Form)
        self.BrainPic_3.setGeometry(QtCore.QRect(740, 10, 81, 81))
        self.BrainPic_3.setText("")
        self.BrainPic_3.setPixmap(QtGui.QPixmap("logo2.png"))
        self.BrainPic_3.setObjectName("BrainPic_3")
        self.TxtMod = QtWidgets.QLabel(Form)
        self.TxtMod.setGeometry(QtCore.QRect(210, 170, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.TxtMod.setFont(font)
        self.TxtMod.setStyleSheet("color:rgb(255, 0, 0)\n"
"")
        self.TxtMod.setObjectName("TxtMod")
        self.TxtDes = QtWidgets.QLabel(Form)
        self.TxtDes.setGeometry(QtCore.QRect(210, 160, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.TxtDes.setFont(font)
        self.TxtDes.setStyleSheet("color:rgb(255, 0, 0)\n"
"")
        self.TxtDes.setObjectName("TxtDes")
        self.TxtAvg = QtWidgets.QLabel(Form)
        self.TxtAvg.setGeometry(QtCore.QRect(210, 140, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.TxtAvg.setFont(font)
        self.TxtAvg.setStyleSheet("color:rgb(255, 0, 0)\n"
"")
        self.TxtAvg.setObjectName("TxtAvg")
        self.TxtEff = QtWidgets.QLabel(Form)
        self.TxtEff.setGeometry(QtCore.QRect(210, 380, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.TxtEff.setFont(font)
        self.TxtEff.setStyleSheet("color:rgb(255, 0, 0)\n"
"")
        self.TxtEff.setObjectName("TxtEff")
        self.TxtDeg = QtWidgets.QLabel(Form)
        self.TxtDeg.setGeometry(QtCore.QRect(210, 370, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.TxtDeg.setFont(font)
        self.TxtDeg.setStyleSheet("color:rgb(255, 0, 0)\n"
"")
        self.TxtDeg.setObjectName("TxtDeg")
        self.BtnLocal = QtWidgets.QPushButton(Form)
        self.BtnLocal.setGeometry(QtCore.QRect(80, 440, 191, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BtnLocal.sizePolicy().hasHeightForWidth())
        self.BtnLocal.setSizePolicy(sizePolicy)
        self.BtnLocal.setSizeIncrement(QtCore.QSize(0, 0))
        self.BtnLocal.setBaseSize(QtCore.QSize(10, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.BtnLocal.setFont(font)
        self.BtnLocal.setStyleSheet("QPushButton {\n"
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
        self.BtnLocal.setAutoDefault(True)
        self.BtnLocal.setDefault(True)
        self.BtnLocal.setObjectName("BtnLocal")
        self.cBoxElectrode = QtWidgets.QComboBox(Form)
        self.cBoxElectrode.setGeometry(QtCore.QRect(180, 330, 69, 22))
        self.cBoxElectrode.setObjectName("cBoxElectrode")
        self.cBoxPname = QtWidgets.QComboBox(Form)
        self.cBoxPname.setGeometry(QtCore.QRect(130, 30, 151, 22))
        self.cBoxPname.setObjectName("cBoxPname")
        self.BrainGraph = QtWidgets.QLabel(Form)
        self.BrainGraph.setGeometry(QtCore.QRect(380, 120, 411, 361))
        self.BrainGraph.setText("")
        self.BrainGraph.setObjectName("BrainGraph")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    # ---------------------------------Added Code -------------------------------------------- #
        self.cBoxPname.addItem('')
        patient = Patient('id','full_name','group','research','file_path')
        comoboBox_patients = list(dict.fromkeys(patient.get_data_from_JSON('full_name')))
        self.cBoxPname.addItems(comoboBox_patients)

    # ------------------------------- Call to Functions -------------------------------------- #
    #     self.BtnGlobal.clicked.connect(self.show_results)
        self.cBoxPname.currentTextChanged.connect(self.show_results)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Patient Result"))
        self.txtPatient.setText(_translate("Form", "Patient:"))
        self.txtGlobal.setText(_translate("Form", "Global Parameters Of The Graph:"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("Form", "Avarage Shortest Path Length:"))
        item = self.listWidget.item(1)
        item.setText(_translate("Form", "Density:"))
        item = self.listWidget.item(2)
        item.setText(_translate("Form", "Modularity:"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.txtLocal.setText(_translate("Form", "Local Parameters Of The Graph:"))
        self.txtEloctrode.setText(_translate("Form", "Choose Electrode:"))
        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        item = self.listWidget_2.item(0)
        item.setText(_translate("Form", "Degree:"))
        item = self.listWidget_2.item(1)
        item.setText(_translate("Form", "Local Efficiency:"))
        self.listWidget_2.setSortingEnabled(__sortingEnabled)
        self.BtnGlobal.setText(_translate("Form", "Global Parameters Explaining"))
        self.txtBrain.setText(_translate("Form", "Brain Connectivity Graph"))
        self.label.setText(_translate("Form", "of   1.000"))
        self.label_2.setText(_translate("Form", "of   1.000"))
        self.label_3.setText(_translate("Form", "of    64"))
        self.label_4.setText(_translate("Form", "of   1.000"))
        self.TxtMod.setText(_translate("Form", "Txt"))
        self.TxtDes.setText(_translate("Form", "Txt"))
        self.TxtAvg.setText(_translate("Form", "Txt"))
        self.TxtEff.setText(_translate("Form", "Txt"))
        self.TxtDeg.setText(_translate("Form", "Txt"))
        self.BtnLocal.setText(_translate("Form", "Local Parameters Explaining"))

    # -------------------------------------- Functions ----------------------------------------- #

    def show_results(self,value):
        from undirectedGraph import Graph
        g = Graph()
        g.create_nodes(g.create_edges(value))
        self.TxtDes.setText(str(g.density))
        self.TxtAvg.setText(str(g.shortest_paths[7][6]))
        self.TxtMod.setText(str(g.modularity_matrix[0,0]))

        # ---- For the COMOBO BOX -------- #
        self.TxtDeg.setText(str(g.degree[10]))
        self.TxtEff.setText(str(g.efficiency[10]))

        self.BrainGraph.setPixmap(QtGui.QPixmap(value+".png"))

if __name__ == "__main__":
    import sys
    # ---------------------------------------------
    # ---------------------------------------------
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())



