from sqlite3 import *
from tkinter import *
from tkinter import messagebox
 
# Class bibliothéque ________________________________________________________________________________________________________________
 
class biblihotheque:
    def __init__(self, name_base_info, name_table):
        self.name_base_info = name_base_info
        self.name_table = name_table
        print("démarage de la class biblihotéque ;)")
 
    def get_base_info(self):
        return self.name_base_info
 
    def get_table(self):
        return self.name_table
 
# Ouverture d'une base de donné -----------------------------------------------------------------------------------------------------
 
    def open(self):
        try:
            conection = connect(self.name_base_info)
            cursorr = conection.cursor()
            req = cursorr.execute('SELECT Table_name FROM db_names_bases')
            vallue = req.fetchall()
            number_bibli = len(vallue)
            print(number_bibli)
        except:
            print("Nom de la base non valide !!")
            warning = messagebox.showerror("Erreur_base_de_donné", "Veuillez entrer un nom de base\n de donné valide :(")
 
# Ajout d'une biblihothéque ---------------------------------------------------------------------------------------------------------
    
    def add_table(self, new_table):
        biblihotheque.open(self)
        self.new_table = new_table
        table = (self.new_table,)
 
        conection1 = connect(self.name_base_info)
        cursorr1 = conection1.cursor()
        req1 = cursorr1.execute('SELECT Table_name FROM db_names_bases')
        vallue1 = req1.fetchall()
 
        if table in vallue1:
            print("La biblihothéque exsiste deja !")
            warning = messagebox.showerror("Erreur_table", "La biblihothéque exsiste deja !")
 
        else:
            print("La biblihothéque {} n'exsiste pas.".format(self.new_table))
            conect = connect(self.name_base_info)
            cursor1 = conect.cursor()
            new_proj = (cursor1.lastrowid, self.new_table)
            req2 = cursor1.execute('INSERT INTO db_names_bases VALUES(?,?)', (new_proj))
            conect.commit()
            new_table = cursor1.execute("CREATE TABLE IF NOT EXISTS {}(id INTEGER PRIMARY KEY AUTOINCREMENT, TITRE TEXT NOT NULL, PAGES TEXT NOT NULL, ETAT TEXT NOT NULL, COLLECTION TEXT NOT NULL, ANNEE TEXT NOT NULL)".format(self.new_table))
            conect.commit()
                
# Supretion d'une biblihotéque ------------------------------------------------------------------------------------------------------
    
    def delete_table(self, delete_table_name):
        self.delete_table_name = delete_table_name
        try:
            conection = connect(self.name_base_info)
            cursor1 = conection.cursor()
            req1 = cursor1.execute('DROP TABLE {}'.format(self.delete_table_name))
            conection.commit()
            print("Table efacer")
        except:
            print("La table n'exsiste pas!")
 
# Connection a une biblihothéque ------------------------------------------------------------------------------------------------------
 
    def connection_table(self, open_table):
        self.open_table = open_table
        conection1 = connect(self.name_base_info)
        cursorr1 = conection1.cursor()
        req1 = cursorr1.execute('SELECT Table_name FROM db_names_bases')
        vallue1 = req1.fetchall()
        vallue_open = (open_table,)
        if vallue_open in vallue1:
            try:
                print("Ouverture de la biblihothéque {}".format(open_table))
                req2 = cursorr1.execute('SELECT * FROM {}'.format(self.open_table))
                bibli_vallues = req2.fetchall()
                print(bibli_vallues)
            except:
                print("Ouverture de la table impossible")
 
        else:
            print("Nom de biblihotéque non valide")
            messagebox.showerror("ERREUR_DE_BIBLIHOTEQUE", "Aucune biblihotéque ne porte ce nom")-
