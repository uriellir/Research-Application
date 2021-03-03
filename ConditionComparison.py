# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ConditionComparison.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from Patient import Patient
from Research import Research

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(894, 570)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("brainPic.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        Form.setWindowIcon(icon)
        self.txtGlobalComp = QtWidgets.QLabel(Form)
        self.txtGlobalComp.setGeometry(QtCore.QRect(450, 50, 301, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.txtGlobalComp.setFont(font)
        self.txtGlobalComp.setObjectName("txtGlobalComp")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(460, 100, 341, 51))
        self.listWidget.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.listWidget.setLineWidth(3)
        self.listWidget.setMidLineWidth(3)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.txtLocal = QtWidgets.QLabel(Form)
        self.txtLocal.setGeometry(QtCore.QRect(460, 330, 311, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.txtLocal.setFont(font)
        self.txtLocal.setObjectName("txtLocal")
        self.txtEloctrode = QtWidgets.QLabel(Form)
        self.txtEloctrode.setGeometry(QtCore.QRect(460, 360, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.txtEloctrode.setFont(font)
        self.txtEloctrode.setObjectName("txtEloctrode")
        self.listWidget_2 = QtWidgets.QListWidget(Form)
        self.listWidget_2.setGeometry(QtCore.QRect(460, 410, 341, 51))
        self.listWidget_2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.listWidget_2.setLineWidth(3)
        self.listWidget_2.setMidLineWidth(3)
        self.listWidget_2.setObjectName("listWidget_2")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        self.BtnGlobal = QtWidgets.QPushButton(Form)
        self.BtnGlobal.setGeometry(QtCore.QRect(520, 170, 191, 31))
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
        self.BrainPic_3 = QtWidgets.QLabel(Form)
        self.BrainPic_3.setGeometry(QtCore.QRect(800, 10, 81, 81))
        self.BrainPic_3.setText("")
        self.BrainPic_3.setPixmap(QtGui.QPixmap("logo2.png"))
        self.BrainPic_3.setObjectName("BrainPic_3")
        self.TxtDes = QtWidgets.QLabel(Form)
        self.TxtDes.setGeometry(QtCore.QRect(630, 120, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.TxtDes.setFont(font)
        self.TxtDes.setStyleSheet("color:rgb(0, 0, 0)\n"
"")
        self.TxtDes.setObjectName("TxtDes")
        self.TxtAvg = QtWidgets.QLabel(Form)
        self.TxtAvg.setGeometry(QtCore.QRect(630, 100, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.TxtAvg.setFont(font)
        self.TxtAvg.setStyleSheet("color:rgb(0, 0, 0)\n"
"")
        self.TxtAvg.setObjectName("TxtAvg")
        self.BtnLocal = QtWidgets.QPushButton(Form)
        self.BtnLocal.setGeometry(QtCore.QRect(520, 470, 191, 31))
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
        self.cBoxElectrode.setGeometry(QtCore.QRect(570, 360, 69, 22))
        self.cBoxElectrode.setObjectName("cBoxElectrode")
        self.txtGlobHeaSub = QtWidgets.QLabel(Form)
        self.txtGlobHeaSub.setGeometry(QtCore.QRect(610, 80, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.txtGlobHeaSub.setFont(font)
        self.txtGlobHeaSub.setObjectName("txtGlobHeaSub")
        self.TxtDes1 = QtWidgets.QLabel(Form)
        self.TxtDes1.setGeometry(QtCore.QRect(710, 120, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.TxtDes1.setFont(font)
        self.TxtDes1.setStyleSheet("color:rgb(0, 0, 0)\n"
"")
        self.TxtDes1.setObjectName("TxtDes1")
        self.TxtAvg1 = QtWidgets.QLabel(Form)
        self.TxtAvg1.setGeometry(QtCore.QRect(710, 100, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.TxtAvg1.setFont(font)
        self.TxtAvg1.setStyleSheet("color:rgb(0, 0, 0)\n"
"")
        self.TxtAvg1.setObjectName("TxtAvg1")
        self.TxtAvg2 = QtWidgets.QLabel(Form)
        self.TxtAvg2.setGeometry(QtCore.QRect(760, 100, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.TxtAvg2.setFont(font)
        self.TxtAvg2.setStyleSheet("color:rgb(255, 0, 0)\n"
"")
        self.TxtAvg2.setObjectName("TxtAvg2")
        self.TxtDes3 = QtWidgets.QLabel(Form)
        self.TxtDes3.setGeometry(QtCore.QRect(760, 120, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.TxtDes3.setFont(font)
        self.TxtDes3.setStyleSheet("color:rgb(255, 0, 0)\n"
"")
        self.TxtDes3.setObjectName("TxtDes3")
        self.listWidget_5 = QtWidgets.QListWidget(Form)
        self.listWidget_5.setGeometry(QtCore.QRect(460, 240, 341, 51))
        self.listWidget_5.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.listWidget_5.setLineWidth(3)
        self.listWidget_5.setMidLineWidth(3)
        self.listWidget_5.setObjectName("listWidget_5")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_5.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_5.addItem(item)
        self.TxtHelMaxD = QtWidgets.QLabel(Form)
        self.TxtHelMaxD.setGeometry(QtCore.QRect(600, 260, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.TxtHelMaxD.setFont(font)
        self.TxtHelMaxD.setStyleSheet("")
        self.TxtHelMaxD.setObjectName("TxtHelMaxD")
        self.TxtSubMinD = QtWidgets.QLabel(Form)
        self.TxtSubMinD.setGeometry(QtCore.QRect(670, 240, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.TxtSubMinD.setFont(font)
        self.TxtSubMinD.setStyleSheet("")
        self.TxtSubMinD.setObjectName("TxtSubMinD")
        self.TxtSubMaxD = QtWidgets.QLabel(Form)
        self.TxtSubMaxD.setGeometry(QtCore.QRect(670, 260, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.TxtSubMaxD.setFont(font)
        self.TxtSubMaxD.setStyleSheet("")
        self.TxtSubMaxD.setObjectName("TxtSubMaxD")
        self.TxtDes_2 = QtWidgets.QLabel(Form)
        self.TxtDes_2.setGeometry(QtCore.QRect(580, 430, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.TxtDes_2.setFont(font)
        self.TxtDes_2.setStyleSheet("")
        self.TxtDes_2.setObjectName("TxtDes_2")
        self.TxtDes3_2 = QtWidgets.QLabel(Form)
        self.TxtDes3_2.setGeometry(QtCore.QRect(730, 430, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.TxtDes3_2.setFont(font)
        self.TxtDes3_2.setStyleSheet("color:rgb(255, 0, 0)\n"
"")
        self.TxtDes3_2.setObjectName("TxtDes3_2")
        self.TxtAvg2_2 = QtWidgets.QLabel(Form)
        self.TxtAvg2_2.setGeometry(QtCore.QRect(730, 410, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.TxtAvg2_2.setFont(font)
        self.TxtAvg2_2.setStyleSheet("color:rgb(255, 0, 0)\n"
"")
        self.TxtAvg2_2.setObjectName("TxtAvg2_2")
        self.TxtAvg_2 = QtWidgets.QLabel(Form)
        self.TxtAvg_2.setGeometry(QtCore.QRect(580, 410, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.TxtAvg_2.setFont(font)
        self.TxtAvg_2.setStyleSheet("")
        self.TxtAvg_2.setObjectName("TxtAvg_2")
        self.TxtAvg1_2 = QtWidgets.QLabel(Form)
        self.TxtAvg1_2.setGeometry(QtCore.QRect(650, 410, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.TxtAvg1_2.setFont(font)
        self.TxtAvg1_2.setStyleSheet("")
        self.TxtAvg1_2.setObjectName("TxtAvg1_2")
        self.TxtDes1_2 = QtWidgets.QLabel(Form)
        self.TxtDes1_2.setGeometry(QtCore.QRect(650, 430, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.TxtDes1_2.setFont(font)
        self.TxtDes1_2.setStyleSheet("")
        self.TxtDes1_2.setObjectName("TxtDes1_2")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 0, 411, 571))
        self.widget.setStyleSheet("background-color: rgb(227, 227, 227);")
        self.widget.setObjectName("widget")
        self.txtCompare_3 = QtWidgets.QLabel(self.widget)
        self.txtCompare_3.setGeometry(QtCore.QRect(50, 120, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.txtCompare_3.setFont(font)
        self.txtCompare_3.setObjectName("txtCompare_3")
        self.txtCompare1 = QtWidgets.QLabel(self.widget)
        self.txtCompare1.setGeometry(QtCore.QRect(100, 160, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.txtCompare1.setFont(font)
        self.txtCompare1.setObjectName("txtCompare1")
        self.txtResearch = QtWidgets.QLabel(self.widget)
        self.txtResearch.setGeometry(QtCore.QRect(60, 40, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.txtResearch.setFont(font)
        self.txtResearch.setStyleSheet("color: rgb(0, 0, 0);\n"
"")
        self.txtResearch.setObjectName("txtResearch")
        self.cBoxCond = QtWidgets.QComboBox(self.widget)
        self.cBoxCond.setGeometry(QtCore.QRect(60, 60, 191, 22))
        self.cBoxCond.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cBoxCond.setObjectName("cBoxCond")
        self.txtCompare2 = QtWidgets.QLabel(self.widget)
        self.txtCompare2.setGeometry(QtCore.QRect(270, 160, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.txtCompare2.setFont(font)
        self.txtCompare2.setObjectName("txtCompare2")
        self.cBoxGrp1 = QtWidgets.QComboBox(self.widget)
        self.cBoxGrp1.setGeometry(QtCore.QRect(50, 180, 141, 22))
        self.cBoxGrp1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cBoxGrp1.setObjectName("cBoxGrp1")
        self.cBoxGrp2 = QtWidgets.QComboBox(self.widget)
        self.cBoxGrp2.setGeometry(QtCore.QRect(220, 180, 141, 22))
        self.cBoxGrp2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cBoxGrp2.setObjectName("cBoxGrp2")
        self.txtCond = QtWidgets.QLabel(self.widget)
        self.txtCond.setGeometry(QtCore.QRect(50, 250, 201, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.txtCond.setFont(font)
        self.txtCond.setObjectName("txtCond")
        self.txtCondition2 = QtWidgets.QLabel(self.widget)
        self.txtCondition2.setGeometry(QtCore.QRect(250, 290, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.txtCondition2.setFont(font)
        self.txtCondition2.setObjectName("txtCondition2")
        self.cBoxGond2 = QtWidgets.QComboBox(self.widget)
        self.cBoxGond2.setGeometry(QtCore.QRect(220, 310, 141, 22))
        self.cBoxGond2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cBoxGond2.setObjectName("cBoxGond2")
        self.txtCondition1 = QtWidgets.QLabel(self.widget)
        self.txtCondition1.setGeometry(QtCore.QRect(80, 290, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.txtCondition1.setFont(font)
        self.txtCondition1.setObjectName("txtCondition1")
        self.cBoxCond1 = QtWidgets.QComboBox(self.widget)
        self.cBoxCond1.setGeometry(QtCore.QRect(50, 310, 141, 22))
        self.cBoxCond1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cBoxCond1.setObjectName("cBoxCond1")
        self.BtnConExp = QtWidgets.QPushButton(self.widget)
        self.BtnConExp.setGeometry(QtCore.QRect(130, 490, 151, 31))
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
        self.TxtHelMinD = QtWidgets.QLabel(Form)
        self.TxtHelMinD.setGeometry(QtCore.QRect(600, 240, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.TxtHelMinD.setFont(font)
        self.TxtHelMinD.setStyleSheet("color:rgb(0, 0, 0)\n"
"")
        self.TxtHelMinD.setObjectName("TxtHelMinD")
        self.txtGlobHeaSub_4 = QtWidgets.QLabel(Form)
        self.txtGlobHeaSub_4.setGeometry(QtCore.QRect(560, 390, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.txtGlobHeaSub_4.setFont(font)
        self.txtGlobHeaSub_4.setObjectName("txtGlobHeaSub_4")
        self.txtGlobHeaSub_5 = QtWidgets.QLabel(Form)
        self.txtGlobHeaSub_5.setGeometry(QtCore.QRect(580, 220, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.txtGlobHeaSub_5.setFont(font)
        self.txtGlobHeaSub_5.setObjectName("txtGlobHeaSub_5")
        self.buttonBox = QtWidgets.QDialogButtonBox(Form)
        self.buttonBox.setGeometry(QtCore.QRect(800, 520, 51, 31))
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

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


        # -------------------- Added Code ------------------------- #
        self.cBoxCond.addItem("")
        patient = Patient("id", "full_name", "group", 'research', "file_path")
        comoboBox_data = list(dict.fromkeys(patient.get_data_from_JSON(
            'research_name')))  # Remove duplicates from list - dictionary cannot have duplicates.
        self.cBoxCond.addItems(comoboBox_data)

        self.cBoxGrp1.addItem("")
        self.cBoxGrp1.setEnabled(False)

        self.cBoxGrp2.addItem("")
        self.cBoxGrp2.setEnabled(False)

        self.cBoxCond1.addItem("")
        self.cBoxCond1.setEnabled(False)

        self.cBoxGond2.addItem("")
        self.cBoxGond2.setEnabled(False)

        self.cBoxElectrode.addItem("")
        self.cBoxElectrode.setEnabled(False)
        self.cBoxElectrode.addItems(str(x) for x in range(1, 24))


        # ---------------- Call to Functions ------------- #
        self.cBoxCond.currentTextChanged.connect(self.research_changed)
        self.cBoxGrp1.currentTextChanged.connect(self.group1_changed)
        self.cBoxGrp2.currentTextChanged.connect(self.group2_changed)
        self.cBoxCond1.currentTextChanged.connect(self.cond1_changed)
        self.cBoxGond2.currentTextChanged.connect(self.cond2_changed)
        self.cBoxElectrode.currentTextChanged.connect(self.electrode_changed)
        self.BtnConExp.clicked.connect(self.cond_explained)
        self.BtnGlobal.clicked.connect(self.global_explained)
        self.BtnLocal.clicked.connect(self.local_explained)

    def retranslateUi(self, Form):
            _translate = QtCore.QCoreApplication.translate
            Form.setWindowTitle(_translate("Form", "Condition Comparison"))
            self.txtGlobalComp.setText(_translate("Form", "Comparation of Global Parameters Of The Graph:"))
            __sortingEnabled = self.listWidget.isSortingEnabled()
            self.listWidget.setSortingEnabled(False)
            item = self.listWidget.item(0)
            item.setText(_translate("Form", "Avarage Shortest Path Length:"))
            item = self.listWidget.item(1)
            item.setText(_translate("Form", "Density:"))
            self.listWidget.setSortingEnabled(__sortingEnabled)
            self.txtLocal.setText(_translate("Form", "Comparation of Local Parameters Of The Graph:"))
            self.txtEloctrode.setText(_translate("Form", "Choose Electrode:"))
            __sortingEnabled = self.listWidget_2.isSortingEnabled()
            self.listWidget_2.setSortingEnabled(False)
            item = self.listWidget_2.item(0)
            item.setText(_translate("Form", "Degree:"))
            item = self.listWidget_2.item(1)
            item.setText(_translate("Form", "Local Efficiency:"))
            self.listWidget_2.setSortingEnabled(__sortingEnabled)
            self.BtnGlobal.setText(_translate("Form", "Global Parameters Explaining"))
            self.TxtDes.setText(_translate("Form", "Txt"))
            self.TxtAvg.setText(_translate("Form", "Txt"))
            self.BtnLocal.setText(_translate("Form", "Local Parameters Explaining"))
            self.txtGlobHeaSub.setText(_translate("Form", "Condition1          condition2      Diff"))
            self.TxtDes1.setText(_translate("Form", "Txt"))
            self.TxtAvg1.setText(_translate("Form", "Txt"))
            self.TxtAvg2.setText(_translate("Form", "Txt"))
            self.TxtDes3.setText(_translate("Form", "Txt"))
            __sortingEnabled = self.listWidget_5.isSortingEnabled()
            self.listWidget_5.setSortingEnabled(False)
            item = self.listWidget_5.item(0)
            item.setText(_translate("Form", "Min Degree:"))
            item = self.listWidget_5.item(1)
            item.setText(_translate("Form", "Max Degree:"))
            self.listWidget_5.setSortingEnabled(__sortingEnabled)
            self.TxtHelMaxD.setText(_translate("Form", "Txt"))
            self.TxtSubMinD.setText(_translate("Form", "Txt"))
            self.TxtSubMaxD.setText(_translate("Form", "Txt"))
            self.TxtDes_2.setText(_translate("Form", "Txt"))
            self.TxtDes3_2.setText(_translate("Form", "Txt"))
            self.TxtAvg2_2.setText(_translate("Form", "Txt"))
            self.TxtAvg_2.setText(_translate("Form", "Txt"))
            self.TxtAvg1_2.setText(_translate("Form", "Txt"))
            self.TxtDes1_2.setText(_translate("Form", "Txt"))
            self.txtCompare_3.setText(_translate("Form", "Select Groups :"))
            self.txtCompare1.setText(_translate("Form", "Group 1"))
            self.txtResearch.setText(_translate("Form", "Choose Research:"))
            self.txtCompare2.setText(_translate("Form", "Group 2"))
            self.txtCond.setText(_translate("Form", "Select Conditions to compare:"))
            self.txtCondition2.setText(_translate("Form", "Condition 2"))
            self.txtCondition1.setText(_translate("Form", "Condition 1"))
            self.BtnConExp.setText(_translate("Form", "Conditions Explaining"))
            self.TxtHelMinD.setText(_translate("Form", "Txt"))
            self.txtGlobHeaSub_4.setText(_translate("Form", "Condition1        condition2              Diff"))
            self.txtGlobHeaSub_5.setText(_translate("Form", "Condition1        condition2     "))

    def research_changed(self,value):
        """Research name comobo-box change event, fills the conditions combo-boxes.
                            :param value: research name combo-box value.
                            :type value: String.
                            :return value: NONE.
                            """
        if(value == ""):
            self.cBoxGrp1.clear()
            self.cBoxGrp2.clear()
            self.cBoxCond1.clear()
            self.cBoxGond2.clear()
            # self.cBoxElectrode.setCurrentIndex(0)
            self.cBoxCond1.setEnabled(False)
            self.cBoxGond2.setEnabled(False)
            self.cBoxGrp1.setEnabled(False)
            self.cBoxGrp2.setEnabled(False)
            # self.cBoxElectrode.setEnabled(False)
        else:
            self.cBoxCond1.clear()
            self.cBoxGond2.clear()
            self.cBoxGrp1.clear()
            self.cBoxGrp2.clear()
            # self.cBoxElectrode.clear()
            self.cBoxGrp1.setEnabled(True)
            self.cBoxGrp2.setEnabled(True)

            patient = Patient("","","","","")
            comoboBox_data = list(dict.fromkeys(patient.get_treshold_Dsection_from_JSON(self.cBoxCond.currentText(),'groups')))  # Remove duplicates from list - dictionary cannot have duplicates.

            self.cBoxGrp1.addItems(comoboBox_data)
            self.cBoxGrp2.addItems(comoboBox_data)
            self.cBoxGond2.addItems(['Alone', 'Spontaneous', 'Synchronic'])
            self.cBoxCond1.addItems(['Alone', 'Spontaneous', 'Synchronic'])



    def group1_changed(self, value):
        """Group 1 comobo-box change event, fills the conditions combo-boxes.
                :param value: group name combo-box value.
                :type value: String.
                :return value: NONE.
                """
        if (value == ""):
            self.cBoxCond1.clear()
        else:
            self.cBoxCond1.clear()
            self.cBoxCond1.addItems(['Alone', 'Spontaneous', 'Synchronic'])
            self.cBoxCond1.setEnabled(True)


    def group2_changed(self,value):
        """Group 2 comobo-box change event, fills the conditions combo-boxes.
                :param value: group name combo-box value.
                :type value: String.
                :return value: NONE.
                """
        if(value == ""):
            self.cBoxGond2.clear()
        else:
            self.cBoxCond1.clear()
            self.cBoxCond1.addItems(['Alone', 'Spontaneous', 'Synchronic'])
            self.cBoxGond2.setEnabled(True)

    def cond1_changed(self,value):
            """Condition 1 comobo-box change event, presents the results.
                            :param value: condition name combo-box value.
                            :type value: String.
                            :return value: NONE.
                            """
            if(value == ''):
                # self.cBoxElectrode.clear()
                # self.cBoxElectrode.setEnabled(False)
                self.TxtAvg.clear()  # Group 2 - Average Shortest Path
                self.TxtDes.clear()  # Group 2 - Density

                self.TxtHelMinD.clear()  # Group 2 - Min Degree
                self.TxtHelMaxD.clear()  # Group 2 - Max Degree
            else:
                    global cond1
                    if (value == 'Alone'):
                            cond1 = 'B'
                    elif (value == 'Spontaneous'):
                            cond1 = 'C'
                    else:
                            cond1 = 'D'
                    research = Research("", "", "", "", "", "", "")
                    # self.cBoxElectrode.setEnabled(True)
                    # self.cBoxElectrode.addItem("")
                    # self.cBoxElectrode.addItems(str(x) for x in range(1, 24))
                    density, shortest_path, min_degree, max_degree, degrees, local_efficiency = research.get_condition_data(self.cBoxCond.currentText(), self.cBoxGrp1.currentText(), cond1)
                    self.TxtAvg.setText(str(round(shortest_path,3)))  # Group 2 - Average Shortest Path
                    self.TxtDes.setText(str(round(density,3)))  # Group 2 - Density

                    self.TxtHelMinD.setText(str(round(min_degree,3)))  # Group 2 - Min Degree
                    self.TxtHelMaxD.setText(str(round(max_degree,3)))  # Group 2 - Max Degree

                    self.check_patients()

    def cond2_changed(self,value):
            """Condition 2 comobo-box change event, presents the results.
                                        :param value: condition name combo-box value.
                                        :type value: String.
                                        :return value: NONE.
                                        """
            if(value == ''):
                # self.cBoxElectrode.clear()
                # self.cBoxElectrode.setEnabled(False)
                self.TxtAvg1.clear()  # Group 2 - Average Shortest Path
                self.TxtDes1.clear()  # Group 2 - Density

                self.TxtSubMinD.clear()  # Group 2 - Min Degree
                self.TxtSubMaxD.clear()  # Group 2 - Max Degree
            else:
                    global cond2
                    if (value == 'Alone'):
                            cond2 = 'B'
                    elif (value == 'Spontaneous'):
                            cond2 = 'C'
                    else:
                            cond2 = 'D'
                    research = Research("", "", "", "", "", "", "")
                    # self.cBoxElectrode.setEnabled(True)
                    # self.cBoxElectrode.addItem("")
                    # self.cBoxElectrode.addItems(str(x) for x in range(1, 24))
                    density, shortest_path, min_degree, max_degree, degrees, local_efficiency = research.get_condition_data(self.cBoxCond.currentText(), self.cBoxGrp2.currentText(), cond2)
                    self.TxtAvg1.setText(str(round(shortest_path,3)))  # Group 2 - Average Shortest Path
                    self.TxtDes1.setText(str(round(density,3)))  # Group 2 - Density

                    self.TxtSubMinD.setText(str(round(min_degree,3)))  # Group 2 - Min Degree
                    self.TxtSubMaxD.setText(str(round(max_degree,3)))  # Group 2 - Max Degree

                    self.check_patients()

    def check_patients(self):
            """This function checks if both of the conditions combo-boxes aren't empty, if so
                , it presents the difference results."""
            if ((self.cBoxCond1.currentText() != '') and (self.cBoxGond2.currentText() != '')):
                    self.TxtAvg2.setText(str(round(abs(float(self.TxtAvg.text()) - float(self.TxtAvg1.text())),3)))  # Diff Average shortest path
                    self.TxtDes3.setText(str(round(abs(float(self.TxtDes.text()) - float(self.TxtDes1.text())),3))) # Diff Density

                    self.cBoxElectrode.setEnabled(True)
            # else:
            #     self.TxtDesGloDif.clear()
            #     self.TxtAvgGlobDif.clear()
            #     self.TxtModGloDif.clear()

    def electrode_changed(self,value):
        """Electrode comobo-box change event, presents the results.
                :param value: Electrode number combo-box value.
                :type value: String.
                :return value: NONE.
                """
        if (value == ""):
            print("")
        else:

            research = Research("", "", "", "", "", "", "")
            density1, shortest_path1, min_degree1, max_degree1, degrees1, local_efficiency1 = research.get_condition_data(self.cBoxCond.currentText(), self.cBoxGrp1.currentText(), cond1)
            density2, shortest_path2, min_degree2, max_degree2, degrees2, local_efficiency2 = research.get_condition_data(self.cBoxCond.currentText(), self.cBoxGrp2.currentText(), cond2)
            # ---- For the COMOBO BOX -------- #
            self.TxtAvg_2.setText(str(round(degrees1[int(self.cBoxElectrode.currentText())-1],3)))  # Group 1 - Electrode Degree
            self.TxtDes_2.setText(str(round(local_efficiency1[int(self.cBoxElectrode.currentText())-1],3)))  # Group 1 - Electrode Local Efficiency

            self.TxtAvg1_2.setText(str(round(degrees2[int(self.cBoxElectrode.currentText())-1],3)))  # Group 2 - Electrode Degree
            self.TxtDes1_2.setText(str(round(local_efficiency2[int(self.cBoxElectrode.currentText())-1],3)))  # Group 2 - Electrode Local Efficiency

            self.TxtAvg2_2.setText(str(round(abs(float(self.TxtAvg_2.text()) - float(self.TxtAvg1_2.text())),3)))  # Diff Electrode - Degree
            self.TxtDes3_2.setText(str(round(abs(float(self.TxtDes_2.text()) - float(self.TxtDes1_2.text())),3)))  # Diff Electrode - Local Efficiency



    def cond_explained(self):
            from ConditionExplaining import Ui_Form
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_Form()
            self.ui.setupUi(self.window)
            self.window.show()
            # MainWindow.hide()

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
