# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GroupComparisonScreen.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


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
        self.listWidget.setGeometry(QtCore.QRect(460, 100, 311, 61))
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
        self.txtLocal.setGeometry(QtCore.QRect(460, 340, 311, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.txtLocal.setFont(font)
        self.txtLocal.setObjectName("txtLocal")
        self.txtEloctrode = QtWidgets.QLabel(Form)
        self.txtEloctrode.setGeometry(QtCore.QRect(460, 370, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.txtEloctrode.setFont(font)
        self.txtEloctrode.setObjectName("txtEloctrode")
        self.listWidget_2 = QtWidgets.QListWidget(Form)
        self.listWidget_2.setGeometry(QtCore.QRect(460, 420, 311, 51))
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
        self.TxtMod = QtWidgets.QLabel(Form)
        self.TxtMod.setGeometry(QtCore.QRect(630, 130, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.TxtMod.setFont(font)
        self.TxtMod.setStyleSheet("color:rgb(0, 0, 0)\n"
"")
        self.TxtMod.setObjectName("TxtMod")
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
        self.BtnLocal.setGeometry(QtCore.QRect(520, 480, 191, 31))
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
        self.cBoxElectrode.setGeometry(QtCore.QRect(570, 370, 69, 22))
        self.cBoxElectrode.setObjectName("cBoxElectrode")
        self.txtGlobHeaSub = QtWidgets.QLabel(Form)
        self.txtGlobHeaSub.setGeometry(QtCore.QRect(620, 80, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.txtGlobHeaSub.setFont(font)
        self.txtGlobHeaSub.setObjectName("txtGlobHeaSub")
        self.TxtMod1 = QtWidgets.QLabel(Form)
        self.TxtMod1.setGeometry(QtCore.QRect(680, 130, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.TxtMod1.setFont(font)
        self.TxtMod1.setStyleSheet("color:rgb(0, 0, 0)\n"
"")
        self.TxtMod1.setObjectName("TxtMod1")
        self.TxtDes1 = QtWidgets.QLabel(Form)
        self.TxtDes1.setGeometry(QtCore.QRect(680, 120, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.TxtDes1.setFont(font)
        self.TxtDes1.setStyleSheet("color:rgb(0, 0, 0)\n"
"")
        self.TxtDes1.setObjectName("TxtDes1")
        self.TxtAvg1 = QtWidgets.QLabel(Form)
        self.TxtAvg1.setGeometry(QtCore.QRect(680, 100, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.TxtAvg1.setFont(font)
        self.TxtAvg1.setStyleSheet("color:rgb(0, 0, 0)\n"
"")
        self.TxtAvg1.setObjectName("TxtAvg1")
        self.TxtAvg2 = QtWidgets.QLabel(Form)
        self.TxtAvg2.setGeometry(QtCore.QRect(730, 100, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.TxtAvg2.setFont(font)
        self.TxtAvg2.setStyleSheet("color:rgb(255, 0, 0)\n"
"")
        self.TxtAvg2.setObjectName("TxtAvg2")
        self.TxtMod2 = QtWidgets.QLabel(Form)
        self.TxtMod2.setGeometry(QtCore.QRect(730, 130, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.TxtMod2.setFont(font)
        self.TxtMod2.setStyleSheet("color:rgb(255, 0, 0)\n"
"")
        self.TxtMod2.setObjectName("TxtMod2")
        self.TxtDes3 = QtWidgets.QLabel(Form)
        self.TxtDes3.setGeometry(QtCore.QRect(730, 120, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.TxtDes3.setFont(font)
        self.TxtDes3.setStyleSheet("color:rgb(255, 0, 0)\n"
"")
        self.TxtDes3.setObjectName("TxtDes3")
        self.listWidget_5 = QtWidgets.QListWidget(Form)
        self.listWidget_5.setGeometry(QtCore.QRect(460, 230, 311, 81))
        self.listWidget_5.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.listWidget_5.setLineWidth(3)
        self.listWidget_5.setMidLineWidth(3)
        self.listWidget_5.setObjectName("listWidget_5")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_5.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_5.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_5.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_5.addItem(item)
        self.txtGlobHeaSub_2 = QtWidgets.QLabel(Form)
        self.txtGlobHeaSub_2.setGeometry(QtCore.QRect(590, 210, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.txtGlobHeaSub_2.setFont(font)
        self.txtGlobHeaSub_2.setObjectName("txtGlobHeaSub_2")
        self.TxtSHealMinE = QtWidgets.QLabel(Form)
        self.TxtSHealMinE.setGeometry(QtCore.QRect(600, 260, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.TxtSHealMinE.setFont(font)
        self.TxtSHealMinE.setStyleSheet("")
        self.TxtSHealMinE.setObjectName("TxtSHealMinE")
        self.TxtHelMaxD = QtWidgets.QLabel(Form)
        self.TxtHelMaxD.setGeometry(QtCore.QRect(600, 250, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.TxtHelMaxD.setFont(font)
        self.TxtHelMaxD.setStyleSheet("")
        self.TxtHelMaxD.setObjectName("TxtHelMaxD")
        self.TxtSubMinE_2 = QtWidgets.QLabel(Form)
        self.TxtSubMinE_2.setGeometry(QtCore.QRect(670, 260, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.TxtSubMinE_2.setFont(font)
        self.TxtSubMinE_2.setStyleSheet("")
        self.TxtSubMinE_2.setObjectName("TxtSubMinE_2")
        self.TxtSubMinD = QtWidgets.QLabel(Form)
        self.TxtSubMinD.setGeometry(QtCore.QRect(670, 230, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.TxtSubMinD.setFont(font)
        self.TxtSubMinD.setStyleSheet("")
        self.TxtSubMinD.setObjectName("TxtSubMinD")
        self.TxtSubMaxD = QtWidgets.QLabel(Form)
        self.TxtSubMaxD.setGeometry(QtCore.QRect(670, 250, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.TxtSubMaxD.setFont(font)
        self.TxtSubMaxD.setStyleSheet("\n"
"")
        self.TxtSubMaxD.setObjectName("TxtSubMaxD")
        self.TxtSubMaxE = QtWidgets.QLabel(Form)
        self.TxtSubMaxE.setGeometry(QtCore.QRect(670, 280, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.TxtSubMaxE.setFont(font)
        self.TxtSubMaxE.setStyleSheet("")
        self.TxtSubMaxE.setObjectName("TxtSubMaxE")
        self.txtGlobHeaSub_3 = QtWidgets.QLabel(Form)
        self.txtGlobHeaSub_3.setGeometry(QtCore.QRect(570, 400, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.txtGlobHeaSub_3.setFont(font)
        self.txtGlobHeaSub_3.setObjectName("txtGlobHeaSub_3")
        self.TxtDes_2 = QtWidgets.QLabel(Form)
        self.TxtDes_2.setGeometry(QtCore.QRect(580, 440, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.TxtDes_2.setFont(font)
        self.TxtDes_2.setStyleSheet("")
        self.TxtDes_2.setObjectName("TxtDes_2")
        self.TxtDes3_2 = QtWidgets.QLabel(Form)
        self.TxtDes3_2.setGeometry(QtCore.QRect(710, 440, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.TxtDes3_2.setFont(font)
        self.TxtDes3_2.setStyleSheet("color:rgb(255, 0, 0)\n"
"")
        self.TxtDes3_2.setObjectName("TxtDes3_2")
        self.TxtAvg2_2 = QtWidgets.QLabel(Form)
        self.TxtAvg2_2.setGeometry(QtCore.QRect(710, 420, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.TxtAvg2_2.setFont(font)
        self.TxtAvg2_2.setStyleSheet("color:rgb(255, 0, 0)\n"
"")
        self.TxtAvg2_2.setObjectName("TxtAvg2_2")
        self.TxtAvg_2 = QtWidgets.QLabel(Form)
        self.TxtAvg_2.setGeometry(QtCore.QRect(580, 420, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.TxtAvg_2.setFont(font)
        self.TxtAvg_2.setStyleSheet("\n"
"")
        self.TxtAvg_2.setObjectName("TxtAvg_2")
        self.TxtAvg1_2 = QtWidgets.QLabel(Form)
        self.TxtAvg1_2.setGeometry(QtCore.QRect(650, 420, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.TxtAvg1_2.setFont(font)
        self.TxtAvg1_2.setStyleSheet("\n"
"")
        self.TxtAvg1_2.setObjectName("TxtAvg1_2")
        self.TxtDes1_2 = QtWidgets.QLabel(Form)
        self.TxtDes1_2.setGeometry(QtCore.QRect(650, 440, 41, 20))
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
        self.buttonBox = QtWidgets.QDialogButtonBox(self.widget)
        self.buttonBox.setGeometry(QtCore.QRect(40, 510, 51, 31))
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
        self.cBoxGrp1 = QtWidgets.QComboBox(self.widget)
        self.cBoxGrp1.setGeometry(QtCore.QRect(50, 180, 141, 22))
        self.cBoxGrp1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cBoxGrp1.setObjectName("cBoxGrp1")
        self.cBoxGrp2 = QtWidgets.QComboBox(self.widget)
        self.cBoxGrp2.setGeometry(QtCore.QRect(220, 180, 141, 22))
        self.cBoxGrp2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cBoxGrp2.setObjectName("cBoxGrp2")
        self.TxtHelMinD = QtWidgets.QLabel(Form)
        self.TxtHelMinD.setGeometry(QtCore.QRect(600, 230, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.TxtHelMinD.setFont(font)
        self.TxtHelMinD.setStyleSheet("color:rgb(0, 0, 0)\n"
"")
        self.TxtHelMinD.setObjectName("TxtHelMinD")
        self.TxtSubMaxE_2 = QtWidgets.QLabel(Form)
        self.TxtSubMaxE_2.setGeometry(QtCore.QRect(600, 280, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.TxtSubMaxE_2.setFont(font)
        self.TxtSubMaxE_2.setStyleSheet("")
        self.TxtSubMaxE_2.setObjectName("TxtSubMaxE_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Group Comparison"))
        self.txtGlobalComp.setText(_translate("Form", "Comparation of Global Parameters Of The Graph:"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("Form", "Avarage Shortest Path Length:"))
        item = self.listWidget.item(1)
        item.setText(_translate("Form", "Density:"))
        item = self.listWidget.item(2)
        item.setText(_translate("Form", "Modularity:"))
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
        self.TxtMod.setText(_translate("Form", "Txt"))
        self.TxtDes.setText(_translate("Form", "Txt"))
        self.TxtAvg.setText(_translate("Form", "Txt"))
        self.BtnLocal.setText(_translate("Form", "Local Parameters Explaining"))
        self.txtGlobHeaSub.setText(_translate("Form", "Group1      Group2      Diff"))
        self.TxtMod1.setText(_translate("Form", "Txt"))
        self.TxtDes1.setText(_translate("Form", "Txt"))
        self.TxtAvg1.setText(_translate("Form", "Txt"))
        self.TxtAvg2.setText(_translate("Form", "Txt"))
        self.TxtMod2.setText(_translate("Form", "Txt"))
        self.TxtDes3.setText(_translate("Form", "Txt"))
        __sortingEnabled = self.listWidget_5.isSortingEnabled()
        self.listWidget_5.setSortingEnabled(False)
        item = self.listWidget_5.item(0)
        item.setText(_translate("Form", "Min Degree:"))
        item = self.listWidget_5.item(1)
        item.setText(_translate("Form", "Max Degree:"))
        item = self.listWidget_5.item(2)
        item.setText(_translate("Form", "Min Efficiency:"))
        item = self.listWidget_5.item(3)
        item.setText(_translate("Form", "Max Efficiency:"))
        self.listWidget_5.setSortingEnabled(__sortingEnabled)
        self.txtGlobHeaSub_2.setText(_translate("Form", "Group1               Group2"))
        self.TxtSHealMinE.setText(_translate("Form", "Txt"))
        self.TxtHelMaxD.setText(_translate("Form", "Txt"))
        self.TxtSubMinE_2.setText(_translate("Form", "Txt"))
        self.TxtSubMinD.setText(_translate("Form", "Txt"))
        self.TxtSubMaxD.setText(_translate("Form", "Txt"))
        self.TxtSubMaxE.setText(_translate("Form", "Txt"))
        self.txtGlobHeaSub_3.setText(_translate("Form", "Group1           Group2           Diff"))
        self.TxtDes_2.setText(_translate("Form", "Txt"))
        self.TxtDes3_2.setText(_translate("Form", "Txt"))
        self.TxtAvg2_2.setText(_translate("Form", "Txt"))
        self.TxtAvg_2.setText(_translate("Form", "Txt"))
        self.TxtAvg1_2.setText(_translate("Form", "Txt"))
        self.TxtDes1_2.setText(_translate("Form", "Txt"))
        self.txtCompare_3.setText(_translate("Form", "Select Groups to compare:"))
        self.txtCompare1.setText(_translate("Form", "Group 1"))
        self.txtResearch.setText(_translate("Form", "Choose Research:"))
        self.txtCompare2.setText(_translate("Form", "Group 2"))
        self.TxtHelMinD.setText(_translate("Form", "Txt"))
        self.TxtSubMaxE_2.setText(_translate("Form", "Txt"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
