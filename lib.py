from sqlite3 import *
#from tkinter import *
#from tkinter import messagebox

# Class bibliothéque ________________________________________________________________________________________________________________
# Dans ton constructeur (__init__), j'ai essaye de comprendre ce que tu as voulu faire avec "name_table"
# dans mes appels a la fin du fichier, je fais:
#  b = biblihotheque("test.db", "lol")
#
# J'imagine que "lol" c'est le nom de ta table principale? Si c'est le cas, alors j'ai rajoute
# les "... {} ...".format(self.name_table) qui vont bien.
# Par contre, il ne faut pas confondre le formatting des chaines de caracteres (strings) avec
# " ? " (point d'interrogation) dans les INSERTs qui sont interpretes par sqlite lui meme
class biblihotheque:
    def __init__(self, db_file, name_table):
        self.db_file = db_file
        self.name_table = name_table
        print("démarage de la class biblihotéque ;)")
        con = connect(self.db_file)
        cur = con.cursor()
        # Create table
        cur.execute('CREATE TABLE IF NOT EXISTS {} (Table_name text)'.format(self.name_table))

        con.commit()
        con.close()

    def get_base_info(self):
        return self.db_file

    def get_table(self):
        return self.name_table

# Ouverture d'une base de donné -----------------------------------------------------------------------------------------------------

    # A quoi elle sert cette methode ?
    # tu veux ouvrir la DB? dans ce cas la, tu fais un connect.
    def open(self):
        try:
            conection = connect(self.db_file)
            cursorr = conection.cursor()
            req = cursorr.execute('SELECT Table_name FROM {}'.format(self.name_table))
            vallue = req.fetchall()
            number_bibli = len(vallue)
            print(number_bibli)
        except:
            print("Nom de la base non valide !!")
            #warning = messagebox.showerror("Erreur_base_de_donné", "Veuillez entrer un nom de base\n de donné valide :(")

# Ajout d'une biblihothéque ---------------------------------------------------------------------------------------------------------

    def add_table(self, new_table):
        con = connect(self.db_file)
        cur = con.cursor()
        results = cur.execute('SELECT Table_name FROM {}'.format(self.name_table))
        values = results.fetchall()

        if (new_table,) in values:
            print("La biblihothéque exsiste deja !")
            #warning = messagebox.showerror("Erreur_table", "La biblihothéque exsiste deja !")

        else:
            print("La biblihothéque {} n'exsiste pas.".format(new_table))
            cur.execute("INSERT INTO {} VALUES(?)".format(self.name_table), (new_table, ))
            cur.execute("CREATE TABLE IF NOT EXISTS {}(id INTEGER PRIMARY KEY AUTOINCREMENT, TITRE TEXT NOT NULL, PAGES TEXT NOT NULL, ETAT TEXT NOT NULL, COLLECTION TEXT NOT NULL, ANNEE TEXT NOT NULL)".format(new_table))
        con.commit()
        con.close()

# Supretion d'une biblihotéque ------------------------------------------------------------------------------------------------------

    # Je pense que ton soucis etait la:
    # Tu voulais avoir une table principale qui reference d'autres tables -> OK
    # Par contre, avec SQLite, il y a des regles a respecter:
    #  - tu ouvres pas 15 connections en meme temps,
    #  - tu ouvres une porte, tu fermes la porte, les connections, c'est la meme
    #  - Quand tu executes des commandes, il faut commit pour que ce soit pris en compte
    def delete_table(self, delete_table_name):
        con = connect(self.db_file)
        cur = con.cursor()
        cur.execute('DROP TABLE IF EXISTS {}'.format(delete_table_name))
        cur.execute("DELETE FROM {} WHERE Table_name = ?".format(self.name_table), (delete_table_name, ))
        con.commit()
        con.close()
        print("Drop table done")

# Connection a une biblihothéque ------------------------------------------------------------------------------------------------------

    def connection_table(self, open_table):
        self.open_table = open_table
        conection1 = connect(self.db_file)
        cursorr1 = conection1.cursor()
        req1 = cursorr1.execute('SELECT Table_name FROM {}'.format(self.name_table))
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
            #messagebox.showerror("ERREUR_DE_BIBLIHOTEQUE", "Aucune biblihotéque ne porte ce nom")


b = biblihotheque("test.db", "lol")
b.add_table("table_1")
b.add_table("table_1")
b.delete_table("table_1")
