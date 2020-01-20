# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aendern.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtWidgets, QtGui
import os, sys, win32com.client,codecs
from DB_Pornos import *


class Ui_Aendern(object):
    def setupUi(self, Aendern):
        Aendern.setObjectName("Aendern")
        Aendern.setWindowModality(QtCore.Qt.WindowModal)
        Aendern.resize(1302, 886)
        Aendern.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        icon = QtGui.QIcon.fromTheme("icon.ico")
        Aendern.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(Aendern)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pBar = QtWidgets.QProgressBar(Aendern)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(120)
        sizePolicy.setVerticalStretch(25)
        sizePolicy.setHeightForWidth(self.pBar.sizePolicy().hasHeightForWidth())
        self.pBar.setSizePolicy(sizePolicy)
        self.pBar.setProperty("value", 0)
        self.pBar.setObjectName("pBar")
        self.horizontalLayout_2.addWidget(self.pBar)
        spacerItem1 = QtWidgets.QSpacerItem(20, 25, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.Anzahl = QtWidgets.QLabel(Aendern)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(25)
        sizePolicy.setHeightForWidth(self.Anzahl.sizePolicy().hasHeightForWidth())
        self.Anzahl.setSizePolicy(sizePolicy)
        self.Anzahl.setText("")
        self.Anzahl.setObjectName("Anzahl")
        self.horizontalLayout_2.addWidget(self.Anzahl)
        self.gridLayout.addLayout(self.horizontalLayout_2, 11, 1, 1, 8)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Mark_lbl = QtWidgets.QLabel(Aendern)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(40)
        sizePolicy.setVerticalStretch(25)
        sizePolicy.setHeightForWidth(self.Mark_lbl.sizePolicy().hasHeightForWidth())
        self.Mark_lbl.setSizePolicy(sizePolicy)
        self.Mark_lbl.setObjectName("Mark_lbl")
        self.horizontalLayout.addWidget(self.Mark_lbl)
        self.replace_cBox = QtWidgets.QComboBox(Aendern)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(25)
        sizePolicy.setHeightForWidth(self.replace_cBox.sizePolicy().hasHeightForWidth())
        self.replace_cBox.setSizePolicy(sizePolicy)
        self.replace_cBox.setEditable(True)
        self.replace_cBox.setObjectName("replace_cBox")
        self.horizontalLayout.addWidget(self.replace_cBox)
        spacerItem3 = QtWidgets.QSpacerItem(20, 25, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.del_Btn = QtWidgets.QPushButton(Aendern)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(25)
        sizePolicy.setHeightForWidth(self.del_Btn.sizePolicy().hasHeightForWidth())
        self.del_Btn.setSizePolicy(sizePolicy)
        self.del_Btn.setObjectName("del_Btn")
        self.horizontalLayout.addWidget(self.del_Btn)
        self.replaceBtn = QtWidgets.QPushButton(Aendern)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(25)
        sizePolicy.setHeightForWidth(self.replaceBtn.sizePolicy().hasHeightForWidth())
        self.replaceBtn.setSizePolicy(sizePolicy)
        self.replaceBtn.setObjectName("replaceBtn")
        self.horizontalLayout.addWidget(self.replaceBtn)
        self.gridLayout.addLayout(self.horizontalLayout, 13, 1, 1, 8)
        self.Info_lbl = QtWidgets.QLabel(Aendern)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.Info_lbl.sizePolicy().hasHeightForWidth())
        self.Info_lbl.setSizePolicy(sizePolicy)
        self.Info_lbl.setText("")
        self.Info_lbl.setObjectName("Info_lbl")
        self.gridLayout.addWidget(self.Info_lbl, 8, 1, 1, 1)
        self.pasteBtn = QtWidgets.QPushButton(Aendern)
        self.pasteBtn.setObjectName("pasteBtn")
        self.gridLayout.addWidget(self.pasteBtn, 8, 6, 1, 1)
        self.OK_lbl = QtWidgets.QLabel(Aendern)
        self.OK_lbl.setText("")
        self.OK_lbl.setPixmap(QtGui.QPixmap("ok.jpg"))
        self.OK_lbl.setObjectName("OK_lbl")
        self.gridLayout.addWidget(self.OK_lbl, 8, 2, 1, 1)
        self.Ordner = QtWidgets.QLabel(Aendern)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.Ordner.setFont(font)
        self.Ordner.setObjectName("Ordner")
        self.gridLayout.addWidget(self.Ordner, 0, 1, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(10, -1, 0, -1)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.OrdnerBtn = QtWidgets.QPushButton(Aendern)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OrdnerBtn.sizePolicy().hasHeightForWidth())
        self.OrdnerBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.OrdnerBtn.setFont(font)
        self.OrdnerBtn.setObjectName("OrdnerBtn")
        self.verticalLayout_2.addWidget(self.OrdnerBtn)
        spacerItem4 = QtWidgets.QSpacerItem(40, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem4)
        self.addDB_Btn = QtWidgets.QPushButton(Aendern)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addDB_Btn.sizePolicy().hasHeightForWidth())
        self.addDB_Btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.addDB_Btn.setFont(font)
        self.addDB_Btn.setObjectName("addDB_Btn")
        self.verticalLayout_2.addWidget(self.addDB_Btn)
        spacerItem5 = QtWidgets.QSpacerItem(40, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem5)
        self.einfuegBtn = QtWidgets.QPushButton(Aendern)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.einfuegBtn.sizePolicy().hasHeightForWidth())
        self.einfuegBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.einfuegBtn.setFont(font)
        self.einfuegBtn.setObjectName("einfuegBtn")
        self.verticalLayout_2.addWidget(self.einfuegBtn)
        spacerItem6 = QtWidgets.QSpacerItem(40, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem6)
        self.ZurueckBtn = QtWidgets.QPushButton(Aendern)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ZurueckBtn.sizePolicy().hasHeightForWidth())
        self.ZurueckBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.ZurueckBtn.setFont(font)
        self.ZurueckBtn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ZurueckBtn.setObjectName("ZurueckBtn")
        self.verticalLayout_2.addWidget(self.ZurueckBtn)
        spacerItem7 = QtWidgets.QSpacerItem(40, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem7)
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 9, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem8, 14, 8, 1, 1)
        self.copyBtn = QtWidgets.QPushButton(Aendern)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.copyBtn.sizePolicy().hasHeightForWidth())
        self.copyBtn.setSizePolicy(sizePolicy)
        self.copyBtn.setObjectName("copyBtn")
        self.gridLayout.addWidget(self.copyBtn, 8, 5, 1, 1)
        self.delBtn = QtWidgets.QPushButton(Aendern)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delBtn.sizePolicy().hasHeightForWidth())
        self.delBtn.setSizePolicy(sizePolicy)
        self.delBtn.setObjectName("delBtn")
        self.gridLayout.addWidget(self.delBtn, 8, 4, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem9, 1, 10, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(Aendern)
        self.tableWidget.setRowCount(16)
        self.tableWidget.setColumnCount(16)
        self.tableWidget.setObjectName("tableWidget")
        self.gridLayout.addWidget(self.tableWidget, 1, 1, 6, 8)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Muster = QtWidgets.QLabel(Aendern)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(25)
        sizePolicy.setHeightForWidth(self.Muster.sizePolicy().hasHeightForWidth())
        self.Muster.setSizePolicy(sizePolicy)
        self.Muster.setObjectName("Muster")
        self.horizontalLayout_3.addWidget(self.Muster)
        self.Muster_cBox = QtWidgets.QComboBox(Aendern)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(25)
        sizePolicy.setHeightForWidth(self.Muster_cBox.sizePolicy().hasHeightForWidth())
        self.Muster_cBox.setSizePolicy(sizePolicy)
        self.Muster_cBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Muster_cBox.setObjectName("Muster_cBox")
        self.horizontalLayout_3.addWidget(self.Muster_cBox)
        spacerItem10 = QtWidgets.QSpacerItem(20, 25, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem10)
        self.renamBtn = QtWidgets.QPushButton(Aendern)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(25)
        sizePolicy.setHeightForWidth(self.renamBtn.sizePolicy().hasHeightForWidth())
        self.renamBtn.setSizePolicy(sizePolicy)
        self.renamBtn.setObjectName("renamBtn")
        self.horizontalLayout_3.addWidget(self.renamBtn)
        self.gridLayout.addLayout(self.horizontalLayout_3, 12, 1, 1, 8)
        spacerItem11 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem11, 8, 3, 1, 1)

        self.retranslateUi(Aendern)
        self.ZurueckBtn.clicked.connect(self.ZurueckBtn.animateClick)
        QtCore.QMetaObject.connectSlotsByName(Aendern)
        Aendern.setTabOrder(self.OrdnerBtn, self.Muster_cBox)
        Aendern.setTabOrder(self.Muster_cBox, self.replaceBtn)

    def retranslateUi(self, Aendern):
        _translate = QtCore.QCoreApplication.translate
        Aendern.setWindowTitle(_translate("Aendern", "Form"))
        self.Mark_lbl.setText(_translate("Aendern", "2.markiere Stellen: "))
        self.del_Btn.setText(_translate("Aendern", "Löschen"))
        self.replaceBtn.setText(_translate("Aendern", "OK"))
        self.pasteBtn.setText(_translate("Aendern", "einfügen"))
        self.Ordner.setText(_translate("Aendern", "Ordner: "))
        self.OrdnerBtn.setToolTip(_translate("Aendern", "<html><head/><body><p>Er liest ein Ordner ein was neu ist, um die Dateinamen zu ändern</p></body></html>"))
        self.OrdnerBtn.setText(_translate("Aendern", "Ordner einlesen"))
        self.addDB_Btn.setText(_translate("Aendern", "Datenbank hinzufügen"))
        self.einfuegBtn.setText(_translate("Aendern", "  Daten einfügen  "))
        self.ZurueckBtn.setToolTip(_translate("Aendern", "<html><head/><body><p>Er liest ein Ordner ein was neu ist, um die Dateinamen zu ändern</p></body></html>"))
        self.ZurueckBtn.setText(_translate("Aendern", "       Zurück       "))
        self.copyBtn.setText(_translate("Aendern", "kopieren"))
        self.delBtn.setText(_translate("Aendern", "Löschen"))
        self.Muster.setText(_translate("Aendern", "1. Muster:"))
        self.renamBtn.setText(_translate("Aendern", "Ok"))


        # eigener Code  
           
        self.OK_lbl.hide()
        self.Muster_cBox.addItem("Firma - Titel-Darsteller[Art]-SPRACHE(720p)")
        self.Muster_cBox.addItem("Firma - Darsteller-Titel[Art]-SPRACHE(720p)")
        self.Muster_cBox.addItem("Datum - Firma-Darsteller(Titel)(720p)")
        self.Muster_cBox.addItem("Keine Ahnung wie :)")       
        self.tableWidget.setHorizontalHeaderLabels(['    Ordner    ', 'Dateiname', '  Firma    ','   Titel  ', 'Darstellerin', 'Darsteller' ,'    Art    ','Sprache', ' Bild ','Breite','Dauer','Bitrate','Größe','Datum','Erklärung','Hash'])
        self.ZurueckBtn.clicked.connect(lambda:self.closeFenster(Aendern))        
        self.OrdnerBtn.clicked.connect(lambda:self.Ordner_Scan(Aendern))
        self.einfuegBtn.clicked.connect(lambda:self.Daten_einfug(Aendern))
        self.del_Btn.clicked.connect(lambda:self.Del_Filter(Aendern))
        self.replaceBtn.clicked.connect(lambda:self.Filter(Aendern))
        self.renamBtn.clicked.connect(lambda:self.Muster_Rename(Aendern)) 
        self.addDB_Btn.clicked.connect(lambda:self.DB_adden(Aendern))      
        self.ladeComboBox(Aendern)

    def closeFenster(self,Aendern):
        # hide the Screen on Exit
        Aendern.hide()  
    def ladeComboBox(self,Aendern): 
        if os.path.exists("ComboBox.ini"):                   
            Inhalt=str(open('ComboBox.ini').readlines()) 
            count = 0
            Inhalt=Inhalt[2:]
            for char in Inhalt:
                if char == ',':
                    count = count + 1                           
            for i in range (count):            
                f=Inhalt.find(',') 
                if f > 0:
                    Teil=Inhalt[2:Inhalt.find(',')-1];Inhalt=Inhalt[Inhalt.find(',')+1:]                
                    self.replace_cBox.addItem(Teil)
            self.replace_cBox.addItem(Inhalt[2:len(Inhalt)-4]) 
        else:
            Inhalt="";open('ComboBox.ini','w')
            msg=QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setWindowTitle('Info')
            msg.setText("Datei neu angelegt")
            msg.setInformativeText("für die Filterung von DAteinamen wurde eine neue ComboBox Filter-Datei angelegt")
            msg.exec_()      
    
    # Filter Muster löschen "del_Btn"
    def Del_Filter(self,Aendern):
        cur=self.replace_cBox.currentText()
        self.Info_lbl.setText(cur+'  gelöscht !') 
        i= self.replace_cBox.findText(cur,QtCore.Qt.MatchFixedString)        
        self.replace_cBox.removeItem(i)
        self.replace_cBox.clearEditText()
        with open('ComboBox.ini', 'w+') as AllItems:
            Inhalt = str([self.replace_cBox.itemText(i) for i in range(self.replace_cBox.count())])
            Inhalt.encode("ascii", "ignore")
            AllItems.write(Inhalt)
    def DB_adden(self,Aendern):
        neu=0;up=0
        thing = self.tableWidget.item(0,1)
        if self.tableWidget.item(0,1) is not None and thing.text() != '':
            for row in range(self.tableWidget.rowCount()):
                QtWidgets.QApplication.processEvents()
                DIR=str(self.tableWidget.item(row, 0).text())
                Filename=str(self.tableWidget.item(row, 1).text())
                r=DIR.replace('/','\\') 
                DIR= DIR=os.path.join(r,Filename)
                DSatz=self.FileDetails(row,Filename,DIR)
                isin=self.isinDB(Aendern,DIR,DSatz[9])
                if isin == 2: # neu
                     
                    self.Info_lbl.setText(str(Filename)+" <----    Dateiist neu !") 
                    self.OK_lbl.show()
                    Hash=self.addDB(Aendern,DSatz)
                    self.tableWidget.setItem(row,15,QtWidgets.QTableWidgetItem(Hash))
                    neu +=1
                elif isin == 3: #dirname updatet
                    self.UpdateDir(Aendern,DIR,DSatz[9]) 
                    self.Info_lbl.setText(str(Filename)+" <----    Dateiname wurde updatet !") 
                    self.UpdateDB(Aendern,DSatz) 
                    up += 1        
                elif isin == 1:  #ist da update
                    self.Info_lbl.setText(str(Filename)) 
                    self.OK_lbl.hide()                                    
                    self.UpdateDB(Aendern,DSatz)
                    up += 1    
                elif isin == 4:
                    print(isin)
                    self.Info_lbl.setText(str(Filename)) 
                    self.OK_lbl.hide() 
                    msg=QtWidgets.QMessageBox()
                    msg.setIcon(QtWidgets.QMessageBox.Warning)
                    msg.setWindowTitle('Warnung')
                    msg.setText("Doppelte Datei erkannt")
                    msg.setInformativeText("Lösche eine der Dateien, es sind beide identisch")
                    msg.exec_()       
            msg=QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setWindowTitle('Info')
            msg.setText(str(neu)+" neue Daten in der Datenbank!\n"+str(up)+" Daten sind updatet")
            msg.setInformativeText("die Daten sind neu oder verändert angelegt worden !")
            msg.exec_()               
        else: 
            msg=QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setWindowTitle('Warnung')
            msg.setText("Keine Daten da!")
            msg.setInformativeText("Ich kann nichts hinzufügen wenn nichts da ist")
            msg.exec_()
        
            
    def FileDetails(self,row,mp4file,DIR):
        thing = self.tableWidget.item(row,2) #Firma
        if self.tableWidget.item(row,2) is not None and thing.text() != '':
            Firma=str(self.tableWidget.item(row, 2).text())
        else:
            Firma=""
        thing = self.tableWidget.item(row,3) #Titel
        if self.tableWidget.item(row,3) is not None and thing.text() != '':
            Titel=str(self.tableWidget.item(row, 3).text())
        else:
            Titel=""
        thing = self.tableWidget.item(row,4) #Darstellerin
        if self.tableWidget.item(row,4) is not None and thing.text() != '':
            Darstin=str(self.tableWidget.item(row, 4).text())
        else:
            Darstin=""
        thing = self.tableWidget.item(row,5) #Darsteller
        if self.tableWidget.item(row,5) is not None and thing.text() != '':
            Darst=str(self.tableWidget.item(row, 5).text())
        else:
            Darst=""
        thing = self.tableWidget.item(row,6) #Art
        if self.tableWidget.item(row,6) is not None and thing.text() != '':
            Art=str(self.tableWidget.item(row, 6).text())
        else:
            Art=""
        thing = self.tableWidget.item(row,7) #Sprache 0-6
        if self.tableWidget.item(row,7) is not None and thing.text() != '':
            Sprache=str(self.tableWidget.item(row, 7).text())
        else:
            Sprache=0
        thing = self.tableWidget.item(row,8) #Bildhoehe
        if self.tableWidget.item(row,8) is not None and thing.text() != '':
            Hoehe=str(self.tableWidget.item(row, 8).text())

        thing = self.tableWidget.item(row,9) #Bildbreite
        if self.tableWidget.item(row,9) is not None and thing.text() != '':
            Breite=str(self.tableWidget.item(row, 9).text())

        thing = self.tableWidget.item(row,10) #Dauer
        if self.tableWidget.item(row,10) is not None and thing.text() != '':
            Dauer=str(self.tableWidget.item(row, 10).text())

        thing = self.tableWidget.item(row,11) #Bitrate
        if self.tableWidget.item(row,11) is not None and thing.text() != '':
            Bitrate=str(self.tableWidget.item(row, 11).text())

        thing = self.tableWidget.item(row,12) #Größe
        if self.tableWidget.item(row,12) is not None and thing.text() != '':
            Groesse=str(self.tableWidget.item(row, 12).text())

        thing = self.tableWidget.item(row,13) #Datum
        if self.tableWidget.item(row,13) is not None and thing.text() != '':
            Datum=str(self.tableWidget.item(row, 13).text())
        else:
            Datum=""
        thing = self.tableWidget.item(row,14) #Erklärung
        if self.tableWidget.item(row,14) is not None and thing.text() != '':
            Erklaerung=str(self.tableWidget.item(row, 14).text())
        else:
            Erklaerung=""
        return [DIR,Firma,Titel,Darstin,Darst,Art,Sprache,Hoehe,Breite,Dauer,Bitrate,Groesse,Datum,Erklaerung]
    def Daten_einfug(self,Aendern):
        gefunden=0
        Filter="ANAL","TEEN","DP","MILF","ASIAN"
        # Filename aufsplitten
        thing = self.tableWidget.item(0,1)#Filename
            
        if self.tableWidget.item(0,1) is not None and thing.text() != '':             
            for row in range(self.tableWidget.rowCount()): 
                Firma=""; Titel="";Art="";Sprache=0;besetzt=0                               
                mp4file=str(self.tableWidget.item(row,1).text())
                Datei = mp4file[:len(mp4file)-4] 
                if "[" and "]" in Datei:                    
                    a=Datei.find("[")
                    b=Datei.find("]")+1
                    Art=Datei[a+1:b-1].upper()
                    Art=Art.strip()+" "
                    Datei=Datei.replace(Datei[a:b],"")
                    gefunden += 1  
                # Sprache
                if "GERMAN" in Datei:
                    Sprache=1;Datei=Datei.replace("GERMAN","");gefunden = 1
                if "FRANCE" in Datei:
                    Sprache=2;Datei=Datei.replace("FRANCE","");gefunden = 1
                if "ITALIAN" in Datei:
                    Sprache=3;Datei=Datei.replace("ITALIAN","");gefunden = 1
                if "RUSSIAN" in Datei:
                    Sprache=4;Datei=Datei.replace("RUSSIAN","");gefunden = 1
                if "NORWEGIAN" in Datei:
                    Sprache=5;Datei=Datei.replace("NORWEGIAN","");gefunden = 1
                if "JAPAN" in Datei or "Japanese" in Datei:
                    Sprache=6;Datei=Datei.replace("JAPAN","")
                    Datei=Datei.replace("Japanese","");gefunden = 1
                if Datei.rfind("(") == len(Datei)-6 and Datei.rfind(")") == len(Datei)-1:                    
                    Datei = Datei[:len(Datei)-6] 
                                 
                if Datei.find(' - ') > -1:  
                                     
                    gefunden += 1;besetzt=1
                    Firma = Datei[:Datei.find(' - ')]
                    Datei = Datei[Datei.find(' - ')+3:len(Datei)]   
                            
                    
                # Titel und Name erkennen und löschen 
                if  Datei.find('-') > -1:
                    gefunden += 1;besetzt=2
                    Titel = Datei[:Datei.find('-')].strip()
                    Datei = Datei.replace(Titel,"").strip()                   
                    Datei = Datei[1:].strip()
                   
               # [ANAL Teen] erkennen und löschen 
                Dat=Datei.upper()
               

                for index in range(4):
                    F=str(Filter[index])                    
                    b=Dat.find(F);L=len(F)

                    if b>2 :
                        o1=ord(Datei[b-1:b])
                        if len(Datei)== b+L:
                            o2=ord(Datei[b+L-1:])
                        else:                            
                            o2=ord(Datei[b+L:b+L+1])
                            
                        Datei=Datei.replace(" "+F+" ","")
                        if o1 <65 or o1>90 and o2 <65 or o2>90:
                            Datei=Datei.replace(chr(o1)+F+chr(o2),"")
                        if o1 <65 or o1>90 or o2 <65 or o2>90:
                            Datei=Datei.replace(chr(o1)+F+chr(o2),"")
                            
                   
                 
                self.tableWidget.setItem(row,2,QtWidgets.QTableWidgetItem(str(Firma)))
                self.tableWidget.setItem(row,3,QtWidgets.QTableWidgetItem(str(Titel)))
                self.tableWidget.setItem(row,besetzt+2,QtWidgets.QTableWidgetItem(str(Datei)))
                self.tableWidget.setItem(row,6,QtWidgets.QTableWidgetItem(str(Art)))
                self.tableWidget.setItem(row,7,QtWidgets.QTableWidgetItem(str(Sprache)))        
                self.Info_lbl.setText(mp4file)

        else:
            msg=QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setWindowTitle('Info')
            msg.setText("Keine Datei geladen")
            msg.setInformativeText("Ohne daten kann ich den Dateinamen nichts analysieren !")
            msg.exec_() 
            gefunden =-1 
        if gefunden>0:
            msg=QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setWindowTitle('Info')
            msg.setText("Man hat "+str(gefunden)+" Elemente finden können")
            msg.setInformativeText("Analye erfolgreich !")
            msg.exec_() 
        elif gefunden==0:            
            msg=QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setWindowTitle('Info')
            msg.setText("nichts erkannt !")
            msg.setInformativeText("Die Analyse der Dateinamen haben nichts erkannt. Zu wenige Informationen")
            msg.exec_() 
           

    # Nach Muster alles umbennen
    def Muster_Rename(self,Aendern):
        
        I=-1;anz=0;b=0;sp=0
        I=self.Muster_cBox.currentIndex()        
        #Auswahl Firma - Titel-Darsteller[Art]-SPRACHE(720p)
        if I==0:
            for row in range(self.tableWidget.rowCount()):
                ist=0;b=0
                m1="";m2="";m3="";m4="";m5="";m2a=""
                thing = self.tableWidget.item(row,1)#Filename
                if self.tableWidget.item(row,1) is not None and thing.text() != '': 
                    DIR=str(self.tableWidget.item(row, 0).text())  
                    Inhalt_alt=str(self.tableWidget.item(row, 1).text())                     
                    thing = self.tableWidget.item(row,2) # Firma
                    if self.tableWidget.item(row,2) is not None and thing.text() != '':
                        Firma=self.tableWidget.item(row, 2).text();m1=" - "
                    else:
                        Firma="";ist+=1
                    thing = self.tableWidget.item(row,3) #Titel
                    if self.tableWidget.item(row,3) is not None and thing.text() != '':
                        Titel=self.tableWidget.item(row, 3).text();m2="-"
                    else:
                        Titel="";ist+=1
                    thing = self.tableWidget.item(row,4) #Darstellerin
                    if self.tableWidget.item(row,4) is not None and thing.text() != '':
                        Darstellerin=self.tableWidget.item(row, 4).text()
                    else:
                        Darstellerin="";ist+=1
                    thing = self.tableWidget.item(row,5) #Darsteller
                    if self.tableWidget.item(row,5) is not None and thing.text() != '':
                        Darsteller=self.tableWidget.item(row, 5).text();m2a=" & "
                    else:
                        Darsteller="";ist+=1
                    thing = self.tableWidget.item(row,6) #Art
                    if self.tableWidget.item(row,6) is not None and thing.text() != '':
                        Art=self.tableWidget.item(row, 6).text().strip()
                        print(Inhalt_alt+"   zeichen drin");m3="[";m4="]"
                    else:
                       Art="";ist+=1
                    thing = self.tableWidget.item(row,7) #Sprache
                    Sprache="","GERMAN","FRANCE","ITALIAN","RUSSIAN","NORWEGIAN","JAPAN"
                    if self.tableWidget.item(row,7) is not None and thing.text() != '':
                        sp=int(self.tableWidget.item(row, 7).text())
                        if sp>0:
                            m5="-"
                    else:
                        sp=0
                    Hoehe = int(self.tableWidget.item(row,8).text()) #Hoehe
                    thing = self.tableWidget.item(row,1).text() #SFilename
                    print(thing.rfind("p).mp4"))
                    if thing.rfind("p).mp4") > 2:
                        Bild="";b=6 
                    if Hoehe < 300:
                        Bild="(240p)"
                    if Hoehe >=300 and Hoehe < 430:
                        Bild="(360p)"
                    if Hoehe >=300 and Hoehe < 430:
                        Bild="(360p)"
                    if Hoehe >=430 and Hoehe < 520:
                        Bild="(480p)"
                    if Hoehe >=520 and Hoehe < 690:
                        Bild="(576p)"
                    if Hoehe >= 690:
                        Bild="(720p)"                    
                    
                    DIR=DIR.replace('/','\\')
                     
                    # Keine Daten vorhanden
                    
                    if ist == 4:                                                                                            
                        Firma=Inhalt_alt[:len(Inhalt_alt)-4-b]
                        Inhalt=Firma+Bild+".mp4"
                        self.tableWidget.setItem(row,2,QtWidgets.QTableWidgetItem(str(Firma[:len(Inhalt)])))
                        
                    else:
                        Inhalt=Firma+m1+Titel+m2+Darstellerin+m2a+Darsteller+m3+Art+m4+m5+Sprache[sp]+Bild+".mp4"                    
                    old_file=os.path.join(DIR,Inhalt_alt)
                    new_file=os.path.join(DIR,Inhalt)  
                                                       
                    if not os.path.exists(new_file):                
                        os.rename(old_file,new_file)
                        anz+=1                        
                        self.tableWidget.setItem(row,1,QtWidgets.QTableWidgetItem(str(Inhalt)))
                    
                else:
                    msg=QtWidgets.QMessageBox()
                    msg.setIcon(QtWidgets.QMessageBox.Warning)
                    msg.setWindowTitle('Info')
                    msg.setText("Keine Datei geladen")
                    msg.setInformativeText("Ohne daten kann ich den Dateinamen nicht verändern !")
                    msg.exec_()
                    break
        msg=QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setWindowTitle('Info')
        msg.setText("Es wurden "+str(anz)+" Datenen umbenannt")
        msg.setInformativeText("nach Muster: Firma - Titel-Darsteller[Art]-SPRACHE(720p)")
        msg.exec_()

            


    # Filter anwenden "replace_Btn"        
    def Filter(self,Aendern):
        i=0;a=0      
        for row in range(self.tableWidget.rowCount()):                    
            Inhalt_alt=self.tableWidget.item(row, 1).text()                        
            Inhalt=str(Inhalt_alt.encode("ascii", "ignore")) 
                      
            Inhalt=Inhalt.replace(',','');Inhalt=Inhalt[2:len(Inhalt)-1]
            #doppelte Leerzeichen wegmachen
            Inhalt='\n'.join(' '.join(line.split()) for line in Inhalt.splitlines())                         
            for i in range(self.replace_cBox.count()): 
                Inhalt=Inhalt.replace(self.replace_cBox.itemText(i),'')                
                if Inhalt=="":
                    Inhalt="XXX"+str(i)
            self.tableWidget.setItem(row,1,QtWidgets.QTableWidgetItem(str(Inhalt)))
            DIR=str(self.tableWidget.item(row, 0).text())
            DIR=DIR.replace('/','\\')
            old_file=os.path.join(DIR,Inhalt_alt)
            new_file=os.path.join(DIR,Inhalt)
            if not os.path.exists(new_file):                
                os.rename(old_file,new_file)
                a+=1
        msg=QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setWindowTitle('Info')
        msg.setText("Es wurden "+str(a)+" Datenen umbenannt")
        msg.setInformativeText("nach Muster Erkennung wurden die Daten umbenannt !")
        msg.exec_()
                    
        

    def Ordner_Scan(self,Aendern):        
        dname = str(self.DirDialog(Aendern))             
        self.tableWidget.setRowCount(0)
        i=0;Zeile=0;Spalte=[]
        self.pBar.setValue(0)               
        c=sum(len(files) for _, _, files in os.walk(dname))
        if os.path.exists(dname):
            self.Ordner.setText(dname)           
            self.tableWidget.setRowCount(c)
            
            for root,dir,files in os.walk(dname,"*,mp4"):
                r=root.replace('/','\\') 
                                        
                for filename in files:   
                    QtWidgets.QApplication.processEvents()
                    #Zeile += 1 
                    DIR=os.path.join(r,filename)
                    
                    TheShell = win32com.client.gencache.EnsureDispatch('Shell.Application',0)
                    AFolder = TheShell.NameSpace(os.path.dirname(DIR))
                    AFile = AFolder.ParseName(os.path.basename(DIR))                             
                    Groesse=AFolder.GetDetailsOf(AFile,1)                    
                    try: 
                        Breite=int(AFolder.GetDetailsOf(AFile,316))
                    except ValueError: 
                        Breite=0
                    # print ("Breite : " + str(Breite))
                    try: 
                        Hoehe=int(AFolder.GetDetailsOf(AFile,314))
                    except ValueError: 
                        Hoehe=0       
                    # print ("Höhe : " + str(Hoehe))
                    try: 
                        Bitrate=AFolder.GetDetailsOf(AFile,313).replace('kBit/s','')
                    except ValueError: 
                        Bitrate=0                 
                    Dauer=AFolder.GetDetailsOf(AFile,27)                   
                    self.tableWidget.setItem(Zeile,0,QtWidgets.QTableWidgetItem(str(root)))
                    self.tableWidget.setItem(Zeile,1,QtWidgets.QTableWidgetItem(str(filename)))
                    self.tableWidget.setItem(Zeile,8,QtWidgets.QTableWidgetItem(str(Hoehe)))
                    self.tableWidget.setItem(Zeile,9,QtWidgets.QTableWidgetItem(str(Breite)))
                    self.tableWidget.setItem(Zeile,10,QtWidgets.QTableWidgetItem(str(Dauer)))
                    self.tableWidget.setItem(Zeile,11,QtWidgets.QTableWidgetItem(str(Bitrate)))
                    self.tableWidget.setItem(Zeile,12,QtWidgets.QTableWidgetItem(str(Groesse))) 
                    if self.isinDB(Aendern,DIR,Dauer) == 1:                        
                        for Spalte in self.upDB(Aendern,DIR):
                            self.tableWidget.setItem(Zeile,2,QtWidgets.QTableWidgetItem(str(Spalte[0])))
                            self.tableWidget.setItem(Zeile,3,QtWidgets.QTableWidgetItem(str(Spalte[1])))
                            self.tableWidget.setItem(Zeile,4,QtWidgets.QTableWidgetItem(str(Spalte[2])))
                            self.tableWidget.setItem(Zeile,5,QtWidgets.QTableWidgetItem(str(Spalte[3])))
                            self.tableWidget.setItem(Zeile,6,QtWidgets.QTableWidgetItem(str(Spalte[4])))
                            self.tableWidget.setItem(Zeile,7,QtWidgets.QTableWidgetItem(str(Spalte[5])))
                            self.tableWidget.setItem(Zeile,13,QtWidgets.QTableWidgetItem(str(Spalte[6].strip())))
                            self.tableWidget.setItem(Zeile,14,QtWidgets.QTableWidgetItem(str(Spalte[7])))
                            self.tableWidget.setItem(Zeile,15,QtWidgets.QTableWidgetItem(str(Spalte[8])))
                    Zeile += 1 
                    self.pBar.setValue(int(Zeile/c*100)) 
                    self.Info_lbl.setText(filename)
                    self.Anzahl.setText(str(Zeile)+' von '+str(c))
                    Aendern.showMaximized()
                          
                   
    def Analyse(self,Aendern,Datei):

        Analyse=[]
        Firma="";Titel="";Darsteller="";Art="";Sprache=""
        if ' - ' in Datei:
            Firma = Datei[0:Datei.find(' - ')]
            Analyse.append(Firma)
            Datei = Datei[Datei.find(' - ')+3:len(Datei)]       
  
        # Titel und Name erkennen und löschen 
        if '-' in Datei:
            Titel = Datei[0:Datei.find('-')]
            Datei = Datei[Datei.find('-')+1:len(Datei)]
            Analyse.append(Titel)  
               
        # (720p) erkennen und löschen
        if 'p)' in Datei:
            #Bild = Datei[len(Datei)-6:len(Datei)]
            Datei = Datei[0:Datei.rfind('(')]
            
        # Sprache
        if "GERMAN" in Datei:
            Sprache=1;Datei=Datei.replace("GERMAN","")
        if "FRANCE" in Datei:
            Sprache=2;Datei=Datei.replace("FRANCE","")
        if "ITALIAN" in Datei:
            Sprache=3;Datei=Datei.replace("ITALIAN","")
        if "RUSSIAN" in Datei:
            Sprache=4;Datei=Datei.replace("RUSSIAN","")
        if "NORWEGIAN" in Datei:
            Sprache=5;Datei=Datei.replace("NORWEGIAN","")
        #Analyse = Analyse[:4] + (Sprache) + Analyse[5:]
        # [ANAL Teen] erkennen und löschen 
        if "[" and "]" in Datei:
            Art = Datei[Datei.rfind('['):Datei.rfind(']')+1]
            Datei = Datei[0:Datei.rfind('[')]
        if Titel == "":
            Titel=Datei
        else:
            if Datei != "":
                Darsteller=Datei 
            
        Analyse=Firma,Titel,Darsteller,Art,Sprache
        return Analyse
                          
    def addDB(self,Aendern, Dsatz=[]):        
        self.Obj = DB_Pornos() 
        Hash=self.Obj.addPorns(Dsatz[0],Dsatz[1],Dsatz[2],Dsatz[3],Dsatz[4],Dsatz[5],Dsatz[6],Dsatz[7],Dsatz[8],Dsatz[9],Dsatz[10],Dsatz[11],Dsatz[12],Dsatz[13])  
        return Hash 
    def UpdateDB(self,Aendern,Dsatz=[]):
        self.Obj = DB_Pornos() 
        self.Obj.UpdatePorns(Dsatz[0],Dsatz[1],Dsatz[2],Dsatz[3],Dsatz[4],Dsatz[5],Dsatz[6],Dsatz[7],Dsatz[8],Dsatz[9],Dsatz[10],Dsatz[11],Dsatz[12],Dsatz[13])  

    def isinDB(self,Aendern,DIR,Dauer):
        self.Obj = DB_Pornos()       
        return self.Obj.SuchDB(DIR,Dauer)
    def upDB(self,Aendern,DIR):
        self.Obj = DB_Pornos()       
        return self.Obj.DatenHolen(DIR)
    def UpdateDir(self,Aendern,DIR,Hash):
        self.Obj = DB_Pornos()       
        return self.Obj.SuchHash(DIR,Hash)
    

    def DirDialog(self,Aendern):
        dialog = QtWidgets.QFileDialog(Aendern,"Ordner öffnen")
        dialog.setAcceptMode(QtWidgets.QFileDialog.AcceptOpen)
        dialog.setDirectory("D:\\")
        dialog.setFileMode(QtWidgets.QFileDialog.Directory)
        dialog.setOption(QtWidgets.QFileDialog.ShowDirsOnly, True)
        dialog.setViewMode(QtWidgets.QFileDialog.Detail) 
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            dirname = dialog.selectedFiles()[0]  # returns a list
            return dirname  

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)    
    Aendern = QtWidgets.QWidget()
    ui = Ui_Aendern()
    ui.setupUi(Aendern)
    Aendern.setWindowIcon(QtGui.QIcon('icon.ico'))
    Aendern.show()
    sys.exit(app.exec_())




