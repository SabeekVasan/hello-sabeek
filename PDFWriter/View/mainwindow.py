# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PDFWriterMain.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from pip._internal import self_outdated_check
from ViewModel.VM_mainWindow import VM_maindwindow
from samba.dcerpc.messaging import rec
from _datetime import datetime


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.MainWin = MainWindow
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(476, 435)              
        self.actionE_xit = QAction(MainWindow)
        self.actionE_xit.setObjectName(u"actionE_xit")
        self.actionE_xit.triggered.connect(lambda:self.fileExit("Exit"))        
        self.action_About = QAction(MainWindow)
        self.action_About.setObjectName(u"action_About")
        self.action_About.triggered.connect(lambda:self.fileExit("About")) 
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(260, 350, 188, 30))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.clicked.connect(self.btnCreateClick)

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.clicked.connect(self.btnClose)

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.widget1 = QWidget(self.centralwidget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(20, 20, 431, 141))
        self.formLayout = QFormLayout(self.widget1)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget1)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.lineEdit = QLineEdit(self.widget1)
        self.lineEdit.setObjectName(u"lineEdit")
        #self.lineEdit.textChanged.connect(self.lineEditTxtChange) 
        self.lineEdit.returnPressed.connect(self.lineEditEnterKey)
        self.lineEdit.setPlaceholderText("enter employee name")
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit)

        self.label_2 = QLabel(self.widget1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.lineEdit_2 = QLineEdit(self.widget1)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_2)

        self.label_3 = QLabel(self.widget1)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.lineEdit_3 = QLineEdit(self.widget1)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_3)

        self.label_4 = QLabel(self.widget1)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.lineEdit_4 = QLineEdit(self.widget1)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lineEdit_4)

        self.widget2 = QWidget(self.centralwidget)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(20, 190, 431, 141))
        self.gridLayout = QGridLayout(self.widget2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.widget2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)

        self.dateEdit = QDateEdit(self.widget2)
        self.dateEdit.setDate(QDate.currentDate())
        self.dateEdit.setObjectName(u"dateEdit")

        self.gridLayout.addWidget(self.dateEdit, 1, 1, 1, 1)

        self.label_6 = QLabel(self.widget2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_6, 1, 2, 1, 1)

        self.dateEdit_2 = QDateEdit(self.widget2)
        self.dateEdit_2.setDate(QDate.currentDate())
        self.dateEdit_2.setObjectName(u"dateEdit_2")
        self.dateEdit_2.setCalendarPopup(True)

        self.gridLayout.addWidget(self.dateEdit_2, 1, 3, 1, 1)

        self.label_7 = QLabel(self.widget2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_7, 2, 2, 1, 1)

        self.dateEdit_3 = QDateEdit(self.widget2)
        self.dateEdit_3.setDate(QDate.currentDate())
        self.dateEdit_3.setObjectName(u"dateEdit_3")
        self.dateEdit_3.setCalendarPopup(True)

        self.gridLayout.addWidget(self.dateEdit_3, 2, 3, 1, 1)

        self.radioButton = QRadioButton(self.widget2)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setChecked(True)

        self.gridLayout.addWidget(self.radioButton, 0, 1, 1, 1)

        self.radioButton_2 = QRadioButton(self.widget2)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.gridLayout.addWidget(self.radioButton_2, 0, 3, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 476, 22))
        self.menu_file = QMenu(self.menubar)
        self.menu_file.setObjectName(u"menu_file")
        self.menu_Help = QMenu(self.menubar)
        self.menu_Help.setObjectName(u"menu_Help")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
                
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())
        self.menu_file.addAction(self.actionE_xit)
        self.menu_Help.addAction(self.action_About)

        self.retranslateUi(MainWindow)
        
        # Adding Completer.        
        self.vmwin = VM_maindwindow()
        completer = QCompleter(self.vmwin.getNames())        
        self.lineEdit.setCompleter(completer)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionE_xit.setText(QCoreApplication.translate("MainWindow", u"E&xit", None))
#if QT_CONFIG(shortcut)
        self.actionE_xit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+X", None))
#endif // QT_CONFIG(shortcut)
        self.action_About.setText(QCoreApplication.translate("MainWindow", u"&About", None))
#if QT_CONFIG(shortcut)
        self.action_About.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+A", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Create", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Employee Name :", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Badge :", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Extension :", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Title :", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Month :", None))
        self.dateEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"MMM", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"From :", None))
        self.dateEdit_2.setDisplayFormat(QCoreApplication.translate("MainWindow", u"d/M/yy", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"To :", None))
        self.dateEdit_3.setDisplayFormat(QCoreApplication.translate("MainWindow", u"d/M/yy", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Monthly Report", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Day based report", None))
        self.menu_file.setTitle(QCoreApplication.translate("MainWindow", u"&File", None))
        self.menu_Help.setTitle(QCoreApplication.translate("MainWindow", u"&Help", None))
    # retranslateUi
    def fileExit(self,text):
        if text == "Exit":
            self.MainWin.close()
        elif text == "About" :
            QMessageBox.about(self.MainWin, "PDFWriter", "PDFWriter to create overtime report.")
    
    def btnCreateClick(self):
        
        #checking for employee details
        if len(self.lineEdit.text()) == 0:
            createErr  = QMessageBox()
            createErr.setIcon(createErr.Icon.Warning)
            createErr.setText("Unable to create report, employee records not available.")   
            createErr.setWindowTitle("PDFWriter Error...")     
            createErr.exec_()            
            return
        
        #get all date values from window
        
        date1 = self.dateEdit.date()
        date2 = self.dateEdit_2.date()
        date3 = self.dateEdit_3.date()
        
        dateToday = QDate.currentDate()
        
        print(date1.day(), date1.month(),date1.year())
        print(date2.day(), date2.month(),date2.year())
        print(date3.day(), date3.month(),date3.year())
           
        #setting up values to generate report based on option selected.        
        if self.radioButton.isChecked() == True:  
            self.vmwin.process4Report(date1.day(), date1.month(), date1.year(), date1.daysInMonth(), date1.month(), date1.year())          
            print(date1.daysInMonth())           
        elif self.radioButton_2.isChecked() == True:            
            if date3 < date2 :
                createErr  = QMessageBox()
                createErr.setIcon(createErr.Icon.Warning)
                createErr.setText("TO date is less than From date")   
                createErr.setWindowTitle("PDFWriter Error...")     
                createErr.exec_() 
                return
            self.vmwin.process4Report(date2.day(), date2.month(), date2.year(), date3.day(), date3.month(), date3.year())
      
        
    def btnClose(self):        
        self.MainWin.close()
        
    #def lineEditTxtChange(self):
        #print("Text Change")
        
    def lineEditEnterKey(self):        
        rec = self.vmwin.getRecords(self.lineEdit.text())
        #print(rec.Badge)        
        self.lineEdit_2.setText("{}".format(rec.Badge))
        self.lineEdit_3.setText("{}".format(rec.Ext))
        self.lineEdit_4.setText("{}".format(rec.Title))
