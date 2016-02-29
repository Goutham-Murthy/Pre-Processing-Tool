# -*- coding: utf-8 -*
from PySide import QtCore, QtGui

class UiMainWindow(object):
    def setup_gui(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(887, 329)
        MainWindow.setAcceptDrops(True)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tabTechnologies = QtGui.QWidget()
        self.tabTechnologies.setObjectName("tabTechnologies")
        self.verticalLayout = QtGui.QVBoxLayout(self.tabTechnologies)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label1 = QtGui.QLabel(self.tabTechnologies)
        self.label1.setTextFormat(QtCore.Qt.RichText)
        self.label1.setWordWrap(True)
        self.label1.setObjectName("label1")
        self.verticalLayout.addWidget(self.label1)
        self.check_box_chp = QtGui.QCheckBox(self.tabTechnologies)
        self.check_box_chp.setObjectName("check_box_chp")
        self.verticalLayout.addWidget(self.check_box_chp)
        self.check_box_boiler = QtGui.QCheckBox(self.tabTechnologies)
        self.check_box_boiler.setObjectName("check_box_boiler")
        self.verticalLayout.addWidget(self.check_box_boiler)
        self.check_box_thst = QtGui.QCheckBox(self.tabTechnologies)
        self.check_box_thst.setObjectName("check_box_thst")
        self.verticalLayout.addWidget(self.check_box_thst)
        self.check_box_solth = QtGui.QCheckBox(self.tabTechnologies)
        self.check_box_solth.setObjectName("check_box_solth")
        self.verticalLayout.addWidget(self.check_box_solth)
        self.check_box_elhe = QtGui.QCheckBox(self.tabTechnologies)
        self.check_box_elhe.setObjectName("check_box_elhe")
        self.verticalLayout.addWidget(self.check_box_elhe)
        self.check_box_pv = QtGui.QCheckBox(self.tabTechnologies)
        self.check_box_pv.setObjectName("check_box_pv")
        self.verticalLayout.addWidget(self.check_box_pv)
        self.check_box_elst = QtGui.QCheckBox(self.tabTechnologies)
        self.check_box_elst.setObjectName("check_box_elst")
        self.verticalLayout.addWidget(self.check_box_elst)
        self.tabWidget.addTab(self.tabTechnologies, "")
        self.tabFolders = QtGui.QWidget()
        self.tabFolders.setObjectName("tabFolders")
        self.gridLayout = QtGui.QGridLayout(self.tabFolders)
        self.gridLayout.setObjectName("gridLayout")
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        # Output folder
        self.label = QtGui.QLabel(self.tabFolders)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.OutputFolderLineEdit = QtGui.QLineEdit(self.tabFolders)
        self.OutputFolderLineEdit.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.OutputFolderLineEdit.setObjectName("OutputFolderLineEdit")
        self.OutputFolderLineEdit.setText("D:/aja-gmu/Simulation_Files/Output")
        self.gridLayout.addWidget(self.OutputFolderLineEdit, 1, 0, 1, 1)
        self.btnOutputBrowse = QtGui.QPushButton(self.tabFolders)
        self.btnOutputBrowse.setObjectName("btnOutputBrowse")
        self.gridLayout.addWidget(self.btnOutputBrowse, 1, 1, 1, 1)
        self.btnOutputBrowse.setSizePolicy(sizePolicy)
        self.btnOutputBrowse.setDefault(False)

        # Weather folder
        self.label_2 = QtGui.QLabel(self.tabFolders)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.WeatherDataLineEdit = QtGui.QLineEdit(self.tabFolders)
        self.WeatherDataLineEdit.setObjectName("WeatherDataLineEdit")
        self.WeatherDataLineEdit.setText("D:/aja-gmu/Simulation_Files/Wetter_Bottrop_Modelica.csv")
        sizePolicy.setHeightForWidth(self.btnOutputBrowse.sizePolicy().hasHeightForWidth())
        self.gridLayout.addWidget(self.WeatherDataLineEdit, 3, 0, 1, 1)
        self.btnWeathreBrowse = QtGui.QPushButton(self.tabFolders)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnWeathreBrowse.sizePolicy().hasHeightForWidth())
        self.btnWeathreBrowse.setSizePolicy(sizePolicy)
        self.btnWeathreBrowse.setObjectName("btnWeathreBrowse")
        self.gridLayout.addWidget(self.btnWeathreBrowse, 3, 1, 1, 1)

        # Heat Profiles
        self.label_3 = QtGui.QLabel(self.tabFolders)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.HProfileLineEdit = QtGui.QLineEdit(self.tabFolders)
        self.HProfileLineEdit.setObjectName("HProfileLineEdit")
        self.HProfileLineEdit.setText("D:/aja-gmu/Simulation_Files/Heat profiles.xlsx")
        self.gridLayout.addWidget(self.HProfileLineEdit, 5, 0, 1, 1)
        self.btnHeatprofilesBrowse = QtGui.QPushButton(self.tabFolders)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnHeatprofilesBrowse.sizePolicy().hasHeightForWidth())
        self.btnHeatprofilesBrowse.setSizePolicy(sizePolicy)
        self.btnHeatprofilesBrowse.setObjectName("btnHeatprofilesBrowse")
        self.gridLayout.addWidget(self.btnHeatprofilesBrowse, 5, 1, 1, 1)

        # El Profiles
        self.label_4 = QtGui.QLabel(self.tabFolders)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 6, 0, 1, 1)
        self.ElProfileLineEdit = QtGui.QLineEdit(self.tabFolders)
        self.ElProfileLineEdit.setObjectName("ElProfileLineEdit")
        self.ElProfileLineEdit.setText("D:/aja-gmu/Simulation_Files/Heat profiles.xlsx")
        self.gridLayout.addWidget(self.ElProfileLineEdit, 7, 0, 1, 1)
        self.btnElProfileBrowse = QtGui.QPushButton(self.tabFolders)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnElProfileBrowse.sizePolicy().hasHeightForWidth())
        self.btnElProfileBrowse.setSizePolicy(sizePolicy)
        self.btnElProfileBrowse.setObjectName("btnElProfileBrowse")
        self.gridLayout.addWidget(self.btnElProfileBrowse, 7, 1, 1, 1)
        self.rbtn_hourly_excels = QtGui.QRadioButton(self.tabFolders)
        self.rbtn_hourly_excels.setObjectName("rbtn_hourly_excels")
        self.gridLayout.addWidget(self.rbtn_hourly_excels, 8, 0, 1, 1)

        self.tabWidget.addTab(self.tabFolders, "")
        self.tabGDetails = QtGui.QWidget()
        self.tabGDetails.setObjectName("tabGDetails")
        self.gridLayout_2 = QtGui.QGridLayout(self.tabGDetails)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.labelElPrice = QtGui.QLabel(self.tabGDetails)
        self.labelElPrice.setObjectName("labelElPrice")
        self.gridLayout_2.addWidget(self.labelElPrice, 0, 0, 1, 1)

        self.lineEditElPrice = QtGui.QLineEdit(self.tabGDetails)
        self.lineEditElPrice.setObjectName("lineEditElPrice")
        self.lineEditElPrice.setText('0.26')
        self.gridLayout_2.addWidget(self.lineEditElPrice, 0, 1, 1, 1)

        self.labelElPriceUnit = QtGui.QLabel(self.tabGDetails)
        self.labelElPriceUnit.setObjectName("labelElPriceUnit")
        self.gridLayout_2.addWidget(self.labelElPriceUnit, 0, 2, 1, 1)

        self.labelGprice = QtGui.QLabel(self.tabGDetails)
        self.labelGprice.setObjectName("labelGprice")
        self.gridLayout_2.addWidget(self.labelGprice, 1, 0, 1, 1)

        self.lineEditGPrice = QtGui.QLineEdit(self.tabGDetails)
        self.lineEditGPrice.setObjectName("lineEditGPrice")
        self.gridLayout_2.addWidget(self.lineEditGPrice, 1, 1, 1, 1)
        self.lineEditGPrice.setText('0.067')

        self.labelGPriceUnit = QtGui.QLabel(self.tabGDetails)
        self.labelGPriceUnit.setObjectName("labelGPriceUnit")
        self.gridLayout_2.addWidget(self.labelGPriceUnit, 1, 2, 1, 1)

        self.labelObPeriod = QtGui.QLabel(self.tabGDetails)
        self.labelObPeriod.setObjectName("ObPeriod")
        self.gridLayout_2.addWidget(self.labelObPeriod, 2, 0, 1, 1)

        self.lineEditObPeriod = QtGui.QLineEdit(self.tabGDetails)
        self.lineEditObPeriod.setObjectName("lineEditObPeriod")
        self.gridLayout_2.addWidget(self.lineEditObPeriod, 2, 1, 1, 1)
        self.lineEditObPeriod.setText('10.0')

        self.labelObPeriodUnit = QtGui.QLabel(self.tabGDetails)
        self.labelObPeriodUnit.setObjectName("labelObPeriodUnit")
        self.gridLayout_2.addWidget(self.labelObPeriodUnit, 2, 2, 1, 1)


        self.tabWidget.addTab(self.tabGDetails, "")
        self.tabCHP = QtGui.QWidget()
        self.tabCHP.setObjectName("tabCHP")
        self.gridLayout_3 = QtGui.QGridLayout(self.tabCHP)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButtonAddCHP = QtGui.QPushButton(self.tabCHP)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonAddCHP.sizePolicy().hasHeightForWidth())
        self.pushButtonAddCHP.setSizePolicy(sizePolicy)
        self.pushButtonAddCHP.setObjectName("pushButtonAddCHP")
        self.gridLayout_3.addWidget(self.pushButtonAddCHP, 5, 0, 1, 2)

        self.labelCHPFIT = QtGui.QLabel(self.tabCHP)
        self.labelCHPFIT.setObjectName("labelCHPFIT")
        self.gridLayout_3.addWidget(self.labelCHPFIT, 3, 0, 1, 1)

        self.lineEditCHPFIT = QtGui.QLineEdit(self.tabCHP)
        self.lineEditCHPFIT.setObjectName("lineEditCHPFIT")
        self.lineEditCHPFIT.setText("0.10")
        self.gridLayout_3.addWidget(self.lineEditCHPFIT, 3, 1, 1, 1)

        self.labelCHPFITUnit = QtGui.QLabel(self.tabCHP)
        self.labelCHPFITUnit.setObjectName("labelCHPFITUnit")
        self.gridLayout_3.addWidget(self.labelCHPFITUnit, 3, 2, 1, 1)

        self.pushButtonAdvAnnuityCHP = QtGui.QPushButton(self.tabCHP)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonAdvAnnuityCHP.sizePolicy().hasHeightForWidth())
        self.pushButtonAdvAnnuityCHP.setSizePolicy(sizePolicy)
        self.pushButtonAdvAnnuityCHP.setObjectName("pushButtonAdvAnnuityCHP")
        self.gridLayout_3.addWidget(self.pushButtonAdvAnnuityCHP, 4, 0, 1, 2)
        self.radioButtonContCHP = QtGui.QRadioButton(self.tabCHP)
        self.radioButtonContCHP.setObjectName("radioButtonContCHP")
        self.gridLayout_3.addWidget(self.radioButtonContCHP, 2, 0, 1, 1)
        self.radioButtonONOFFCHP = QtGui.QRadioButton(self.tabCHP)
        self.radioButtonONOFFCHP.setObjectName("radioButtonONOFFCHP")
        self.radioButtonONOFFCHP.setChecked(True)
        self.gridLayout_3.addWidget(self.radioButtonONOFFCHP, 0, 0, 1, 1)
        self.radioButtonModCHP = QtGui.QRadioButton(self.tabCHP)
        self.radioButtonModCHP.setObjectName("radioButtonModCHP")
        self.gridLayout_3.addWidget(self.radioButtonModCHP, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tabCHP, "")
        self.tabBoiler = QtGui.QWidget()
        self.tabBoiler.setObjectName("tabBoiler")
        self.gridLayout_4 = QtGui.QGridLayout(self.tabBoiler)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pushButtonAddBoiler = QtGui.QPushButton(self.tabBoiler)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonAddBoiler.sizePolicy().hasHeightForWidth())
        self.pushButtonAddBoiler.setSizePolicy(sizePolicy)
        self.pushButtonAddBoiler.setObjectName("pushButtonAddBoiler")
        self.gridLayout_4.addWidget(self.pushButtonAddBoiler, 1, 0, 1, 2)
        self.pushButtonAdvAnnuityBoiler = QtGui.QPushButton(self.tabBoiler)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonAdvAnnuityBoiler.sizePolicy().hasHeightForWidth())
        self.pushButtonAdvAnnuityBoiler.setSizePolicy(sizePolicy)
        self.pushButtonAdvAnnuityBoiler.setObjectName("pushButtonAdvAnnuityBoiler")
        self.gridLayout_4.addWidget(self.pushButtonAdvAnnuityBoiler, 0, 0, 1, 2)
        self.tabWidget.addTab(self.tabBoiler, "")

        self.tabThSt = QtGui.QWidget()
        self.tabThSt.setObjectName("tabThSt")
        self.gridLayout_5 = QtGui.QGridLayout(self.tabThSt)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.pushButtonAdvAnnuityThSt = QtGui.QPushButton(self.tabThSt)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonAdvAnnuityThSt.sizePolicy().hasHeightForWidth())
        self.pushButtonAdvAnnuityThSt.setSizePolicy(sizePolicy)
        self.pushButtonAdvAnnuityThSt.setObjectName("pushButtonAdvAnnuityThSt")
        self.gridLayout_5.addWidget(self.pushButtonAdvAnnuityThSt, 0, 0, 1, 2)
        self.pushButtonAddThSt = QtGui.QPushButton(self.tabThSt)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonAddThSt.sizePolicy().hasHeightForWidth())
        self.pushButtonAddThSt.setSizePolicy(sizePolicy)
        self.pushButtonAddThSt.setObjectName("pushButtonAddThSt")
        self.gridLayout_5.addWidget(self.pushButtonAddThSt, 1, 0, 1, 2)
        self.tabWidget.addTab(self.tabThSt, "")

        # ==============================================================================================================
        # Solar thermal tab
        self.tabSolTh = QtGui.QWidget()
        self.tabSolTh.setObjectName("tabSolTh")
        self.gridLayout_6 = QtGui.QGridLayout(self.tabSolTh)
        self.gridLayout_6.setObjectName("gridLayout_6")

        self.pushButtonAdvAnnuitySolTh = QtGui.QPushButton(self.tabSolTh)
        self.pushButtonAdvAnnuitySolTh.setSizePolicy(sizePolicy)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonAdvAnnuitySolTh.sizePolicy().hasHeightForWidth())
        self.pushButtonAdvAnnuitySolTh.setObjectName("pushButtonAdvAnnuitySolTh")
        self.gridLayout_6.addWidget(self.pushButtonAdvAnnuitySolTh, 0, 0, 1, 1)

        self.labelSolThAvailArea = QtGui.QLabel(self.tabSolTh)
        self.labelSolThAvailArea.setObjectName("labelSolThModArea")
        self.gridLayout_6.addWidget(self.labelSolThAvailArea, 1, 0, 1, 1)
        self.lineEditSolThAvailArea = QtGui.QLineEdit(self.tabSolTh)
        self.lineEditSolThAvailArea.setObjectName("lineEditSolThAvailArea")
        self.gridLayout_6.addWidget(self.lineEditSolThAvailArea, 1, 1, 1, 1)
        self.labelSolThAvailAreaUnit = QtGui.QLabel(self.tabSolTh)
        self.labelSolThAvailAreaUnit.setObjectName("labelSolThAvailAreaUnit")
        self.gridLayout_6.addWidget(self.labelSolThAvailAreaUnit, 1, 2, 1, 1)

        self.labelSolThModArea = QtGui.QLabel(self.tabSolTh)
        self.labelSolThModArea.setObjectName("labelSolThModArea")
        self.gridLayout_6.addWidget(self.labelSolThModArea, 2, 0, 1, 1)
        self.lineEditSolThModArea = QtGui.QLineEdit(self.tabSolTh)
        self.lineEditSolThModArea.setObjectName("lineEditSolThModArea")
        self.gridLayout_6.addWidget(self.lineEditSolThModArea, 2, 1, 1, 1)
        self.labelSolThModAreaUnit = QtGui.QLabel(self.tabSolTh)
        self.labelSolThModAreaUnit.setObjectName("labelSolThModAreaUnit")
        self.gridLayout_6.addWidget(self.labelSolThModAreaUnit, 2, 2, 1, 1)

        self.labelSolThModelFix = QtGui.QLabel(self.tabSolTh)
        self.labelSolThModelFix.setObjectName("labelSolThModelFix")
        self.gridLayout_6.addWidget(self.labelSolThModelFix, 5, 0, 1, 1)
        self.lineEditSolThModelFix = QtGui.QLineEdit(self.tabSolTh)
        self.lineEditSolThModelFix.setObjectName("lineEditSolThModelFix")
        self.gridLayout_6.addWidget(self.lineEditSolThModelFix, 5, 1, 1, 1)
        self.labelSolThModelFixUnit = QtGui.QLabel(self.tabSolTh)
        self.labelSolThModelFixUnit.setObjectName("labelSolThArea")
        self.gridLayout_6.addWidget(self.labelSolThModelFixUnit, 5, 2, 1, 1)

        self.checkBoxFixSolTh = QtGui.QCheckBox(self.tabSolTh)
        self.checkBoxFixSolTh.setObjectName("checkBoxFixSolTh")
        self.gridLayout_6.addWidget(self.checkBoxFixSolTh, 4, 0, 1, 1)

        self.tabWidget.addTab(self.tabSolTh, "")

        # =====================================================================================================
        # Electric heater tab
        self.tabElHe = QtGui.QWidget()
        self.tabElHe.setObjectName("tabElHe")
        self.gridLayout_7 = QtGui.QGridLayout(self.tabElHe)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.pushButtonAdvAnnuityElHe = QtGui.QPushButton(self.tabElHe)
        self.pushButtonAdvAnnuityElHe.setSizePolicy(sizePolicy)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonAdvAnnuityElHe.sizePolicy().hasHeightForWidth())
        self.pushButtonAdvAnnuityElHe.setObjectName("pushButtonAdvAnnuityElHe")
        self.gridLayout_7.addWidget(self.pushButtonAdvAnnuityElHe, 0, 0, 1, 1)

        self.labelElHeModCap = QtGui.QLabel(self.tabElHe)
        self.labelElHeModCap.setObjectName("labelElHeModCap")
        self.gridLayout_7.addWidget(self.labelElHeModCap, 1, 0, 1, 1)
        self.lineEditElHeModCap = QtGui.QLineEdit(self.tabElHe)
        self.lineEditElHeModCap.setObjectName("lineEditElHeModCap")
        self.gridLayout_7.addWidget(self.lineEditElHeModCap, 1, 1, 1, 1)
        self.labelElHeModCapUnit = QtGui.QLabel(self.tabElHe)
        self.labelElHeModCapUnit.setObjectName("labelElHeModCapUnit")
        self.gridLayout_7.addWidget(self.labelElHeModCapUnit, 1, 2, 1, 1)

        self.checkBoxFixElHe = QtGui.QCheckBox(self.tabElHe)
        self.checkBoxFixElHe.setObjectName("checkBoxFixElHe")
        self.gridLayout_7.addWidget(self.checkBoxFixElHe, 2, 0, 1, 1)
        self.labelElHeModelFix = QtGui.QLabel(self.tabElHe)
        self.labelElHeModelFix.setObjectName("labelElHeModelFix")
        self.gridLayout_7.addWidget(self.labelElHeModelFix, 3, 0, 1, 1)
        self.lineEditElHeModelFix = QtGui.QLineEdit(self.tabElHe)
        self.lineEditElHeModelFix.setObjectName("lineEditElHeModelFix")
        self.gridLayout_7.addWidget(self.lineEditElHeModelFix, 3, 1, 1, 1)
        self.labelElHeModelFixUnit = QtGui.QLabel(self.tabElHe)
        self.labelElHeModelFixUnit.setObjectName("labelElHeModelFixUnit")
        self.gridLayout_7.addWidget(self.labelElHeModelFixUnit, 3, 2, 1, 1)
        self.tabWidget.addTab(self.tabElHe, "")

        # =====================================================================================================
        # PV tab
        self.tabPV = QtGui.QWidget()
        self.tabPV.setObjectName("tabPV")
        self.gridLayout_8 = QtGui.QGridLayout(self.tabPV)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.pushButtonAdvAnnuityPV = QtGui.QPushButton(self.tabPV)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonAdvAnnuityPV.sizePolicy().hasHeightForWidth())
        self.pushButtonAdvAnnuityPV.setSizePolicy(sizePolicy)
        self.pushButtonAdvAnnuityPV.setObjectName("pushButtonAdvAnnuityPV")
        self.gridLayout_8.addWidget(self.pushButtonAdvAnnuityPV, 0, 0, 1, 1)

        self.labelPVFIT = QtGui.QLabel(self.tabPV)
        self.labelPVFIT.setObjectName("labelPVFIT")
        self.gridLayout_8.addWidget(self.labelPVFIT, 1, 0, 1, 1)

        self.lineEditPVFIT = QtGui.QLineEdit(self.tabPV)
        self.lineEditPVFIT.setObjectName("lineEditPVFIT")
        self.lineEditPVFIT.setText("0.12")
        self.gridLayout_8.addWidget(self.lineEditPVFIT, 1, 1, 1, 1)

        self.labelPVFITUnit = QtGui.QLabel(self.tabPV)
        self.labelPVFITUnit.setObjectName("labelPVFITUnit")
        self.gridLayout_8.addWidget(self.labelPVFITUnit, 1, 2, 1, 1)


        self.labelPVAvailArea = QtGui.QLabel(self.tabPV)
        self.labelPVAvailArea.setObjectName("labelPVAvailArea")
        self.gridLayout_8.addWidget(self.labelPVAvailArea, 2, 0, 1, 1)
        self.lineEditPVAvailArea = QtGui.QLineEdit(self.tabPV)
        self.lineEditPVAvailArea.setObjectName("lineEditPVAvailArea")
        self.gridLayout_8.addWidget(self.lineEditPVAvailArea, 2, 1, 1, 1)
        self.labelPVAvailAreaUnit = QtGui.QLabel(self.tabPV)
        self.labelPVAvailAreaUnit.setObjectName("labelPVAvailAreaUnit")
        self.gridLayout_8.addWidget(self.labelPVAvailAreaUnit, 2, 2, 1, 1)

        self.labelPVModArea = QtGui.QLabel(self.tabPV)
        self.labelPVModArea.setObjectName("labelPVModArea")
        self.gridLayout_8.addWidget(self.labelPVModArea, 3, 0, 1, 1)
        self.lineEditPVModArea = QtGui.QLineEdit(self.tabPV)
        self.lineEditPVModArea.setObjectName("lineEditPVModArea")
        self.gridLayout_8.addWidget(self.lineEditPVModArea, 3, 1, 1, 1)
        self.labelPVModAreaUnit = QtGui.QLabel(self.tabPV)
        self.labelPVModAreaUnit.setObjectName("labelPVModAreaUnit")
        self.gridLayout_8.addWidget(self.labelPVModAreaUnit, 3, 2, 1, 1)

        self.labelPVModelFix = QtGui.QLabel(self.tabPV)
        self.labelPVModelFix.setObjectName("labelPVModelFix")
        self.gridLayout_8.addWidget(self.labelPVModelFix, 5, 0, 1, 1)
        self.lineEditPVModelFix = QtGui.QLineEdit(self.tabPV)
        self.lineEditPVModelFix.setObjectName("lineEditPVModelFix")
        self.gridLayout_8.addWidget(self.lineEditPVModelFix, 5, 1, 1, 1)
        self.labelPVModelFixUnit = QtGui.QLabel(self.tabPV)
        self.labelPVModelFixUnit.setObjectName("labelPVArea")
        self.gridLayout_8.addWidget(self.labelPVModelFixUnit, 5, 2, 1, 1)

        self.checkBoxFixPV = QtGui.QCheckBox(self.tabPV)
        self.checkBoxFixPV.setObjectName("checkBoxFixPV")
        self.gridLayout_8.addWidget(self.checkBoxFixPV, 4, 0, 1, 1)
        self.tabWidget.addTab(self.tabPV, "")

        # ==============================================================================================================
        # Electric Storage Tab
        self.tabElSt = QtGui.QWidget()
        self.tabElSt.setObjectName("tabElSt")
        self.gridLayout_9 = QtGui.QGridLayout(self.tabElSt)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.pushButtonAdvAnnuityElSt = QtGui.QPushButton(self.tabElSt)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonAdvAnnuityElSt.sizePolicy().hasHeightForWidth())
        self.pushButtonAdvAnnuityElSt.setSizePolicy(sizePolicy)
        self.pushButtonAdvAnnuityElSt.setObjectName("pushButtonAdvAnnuityElSt")
        self.gridLayout_9.addWidget(self.pushButtonAdvAnnuityElSt, 0, 0, 1, 2)

        self.labelElStModelFix = QtGui.QLabel(self.tabElSt)
        self.labelElStModelFix.setObjectName("labelElStModelFix")
        self.gridLayout_9.addWidget(self.labelElStModelFix, 1, 0, 1, 1)
        self.lineEditElStModelFix = QtGui.QLineEdit(self.tabElSt)
        self.lineEditElStModelFix.setObjectName("lineEditElStModelFix")
        self.gridLayout_9.addWidget(self.lineEditElStModelFix, 1, 1, 1, 1)
        self.labelElStModelFixUnit = QtGui.QLabel(self.tabElSt)
        self.labelElStModelFixUnit.setObjectName("labelElStModelFixUnit")
        self.gridLayout_9.addWidget(self.labelElStModelFixUnit, 1, 2, 1, 1)
        self.tabWidget.addTab(self.tabElSt, "")

        self.labelElStMaxhour = QtGui.QLabel(self.tabElSt)
        self.labelElStMaxhour.setObjectName("labelElStMaxhour")
        self.gridLayout_9.addWidget(self.labelElStMaxhour, 2, 0, 1, 1)
        self.lineEditElStMaxhour = QtGui.QLineEdit(self.tabElSt)
        self.lineEditElStMaxhour.setObjectName("lineEditElHeMaxhour")
        self.gridLayout_9.addWidget(self.lineEditElStMaxhour, 2, 1, 1, 1)
        self.labelElStMaxhourUnit = QtGui.QLabel(self.tabElSt)
        self.labelElStMaxhourUnit.setObjectName("labelElStMaxhourUnit")
        self.gridLayout_9.addWidget(self.labelElStMaxhourUnit, 2, 2, 1, 1)
        self.tabWidget.addTab(self.tabElSt, "")

        # ==============================================================================================================
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.buttonBox = QtGui.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setGeometry(QtCore.QRect(60, 350, 156, 23))
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 914, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        for index in range(3, 10):
            self.tabWidget.setTabEnabled(index, False)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.lineEditSolThModelFix.setEnabled(False)
        self.lineEditSolThModArea.setText('2.55')
        self.lineEditSolThAvailArea.setText('10.0')
        self.lineEditSolThModelFix.setText('10.0')

        self.lineEditElHeModelFix.setEnabled(False)
        self.lineEditElHeModCap.setText('100.0')

        self.lineEditPVModelFix.setEnabled(False)
        self.lineEditPVModArea.setText('1.6434')
        self.lineEditPVAvailArea.setText('10.0')
        self.lineEditPVModelFix.setText('10.0')

        self.lineEditElStModelFix.setText('1000.0')
        self.lineEditElStMaxhour.setText('20.0')

        # QtCore.QObject.connect(self.check_box_chp, QtCore.SIGNAL("clicked(bool)"), self.check_box_chp.setChecked)
        # QtCore.QObject.connect(self.check_box_boiler, QtCore.SIGNAL("clicked(bool)"), self.check_box_boiler.setChecked)
        # QtCore.QObject.connect(self.check_box_elhe, QtCore.SIGNAL("clicked(bool)"), self.check_box_elhe.setChecked)
        # QtCore.QObject.connect(self.check_box_elst, QtCore.SIGNAL("clicked(bool)"), self.check_box_elst.setChecked)
        # QtCore.QObject.connect(self.check_box_pv, QtCore.SIGNAL("clicked(bool)"), self.check_box_pv.setChecked)
        # QtCore.QObject.connect(self.check_box_solth, QtCore.SIGNAL("clicked(bool)"), self.check_box_solth.setChecked)
        # QtCore.QObject.connect(self.check_box_thst, QtCore.SIGNAL("clicked(bool)"), self.check_box_thst.setChecked)
        # QtCore.QObject.connect(self.rbtn_hourly_excels, QtCore.SIGNAL("clicked(bool)"), self.rbtn_hourly_excels.setChecked)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Welcome to the SGT UI", None, QtGui.QApplication.UnicodeUTF8))
        self.label1.setText(QtGui.QApplication.translate("MainWindow", "Choose technologies that can be present in the system:", None, QtGui.QApplication.UnicodeUTF8))
        self.check_box_chp.setText(QtGui.QApplication.translate("MainWindow", "CHP", None, QtGui.QApplication.UnicodeUTF8))
        self.check_box_boiler.setText(QtGui.QApplication.translate("MainWindow", "Boiler", None, QtGui.QApplication.UnicodeUTF8))
        self.check_box_thst.setText(QtGui.QApplication.translate("MainWindow", "Thermal Storage", None, QtGui.QApplication.UnicodeUTF8))
        self.check_box_solth.setText(QtGui.QApplication.translate("MainWindow", "Solar Thermal", None, QtGui.QApplication.UnicodeUTF8))
        self.check_box_elhe.setText(QtGui.QApplication.translate("MainWindow", "Electric Heater", None, QtGui.QApplication.UnicodeUTF8))
        self.check_box_pv.setText(QtGui.QApplication.translate("MainWindow", "Photovoltaics", None, QtGui.QApplication.UnicodeUTF8))
        self.check_box_elst.setText(QtGui.QApplication.translate("MainWindow", "Electric Storage", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabTechnologies), QtGui.QApplication.translate("MainWindow", "Technologies", None, QtGui.QApplication.UnicodeUTF8))
        self.OutputFolderLineEdit.setPlaceholderText(QtGui.QApplication.translate("MainWindow", "Choose Output folder", None, QtGui.QApplication.UnicodeUTF8))
        self.btnOutputBrowse.setText(QtGui.QApplication.translate("MainWindow", "Browse..", None, QtGui.QApplication.UnicodeUTF8))
        self.WeatherDataLineEdit.setPlaceholderText(QtGui.QApplication.translate("MainWindow", "Choose TRY weather file", None, QtGui.QApplication.UnicodeUTF8))
        self.btnWeathreBrowse.setText(QtGui.QApplication.translate("MainWindow", "Browse..", None, QtGui.QApplication.UnicodeUTF8))
        self.ElProfileLineEdit.setPlaceholderText(QtGui.QApplication.translate("MainWindow", "Choose electrical profile", None, QtGui.QApplication.UnicodeUTF8))
        self.btnHeatprofilesBrowse.setText(QtGui.QApplication.translate("MainWindow", "Browse..", None, QtGui.QApplication.UnicodeUTF8))
        self.HProfileLineEdit.setPlaceholderText(QtGui.QApplication.translate("MainWindow", "Choose heat profile", None, QtGui.QApplication.UnicodeUTF8))
        self.btnElProfileBrowse.setText(QtGui.QApplication.translate("MainWindow", "Browse..", None, QtGui.QApplication.UnicodeUTF8))
        self.rbtn_hourly_excels.setText(QtGui.QApplication.translate("MainWindow", "Hourly excels required?", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabFolders), QtGui.QApplication.translate("MainWindow", "Source and destination Folders", None, QtGui.QApplication.UnicodeUTF8))
        self.labelElPrice.setText(QtGui.QApplication.translate("MainWindow", "Electricity price", None, QtGui.QApplication.UnicodeUTF8))
        self.labelElPriceUnit.setText(QtGui.QApplication.translate("MainWindow", "[Euros/kWh]", None, QtGui.QApplication.UnicodeUTF8))
        self.labelGprice.setText(QtGui.QApplication.translate("MainWindow", "Gas price", None, QtGui.QApplication.UnicodeUTF8))
        self.labelGPriceUnit.setText(QtGui.QApplication.translate("MainWindow", "[Euros/kWh]", None, QtGui.QApplication.UnicodeUTF8))
        self.labelObPeriod.setText(QtGui.QApplication.translate("MainWindow", "Observation Period", None, QtGui.QApplication.UnicodeUTF8))
        self.labelObPeriodUnit.setText(QtGui.QApplication.translate("MainWindow", "[years]", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabGDetails), QtGui.QApplication.translate("MainWindow", "General Details", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAddCHP.setText(QtGui.QApplication.translate("MainWindow", "Add/Modify Models in database", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAdvAnnuityCHP.setText(QtGui.QApplication.translate("MainWindow", "Modify Annuity Factors", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButtonContCHP.setText(QtGui.QApplication.translate("MainWindow", "Continuous CHP", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButtonONOFFCHP.setText(QtGui.QApplication.translate("MainWindow", "ON/OFF CHP", None, QtGui.QApplication.UnicodeUTF8))
        self.labelCHPFIT.setText(QtGui.QApplication.translate("MainWindow", "CHP FIT in Euro Cents", None, QtGui.QApplication.UnicodeUTF8))
        self.labelCHPFITUnit.setText(QtGui.QApplication.translate("MainWindow", "[Euros/kWh]", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButtonModCHP.setText(QtGui.QApplication.translate("MainWindow", "Modulating CHP", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabCHP), QtGui.QApplication.translate("MainWindow", "CHP", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAddBoiler.setText(QtGui.QApplication.translate("MainWindow", "Add/Modify Models in database", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAdvAnnuityBoiler.setText(QtGui.QApplication.translate("MainWindow", "Modify Annuity Factors", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabBoiler), QtGui.QApplication.translate("MainWindow", "Boiler", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAdvAnnuityThSt.setText(QtGui.QApplication.translate("MainWindow", "Modify Annuity Factors", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAddThSt.setText(QtGui.QApplication.translate("MainWindow", "Add/Modify Models in database", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabThSt), QtGui.QApplication.translate("MainWindow", "Thermal Storage", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAdvAnnuitySolTh.setText(QtGui.QApplication.translate("MainWindow", "Modify Annuity Factors", None, QtGui.QApplication.UnicodeUTF8))
        self.labelSolThModArea.setText(QtGui.QApplication.translate("MainWindow", "Module Area", None, QtGui.QApplication.UnicodeUTF8))
        self.labelSolThModAreaUnit.setText(QtGui.QApplication.translate("MainWindow", "[m2]", None, QtGui.QApplication.UnicodeUTF8))
        self.labelSolThModelFix.setText(QtGui.QApplication.translate("MainWindow", "Area", None, QtGui.QApplication.UnicodeUTF8))
        self.labelSolThModelFixUnit.setText(QtGui.QApplication.translate("MainWindow", "[m2]", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabSolTh), QtGui.QApplication.translate("MainWindow", "Solar Thermal", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAdvAnnuityElHe.setText(QtGui.QApplication.translate("MainWindow", "Modify Annuity Factors", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxFixElHe.setText(QtGui.QApplication.translate("MainWindow", "Fix Electric Heater capacity?", None, QtGui.QApplication.UnicodeUTF8))
        self.labelElHeModelFix.setText(QtGui.QApplication.translate("MainWindow", "Capacity", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabElHe), QtGui.QApplication.translate("MainWindow", "Electric Heater", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAdvAnnuityPV.setText(QtGui.QApplication.translate("MainWindow", "Modify Annuity Factors", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabPV), QtGui.QApplication.translate("MainWindow", "PV", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAdvAnnuityElSt.setText(QtGui.QApplication.translate("MainWindow", "Modify Annuity Factors", None, QtGui.QApplication.UnicodeUTF8))
        self.labelElStModelFix.setText(QtGui.QApplication.translate("MainWindow", "Electrical Storage Capacity", None, QtGui.QApplication.UnicodeUTF8))
        self.labelElStModelFixUnit.setText(QtGui.QApplication.translate("MainWindow", "[kWh]", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabElSt), QtGui.QApplication.translate("MainWindow", "Electric Storage", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Select Output Folder", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Select Heat Profile file ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Select Weather File", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Select Electrical Profile file", None, QtGui.QApplication.UnicodeUTF8))
        self.labelPVFIT.setText(QtGui.QApplication.translate("MainWindow", "PV FIT in Euro Cents", None, QtGui.QApplication.UnicodeUTF8))
        self.labelPVFITUnit.setText(QtGui.QApplication.translate("MainWindow", "[Euros/kWh]", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxFixSolTh.setText(QtGui.QApplication.translate("MainWindow", "Fix Solar thermal total area?", None, QtGui.QApplication.UnicodeUTF8))
        self.labelSolThAvailArea.setText(QtGui.QApplication.translate("MainWindow", "Available Area", None, QtGui.QApplication.UnicodeUTF8))
        self.labelSolThAvailAreaUnit.setText(QtGui.QApplication.translate("MainWindow", "[m2]", None, QtGui.QApplication.UnicodeUTF8))
        self.labelElHeModelFixUnit.setText(QtGui.QApplication.translate("MainWindow", "[kW]", None, QtGui.QApplication.UnicodeUTF8))
        self.labelElHeModCap.setText(QtGui.QApplication.translate("MainWindow", "Module Capacity", None, QtGui.QApplication.UnicodeUTF8))
        self.labelElHeModCapUnit.setText(QtGui.QApplication.translate("MainWindow", "[kW]", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxFixPV.setText(QtGui.QApplication.translate("MainWindow", "Fix PV total area?", None, QtGui.QApplication.UnicodeUTF8))
        self.labelPVAvailArea.setText(QtGui.QApplication.translate("MainWindow", "Available Area", None, QtGui.QApplication.UnicodeUTF8))
        self.labelPVAvailAreaUnit.setText(QtGui.QApplication.translate("MainWindow", "[m2]", None, QtGui.QApplication.UnicodeUTF8))
        self.labelPVModArea.setText(QtGui.QApplication.translate("MainWindow", "Module Area", None, QtGui.QApplication.UnicodeUTF8))
        self.labelPVModAreaUnit.setText(QtGui.QApplication.translate("MainWindow", "[m2]", None, QtGui.QApplication.UnicodeUTF8))
        self.labelPVModelFix.setText(QtGui.QApplication.translate("MainWindow", "Area", None, QtGui.QApplication.UnicodeUTF8))
        self.labelPVModelFixUnit.setText(QtGui.QApplication.translate("MainWindow", "[m2]", None, QtGui.QApplication.UnicodeUTF8))
        self.labelElStMaxhour.setText(QtGui.QApplication.translate("MainWindow", "Electrical Storage maximum input kWh", None, QtGui.QApplication.UnicodeUTF8))
        self.labelElStMaxhourUnit.setText(QtGui.QApplication.translate("MainWindow", "[kWh]", None, QtGui.QApplication.UnicodeUTF8))