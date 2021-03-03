# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddNewResearchScreen.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!



from PyQt5 import QtCore, QtGui, QtWidgets
from results import results
from Research import Research



class Ui_AddNewResearch(object):
    def setupUi(self, AddNewResearch):
        AddNewResearch.setObjectName("AddNewResearch")
        AddNewResearch.resize(834, 506)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("brainPic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AddNewResearch.setWindowIcon(icon)
        self.lineReserchName = QtWidgets.QLineEdit(AddNewResearch)
        self.lineReserchName.setGeometry(QtCore.QRect(160, 100, 131, 20))
        self.lineReserchName.setText("")
        self.lineReserchName.setObjectName("lineReserchName")
        self.labelResName = QtWidgets.QLabel(AddNewResearch)
        self.labelResName.setGeometry(QtCore.QRect(40, 100, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.labelResName.setFont(font)
        self.labelResName.setObjectName("labelResName")
        self.labelGroup = QtWidgets.QLabel(AddNewResearch)
        self.labelGroup.setGeometry(QtCore.QRect(310, 100, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.labelGroup.setFont(font)
        self.labelGroup.setObjectName("labelGroup")
        self.spinBoxDSec = QtWidgets.QSpinBox(AddNewResearch)
        self.spinBoxDSec.setGeometry(QtCore.QRect(160, 330, 61, 22))
        self.spinBoxDSec.setObjectName("spinBoxDSec")
        self.labelConditions = QtWidgets.QLabel(AddNewResearch)
        self.labelConditions.setGeometry(QtCore.QRect(540, 100, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.labelConditions.setFont(font)
        self.labelConditions.setObjectName("labelConditions")
        self.labelDesc = QtWidgets.QLabel(AddNewResearch)
        self.labelDesc.setGeometry(QtCore.QRect(40, 170, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.labelDesc.setFont(font)
        self.labelDesc.setObjectName("labelDesc")
        self.labelDSection = QtWidgets.QLabel(AddNewResearch)
        self.labelDSection.setGeometry(QtCore.QRect(50, 330, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.labelDSection.setFont(font)
        self.labelDSection.setObjectName("labelDSection")
        self.labelTreshold = QtWidgets.QLabel(AddNewResearch)
        self.labelTreshold.setGeometry(QtCore.QRect(50, 370, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.labelTreshold.setFont(font)
        self.labelTreshold.setObjectName("labelTreshold")
        self.doubleBoxTreshold = QtWidgets.QDoubleSpinBox(AddNewResearch)
        self.doubleBoxTreshold.setGeometry(QtCore.QRect(160, 370, 62, 22))
        self.doubleBoxTreshold.setObjectName("doubleBoxTreshold")
        self.pushButton = QtWidgets.QPushButton(AddNewResearch)
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
        self.pushButton_2 = QtWidgets.QPushButton(AddNewResearch)
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
        self.labelCHarge = QtWidgets.QLabel(AddNewResearch)
        self.labelCHarge.setGeometry(QtCore.QRect(290, 330, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.labelCHarge.setFont(font)
        self.labelCHarge.setObjectName("labelCHarge")
        self.lineEditCharge = QtWidgets.QLineEdit(AddNewResearch)
        self.lineEditCharge.setGeometry(QtCore.QRect(440, 330, 131, 20))
        self.lineEditCharge.setText("")
        self.lineEditCharge.setObjectName("lineEditCharge")
        self.txtResearcher = QtWidgets.QLabel(AddNewResearch)
        self.txtResearcher.setGeometry(QtCore.QRect(30, 30, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.txtResearcher.setFont(font)
        self.txtResearcher.setObjectName("txtResearcher")
        self.line = QtWidgets.QFrame(AddNewResearch)
        self.line.setGeometry(QtCore.QRect(30, 40, 211, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.textDesc = QtWidgets.QTextEdit(AddNewResearch)
        self.textDesc.setGeometry(QtCore.QRect(160, 170, 321, 131))
        self.textDesc.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.textDesc.setObjectName("textDesc")
        self.txtResearcher_2 = QtWidgets.QLabel(AddNewResearch)
        self.txtResearcher_2.setGeometry(QtCore.QRect(110, 30, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.txtResearcher_2.setFont(font)
        self.txtResearcher_2.setObjectName("txtResearcher_2")
        self.BrainPic_3 = QtWidgets.QLabel(AddNewResearch)
        self.BrainPic_3.setGeometry(QtCore.QRect(740, 10, 81, 81))
        self.BrainPic_3.setText("")
        self.BrainPic_3.setPixmap(QtGui.QPixmap("logo2.png"))
        self.BrainPic_3.setObjectName("BrainPic_3")
        self.TxtGroups = QtWidgets.QLineEdit(AddNewResearch)
        self.TxtGroups.setGeometry(QtCore.QRect(380, 100, 141, 20))
        self.TxtGroups.setText("")
        self.TxtGroups.setObjectName("TxtGroups")
        self.TxtCond = QtWidgets.QLineEdit(AddNewResearch)
        self.TxtCond.setGeometry(QtCore.QRect(630, 100, 161, 20))
        self.TxtCond.setText("")
        self.TxtCond.setObjectName("TxtCond")
        self.labelinfo = QtWidgets.QLabel(AddNewResearch)
        self.labelinfo.setGeometry(QtCore.QRect(320, 120, 371, 20))
        self.labelinfo.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 75 8pt \"MS Shell Dlg 2\";")
        self.labelinfo.setObjectName("labelinfo")
        self.SaveButton = QtWidgets.QPushButton(AddNewResearch)
        self.SaveButton.setGeometry(QtCore.QRect(640, 460, 75, 23))
        self.SaveButton.setObjectName("SaveButton")
        self.CanButton = QtWidgets.QPushButton(AddNewResearch)
        self.CanButton.setGeometry(QtCore.QRect(720, 460, 75, 23))
        self.CanButton.setObjectName("CanButton")

        self.retranslateUi(AddNewResearch)
        QtCore.QMetaObject.connectSlotsByName(AddNewResearch)
        # ------------------------- Added Code ---------------------------- #
        self.spinBoxDSec.setMinimum(0)
        self.spinBoxDSec.setMaximum(30)
        self.spinBoxDSec.setSingleStep(1)
        self.doubleBoxTreshold.setMinimum(0.0)
        self.doubleBoxTreshold.setMaximum(1.0)
        self.doubleBoxTreshold.setSingleStep(0.1)
        # ------------------------------- Call to Functions -------------------------------------- #
        self.SaveButton.clicked.connect(self.btn_Save_new_research_clicked)
        self.CanButton.clicked.connect(self.btn_Cancel_clicked)

    def retranslateUi(self, AddNewResearch):
            _translate = QtCore.QCoreApplication.translate
            AddNewResearch.setWindowTitle(_translate("AddNewResearch", "Add New Research"))
            self.labelResName.setText(_translate("AddNewResearch", "* Research Name:"))
            self.labelGroup.setText(_translate("AddNewResearch", "* Groups:"))
            self.labelConditions.setText(_translate("AddNewResearch", "* Conditions:"))
            self.labelDesc.setText(_translate("AddNewResearch", "* Description:"))
            self.labelDSection.setText(_translate("AddNewResearch", "* Data Sections:"))
            self.labelTreshold.setText(_translate("AddNewResearch", "* DataTreshold:"))
            self.pushButton.setToolTip(
                _translate("AddNewResearch", "Data Section is sequence of samples in a segment."))
            self.pushButton.setWhatsThis(_translate("AddNewResearch", "from PyQt5 import QtCore, QtGui, QtWidgets\n"
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
            self.pushButton.setText(_translate("AddNewResearch", "i"))
            self.pushButton_2.setToolTip(_translate("AddNewResearch",
                                                    "<html><head/><body><p>The threshold will determine if the there is an edge between two electrodes.</p></body></html>"))
            self.pushButton_2.setText(_translate("AddNewResearch", "i"))
            self.labelCHarge.setText(_translate("AddNewResearch", "* Researcher in Charge:"))
            self.txtResearcher.setText(_translate("AddNewResearch", "Researcher:"))
            self.txtResearcher_2.setText(_translate("AddNewResearch", "Name Of Researcher"))
            self.labelinfo.setText(_translate("AddNewResearch",
                                              "The types of groups / conditions must be separated by the character \",\""))
            self.SaveButton.setText(_translate("AddNewResearch", "Save"))
            self.CanButton.setText(_translate("AddNewResearch", "Cancel"))

        # -------------------------------------- Functions ----------------------------------------- #

    # Button New Patient - add a patient name and the results, create the correlation matrix and finally the binary matrix and saves it as a csv file
    def btn_New_Patient_clicked(self):
        """This function is called when the ADD PATIENT button is pressed.
                            :param value: research name combo-box value.
                            :type value: String.
                            :return value: NONE.
                            """
        print("log - New Parinent - clicked")  # we will just print clicked when the button is pressed
        data_section = self.spinBoxDSec.value()
        treshold = self.doubleBoxTreshold.value()
        print(data_section," - data section")
        patient_result = results("Uri")

        res = patient_result.data_section(data_section)
        resu_corr = patient_result.correlation_matrix(res)
        patient_result.binary_matrix(resu_corr, treshold)


    def btn_Save_new_research_clicked(self):
        """This function is activated when the SAVE button is pressed, it checks if all the obligatory field have been filled and if so saves
                research details in the system.
                          :param self: components data.
                          :type self: each component has his unique type
                          :return: NONE
                          """
        print("save-new-research clicked")
        if ((self.lineReserchName.text()=='') or (self.TxtGroups.text()=='') or (self.TxtCond.text()=='') or (self.textDesc.toPlainText()=='') or (str(self.spinBoxDSec.value())=='0') or (str(self.doubleBoxTreshold.value())=='0.0') or (self.lineEditCharge.text()=='')):
            print("some fields are missing")
            """Handle when an error occurs
            Show the error in an error message window.
            """
            em = QtWidgets.QErrorMessage()
            em.setWindowTitle("Missing values")
            em.showMessage("Some obligatory field are missing, please fill all the values.")
            em.exec_()
        else:
            research = Research(self.lineReserchName.text(), self.TxtGroups.text(), self.TxtCond.text(), self.textDesc.toPlainText(), str(self.spinBoxDSec.value()), str(self.doubleBoxTreshold.value()), self.lineEditCharge.text())
            print(research)
            research.save_in_JSON()
            em = QtWidgets.QErrorMessage()
            em.setWindowTitle("Research Saved!")
            em.showMessage("Research saved:" + "\n ReserchName: " + self.lineReserchName.text() + "\n Groups: " + self.TxtGroups.text() + "\n Conditions: " + self.TxtCond.text() + "\n Description: " + self.textDesc.toPlainText() + "\n Data section: " + str(self.spinBoxDSec.value()) + "\n Treshold: " + str(self.doubleBoxTreshold.value()) + "\n Researcher in charge: " + self.lineEditCharge.text())

            returnValue = em.exec_()
            if (returnValue == 1):
                """ Clear labels """
                self.lineReserchName.clear()
                self.TxtGroups.clear()
                self.TxtCond.clear()
                self.textDesc.clear()
                self.spinBoxDSec.setValue(0)
                self.doubleBoxTreshold.setValue(0.0)
                self.lineEditCharge.clear()

    def btn_Cancel_clicked(self):
        """This function is activated when the CANCEL button is pressed,
                it close the current window and go back to the main menu."""
        from MainMenu import Ui_MainWindow
        print("cancel-new-research-clicked")
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        self.AddNewResearch.hide()






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddNewResearch = QtWidgets.QWidget()
    ui = Ui_AddNewResearch()
    ui.setupUi(AddNewResearch)
    AddNewResearch.show()
    sys.exit(app.exec_())