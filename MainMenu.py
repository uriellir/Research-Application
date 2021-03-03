# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainMenu.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(838, 586)
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        MainWindow.setFont(font)
        MainWindow.setFocusPolicy(QtCore.Qt.ClickFocus)
        MainWindow.setAcceptDrops(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("brainPic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.TitleLable = QtWidgets.QLabel(self.centralwidget)
        self.TitleLable.setGeometry(QtCore.QRect(100, 30, 611, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.TitleLable.setFont(font)
        self.TitleLable.setObjectName("TitleLable")
        self.BrainPic = QtWidgets.QLabel(self.centralwidget)
        self.BrainPic.setGeometry(QtCore.QRect(30, 110, 781, 221))
        self.BrainPic.setText("")
        self.BrainPic.setPixmap(QtGui.QPixmap("brain.png"))
        self.BrainPic.setObjectName("BrainPic")
        self.BtnNewRes = QtWidgets.QPushButton(self.centralwidget)
        self.BtnNewRes.setGeometry(QtCore.QRect(350, 350, 131, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BtnNewRes.sizePolicy().hasHeightForWidth())
        self.BtnNewRes.setSizePolicy(sizePolicy)
        self.BtnNewRes.setSizeIncrement(QtCore.QSize(0, 0))
        self.BtnNewRes.setBaseSize(QtCore.QSize(10, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.BtnNewRes.setFont(font)
        self.BtnNewRes.setStyleSheet("QPushButton {\n"
"    color: #323;\n"
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
        self.BtnNewRes.setAutoDefault(True)
        self.BtnNewRes.setDefault(True)
        self.BtnNewRes.setObjectName("BtnNewRes")
        self.BtnNewPat = QtWidgets.QPushButton(self.centralwidget)
        self.BtnNewPat.setGeometry(QtCore.QRect(270, 400, 131, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BtnNewPat.sizePolicy().hasHeightForWidth())
        self.BtnNewPat.setSizePolicy(sizePolicy)
        self.BtnNewPat.setSizeIncrement(QtCore.QSize(0, 0))
        self.BtnNewPat.setBaseSize(QtCore.QSize(10, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.BtnNewPat.setFont(font)
        self.BtnNewPat.setStyleSheet("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
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
        self.BtnNewPat.setAutoDefault(True)
        self.BtnNewPat.setDefault(True)
        self.BtnNewPat.setObjectName("BtnNewPat")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(120, 450, 581, 71))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"selection-color: rgb(255, 170, 255);\n"
"gridline-color: rgb(85, 255, 127);")
        self.frame.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.BtnGroupCom = QtWidgets.QPushButton(self.frame)
        self.BtnGroupCom.setGeometry(QtCore.QRect(420, 20, 151, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BtnGroupCom.sizePolicy().hasHeightForWidth())
        self.BtnGroupCom.setSizePolicy(sizePolicy)
        self.BtnGroupCom.setSizeIncrement(QtCore.QSize(0, 0))
        self.BtnGroupCom.setBaseSize(QtCore.QSize(10, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.BtnGroupCom.setFont(font)
        self.BtnGroupCom.setStyleSheet("QPushButton {\n"
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
        self.BtnGroupCom.setAutoDefault(True)
        self.BtnGroupCom.setDefault(True)
        self.BtnGroupCom.setObjectName("BtnGroupCom")
        self.BtnCondComp = QtWidgets.QPushButton(self.frame)
        self.BtnCondComp.setGeometry(QtCore.QRect(210, 20, 181, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BtnCondComp.sizePolicy().hasHeightForWidth())
        self.BtnCondComp.setSizePolicy(sizePolicy)
        self.BtnCondComp.setSizeIncrement(QtCore.QSize(0, 0))
        self.BtnCondComp.setBaseSize(QtCore.QSize(10, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.BtnCondComp.setFont(font)
        self.BtnCondComp.setStyleSheet("QPushButton {\n"
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
        self.BtnCondComp.setAutoDefault(True)
        self.BtnCondComp.setDefault(True)
        self.BtnCondComp.setObjectName("BtnCondComp")
        self.BtnPatCom = QtWidgets.QPushButton(self.frame)
        self.BtnPatCom.setGeometry(QtCore.QRect(10, 20, 171, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BtnPatCom.sizePolicy().hasHeightForWidth())
        self.BtnPatCom.setSizePolicy(sizePolicy)
        self.BtnPatCom.setSizeIncrement(QtCore.QSize(0, 0))
        self.BtnPatCom.setBaseSize(QtCore.QSize(10, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.BtnPatCom.setFont(font)
        self.BtnPatCom.setStyleSheet("QPushButton {\n"
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
        self.BtnPatCom.setAutoDefault(True)
        self.BtnPatCom.setDefault(True)
        self.BtnPatCom.setObjectName("BtnPatCom")
        self.BrainPic_2 = QtWidgets.QLabel(self.centralwidget)
        self.BrainPic_2.setGeometry(QtCore.QRect(750, 0, 81, 81))
        self.BrainPic_2.setText("")
        self.BrainPic_2.setPixmap(QtGui.QPixmap("logo.png"))
        self.BrainPic_2.setObjectName("BrainPic_2")
        self.BtnPetResult = QtWidgets.QPushButton(self.centralwidget)
        self.BtnPetResult.setGeometry(QtCore.QRect(430, 400, 131, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BtnPetResult.sizePolicy().hasHeightForWidth())
        self.BtnPetResult.setSizePolicy(sizePolicy)
        self.BtnPetResult.setSizeIncrement(QtCore.QSize(0, 0))
        self.BtnPetResult.setBaseSize(QtCore.QSize(10, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.BtnPetResult.setFont(font)
        self.BtnPetResult.setStyleSheet("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
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
        self.BtnPetResult.setAutoDefault(True)
        self.BtnPetResult.setDefault(True)
        self.BtnPetResult.setObjectName("BtnPetResult")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 838, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # ---------------------- Call to Functions ----------------------------
        self.BtnNewRes.clicked.connect(self.research_menu_clicked)
        self.BtnNewPat.clicked.connect(self.add_new_patient_clicked)
        self.BtnPetResult.clicked.connect(self.patient_result_screen_clicked)
        self.BtnPatCom.clicked.connect(self.comarison_patients_clicked)
        self.BtnCondComp.clicked.connect(self.comarison_conditions_clicked)
        self.BtnGroupCom.clicked.connect(self.group_conditions_clicked)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Main Menu"))
        self.TitleLable.setText(_translate("MainWindow", "Analysis of Brain Connectivity Using Methods \n"
                                                         "                of fNIRS And Graph Theory"))
        self.BtnNewRes.setText(_translate("MainWindow", " Research Menu"))
        self.BtnNewPat.setText(_translate("MainWindow", "Add New Patient"))
        self.BtnGroupCom.setText(_translate("MainWindow", "Comparison of Groups"))
        self.BtnCondComp.setText(_translate("MainWindow", "Comparison of Conditions"))
        self.BtnPatCom.setText(_translate("MainWindow", "Comparison of Patients "))
        self.BtnPetResult.setText(_translate("MainWindow", "Patient Result"))

# ------------------------ Functions ----------------------------------
    def research_menu_clicked(self):
        """This function is activated when the RESEARCH MENU button is pressed,
                it close the current window and go to the research menu screen."""
        print("research-menu-clicked")
        from SearchResearchScreen import Ui_ResearchMenu
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ResearchMenu()
        self.ui.setupUi(self.window)
        self.window.show()
        # MainWindow.hide()

    def add_new_patient_clicked(self):
        """This function is activated when the ADD NEW PATIENT button is pressed,
                it close the current window and go to the add new patient screen."""
        print("research-menu-clicked")
        from AddNewPatient import Ui_Form
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()
        # MainWindow.hide()

    def patient_result_screen_clicked(self):
        """This function is activated when the PATIENT RESULT button is pressed,
                it close the current window and go to the patient result screen."""
        print("research-menu-clicked")
        from PatientResultScreen import Ui_Form
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()
        # MainWindow.hide()

    def comarison_patients_clicked(self):
        """This function is activated when the PATIENT RESULT button is pressed,
                it close the current window and go to the patient result screen."""
        print("research-menu-clicked")
        from PatientsComparisonScreen import Ui_Form
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()
        # MainWindow.hide()

    def comarison_conditions_clicked(self):
        """This function is activated when the PATIENT RESULT button is pressed,
                it close the current window and go to the patient result screen."""
        print("research-menu-clicked")
        from ConditionComparison import Ui_Form
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()
        # MainWindow.hide()

    def group_conditions_clicked(self):
        """This function is activated when the PATIENT RESULT button is pressed,
                it close the current window and go to the patient result screen."""
        print("research-menu-clicked")
        from GroupComparisonScreen import Ui_Form
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()
        # MainWindow.hide()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
