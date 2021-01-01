# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddNewPatient.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from MainMenu import Ui_MainWindow
import tkinter
import tkinter.filedialog as fd
from Patient import Patient
from Research import Research


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(615, 315)
        font = QtGui.QFont()
        font.setPointSize(7)
        Form.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("brainPic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.labelFullName = QtWidgets.QLabel(Form)
        self.labelFullName.setGeometry(QtCore.QRect(60, 100, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.labelFullName.setFont(font)
        self.labelFullName.setObjectName("labelFullName")
        self.txtResearcher = QtWidgets.QLabel(Form)
        self.txtResearcher.setGeometry(QtCore.QRect(30, 30, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.txtResearcher.setFont(font)
        self.txtResearcher.setObjectName("txtResearcher")
        self.PatientID = QtWidgets.QLineEdit(Form)
        self.PatientID.setGeometry(QtCore.QRect(170, 70, 171, 20))
        self.PatientID.setText("")
        self.PatientID.setObjectName("PatientID")
        self.BtnBack = QtWidgets.QPushButton(Form)
        self.BtnBack.setGeometry(QtCore.QRect(30, 270, 75, 23))
        self.BtnBack.setObjectName("BtnBack")
        self.BrainPic_3 = QtWidgets.QLabel(Form)
        self.BrainPic_3.setGeometry(QtCore.QRect(520, 10, 81, 81))
        self.BrainPic_3.setText("")
        self.BrainPic_3.setPixmap(QtGui.QPixmap("logo2.png"))
        self.BrainPic_3.setObjectName("BrainPic_3")
        self.PatName = QtWidgets.QLineEdit(Form)
        self.PatName.setGeometry(QtCore.QRect(170, 100, 171, 20))
        self.PatName.setText("")
        self.PatName.setObjectName("PatName")
        self.LblGroup = QtWidgets.QLabel(Form)
        self.LblGroup.setGeometry(QtCore.QRect(60, 160, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.LblGroup.setFont(font)
        self.LblGroup.setObjectName("LblGroup")
        self.labelID = QtWidgets.QLabel(Form)
        self.labelID.setGeometry(QtCore.QRect(60, 70, 21, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.labelID.setFont(font)
        self.labelID.setObjectName("labelID")
        self.CBoxPatGroup = QtWidgets.QComboBox(Form)
        self.CBoxPatGroup.setGeometry(QtCore.QRect(170, 160, 171, 22))
        self.CBoxPatGroup.setObjectName("CBoxPatGroup")
        self.LblPath = QtWidgets.QLabel(Form)
        self.LblPath.setGeometry(QtCore.QRect(60, 210, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.LblPath.setFont(font)
        self.LblPath.setObjectName("LblPath")
        self.TxtPath = QtWidgets.QLineEdit(Form)
        self.TxtPath.setGeometry(QtCore.QRect(160, 210, 291, 20))
        self.TxtPath.setText("")
        self.TxtPath.setObjectName("TxtPath")
        self.BtnBrowser = QtWidgets.QPushButton(Form)
        self.BtnBrowser.setGeometry(QtCore.QRect(460, 210, 71, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BtnBrowser.sizePolicy().hasHeightForWidth())
        self.BtnBrowser.setSizePolicy(sizePolicy)
        self.BtnBrowser.setSizeIncrement(QtCore.QSize(0, 0))
        self.BtnBrowser.setBaseSize(QtCore.QSize(10, 0))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.BtnBrowser.setFont(font)
        self.BtnBrowser.setStyleSheet("QPushButton {\n"
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
        self.BtnBrowser.setAutoDefault(True)
        self.BtnBrowser.setDefault(True)
        self.BtnBrowser.setObjectName("BtnBrowser")
        self.BtnAddPatient = QtWidgets.QPushButton(Form)
        self.BtnAddPatient.setGeometry(QtCore.QRect(480, 270, 101, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BtnAddPatient.sizePolicy().hasHeightForWidth())
        self.BtnAddPatient.setSizePolicy(sizePolicy)
        self.BtnAddPatient.setSizeIncrement(QtCore.QSize(0, 0))
        self.BtnAddPatient.setBaseSize(QtCore.QSize(10, 0))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.BtnAddPatient.setFont(font)
        self.BtnAddPatient.setStyleSheet("QPushButton {\n"
"color: rgb(170, 0, 127);\n"
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
        self.BtnAddPatient.setAutoDefault(True)
        self.BtnAddPatient.setDefault(True)
        self.BtnAddPatient.setObjectName("BtnAddPatient")
        self.CBoxPatGroup_2 = QtWidgets.QComboBox(Form)
        self.CBoxPatGroup_2.setGeometry(QtCore.QRect(170, 130, 171, 22))
        self.CBoxPatGroup_2.setObjectName("CBoxPatGroup_2")
        self.LblGroup_2 = QtWidgets.QLabel(Form)
        self.LblGroup_2.setGeometry(QtCore.QRect(60, 130, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.LblGroup_2.setFont(font)
        self.LblGroup_2.setObjectName("LblGroup_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        # ---------------------------------Added Code -------------------------------------------- #
        self.CBoxPatGroup_2.addItem('')
        self.CBoxPatGroup.addItem('')
        research = Research("researchName","groups",'conditions','description','data_section','treshold','incharge')
        comboBox_research = list(dict.fromkeys(research.get_data_from_JSON('name')))
        self.CBoxPatGroup_2.addItems(comboBox_research)
        comoboBox_data = list(dict.fromkeys(research.get_data_from_JSON('groups')))  # Remove duplicates from list - dictionary cannot have duplicates.

        self.CBoxPatGroup.addItems(comoboBox_data)
        self.TxtPath.setEnabled(False)
        # ------------------------------- Call to Functions -------------------------------------- #
        self.BtnAddPatient.clicked.connect(self.btn_Save_new_patient_clicked)
        self.BtnBack.clicked.connect(self.btn_Back_clicked)
        self.BtnBrowser.clicked.connect(self.chooseFile)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Add New Patient"))
        self.labelFullName.setText(_translate("Form", "Full Name:"))
        self.txtResearcher.setText(_translate("Form", "Insert New Patient Details:"))
        self.BtnBack.setText(_translate("Form", "Back"))
        self.LblGroup.setText(_translate("Form", "Group:"))
        self.labelID.setText(_translate("Form", "ID:"))
        self.LblPath.setText(_translate("Form", "HDFs File Path:"))
        self.BtnBrowser.setText(_translate("Form", "Browser"))
        self.BtnAddPatient.setText(_translate("Form", "Add Patient"))
        self.LblGroup_2.setText(_translate("Form", "Research name:"))

        # -------------------------------------- Functions ----------------------------------------- #

    def btn_Save_new_patient_clicked(self):
        """This function is activated when the ADD PATIENT button is pressed, it checks if all the obligatory field have been filled and if so saves
            patient details in the system.
                      :param self: components data.
                      :type self: each component has his unique type
                      :return: NONE
                      """
        print("save-new-patient-clicked")
        if ((self.PatientID.text()=='') or (self.PatName.text()=='') or (self.CBoxPatGroup_2.currentText()=='') or (self.CBoxPatGroup.currentText()=='') or  (self.TxtPath.text()=='')):
            print("some fields are missing")
            """Handle when an error occurs
            Show the error in an error message window.
            """
            em = QtWidgets.QErrorMessage()
            em.setWindowTitle("Missing values")
            em.showMessage("Some obligatory field are missing, please fill all the values.")
            em.exec_()
        else:
            patient = Patient(self.PatientID.text(), self.PatName.text(), self.CBoxPatGroup.currentText(), self.CBoxPatGroup_2.currentText(), self.TxtPath.text())
            print(patient)
            patient.save_in_JSON() # Saves the Patient details in the Patients.json file.
            pandas_dataFrame = patient.data_section(self.TxtPath.text(),patient.get_treshold_Dsection_from_JSON(self.CBoxPatGroup_2.currentText(),'data_section')) # Needed to add data section from the RESEARCH!!!!!! Calculates the matrix based on the data section.
            correlation_matrix = patient.correlation_matrix(pandas_dataFrame) # Calculates the Correlation Matrix.
            binary_matrix = patient.binary_matrix(correlation_matrix, patient.get_treshold_Dsection_from_JSON(self.CBoxPatGroup_2.currentText(),'treshold')) # Needed to add treshold from the RESEARCH!!!!! Calculates the Binary matrix based on the treshold.
            em = QtWidgets.QErrorMessage()
            em.setWindowTitle("Patient Saved!")
            em.showMessage("Patient saved:" + "\n Patient ID: " + self.PatientID.text() + "\n Patient Name: " + self.PatName.text() + "\n Research: " + self.CBoxPatGroup_2.currentText() + "\n Group: " + self.CBoxPatGroup.currentText() + "\n File Path: " + self.TxtPath.text())
            returnValue = em.exec_()
            if (returnValue == 1):
                """ Clear labels """
                self.PatientID.clear()
                self.PatName.clear()
                self.CBoxPatGroup_2.setCurrentIndex(0)
                self.CBoxPatGroup.setCurrentIndex(0)
                self.TxtPath.clear()

    def btn_Back_clicked(self):
        """This function is activated when the BACK button is pressed,
                it close the current window and go back to the main menu."""
        print("cancel-new-research-clicked")
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        Form.hide()

    def chooseFile(self):
        """ Open a browser to choose the patient's results file"""
        print("choose file clicked")
        patient = Patient("id","full_name","group","research","file_path")
        path_file = patient.chooseFile()
        self.TxtPath.setText(path_file)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
