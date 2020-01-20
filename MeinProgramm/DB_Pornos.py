import sqlite3,os,sys,hashlib



"""
    Datenbank für meine Pornos
    DB_Pornos
        addPorns(nummer)
        getPorns(Interpret,Name,Darsteller,Art,Bild,Cover)
        delPorns(nummer)
        getPorns
"""
class DB_Pornos:
    """
        Destrukter zum freigeben
    """
    def  __init__(self):
        #PATHS = str(os.path.dirname(os.path.abspath(__file__)))
        self.conn =sqlite3.connect('MeinPornos.db')        
        self.c =self.conn.cursor()

    def md5sum(self,filename, blocksize=65536):
        hash = hashlib.md5()
        with open(filename, "rb") as f:
            for block in iter(lambda: f.read(blocksize), b""):
                hash.update(block)
        return hash.hexdigest()    
    """
        addPorns erstellen
    """

    def addPorns(self,DIR,Firma,Titel,Darstin,Darst,Art,Sprache,Hoehe,Breite,Dauer,Bitrate,Groesse,Datum,Erklaerung):        
        assert(isinstance(Firma,str))
        assert(isinstance(Titel,str))
        assert(isinstance(Darstin,str))
        assert(isinstance(Art,str))
        # assert(isinstance(Bildhoehe,str))
        # assert(isinstance(Bildbreite,str))
        # assert(isinstance(Cover,str)) 
        Hash=self.md5sum(DIR)
        staff_data = [ (DIR,Firma,Titel,Darstin,Darst,Art,Sprache,Hoehe,Breite,Dauer,Bitrate,Groesse,Datum,Erklaerung,Hash) ]   
                    
        for p in staff_data:
            format_str = """INSERT INTO dbdaten (ID, Dateiname, Firma, Titel, Darstellerin, Darsteller, Art, Sprache, Bildhoehe, Bildbreite, Dauer, Bitrate, Groesse, Datum, Erklaerung,Hash) VALUES (NULL, "{Dateiname}", "{Firma}", "{Titel}", "{Darstellerin}", "{Darsteller}", "{Art}", "{Sprache}", "{Bildhoehe}", "{Bildbreite}", "{Dauer}", "{Bitrate}", "{Groesse}","{Datum}", "{Erklaerung}", "{Hash}");"""
            sql_command = format_str.format(Dateiname=p[0], Firma=p[1], Titel=p[2],Darstellerin=p[3], Darsteller=p[4], Art=p[5], Sprache=p[6], Bildhoehe=p[7], Bildbreite=p[8], Dauer=p[9], Bitrate=p[10], Groesse=p[11],Datum=p[12],Erklaerung=p[13], Hash=p[14])
            self.c.execute(sql_command)                    
            self.conn.commit() 
                  
            self.conn.close()
        return Hash

    def UpdatePorns(self,DIR,Firma,Titel,Darstin,Darst,Art,Sprache,Hoehe,Breite,Dauer,Bitrate,Groesse,Datum,Erklaerung): 
        assert(isinstance(Firma,str))
        assert(isinstance(Titel,str))
        assert(isinstance(Darstin,str))
        assert(isinstance(Art,str))   
        staff_data = [ (DIR,Firma,Titel,Darstin,Darst,Art,Sprache,Datum,Erklaerung) ]               
        for p in staff_data:
            format_str = """UPDATE dbdaten SET Firma = "{Firma}", Titel = "{Titel}", Darstellerin = "{Darstellerin}", Darsteller = "{Darsteller}", Art = "{Art}", Sprache = "{Sprache}", Datum = "{Datum}", Erklaerung = "{Erklaerung}" WHERE Dateiname = "{Dateiname}";"""
            
            sql_command = format_str.format(Dateiname=p[0], Firma=p[1], Titel=p[2],Darstellerin=p[3], Darsteller=p[4], Art=p[5], Sprache=p[6], Datum=p[7],Erklaerung=p[8])
            
            self.c.execute(sql_command)                    
            self.conn.commit() 
                  
            self.conn.close() 
            

    def DatenHolen(self,DIR):
        assert(isinstance(DIR,str))  
        staff_data =  (DIR)                      
        
        format_str = """SELECT Firma, Titel, Darstellerin, Darsteller, Art, Sprache, Datum, Erklaerung, Hash FROM dbdaten WHERE Dateiname = "{Dateiname}";"""
        sql_command = format_str.format(Dateiname=staff_data)
         
        try:
            self.c.execute(sql_command)             
            self.conn.commit() 
            Ausgabe=self.c.fetchall()
            #for row in self.c.fetchall():
            #    Ausgabe.append(str(row[0]))              
        except sqlite3.Error as e:
            Ausgabe=e.format(e.args[0])                          
        self.conn.close() 
        return Ausgabe 
 
    def SuchDB(self,Dateiname,Dauer):
        Dauer_DB=""
        assert(isinstance(Dateiname,str)) 
        staff_data = (Dateiname)        
        format_str = """SELECT Dateiname, Dauer, Hash FROM dbdaten WHERE Dateiname = "{Dateiname}";""" 
        sql_command = format_str.format(Dateiname=staff_data)                
        self.c.execute(sql_command) 
        rows = self.c.fetchall()
        
        if len(rows) > 0:
            for inhalt in rows:
                print(inhalt)
                Datei_DB=inhalt[0]
                Dauer_DB=inhalt[1]
                Hash_DB=inhalt[2]
        else:
            
            return 2
            #rows=rows[3:len(str(rows))-4]                             
        self.conn.commit()        
        self.conn.close()

        
        if os.path.exists(str(Dateiname)) == True:
            print(Dauer+Dauer_DB)
            if Dauer==Dauer_DB:
                return 1            
        else:            
            Hash=self.md5sum(Dateiname)
            format_str = """SELECT Hash FROM dbdaten WHERE Dateiname="{Hash}";""" 
            sql_command = format_str.format(Hash)                
            self.c.execute(sql_command) 
            Hash_DB = str(self.c.fetchall())
            self.conn.commit()        
            self.conn.close()
            if Hash!=Hash_DB:
                return 2
            else:
                Datei=Dateiname[:Dateiname.rfind("\\")]
                Datei1=Datei_DB[:Datei_DB.rfind("\\")]
                if Datei==Datei1:
                    return 3
                else:
                    return 4
        print("fuck you")

    def SuchHash(self,Dateiname,Hash):
        assert(isinstance(Hash,str))                      
        staff_data = [ (Dateiname,Hash) ]         
        for p in staff_data:   
            format_str = """UPDATE dbdaten SET Dateiname = "{Dateiname}" WHERE Hash = "{Hash}";"""     
            sql_command = format_str.format(Dateiname=p[0], Hash=p[1])
        
            self.c.execute(sql_command)                    
            self.conn.commit() 
                    
            self.conn.close() 




if __name__ == "__main__":
	print("Datei wurde direkt aufgerufen und die Main wird ausgeführt")
else:
	print("Datei wurde als Modul aufgerufen")
print("Ich stehe in der Datei: " + __name__)    