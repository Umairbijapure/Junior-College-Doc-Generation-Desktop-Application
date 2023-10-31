from tkinter import *
from PIL import Image, ImageTk
from homePage import SSA
from tkinter import messagebox
import sqlite3


def EA1_db() :
    con = sqlite3.connect(database="rms.db")
    cur = con.cursor()
    #con.execute('DELETE FROM studentTable')
    cur.execute(
        "CREATE TABLE IF NOT EXISTS studentTable(grno INTEGER PRIMARY KEY AUTOINCREMENT,roll text,name text,email text,gender text,dob text,contact text,mother text,class text,std text,city text,state text,pin text,address text)")
    con.commit()

    cur.execute(
        """CREATE TABLE IF NOT EXISTS marksTable(grno INTEGER PRIMARY KEY AUTOINCREMENT,roll,ET1 INT,ET2 INT, ET3 INT, ET4 INT, ET5 INT, ET6 INT, ET7 INT, ET8 INT, ET9 INT, ET10 INT,ET11 INT,ET12 INT,ET13 INT,ET14 INT,ET15 INT,ET16 INT,ET17 INT,ET18 INT,ET19 INT,ET20 INT,ET21 INT,ET22 INT,ET23 INT,ET24 INT,ET25 INT,ET26 INT,ET27 INT,ET28 INT,ET29 INT,ET30 INT,ET31 INT,ET32 INT,ET33 INT,ET34 INT,ET35 INT,ET36 INT,ET37 INT,ET38 INT,ET39 INT,ET40 INT,ET41 INT,ET42 INT,ET43 INT,ET44 INT,ET45 INT,ET46 INT,ET47 INT,ET48 INT,ET49 INT,ET50 INT,ET51 INT,ET52 INT,ET53 INT,ET54 INT,Cs_2_1 INT,Cs_2_2 INT,Cs_2_3 INT,Cs_2_4 INT,Cs_2_5 INT,Cs_2_6 INT,class text,name text,env text,pe text)""")
    con.commit()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS courseTable(grno INTEGER PRIMARY KEY AUTOINCREMENT,roll text,Class text,English text,Physics text,Chemistry text,Maths text,Biology text,Geo text,Urdu text,Hindi text,CS text)")
    con.commit()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS resultTable(grno INTEGER PRIMARY KEY AUTOINCREMENT,roll text,Std text,Class text,Math text,Bio text,Phy text,Chem text,Urdu text,Eng text,Hin text,Geo text,Cs1 text,Cs2 text,env text,pe text,date text,result text,grandtotal text,perc text,grade text,name text,adress text,reop text)")
    con.commit()

    Table_Query = '''CREATE TABLE if not Exists bqkTablee 
                (ebc_cast TEXT,age TEXT,mothers_name TEXT,
                ht TEXT,grno INT,date_of_birth TEXT,roll_no REAL,students_name varchar,B TEXT,C TEXT,D TEXT)'''

    cur.execute(Table_Query)
    con.commit()

    con.close()


EA1_db()
class standardClass:
    def __init__(self, window):
        self.window = window
        self.window.title("SSA Result Management System")
        self.window.geometry("1500x800+30+30")
        self.window.config(bg="#d9f1ff")
        # ICONS
        img = (Image.open("assets/logo.png"))
        resized_image = img.resize((59, 59))
        self.logo_dash = ImageTk.PhotoImage(resized_image)

        # footer
        title = Label(self.window,text="SSA Result Management System\nContact us for any technical issue:Umer Bijapure-7020152273",font=("goudy old stlye", 10), bg="#87CEFA", fg="White").pack(side=BOTTOM, fill=X)
        self.image1 = Image.open("assets/A.jpeg")
        #self.image1 = self.image1.resize((920, 350))
        self.image1 = ImageTk.PhotoImage(self.image1)
        self.label_image1 = Label(self.window, image=self.image1,bg="#eBffff").place(x=370, y=60, width=1000, height=700)


        # widgets
        title = Label(self.window, text="SSA Result Management System", padx=10, compound=LEFT, image=self.logo_dash,font=("goudy old stlye", 20, "bold"), bg="#87CEFA", fg="White").place(x=0, y=0, relwidth=1,height=50)
        #btn_std = Button(self.window, text="Class A", font=("goudym old style", 15), bg="#0b5377", fg="white",
                         #cursor="hand2", command=self.std11).place(x=160, y=170, width=170, height=35)
        btn_std = Button(self.window, text="Let's Get Started", font=("goudym old style", 15), bg="#0b5377", fg="white",
                         cursor="hand2", command=self.std11).place(x=375, y=200, width=200, height=35)
        btn_all_students = Button(self.window, text="Drop All Data", font=("goudym old style", 15), bg="#0b5377", fg="white",cursor="hand2", command=self.drop_all).place(x=375, y=300, width=200, height=35)



    def drop_all(self):
        conn = sqlite3.connect('rms.db')
        c = conn.cursor()
        op = messagebox.askyesno("Confirm", "Do you really wanto to Drop All?", parent=self.window)
        c.execute('DROP TABLE studentTable')
        c.execute('DROP TABLE marksTable')
        c.execute('DROP TABLE courseTable')
        c.execute('DROP TABLE resultTable')
        c.execute('DROP TABLE  bqkTablee')
        conn.commit()
        conn.close()

    def std11(self):
        self.new_win = Toplevel(self.window)
        self.obj1 = SSA(self.new_win)

    '''def std12(self):
        self.new_win = Toplevel(self.window)
        self.obj2 = SSA(self.new_win)'''


if __name__ == "__main__":
    window = Tk()
    obj = standardClass(window)
    window.mainloop()
