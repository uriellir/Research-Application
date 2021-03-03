# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PatientsComparisonScreen.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from Patient import Patient


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(986, 611)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("brainPic.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        Form.setWindowIcon(icon)
        self.txtPatient = QtWidgets.QLabel(Form)
        self.txtPatient.setGeometry(QtCore.QRect(110, 30, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.txtPatient.setFont(font)
        self.txtPatient.setObjectName("txtPatient")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(110, 50, 211, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.BrainPic = QtWidgets.QLabel(Form)
        self.BrainPic.setGeometry(QtCore.QRect(50, 20, 41, 41))
        self.BrainPic.setText("")
        self.BrainPic.setPixmap(QtGui.QPixmap("user3.png"))
        self.BrainPic.setObjectName("BrainPic")
        self.txtGlobal = QtWidgets.QLabel(Form)
        self.txtGlobal.setGeometry(QtCore.QRect(40, 450, 301, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.txtGlobal.setFont(font)
        self.txtGlobal.setObjectName("txtGlobal")
        self.listWidgetGlob = QtWidgets.QListWidget(Form)
        self.listWidgetGlob.setGeometry(QtCore.QRect(50, 490, 351, 51))
        self.listWidgetGlob.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.listWidgetGlob.setLineWidth(3)
        self.listWidgetGlob.setMidLineWidth(3)
        self.listWidgetGlob.setObjectName("listWidgetGlob")
        item = QtWidgets.QListWidgetItem()
        self.listWidgetGlob.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetGlob.addItem(item)
        self.txtLocal = QtWidgets.QLabel(Form)
        self.txtLocal.setGeometry(QtCore.QRect(490, 450, 311, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.txtLocal.setFont(font)
        self.txtLocal.setObjectName("txtLocal")
        self.txtEloctrode = QtWidgets.QLabel(Form)
        self.txtEloctrode.setGeometry(QtCore.QRect(490, 470, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.txtEloctrode.setFont(font)
        self.txtEloctrode.setObjectName("txtEloctrode")
        self.listWidgetLoc = QtWidgets.QListWidget(Form)
        self.listWidgetLoc.setGeometry(QtCore.QRect(570, 500, 311, 41))
        self.listWidgetLoc.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.listWidgetLoc.setLineWidth(3)
        self.listWidgetLoc.setMidLineWidth(3)
        self.listWidgetLoc.setObjectName("listWidgetLoc")
        item = QtWidgets.QListWidgetItem()
        self.listWidgetLoc.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetLoc.addItem(item)
        self.btnClose = QtWidgets.QDialogButtonBox(Form)
        self.btnClose.setGeometry(QtCore.QRect(920, 540, 41, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.btnClose.setFont(font)
        self.btnClose.setStyleSheet("QPushButton {\n"
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
        self.btnClose.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.btnClose.setObjectName("btnClose")
        self.BtnGlobal = QtWidgets.QPushButton(Form)
        self.BtnGlobal.setGeometry(QtCore.QRect(130, 560, 191, 31))
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
        self.txtBrain2 = QtWidgets.QLabel(Form)
        self.txtBrain2.setGeometry(QtCore.QRect(660, 60, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.txtBrain2.setFont(font)
        self.txtBrain2.setObjectName("txtBrain2")
        self.BrainPic_3 = QtWidgets.QLabel(Form)
        self.BrainPic_3.setGeometry(QtCore.QRect(910, 10, 61, 61))
        self.BrainPic_3.setText("")
        self.BrainPic_3.setPixmap(QtGui.QPixmap("logo3.png"))
        self.BrainPic_3.setObjectName("BrainPic_3")
        self.TxtDesGlob1 = QtWidgets.QLabel(Form)
        self.TxtDesGlob1.setGeometry(QtCore.QRect(220, 510, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.TxtDesGlob1.setFont(font)
        self.TxtDesGlob1.setStyleSheet("color:rgb(255, 0, 0)\n"
"")
        self.TxtDesGlob1.setObjectName("TxtDesGlob1")
        self.TxtAvgGlob1 = QtWidgets.QLabel(Form)
        self.TxtAvgGlob1.setGeometry(QtCore.QRect(220, 490, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.TxtAvgGlob1.setFont(font)
        self.TxtAvgGlob1.setStyleSheet("color:rgb(255, 0, 0)\n"
"")
        self.TxtAvgGlob1.setObjectName("TxtAvgGlob1")
        self.txtPatient_2 = QtWidgets.QLabel(Form)
        self.txtPatient_2.setGeometry(QtCore.QRect(630, 30, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.txtPatient_2.setFont(font)
        self.txtPatient_2.setObjectName("txtPatient_2")
        self.BrainPic_2 = QtWidgets.QLabel(Form)
        self.BrainPic_2.setGeometry(QtCore.QRect(570, 20, 41, 41))
        self.BrainPic_2.setText("")
        self.BrainPic_2.setPixmap(QtGui.QPixmap("user3.png"))
        self.BrainPic_2.setObjectName("BrainPic_2")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(630, 50, 201, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.txtBrain1 = QtWidgets.QLabel(Form)
        self.txtBrain1.setGeometry(QtCore.QRect(150, 60, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.txtBrain1.setFont(font)
        self.txtBrain1.setObjectName("txtBrain1")
        self.TxtDesGlo2 = QtWidgets.QLabel(Form)
        self.TxtDesGlo2.setGeometry(QtCore.QRect(290, 510, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.TxtDesGlo2.setFont(font)
        self.TxtDesGlo2.setStyleSheet("color:rgb(255, 0, 0)\n"
"")
        self.TxtDesGlo2.setObjectName("TxtDesGlo2")
        self.TxtAvgGlob2 = QtWidgets.QLabel(Form)
        self.TxtAvgGlob2.setGeometry(QtCore.QRect(290, 490, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.TxtAvgGlob2.setFont(font)
        self.TxtAvgGlob2.setStyleSheet("color:rgb(255, 0, 0)\n"
"")
        self.TxtAvgGlob2.setObjectName("TxtAvgGlob2")
        self.TxtAvgGlobDif = QtWidgets.QLabel(Form)
        self.TxtAvgGlobDif.setGeometry(QtCore.QRect(360, 490, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.TxtAvgGlobDif.setFont(font)
        self.TxtAvgGlobDif.setStyleSheet("color:rgb(0, 0, 0)\n"
"")
        self.TxtAvgGlobDif.setObjectName("TxtAvgGlobDif")
        self.TxtDesGloDif = QtWidgets.QLabel(Form)
        self.TxtDesGloDif.setGeometry(QtCore.QRect(360, 510, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.TxtDesGloDif.setFont(font)
        self.TxtDesGloDif.setStyleSheet("color:rgb(0, 0, 0)\n"
"")
        self.TxtDesGloDif.setObjectName("TxtDesGloDif")
        self.txtGlobPat1Pat2 = QtWidgets.QLabel(Form)
        self.txtGlobPat1Pat2.setGeometry(QtCore.QRect(210, 470, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.txtGlobPat1Pat2.setFont(font)
        self.txtGlobPat1Pat2.setObjectName("txtGlobPat1Pat2")
        self.BtnLocal = QtWidgets.QPushButton(Form)
        self.BtnLocal.setGeometry(QtCore.QRect(610, 560, 191, 31))
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
        self.txtLocPat1Pat2 = QtWidgets.QLabel(Form)
        self.txtLocPat1Pat2.setGeometry(QtCore.QRect(670, 480, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.txtLocPat1Pat2.setFont(font)
        self.txtLocPat1Pat2.setObjectName("txtLocPat1Pat2")
        self.TxtEffLoc1 = QtWidgets.QLabel(Form)
        self.TxtEffLoc1.setGeometry(QtCore.QRect(680, 520, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.TxtEffLoc1.setFont(font)
        self.TxtEffLoc1.setStyleSheet("color:rgb(255, 0, 0)\n"
"")
        self.TxtEffLoc1.setObjectName("TxtEffLoc1")
        self.TxtDegLoc1_2 = QtWidgets.QLabel(Form)
        self.TxtDegLoc1_2.setGeometry(QtCore.QRect(760, 500, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.TxtDegLoc1_2.setFont(font)
        self.TxtDegLoc1_2.setStyleSheet("color:rgb(255, 0, 0)\n"
"")
        self.TxtDegLoc1_2.setObjectName("TxtDegLoc1_2")
        self.TxtEffLocDif = QtWidgets.QLabel(Form)
        self.TxtEffLocDif.setGeometry(QtCore.QRect(840, 520, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.TxtEffLocDif.setFont(font)
        self.TxtEffLocDif.setStyleSheet("color:rgb(0, 0, 0)\n"
"")
        self.TxtEffLocDif.setObjectName("TxtEffLocDif")
        self.TxtEffLoc2 = QtWidgets.QLabel(Form)
        self.TxtEffLoc2.setGeometry(QtCore.QRect(760, 520, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.TxtEffLoc2.setFont(font)
        self.TxtEffLoc2.setStyleSheet("color:rgb(255, 0, 0)\n"
"")
        self.TxtEffLoc2.setObjectName("TxtEffLoc2")
        self.TxtDegLocDif = QtWidgets.QLabel(Form)
        self.TxtDegLocDif.setGeometry(QtCore.QRect(840, 500, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.TxtDegLocDif.setFont(font)
        self.TxtDegLocDif.setStyleSheet("color:rgb(0, 0, 0)\n"
"")
        self.TxtDegLocDif.setObjectName("TxtDegLocDif")
        self.TxtDegLoc1 = QtWidgets.QLabel(Form)
        self.TxtDegLoc1.setGeometry(QtCore.QRect(680, 500, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.TxtDegLoc1.setFont(font)
        self.TxtDegLoc1.setStyleSheet("color:rgb(255, 0, 0)\n"
"")
        self.TxtDegLoc1.setObjectName("TxtDegLoc1")
        self.cBoxElectrode1 = QtWidgets.QComboBox(Form)
        self.cBoxElectrode1.setGeometry(QtCore.QRect(580, 470, 69, 22))
        self.cBoxElectrode1.setObjectName("cBoxElectrode1")
        self.cBoxPatient1 = QtWidgets.QComboBox(Form)
        self.cBoxPatient1.setGeometry(QtCore.QRect(180, 30, 141, 22))
        self.cBoxPatient1.setObjectName("cBoxPatient1")
        self.cBoxPatient2 = QtWidgets.QComboBox(Form)
        self.cBoxPatient2.setGeometry(QtCore.QRect(690, 30, 141, 22))
        self.cBoxPatient2.setObjectName("cBoxPatient2")
        self.BrainGraph = QtWidgets.QLabel(Form)
        self.BrainGraph.setGeometry(QtCore.QRect(520, 100, 391, 341))
        self.BrainGraph.setText("")
        self.BrainGraph.setObjectName("BrainGraph")
        self.BrainGraph_2 = QtWidgets.QLabel(Form)
        self.BrainGraph_2.setGeometry(QtCore.QRect(30, 100, 391, 341))
        self.BrainGraph_2.setText("")
        self.BrainGraph_2.setObjectName("BrainGraph_2")
        self.cBoxCond = QtWidgets.QComboBox(Form)
        self.cBoxCond.setGeometry(QtCore.QRect(380, 80, 141, 22))
        self.cBoxCond.setObjectName("cBoxCond")
        self.txtCond = QtWidgets.QLabel(Form)
        self.txtCond.setGeometry(QtCore.QRect(390, 60, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.txtCond.setFont(font)
        self.txtCond.setStyleSheet("color: rgb(199, 107, 152);\n"
"\n"
"")
        self.txtCond.setObjectName("txtCond")
        self.txtRes = QtWidgets.QLabel(Form)
        self.txtRes.setGeometry(QtCore.QRect(390, 10, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.txtRes.setFont(font)
        self.txtRes.setStyleSheet("color: rgb(199, 107, 152);\n"
"\n"
"")
        self.txtRes.setObjectName("txtRes")
        self.cBoxRes = QtWidgets.QComboBox(Form)
        self.cBoxRes.setGeometry(QtCore.QRect(380, 30, 141, 22))
        self.cBoxRes.setObjectName("cBoxRes")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # ---------------------- Added Code ------------------------ #
        self.cBoxPatient1.setEnabled(False)
        self.cBoxPatient2.setEnabled(False)

        self.cBoxCond.addItem("")
        self.cBoxCond.addItems(['Alone','Spontaneous','Synchronized'])
        self.cBoxCond.setEnabled(False)

        self.cBoxRes.addItem("")
        patient = Patient("id", "full_name", "group", 'research', "file_path")
        comoboBox_data = list(dict.fromkeys(patient.get_data_from_JSON('research_name')))  # Remove duplicates from list - dictionary cannot have duplicates.
        self.cBoxRes.addItems(comoboBox_data)

        self.cBoxElectrode1.addItem('')
        self.cBoxElectrode1.setEnabled(False)
        self.cBoxElectrode1.addItems(str(x) for x in range(1, 24))

        # ---------------- Call to Functions ------------- #
        self.cBoxRes.currentTextChanged.connect(self.resName_changed)
        self.cBoxCond.currentTextChanged.connect(self.cond_changed)
        self.cBoxPatient1.currentTextChanged.connect(self.patient1_changed)
        self.cBoxPatient2.currentTextChanged.connect(self.patient2_changed)
        self.cBoxElectrode1.currentTextChanged.connect(self.electrode_changed)
        self.BtnGlobal.clicked.connect(self.global_explained)
        self.BtnLocal.clicked.connect(self.local_explained)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Patients Comparison"))
        self.txtPatient.setText(_translate("Form", "Patient1:"))
        self.txtGlobal.setText(_translate("Form", "Comparation of Global Parameters Of The Graph:"))
        __sortingEnabled = self.listWidgetGlob.isSortingEnabled()
        self.listWidgetGlob.setSortingEnabled(False)
        item = self.listWidgetGlob.item(0)
        item.setText(_translate("Form", "Avarage Shortest Path Length:"))
        item = self.listWidgetGlob.item(1)
        item.setText(_translate("Form", "Density:"))
        self.listWidgetGlob.setSortingEnabled(__sortingEnabled)
        self.txtLocal.setText(_translate("Form", "Comparation of Local Parameters Of The Graph:"))
        self.txtEloctrode.setText(_translate("Form", "Choose Electrode:"))
        __sortingEnabled = self.listWidgetLoc.isSortingEnabled()
        self.listWidgetLoc.setSortingEnabled(False)
        item = self.listWidgetLoc.item(0)
        item.setText(_translate("Form", "Degree:"))
        item = self.listWidgetLoc.item(1)
        item.setText(_translate("Form", "Local Efficiency:"))
        self.listWidgetLoc.setSortingEnabled(__sortingEnabled)
        self.BtnGlobal.setText(_translate("Form", "Global Parameters Explaining"))
        self.txtBrain2.setText(_translate("Form", "Brain Connectivity Graph"))
        self.TxtDesGlob1.setText(_translate("Form", "Txt"))
        self.TxtAvgGlob1.setText(_translate("Form", "Txt"))
        self.txtPatient_2.setText(_translate("Form", "Patient2:"))
        self.txtBrain1.setText(_translate("Form", "Brain Connectivity Graph"))
        self.TxtDesGlo2.setText(_translate("Form", "Txt"))
        self.TxtAvgGlob2.setText(_translate("Form", "Txt"))
        self.TxtAvgGlobDif.setText(_translate("Form", "Txt"))
        self.TxtDesGloDif.setText(_translate("Form", "Txt"))
        self.txtGlobPat1Pat2.setText(_translate("Form", "Patient1          Patient2             Diff"))
        self.BtnLocal.setText(_translate("Form", "Local Parameters Explaining"))
        self.txtLocPat1Pat2.setText(_translate("Form", "Patient1            Patient2                 Diff"))
        self.TxtEffLoc1.setText(_translate("Form", "Txt"))
        self.TxtDegLoc1_2.setText(_translate("Form", "Txt"))
        self.TxtEffLocDif.setText(_translate("Form", "Txt"))
        self.TxtEffLoc2.setText(_translate("Form", "Txt"))
        self.TxtDegLocDif.setText(_translate("Form", "Txt"))
        self.TxtDegLoc1.setText(_translate("Form", "Txt"))
        self.txtCond.setText(_translate("Form", "Choose Condition:"))
        self.txtRes.setText(_translate("Form", "Choose Research:"))

    # -------------------------------------- Functions ----------------------------------------- #
    def resName_changed(self,value):
        if(value == ''):
            self.cBoxCond.clear()
        else:
            self.cBoxCond.setEnabled(True)

            patient = Patient("id", "full_name", "group", 'research', "file_path")
            # comoboBox_data = list(dict.fromkeys(patient.get_treshold_Dsection_from_JSON(self.cBoxRes.currentText(),'conditions')))  # Remove duplicates from list - dictionary cannot have duplicates.

            self.cBoxPatient1.clear()
            self.cBoxPatient2.clear()
            self.BrainGraph.clear()
            self.BrainGraph_2.clear()
            # self.cBoxCond.addItems(comoboBox_data)

    def cond_changed(self):
        self.cBoxPatient1.clear()
        self.cBoxPatient2.clear()

        self.cBoxPatient1.setEnabled(True)
        self.cBoxPatient2.setEnabled(True)

        patient = Patient("id", "full_name", "group", 'research', "file_path")
        comoboBox_patients = list(dict.fromkeys(patient.get_specific_patients_JSON(self.cBoxRes.currentText())))
        self.cBoxPatient1.addItem("")
        self.cBoxPatient1.addItems(comoboBox_patients)
        self.cBoxPatient2.addItem("")
        self.cBoxPatient2.addItems(comoboBox_patients)

        global cond
        cond = ''
        if (self.cBoxCond.currentText() == 'Alone'):
            cond = 'B'
        elif (self.cBoxCond.currentText() == 'Spontaneous'):
            cond = 'C'
        else:
            cond = 'D'

    def patient1_changed(self,value):
        print(value)
        condVal = self.cBoxCond.currentText()

        if(value==''):
            self.TxtDesGlob1.clear()
            self.TxtAvgGlob1.clear()
            self.BrainGraph_2.clear()
        else:

            from undirectedGraph import Graph
            g = Graph()
            g.create_nodes(g.create_edges(value + '-' + cond))
            # Global Parameters
            self.TxtDesGlob1.setText(str(round(g.density,3)))
            self.TxtAvgGlob1.setText(str(round(g.shortest_paths,3)))
            self.BrainGraph_2.setPixmap(QtGui.QPixmap(value + '-' + cond + ".png"))
            self.BrainGraph_2.setScaledContents(True)

        self.check_patients()

    def patient2_changed(self,value):
        print(value)
        conddVal = self.cBoxCond.currentText()

        if (value == ''):
            self.TxtDesGlo2.clear()
            self.TxtAvgGlob2.clear()
            self.BrainGraph.clear()
        else:

            from undirectedGraph import Graph
            g = Graph()
            g.create_nodes(g.create_edges(value + '-' + cond))
            self.TxtDesGlo2.setText(str(round(g.density,3)))
            self.TxtAvgGlob2.setText(str(round(g.shortest_paths,3)))
            self.BrainGraph.setPixmap(QtGui.QPixmap(value + '-' + cond + ".png"))
            self.BrainGraph.setScaledContents(True)
            # self.TxtDeg.setText(str(g.degrees[int(self.cBoxElectrode.currentText()) - 1]))
            # self.TxtEff.setText(str(g.locals_efficiency[int(self.cBoxElectrode.currentText()) - 1]))

        self.check_patients()

    def check_patients(self):
        if((self.cBoxPatient1.currentText() != '') and (self.cBoxPatient2.currentText() != '')):
            self.TxtDesGloDif.setText(str(round(abs(float(self.TxtDesGlob1.text()) - float(self.TxtDesGlo2.text())),3)))
            self.TxtAvgGlobDif.setText(str(round(abs(float(self.TxtAvgGlob1.text()) - float(self.TxtAvgGlob2.text())),3)))
            self.cBoxElectrode1.setEnabled(True)
        else:
            self.TxtDesGloDif.clear()
            self.TxtAvgGlobDif.clear()

    def electrode_changed(self):
        value = self.cBoxCond.currentText()

        if(self.cBoxElectrode1.currentText()==''):
            self.TxtDegLoc1.clear()
            self.TxtDegLoc1_2.clear()
            self.TxtDegLocDif.clear()

            self.TxtEffLoc1.clear()
            self.TxtEffLoc2.clear()
            self.TxtEffLocDif.clear()
        else:
            if (value == 'Alone'):
                cond = 'B'
            elif (value == 'Spontaneous'):
                cond = 'C'
            else:
                cond = 'D'

            from undirectedGraph import Graph
            g1 = Graph()
            g1.create_nodes(g1.create_edges(self.cBoxPatient1.currentText() + '-' + cond))
            self.TxtDegLoc1.setText(str(round(g1.degrees[int(self.cBoxElectrode1.currentText()) - 1],3)))
            self.TxtEffLoc1.setText(str(round(g1.locals_efficiency[int(self.cBoxElectrode1.currentText()) - 1],3)))

            g2 = Graph()
            g2.create_nodes(g2.create_edges(self.cBoxPatient2.currentText() + '-' + cond))
            self.TxtDegLoc1_2.setText(str(round(g2.degrees[int(self.cBoxElectrode1.currentText()) - 1],3)))
            self.TxtEffLoc2.setText(str(round(g2.locals_efficiency[int(self.cBoxElectrode1.currentText()) - 1],3)))

            self.TxtDegLocDif.setText(str(round(abs(float(self.TxtDegLoc1.text()) - float(self.TxtDegLoc1_2.text())),3)))
            self.TxtEffLocDif.setText(str(round(abs(float(self.TxtEffLoc1.text()) - float(self.TxtEffLoc2.text())),3)))

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
