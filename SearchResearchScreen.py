# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SearchResearchScreen.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from Patient import Patient
from Research import Research

class Ui_ResearchMenu(object):
    def setupUi(self, ResearchMenu):
        ResearchMenu.setObjectName("ResearchMenu")
        ResearchMenu.resize(808, 579)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("brainPic.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        ResearchMenu.setWindowIcon(icon)
        self.lineReserchName = QtWidgets.QLineEdit(ResearchMenu)
        self.lineReserchName.setGeometry(QtCore.QRect(130, 60, 131, 20))
        self.lineReserchName.setText("")
        self.lineReserchName.setObjectName("lineReserchName")
        self.labelGroup = QtWidgets.QLabel(ResearchMenu)
        self.labelGroup.setGeometry(QtCore.QRect(30, 90, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.labelGroup.setFont(font)
        self.labelGroup.setObjectName("labelGroup")
        self.labelResName = QtWidgets.QLabel(ResearchMenu)
        self.labelResName.setGeometry(QtCore.QRect(30, 60, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.labelResName.setFont(font)
        self.labelResName.setObjectName("labelResName")
        self.labelDesc = QtWidgets.QLabel(ResearchMenu)
        self.labelDesc.setGeometry(QtCore.QRect(300, 60, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.labelDesc.setFont(font)
        self.labelDesc.setObjectName("labelDesc")
        self.textDesc = QtWidgets.QTextEdit(ResearchMenu)
        self.textDesc.setGeometry(QtCore.QRect(380, 60, 261, 91))
        self.textDesc.setObjectName("textDesc")
        self.comboConditions = QtWidgets.QComboBox(ResearchMenu)
        self.comboConditions.setGeometry(QtCore.QRect(130, 120, 131, 22))
        self.comboConditions.setObjectName("comboConditions")
        self.comboBoxGroups = QtWidgets.QComboBox(ResearchMenu)
        self.comboBoxGroups.setGeometry(QtCore.QRect(130, 90, 131, 22))
        self.comboBoxGroups.setObjectName("comboBoxGroups")
        self.labelConditions = QtWidgets.QLabel(ResearchMenu)
        self.labelConditions.setGeometry(QtCore.QRect(30, 120, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.labelConditions.setFont(font)
        self.labelConditions.setObjectName("labelConditions")
        self.txtResearcher = QtWidgets.QLabel(ResearchMenu)
        self.txtResearcher.setGeometry(QtCore.QRect(30, 20, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.txtResearcher.setFont(font)
        self.txtResearcher.setObjectName("txtResearcher")
        self.line = QtWidgets.QFrame(ResearchMenu)
        self.line.setGeometry(QtCore.QRect(20, 30, 331, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.BtnGo = QtWidgets.QPushButton(ResearchMenu)
        self.BtnGo.setGeometry(QtCore.QRect(30, 180, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.BtnGo.setFont(font)
        self.BtnGo.setStyleSheet("QPushButton {\n"
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
        self.BtnGo.setObjectName("BtnGo")
        self.BtnClear = QtWidgets.QPushButton(ResearchMenu)
        self.BtnClear.setGeometry(QtCore.QRect(110, 180, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.BtnClear.setFont(font)
        self.BtnClear.setStyleSheet("QPushButton {\n"
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
        self.BtnClear.setObjectName("BtnClear")
        self.line_2 = QtWidgets.QFrame(ResearchMenu)
        self.line_2.setGeometry(QtCore.QRect(30, 210, 401, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.BtnCreate = QtWidgets.QPushButton(ResearchMenu)
        self.BtnCreate.setGeometry(QtCore.QRect(30, 250, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.BtnCreate.setFont(font)
        self.BtnCreate.setStyleSheet("QPushButton {\n"
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
        self.BtnCreate.setObjectName("BtnCreate")
        self.tableWidget = QtWidgets.QTableWidget(ResearchMenu)
        self.tableWidget.setGeometry(QtCore.QRect(30, 290, 521, 241))
        self.tableWidget.setRowCount(7)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.BtnEdit2 = QtWidgets.QPushButton(ResearchMenu)
        self.BtnEdit2.setGeometry(QtCore.QRect(490, 350, 21, 23))
        self.BtnEdit2.setText("")
        icon = QtGui.QIcon.fromTheme("j")
        self.BtnEdit2.setIcon(icon)
        self.BtnEdit2.setObjectName("BtnEdit2")
        self.BtnEdit3 = QtWidgets.QPushButton(ResearchMenu)
        self.BtnEdit3.setGeometry(QtCore.QRect(490, 380, 21, 23))
        self.BtnEdit3.setText("")
        icon = QtGui.QIcon.fromTheme("j")
        self.BtnEdit3.setIcon(icon)
        self.BtnEdit3.setObjectName("BtnEdit3")
        self.BtnEdit4 = QtWidgets.QPushButton(ResearchMenu)
        self.BtnEdit4.setGeometry(QtCore.QRect(490, 410, 21, 23))
        self.BtnEdit4.setText("")
        icon = QtGui.QIcon.fromTheme("j")
        self.BtnEdit4.setIcon(icon)
        self.BtnEdit4.setObjectName("BtnEdit4")
        self.BtnEdit5 = QtWidgets.QPushButton(ResearchMenu)
        self.BtnEdit5.setGeometry(QtCore.QRect(490, 440, 21, 23))
        self.BtnEdit5.setText("")
        icon = QtGui.QIcon.fromTheme("j")
        self.BtnEdit5.setIcon(icon)
        self.BtnEdit5.setObjectName("BtnEdit5")
        self.BtnEdit1 = QtWidgets.QPushButton(ResearchMenu)
        self.BtnEdit1.setGeometry(QtCore.QRect(490, 320, 21, 23))
        self.BtnEdit1.setText("")
        icon = QtGui.QIcon.fromTheme("j")
        self.BtnEdit1.setIcon(icon)
        self.BtnEdit1.setObjectName("BtnEdit1")
        self.BtnEdit6 = QtWidgets.QPushButton(ResearchMenu)
        self.BtnEdit6.setGeometry(QtCore.QRect(490, 470, 21, 23))
        self.BtnEdit6.setText("")
        icon = QtGui.QIcon.fromTheme("j")
        self.BtnEdit6.setIcon(icon)
        self.BtnEdit6.setObjectName("BtnEdit6")
        self.BtnEdit7 = QtWidgets.QPushButton(ResearchMenu)
        self.BtnEdit7.setGeometry(QtCore.QRect(490, 500, 21, 23))
        self.BtnEdit7.setText("")
        icon = QtGui.QIcon.fromTheme("j")
        self.BtnEdit7.setIcon(icon)
        self.BtnEdit7.setObjectName("BtnEdit7")
        self.BrainPic_3 = QtWidgets.QLabel(ResearchMenu)
        self.BrainPic_3.setGeometry(QtCore.QRect(710, 10, 81, 81))
        self.BrainPic_3.setText("")
        self.BrainPic_3.setPixmap(QtGui.QPixmap("logo2.png"))
        self.BrainPic_3.setObjectName("BrainPic_3")
        self.BtnBack = QtWidgets.QPushButton(ResearchMenu)
        self.BtnBack.setGeometry(QtCore.QRect(710, 540, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.BtnBack.setFont(font)
        self.BtnBack.setStyleSheet("QPushButton {\n"
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
        self.BtnBack.setObjectName("BtnBack")

        self.retranslateUi(ResearchMenu)
        QtCore.QMetaObject.connectSlotsByName(ResearchMenu)


        # --------------- Added Code ----------------------#
        self.comboBoxGroups.addItem('')
        patient = Patient("id", "full_name", "group",'research', "file_path")
        comoboBox_data = list(dict.fromkeys(patient.get_data_from_JSON('group')))  # Remove duplicates from list - dictionary cannot have duplicates.
        self.comboBoxGroups.addItems(comoboBox_data)

        self.comboConditions.addItem('')
        research = Research('','','','','','','')
        comboBox_Con = list(dict.fromkeys(research.get_data_from_JSON('conditions')))
        self.comboConditions.addItems(comboBox_Con)

        # ---------------- Call to Functions ------------- #
        from functools import partial
        self.BtnEdit1.clicked.connect(partial(self.edit_clicked, 0))
        self.BtnEdit2.clicked.connect(partial(self.edit_clicked, 1))
        self.BtnEdit3.clicked.connect(partial(self.edit_clicked, 2))
        self.BtnEdit4.clicked.connect(partial(self.edit_clicked, 3))
        self.BtnEdit5.clicked.connect(partial(self.edit_clicked, 4))
        self.BtnEdit6.clicked.connect(partial(self.edit_clicked, 5))
        self.BtnEdit7.clicked.connect(partial(self.edit_clicked, 6))

        self.BtnGo.clicked.connect(self.search_clicked)
        self.BtnClear.clicked.connect(self.clear_clicked)
        self.BtnCreate.clicked.connect(self.create_clicked)

    def retranslateUi(self, ResearchMenu):
        _translate = QtCore.QCoreApplication.translate
        ResearchMenu.setWindowTitle(_translate("ResearchMenu", "Research Menu"))
        self.labelGroup.setText(_translate("ResearchMenu", "Groups:"))
        self.labelResName.setText(_translate("ResearchMenu", "Research Name:"))
        self.labelDesc.setText(_translate("ResearchMenu", "Description:"))
        self.labelConditions.setText(_translate("ResearchMenu", "Conditions:"))
        self.txtResearcher.setText(_translate("ResearchMenu", "Search Research"))
        self.BtnGo.setText(_translate("ResearchMenu", "Go"))
        self.BtnClear.setText(_translate("ResearchMenu", "Clear"))
        self.BtnCreate.setText(_translate("ResearchMenu", "Create"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ResearchMenu", "Research Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ResearchMenu", "Description"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("ResearchMenu", "Groups"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("ResearchMenu", "Conditions"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("ResearchMenu", "Edit"))
        self.BtnBack.setText(_translate("ResearchMenu", "Back"))

        # ----------------------- Functions -------------------------- #

    def clear_clicked(self):
        self.lineReserchName.setText('')
        self.comboBoxGroups.setCurrentIndex(0)
        self.comboConditions.setCurrentIndex(0)
        self.textDesc.setText('')

    def search_clicked(self):
        # self.tableWidget.clear()
        # All field empty
        if((self.lineReserchName.text()=='') and (self.comboBoxGroups.currentText()=='') and (self.comboConditions.currentText()=='') and (self.textDesc.toPlainText()=='')):
            em = QtWidgets.QErrorMessage()
            em.setWindowTitle("Missing values")
            em.showMessage("Some obligatory field are missing, please fill all the values.")
            em.exec_()
        else:
            research = Research('','','','','','','')
            researchs_array = research.get_data_from_JSON('name')
            names = []
            groups = []
            cond = []
            descr = []
            i = 0
            # Get research names
            if not(self.lineReserchName.text()==''):
                for res in researchs_array:
                    if (self.lineReserchName.text() in res):
                        names.append(res)
                print(names)
            # Get groups
            if not (self.comboBoxGroups.currentText()==''):
                for res_name in researchs_array:
                    if(research.is_in_key(res_name,'groups', self.comboBoxGroups.currentText())):
                        groups.append(res_name)
                print(groups)
            # Get conditions
            if not (self.comboConditions.currentText()==''):
                for res_name in researchs_array:
                    if(research.is_in_key(res_name,'conditions', self.comboConditions.currentText())):
                        cond.append(res_name)
                print(cond)
            # Get description
            if not (self.textDesc.toPlainText()==''):
                for res_name in researchs_array:
                    if(research.is_in_key(res_name,'description', self.textDesc.toPlainText())):
                        descr.append(res_name)
                print(descr)
            # Intersection of Researchs
            import functools
            input_list = [names,groups,cond,descr]
            res_to_show = functools.reduce(set.intersection, map(set, filter(len, input_list)))
            print("Intersection search:")
            print(list(res_to_show))
            for item in (list(res_to_show)):
                print(item)
                self.update_table(item,i)
                i = i+1



    def update_table(self, research, i):
        res = Research('', '', '', '', '', '', '')
        show = res.get_researchs_from_JSON(research)
        print(show)
        self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(show['name']))
        self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(show['description']))
        self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(self.list_to_string(show['groups'])))
        self.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(self.list_to_string(show['conditions'])))

    def list_to_string(self, list):
        string = []
        for item in list:
            string.append(item)
        return ",".join(string)

    def edit_clicked(self,i):
        """This function is activated when the CANCEL button is pressed,
                        it close the current window and go back to the main menu."""
        from EditResearchScreen import Ui_EditNewResearch
        # print("edit-research-clicked")
        # self.window = QtWidgets.QMainWindow()
        arr = [self.tableWidget.item(i,0).text(),self.tableWidget.item(i,1).text(),self.tableWidget.item(i,2).text(),self.tableWidget.item(i,3).text()]
        print(arr)
        # self.ui = Ui_EditNewResearch(arr)
        # self.ui.setupUi(self.window)
        # self.window.show()
        # ResearchMenu.hide()

        global status
        status = True  # This will be your global variable which will check if the window is closed or not
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_EditNewResearch(arr)
        self.ui.setupUi(self.window)
        self.window.show()
        ResearchMenu.hide()
        self.timer = QtCore.QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.checkVar)
        self.timer.start()

    def checkVar(self):
        global status
        if (status == False):
            # Show your hided window here
            self.show()
            print('checkvar '+status)

    def create_clicked(self):
        """This function is activated when the RESEARCH MENU button is pressed,
                it close the current window and go to the research menu screen."""
        print("research-menu-clicked")
        from AddNewResearchScreen import Ui_AddNewResearch
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_AddNewResearch()
        self.ui.setupUi(self.window)
        self.window.show()
        # MainWindow.hide()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ResearchMenu = QtWidgets.QWidget()
    ui = Ui_ResearchMenu()
    ui.setupUi(ResearchMenu)
    ResearchMenu.show()
    sys.exit(app.exec_())
