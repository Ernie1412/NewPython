from PyQt5 import QtWidgets, uic, QtCore,QtGui
import os, sys, unittest, win32com.client
from DB_Pornos import *
from suchFenster import Ui_Suche
from Aendern_Win import Ui_Aendern

"""
    Erstellt ein Fenster "Ui"
        2 Button "LeseButton" , "clearButton"
        1 List "Ausgabe"
        2 Label "Hinweis" , "Ordnername"
"""

class Haupt_Fenster(QtWidgets.QMainWindow):

    def __init__(self):
        super(Haupt_Fenster, self).__init__()                 
        PATHS = str(os.path.dirname(os.path.abspath(__file__)))
        uic.loadUi(os.path.join(PATHS,"Fenster.ui"),self) 
               
        # Button  
        self.Lese = self.findChild(QtWidgets.QPushButton, 'LeseButton') # Find the button
        self.Lese.setToolTip('Sie App scannt einen angegebenen Ordner, scannt auch die Datenbank dabei und addet gegebenfalls')
        self.Lese.clicked.connect(self.openButtonPressed) # Remember to pass the definition/method, not the return value!
        # Button        
        self.such = self.findChild(QtWidgets.QPushButton, 'suchButton') # Find the button
        self.such.clicked.connect(self.Suchen) # Remember to pass the definition/method, not the return value!

        self.loe = self.findChild(QtWidgets.QPushButton, 'delButton') # Find the button
        #self.loe.clicked.connect(self.loeButtonPressed) # Remember to pass the definition/method, not the return value!

        self.chan = self.findChild(QtWidgets.QPushButton, 'chanButton') # Find the button
        self.chan.clicked.connect(self.Aendern) # Remember to pass the definition/method, not the return value!
        
        self.clear = self.findChild(QtWidgets.QPushButton, 'clearButton') # Find the button
        self.clear.clicked.connect(self.clearButtonPressed) # Remember to pass the definition/method, not the return value!
        # Button
        self.add = self.findChild(QtWidgets.QPushButton, 'addDBButton') # Find the button
        
        self.pbar = self.findChild(QtWidgets.QProgressBar, 'StatusBar')
        self.pbar.setValue(0)

        # Liste 
        self.input = self.findChild(QtWidgets.QListWidget, 'Ausgabe')
        self.input.itemClicked.connect(self.lWdgPressed) # Remember to pass the definition/method, not the return value!

        # Labels
        self.label = self.findChild(QtWidgets.QLabel, 'Hinweis')
        self.Ordner = self.findChild(QtWidgets.QLabel, 'Ordnername')
        self.Status = self.findChild(QtWidgets.QLabel, 'Status') # Find the button
        self.c =self.findChild(QtWidgets.QLabel, 'Count')
        #self.DateiAusgabe1 = self.findChild(QtWidgets.QLabel, 'Ausgabe1')
        # Ausgabe
        self.show()

    def Suchen(self):
        self.Such_W = QtWidgets.QWidget()
        self.ui = Ui_Suche()
        self.ui.setupUi(self.Such_W)
        self.Such_W.show()
    def Aendern(self):
        self.Aendern_W = QtWidgets.QWidget()
        self.ui = Ui_Aendern()
        self.ui.setupUi(self.Aendern_W)
        self.Aendern_W.show()
    
    # clear
    def clearButtonPressed(self):        
        self.label.setText("nichts getan !")  
        self.Ordner.clear()                    
        self.input.clear()

    # StatusLabel für DB_Pornos.py


    # starte
    def openButtonPressed(self):
        dname = str(self.DirDialog())         
        DSatz=[]       
        i=0;add=0;value=0
        self.pbar.setValue(0)
        self.clear.setEnabled(False)
        

        c=sum(len(files) for _, _, files in os.walk(dname))
        if os.path.exists(dname):
            self.Ordner.setText(dname)           
            self.input.clear()
            
            for root,dir,files in os.walk(dname,"*,mp4"):
                r=root.replace('/','\\')                          
                for filename in files:
                    value += 1
                    self.pbar.setValue(int(value/c*100)) 
                    self.Status.setText(filename)
                    self.c.setText(str(value)+' von '+str(c))
                    #self.Lese.setText("Abbruch")
                    #self.Lese.clicked.connect(self.breakButtonPressed)
                    QtWidgets.QApplication.processEvents()                                                       
                    DIR=os.path.join(r,filename)                    
                    DSatz=self.FileDetails(i,filename,DIR)
                    if self.isinDB(DIR) == False:
                        self.addDB(DSatz)                       
                        
                        add += 1                   
                        
                    i += 1                        
                    self.input.insertItem(0, filename )
                    
                    self.label.setText(str(add) + " Datensätze \ngeaddet!")            
        
            self.Lese.setText("Start")      
            self.clear.setEnabled(True)
            
        
    def breakButtonPressed(self):
        self.Lese.setText("Start")
        
    def lWdgPressed(self):        
        self.DateiAusgabe1.setText('') 
        self.DateiAusgabe2.setText('')
        self.DateiAusgabe3.setText('')
        self.DateiAusgabe4.setText('')
        self.DateiAusgabe5.setText('')      

        #self.FileDetails(Dalt)
        

            # Öffne Dateiname
    def DirDialog(self,directory='D:\\'):
        dialog = QtWidgets.QFileDialog(self,"Ordner öffnen")
        dialog.setAcceptMode(QtWidgets.QFileDialog.AcceptOpen)
        dialog.setDirectory(directory)
        dialog.setFileMode(QtWidgets.QFileDialog.Directory)
        dialog.setOption(QtWidgets.QFileDialog.ShowDirsOnly, True)
        dialog.setViewMode(QtWidgets.QFileDialog.Detail)        

        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            dirname = dialog.selectedFiles()[0]  # returns a list
            return dirname 

    def FileDetails(self,index,mp4file,DIR):
        Firma=""; Titel=""; Darstin="";Darst""
        Datum="";Erklaerung="";Art="";Hoehe=0;Breite=0
        Dauer="";Groesse="";Bild="";Bitrate="";Sprache=0
        TheShell = win32com.client.gencache.EnsureDispatch('Shell.Application',0)
        AFolder = TheShell.NameSpace(os.path.dirname(DIR))
        AFile = AFolder.ParseName(os.path.basename(DIR)) 
        # Filename aufsplitten
        Datei = mp4file[0:len(mp4file)-4]
        if ' - ' in Datei:
            Firma = Datei[0:Datei.find(' - ')]
            Datei = Datei[Datei.find(' - ')+3:len(Datei)]            
            #self.DateiAusgabe1.setText('1:' + Firma) 
        # Titel und Name erkennen und löschen 
        if '-' in Datei:
            Titel = Datei[0:Datei.find('-')]
            Datei = Datei[Datei.find('-')+1:len(Datei)]
            #self.DateiAusgabe3.setText('3:' + Titel)         
        # (720p) erkennen und löschen
        if 'p)' in Datei:
            Bild = Datei[len(Datei)-6:len(Datei)]
            Datei = Datei[0:len(Datei)-6]
            #self.DateiAusgabe5.setText('5:' + Bild) 
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
        # [ANAL Teen] erkennen und löschen 
        if "[" and "]" in Datei:
            Art = Datei[Datei.rfind('['):Datei.rfind(']')+1]
            Datei = Datei[0:Datei.rfind('[')]
            #self.DateiAusgabe4.setText('4:' + Art)  
            
        if mp4file +'.mp4' == Datei:
            self.label.setText(Datei + '\nHat kein formatierenten Zeichen ') 

        Groesse=AFolder.GetDetailsOf(AFile,1)
        # print ("Größe : " + Darst1)
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
        # print ("Länge : " + Laenge)
        # print ("Interpret : " + AFolder.GetDetailsOf(AFile,13))
        # print ("Jahr : " + AFolder.GetDetailsOf(AFile,15))
        # print ("Genre : " + AFolder.GetDetailsOf(AFile,16))
        # print ("Markierungen : " + AFolder.GetDetailsOf(AFile,18))
        # print ("Titel : " + AFolder.GetDetailsOf(AFile,21))
        # print ("Kommentare : " + AFolder.GetDetailsOf(AFile,24))
        
        return [DIR,Firma,Titel,Sprache,Datei,Darstin,Darst,Art,Hoehe,Breite,Dauer,Bitrate,Groesse,Datum,Erklaerung]
    """
        Hier sind die Datenbanken Kommandos
        addDB
        isinDB

    """
    def addDB(self, Dsatz=[]):        
        self.Obj = DB_Pornos() 
        self.Obj.addPorns(Dsatz[0],Dsatz[1],Dsatz[2],Dsatz[3],Dsatz[4],Dsatz[5],Dsatz[6],Dsatz[7],Dsatz[8],Dsatz[9],Dsatz[10],Dsatz[11],Dsatz[12],Dsatz[13],Dsatz[14])
    
    def isinDB(self,DIR):
        self.Obj = DB_Pornos()       
        return self.Obj.SuchDB(DIR)

    def closeEvent(self,event):
        reply=QtWidgets.QMessageBox.question(self,'Message',"Are you sure to quit?",QtWidgets.QMessageBox.Yes,QtWidgets.QMessageBox.No)
        if reply==QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    
    MainWindow = Haupt_Fenster()
    MainWindow.setWindowIcon(QtGui.QIcon('icon.ico'))
    sys.exit(app.exec_())

  


