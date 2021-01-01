# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EditResearchScreen.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from SearchResearchScreen import Ui_ResearchMenu
from Research import Research


class Ui_EditNewResearch(object):
    def __init__(self,res):
        self.resName = res[0]
        self.description = res[1]
        self.groups = res[2]
        self.conditions = res[3]
        print("inside edit research")
    def setupUi(self, EditNewResearch):
        EditNewResearch.setObjectName("EditNewResearch")
        EditNewResearch.resize(834, 506)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("brainPic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        EditNewResearch.setWindowIcon(icon)
        self.lineReserchName = QtWidgets.QLineEdit(EditNewResearch)
        self.lineReserchName.setGeometry(QtCore.QRect(140, 100, 131, 20))
        self.lineReserchName.setText("")
        self.lineReserchName.setObjectName("lineReserchName")
        self.labelResName = QtWidgets.QLabel(EditNewResearch)
        self.labelResName.setGeometry(QtCore.QRect(40, 100, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.labelResName.setFont(font)
        self.labelResName.setObjectName("labelResName")
        self.labelGroup = QtWidgets.QLabel(EditNewResearch)
        self.labelGroup.setGeometry(QtCore.QRect(300, 100, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.labelGroup.setFont(font)
        self.labelGroup.setObjectName("labelGroup")
        self.spinBoxDSec = QtWidgets.QSpinBox(EditNewResearch)
        self.spinBoxDSec.setGeometry(QtCore.QRect(160, 330, 61, 22))
        self.spinBoxDSec.setObjectName("spinBoxDSec")
        self.labelConditions = QtWidgets.QLabel(EditNewResearch)
        self.labelConditions.setGeometry(QtCore.QRect(530, 100, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.labelConditions.setFont(font)
        self.labelConditions.setObjectName("labelConditions")
        self.labelDesc = QtWidgets.QLabel(EditNewResearch)
        self.labelDesc.setGeometry(QtCore.QRect(40, 170, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.labelDesc.setFont(font)
        self.labelDesc.setObjectName("labelDesc")
        self.labelDSection = QtWidgets.QLabel(EditNewResearch)
        self.labelDSection.setGeometry(QtCore.QRect(50, 330, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.labelDSection.setFont(font)
        self.labelDSection.setObjectName("labelDSection")
        self.labelTreshold = QtWidgets.QLabel(EditNewResearch)
        self.labelTreshold.setGeometry(QtCore.QRect(50, 370, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.labelTreshold.setFont(font)
        self.labelTreshold.setObjectName("labelTreshold")
        self.doubleBoxTreshold = QtWidgets.QDoubleSpinBox(EditNewResearch)
        self.doubleBoxTreshold.setGeometry(QtCore.QRect(160, 370, 62, 22))
        self.doubleBoxTreshold.setObjectName("doubleBoxTreshold")
        self.pushButton = QtWidgets.QPushButton(EditNewResearch)
        self.pushButton.setGeometry(QtCore.QRect(230, 330, 21, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
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
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(EditNewResearch)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 370, 21, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
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
        self.pushButton_2.setObjectName("pushButton_2")
        self.labelCHarge = QtWidgets.QLabel(EditNewResearch)
        self.labelCHarge.setGeometry(QtCore.QRect(290, 330, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.labelCHarge.setFont(font)
        self.labelCHarge.setObjectName("labelCHarge")
        self.lineEditCharge = QtWidgets.QLineEdit(EditNewResearch)
        self.lineEditCharge.setGeometry(QtCore.QRect(430, 330, 131, 20))
        self.lineEditCharge.setText("")
        self.lineEditCharge.setObjectName("lineEditCharge")
        self.txtResearcher = QtWidgets.QLabel(EditNewResearch)
        self.txtResearcher.setGeometry(QtCore.QRect(30, 30, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.txtResearcher.setFont(font)
        self.txtResearcher.setObjectName("txtResearcher")
        self.line = QtWidgets.QFrame(EditNewResearch)
        self.line.setGeometry(QtCore.QRect(30, 40, 211, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.textDesc = QtWidgets.QTextEdit(EditNewResearch)
        self.textDesc.setGeometry(QtCore.QRect(160, 170, 321, 131))
        self.textDesc.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.textDesc.setObjectName("textDesc")
        self.txtResearcher_2 = QtWidgets.QLabel(EditNewResearch)
        self.txtResearcher_2.setGeometry(QtCore.QRect(110, 30, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.txtResearcher_2.setFont(font)
        self.txtResearcher_2.setObjectName("txtResearcher_2")
        self.BrainPic_3 = QtWidgets.QLabel(EditNewResearch)
        self.BrainPic_3.setGeometry(QtCore.QRect(740, 10, 81, 81))
        self.BrainPic_3.setText("")
        self.BrainPic_3.setPixmap(QtGui.QPixmap("logo2.png"))
        self.BrainPic_3.setObjectName("BrainPic_3")
        self.TxtGroups = QtWidgets.QLineEdit(EditNewResearch)
        self.TxtGroups.setGeometry(QtCore.QRect(360, 100, 141, 20))
        self.TxtGroups.setText("")
        self.TxtGroups.setObjectName("TxtGroups")
        self.TxtCond = QtWidgets.QLineEdit(EditNewResearch)
        self.TxtCond.setGeometry(QtCore.QRect(610, 100, 161, 20))
        self.TxtCond.setText("")
        self.TxtCond.setObjectName("TxtCond")
        self.SaveButton = QtWidgets.QPushButton(EditNewResearch)
        self.SaveButton.setGeometry(QtCore.QRect(640, 460, 75, 23))
        self.SaveButton.setObjectName("SaveButton")
        self.CanButton = QtWidgets.QPushButton(EditNewResearch)
        self.CanButton.setGeometry(QtCore.QRect(720, 460, 75, 23))
        self.CanButton.setObjectName("CanButton")

        self.retranslateUi(EditNewResearch)
        QtCore.QMetaObject.connectSlotsByName(EditNewResearch)

        # ------------------------ Added Code ------------------------ #
        self.lineReserchName.setText(self.resName)
        self.textDesc.setText(self.description)
        self.TxtGroups.setText(self.groups)
        self.TxtCond.setText(self.conditions)

        self.spinBoxDSec.setMinimum(0)
        self.spinBoxDSec.setMaximum(30)
        self.spinBoxDSec.setSingleStep(1)
        self.doubleBoxTreshold.setMinimum(0.0)
        self.doubleBoxTreshold.setMaximum(1.0)
        self.doubleBoxTreshold.setSingleStep(0.1)

        # ---------------- Call to Functions ------------- #
        self.CanButton.clicked.connect(self.btn_Cancel_clicked)
        self.SaveButton.clicked.connect(self.btn_Save_clicked)

    def retranslateUi(self, EditNewResearch):
        _translate = QtCore.QCoreApplication.translate
        EditNewResearch.setWindowTitle(_translate("EditNewResearch", "Edit Research"))
        self.labelResName.setText(_translate("EditNewResearch", "Research Name:"))
        self.labelGroup.setText(_translate("EditNewResearch", "Groups:"))
        self.labelConditions.setText(_translate("EditNewResearch", "Conditions:"))
        self.labelDesc.setText(_translate("EditNewResearch", "Description:"))
        self.labelDSection.setText(_translate("EditNewResearch", "Data Sections:"))
        self.labelTreshold.setText(_translate("EditNewResearch", "DataTreshold:"))
        self.pushButton.setToolTip(_translate("EditNewResearch", "Data Section is sequence of samples in a segment."))
        self.pushButton.setWhatsThis(_translate("EditNewResearch", "from PyQt5 import QtCore, QtGui, QtWidgets\n"
                                                                   "\n"
                                                                   "class Ui_Dialog(object):\n"
                                                                   "    def setupUi(self, Dialog):\n"
                                                                   "        Dialog.setObjectName(\"Dialog\")\n"
                                                                   "        Dialog.resize(400, 211)\n"
                                                                   "        self.label = QtWidgets.QLabel(Dialog)\n"
                                                                   "        self.label.setGeometry(QtCore.QRect(20, 70, 360, 71))\n"
                                                                   "        self.label.setObjectName(\"label\")\n"
                                                                   "\n"
                                                                   "        self.retranslateUi(Dialog)\n"
                                                                   "        QtCore.QMetaObject.connectSlotsByName(Dialog)\n"
                                                                   "\n"
                                                                   "    def retranslateUi(self, Dialog):\n"
                                                                   "        Dialog.setWindowTitle(\"Dialog\")\n"
                                                                   "        self.label.setText(\n"
                                                                   "            \"\"\"\n"
                                                                   "              <p><br><br><span style=\\\" font-size:28pt;\\\">This is a new window.</span></p>\n"
                                                                   "            \"\"\")"))
        self.pushButton.setText(_translate("EditNewResearch", "i"))
        self.pushButton_2.setToolTip(_translate("EditNewResearch",
                                                "<html><head/><body><p>The threshold will determine if the there is an edge between two electrodes.</p></body></html>"))
        self.pushButton_2.setText(_translate("EditNewResearch", "i"))
        self.labelCHarge.setText(_translate("EditNewResearch", "Researcher in Charge:"))
        self.txtResearcher.setText(_translate("EditNewResearch", "Researcher:"))
        self.txtResearcher_2.setText(_translate("EditNewResearch", "Name Of Researcher"))
        self.SaveButton.setText(_translate("EditNewResearch", "Save"))
        self.CanButton.setText(_translate("EditNewResearch", "Cancel"))

        # ------------------- Functions --------------------#
    def btn_Cancel_clicked(self):
            """This function is activated when the CANCEL button is pressed,
                    it close the current window and go back to the main menu."""
            print("cancel-edit-research-clicked")
            status = False
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_ResearchMenu()
            self.ui.setupUi(self.window)
            self.window.show()
            EditNewResearch.hide()

    def btn_Save_clicked(self):
        print("save-edit-research-clicked")
        research = Research('','','','','','','')
        print(self.TxtGroups.text())
        res_array = [self.TxtGroups.text(), self.TxtCond.text(), self.textDesc.toPlainText(), str(self.spinBoxDSec.value()), str(self.doubleBoxTreshold.value()), self.lineEditCharge.text()]
        research.update_JSON(self.lineReserchName.text(),res_array)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EditNewResearch = QtWidgets.QWidget()
    ui = Ui_EditNewResearch()
    ui.setupUi(EditNewResearch)
    EditNewResearch.show()
    sys.exit(app.exec_())
