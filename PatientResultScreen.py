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
        self.txtGlobal.setGeometry(QtCore.QRect(60, 120, 211, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.txtGlobal.setFont(font)
        self.txtGlobal.setObjectName("txtGlobal")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(40, 150, 281, 51))
        self.listWidget.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.listWidget.setLineWidth(3)
        self.listWidget.setMidLineWidth(3)
        self.listWidget.setObjectName("listWidget")
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
        self.listWidget_2.setGeometry(QtCore.QRect(40, 370, 281, 51))
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
        self.label.setGeometry(QtCore.QRect(270, 170, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label.setFont(font)
        self.label.setStyleSheet("\n"
"color: rgb(0, 0, 0);")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(260, 370, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 0, 0);\n"
"color: rgb(0, 0, 0);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(260, 380, 51, 31))
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
        self.TxtDes = QtWidgets.QLabel(Form)
        self.TxtDes.setGeometry(QtCore.QRect(210, 170, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.TxtDes.setFont(font)
        self.TxtDes.setStyleSheet("color:rgb(255, 0, 0)\n"
"")
        self.TxtDes.setObjectName("TxtDes")
        self.TxtAvg = QtWidgets.QLabel(Form)
        self.TxtAvg.setGeometry(QtCore.QRect(210, 150, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.TxtAvg.setFont(font)
        self.TxtAvg.setStyleSheet("color:rgb(255, 0, 0)\n"
"")
        self.TxtAvg.setObjectName("TxtAvg")
        self.TxtEff = QtWidgets.QLabel(Form)
        self.TxtEff.setGeometry(QtCore.QRect(150, 380, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.TxtEff.setFont(font)
        self.TxtEff.setStyleSheet("color:rgb(255, 0, 0)\n"
"")
        self.TxtEff.setObjectName("TxtEff")
        self.TxtDeg = QtWidgets.QLabel(Form)
        self.TxtDeg.setGeometry(QtCore.QRect(150, 370, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.TxtDeg.setFont(font)
        self.TxtDeg.setStyleSheet("color:rgb(255, 0, 0)\n"
"")
        self.TxtDeg.setObjectName("TxtDeg")
        self.BtnLocal = QtWidgets.QPushButton(Form)
        self.BtnLocal.setGeometry(QtCore.QRect(80, 430, 191, 31))
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
        self.cBoxPname.setGeometry(QtCore.QRect(140, 30, 151, 22))
        self.cBoxPname.setObjectName("cBoxPname")
        self.BrainGraph = QtWidgets.QLabel(Form)
        self.BrainGraph.setGeometry(QtCore.QRect(380, 120, 411, 361))
        self.BrainGraph.setText("")
        self.BrainGraph.setObjectName("BrainGraph")
        self.CboxCond = QtWidgets.QComboBox(Form)
        self.CboxCond.setGeometry(QtCore.QRect(140, 70, 151, 22))
        self.CboxCond.setObjectName("CboxCond")
        self.txtPatient_2 = QtWidgets.QLabel(Form)
        self.txtPatient_2.setGeometry(QtCore.QRect(70, 70, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.txtPatient_2.setFont(font)
        self.txtPatient_2.setObjectName("txtPatient_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    # ---------------------------------Added Code -------------------------------------------- #
        self.cBoxPname.addItem('')
        patient = Patient('id','full_name','group','research','file_path')
        comoboBox_patients = list(dict.fromkeys(patient.get_data_from_JSON('full_name')))
        self.cBoxPname.addItems(comoboBox_patients)

        self.cBoxElectrode.addItems(str(x) for x in range(1,24))
        self.CboxCond.addItem('')
        self.CboxCond.addItems(['Alone','Spontaneous','Synchronized'])

    # ------------------------------- Call to Functions -------------------------------------- #
        from functools import partial
    #     self.BtnGlobal.clicked.connect(self.show_results)
        self.cBoxPname.currentTextChanged.connect(self.show_results)
        self.CboxCond.currentTextChanged.connect(self.condition_changed)
        self.cBoxElectrode.currentTextChanged.connect(self.show_res_electrode)
        self.BtnGlobal.clicked.connect(self.global_explained)
        self.BtnLocal.clicked.connect(self.local_explained)

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
        self.label_3.setText(_translate("Form", "of    22"))
        self.label_4.setText(_translate("Form", "of   1.000"))
        self.TxtDes.setText(_translate("Form", "Txt"))
        self.TxtAvg.setText(_translate("Form", "Txt"))
        self.TxtEff.setText(_translate("Form", "Txt"))
        self.TxtDeg.setText(_translate("Form", "Txt"))
        self.BtnLocal.setText(_translate("Form", "Local Parameters Explaining"))
        self.txtPatient_2.setText(_translate("Form", "Condition:"))

    # -------------------------------------- Functions ----------------------------------------- #

    def show_results(self,value):
        if(value == ''):
            self.CboxCond.clear()

    def condition_changed(self,value):
        global cond
        cond = ''
        if not(value == ''):
            if (value == 'Alone'):
                cond = 'B'
            elif (value == 'Spontaneous'):
                cond = 'C'
            else:
                cond = 'D'

            from undirectedGraph import Graph
            g = Graph()
            g.create_nodes(g.create_edges(self.cBoxPname.currentText() + '-' + cond))
            self.TxtDes.setText(str(round(g.density,3)))
            self.TxtAvg.setText(str(round(g.shortest_paths,3)))
            self.BrainGraph.setPixmap(QtGui.QPixmap(self.cBoxPname.currentText() + '-' + cond + ".png"))
            self.BrainGraph.setScaledContents(True)
            self.TxtDeg.setText(str(round(g.degrees[int(self.cBoxElectrode.currentText()) - 1],3)))
            self.TxtEff.setText(str(round(g.locals_efficiency[int(self.cBoxElectrode.currentText()) - 1],3)))

        else:
            self.TxtDes.clear()
            self.TxtAvg.clear()
            self.TxtMod.clear()
            self.BrainGraph.clear()
            self.TxtDeg.clear()
            self.TxtEff.clear()

    def show_res_electrode(self):
        from undirectedGraph import Graph
        print(self.cBoxPname.currentText())
        g = Graph()
        g.create_nodes(g.create_edges(self.cBoxPname.currentText() + '-' + cond))
        # ---- For the COMOBO BOX -------- #
        self.TxtDeg.setText(str(round(g.degrees[int(self.cBoxElectrode.currentText())-1],3)))
        self.TxtEff.setText(str(round(g.locals_efficiency[int(self.cBoxElectrode.currentText())-1],3)))

    def global_explained(self):
        from GlobalExplaning import Ui_Form
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()
        # MainWindow.hide()

    def local_explained(self):
        from LocalExplaining import Ui_Form
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()
        # MainWindow.hide()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())



