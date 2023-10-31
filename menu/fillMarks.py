from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
from PyPDF2 import PdfFileWriter, PdfFileReader
import io
import math
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

class class_marks:

    def __init__(self,window):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        cur.execute(
            """CREATE TABLE IF NOT EXISTS marksTable(grno INTEGER PRIMARY KEY AUTOINCREMENT,roll,ET1 INT,ET2 INT, ET3 INT, ET4 INT, ET5 INT, ET6 INT, ET7 INT, ET8 INT, ET9 INT, ET10 INT,ET11 INT,ET12 INT,ET13 INT,ET14 INT,ET15 INT,ET16 INT,ET17 INT,ET18 INT,ET19 INT,ET20 INT,ET21 INT,ET22 INT,ET23 INT,ET24 INT,ET25 INT,ET26 INT,ET27 INT,ET28 INT,ET29 INT,ET30 INT,ET31 INT,ET32 INT,ET33 INT,ET34 INT,ET35 INT,ET36 INT,ET37 INT,ET38 INT,ET39 INT,ET40 INT,ET41 INT,ET42 INT,ET43 INT,ET44 INT,ET45 INT,ET46 INT,ET47 INT,ET48 INT,ET49 INT,ET50 INT,ET51 INT,ET52 INT,ET53 INT,ET54 INT,Cs_2_1 INT,Cs_2_2 INT,Cs_2_3 INT,Cs_2_4 INT,Cs_2_5 INT,Cs_2_6 INT,class text,name text,env text,pe text)""")
        con.commit()
        con.close()
        self.window=window
        self.window.title("Add Student's Marks")
        self.window.geometry("1350x800+80+50")
        self.window.config(bg="#eBffff")
        self.window.focus_force()
        #title = Label(self.window, text="Add Student", padx=10,font=("goudy old stlye", 20, "bold"), bg="#87CEFA", fg="White").place(x=0, y=0, relwidth=1,height=50)
        title = Label(self.window, text="Please fill up Marks ", padx=10,font=("goudy old stlye", 15, "bold"), bg="#87CEFA", fg="white").place(x=0, y=0, relwidth=1,height=30)

        self.var_grno=StringVar()
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_std = StringVar()
        self.var_class=StringVar()
        self.grno_list=[]
        self.fetch_grno()

        self.var_ET1 = IntVar()
        self.var_ET2 = IntVar()
        self.var_ET3 = IntVar()
        self.var_ET4 = IntVar()
        self.var_ET5 = IntVar()
        self.var_ET6 = IntVar()
        self.var_ET7 = IntVar()
        self.var_ET8 = IntVar()
        self.var_ET9 = IntVar()
        self.var_ET10 = IntVar()
        self.var_ET11 = IntVar()
        self.var_ET12 = IntVar()
        self.var_ET13 = IntVar()
        self.var_ET14 = IntVar()
        self.var_ET15 = IntVar()
        self.var_ET16 = IntVar()
        self.var_ET17 = IntVar()
        self.var_ET18 = IntVar()
        self.var_ET19 = IntVar()
        self.var_ET20 = IntVar()
        self.var_ET21 = IntVar()
        self.var_ET22 = IntVar()
        self.var_ET23 = IntVar()
        self.var_ET24 = IntVar()
        self.var_ET25 = IntVar()
        self.var_ET26 = IntVar()
        self.var_ET27 = IntVar()
        self.var_ET28 = IntVar()
        self.var_ET29 = IntVar()
        self.var_ET30 = IntVar()
        self.var_ET31 = IntVar()
        self.var_ET32 = IntVar()
        self.var_ET33 = IntVar()
        self.var_ET34 = IntVar()
        self.var_ET35 = IntVar()
        self.var_ET36 = IntVar()
        self.var_ET37 = IntVar()
        self.var_ET38 = IntVar()
        self.var_ET39 = IntVar()
        self.var_ET40 = IntVar()
        self.var_ET41 = IntVar()
        self.var_ET42 = IntVar()
        self.var_ET43 = IntVar()
        self.var_ET44 = IntVar()
        self.var_ET45 = IntVar()
        self.var_ET46 = IntVar()
        self.var_ET47 = IntVar()
        self.var_ET48 = IntVar()
        self.var_ET49 = IntVar()
        self.var_ET50 = IntVar()
        self.var_ET51 = IntVar()
        self.var_ET52 = IntVar()
        self.var_ET53 = IntVar()
        self.var_ET54 = IntVar()
        self.var_Cs2_1 = IntVar()
        self.var_Cs2_2 = IntVar()
        self.var_Cs2_2 = IntVar()
        self.var_Cs2_3 = IntVar()
        self.var_Cs2_4 = IntVar()
        self.var_Cs2_5 = IntVar()
        self.var_Cs2_6 = IntVar()
        
        self.filenam_raw_entry1=StringVar()
        self.var_env=StringVar()
        self.var_pe =StringVar()
        self.t_name=StringVar()
        #self.n=IntVar()






        # widgets
        lbl_select = Label(self.window, text="GRNo:", font=("goudy old style", 15, "bold"), bg='#eBffff').place(x=20,y=35,height=50)
        lbl_roll = Label(self.window, text="Roll No:", font=("goudy old style", 15, "bold"), bg='#eBffff').place(x=400,y=30,height=50)
        lbl_name = Label(self.window, text="Name:", font=("goudy old style", 15, "bold"), bg='#eBffff').place(x=20,y=70,height=50)
        lbl_std = Label(self.window, text="Std:", font=("goudy old style", 15, "bold"), bg='#eBffff').place(x=20,y=105,height=50)
        lbl_class=Label(self.window, text="Class:", font=("goudy old style", 15, "bold"), bg='#eBffff').place(x=350,y=97,height=50)
        lbl_math = Label(self.window, text="Mathematics:", font=("goudy old style", 15, "bold"), bg='#eBffff').place(x=20,y=160,height=50)
        lbl_bio = Label(self.window, text="Biology:", font=("goudy old style", 15, "bold"), bg='#eBffff').place(x=20,y=200,height=50)
        lbl_phy = Label(self.window, text="Physics:", font=("goudy old style", 15, "bold"), bg='#eBffff').place(x=20,y=240,height=50)
        lbl_chem = Label(self.window, text="Chemistry:", font=("goudy old style", 15, "bold"), bg='#eBffff').place(x=20,y=280,height=50)
        lbl_urdu = Label(self.window, text="Urdu:", font=("goudy old style", 15, "bold"), bg='#eBffff').place(x=20,y=320,height=50)
        lbl_eng = Label(self.window, text="English:", font=("goudy old style", 15, "bold"), bg='#eBffff').place(x=20,y=360,height=50)
        lbl_hindi = Label(self.window, text="Hindi:", font=("goudy olds style", 15, "bold"), bg='#eBffff').place(x=20,y=400,height=50)
        lbl_geo = Label(self.window, text="Geography:", font=("goudy old style", 15, "bold"), bg='#eBffff').place(x=20,y=440,height=50)
        lbl_cs1 = Label(self.window, text="CS1:", font=("goudy old style", 15, "bold"), bg='#eBffff').place(x=20,y=480,height=50)
        lbl_cs2 = Label(self.window, text="CS2:", font=("goudy old style", 15, "bold"), bg='#eBffff').place(x=20,y=520,height=50)
        lbl_env= Label(self.window, text="Envi:", font=("goudy old style", 15, "bold"), bg='#eBffff').place(x=20,y=565,height=20)
        lbl_pe = Label(self.window, text="PE:", font=("goudy old style", 15, "bold"), bg='#eBffff').place(x=350,y=565,height=20)
        self.txt_env = Entry(self.window, textvariable=self.var_env, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_env.place(x=180, y=560, width=80)
        self.txt_pe = Entry(self.window, textvariable=self.var_pe, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_pe.place(x=400, y=560, width=80)
        lbl_file_name=Label(self.window, text="File name:", font=("goudy old style", 15, "bold"), bg='#eBffff').place(x=20,y=640,height=50)
        lbl_file_name=Label(self.window, text="Teacher's name:", font=("goudy old style", 15, "bold"), bg='#eBffff').place(x=20,y=680,height=50)
        #lbl_page_no=Label(self.window, text="Pages:", font=("goudy old style", 15, "bold"), bg='#eBffff').place(x=20,y=640,height=50)
        
        lbl_t1 = Label(self.window, text="UT1", font=("goudy old style", 10, "bold"), bg='#eBffff').place(x=205,y=138,height=20)
        lbl_mid = Label(self.window, text="Mid Term", font=("goudy old style", 10, "bold"), bg='#eBffff').place(x=282,y=138,height=20)
        lbl_t2 = Label(self.window, text="UT2", font=("goudy old style", 10, "bold"), bg='#eBffff').place(x=402,y=138,height=20)
        lbl_final  = Label(self.window, text="Final", font=("goudy old style", 10, "bold"), bg='#eBffff').place(x=498,y=138,height=20)
        lbl_prac  = Label(self.window, text="oral/practical", font=("goudy old style", 10, "bold"), bg='#eBffff').place(x=578,y=138,height=20)
        lbl_total = Label(self.window, text="Total", font=("goudy old style", 10, "bold"), bg='#eBffff').place(x=690,y=138,height=20)

        #Entries
        self.txt_student = ttk.Combobox(self.window, textvariable=self.var_grno,values=self.grno_list, font=("goudy old style", 15, "bold"), justify=CENTER)
        self.txt_student.place(x=180, y=40, width=150)
        self.txt_student.set("Select")
        self.txt_roll = Entry(self.window, textvariable=self.var_roll, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_roll.place(x=500, y=40, width=150)
        self.txt_name = Entry(self.window, textvariable=self.var_name, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_name.place(x=180, y=75, width=400)

        self.txt_std = Entry(self.window, textvariable=self.var_std, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_std.place(x=180, y=110, width=120)

        self.txt_class = Entry(self.window, textvariable=self.var_class, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_class.place(x=420, y=110, width=120)


        self.txt_E1 = Entry(self.window, textvariable=self.var_ET1, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E1.place(x=180, y=160, width=80)

        self.txt_E2 = Entry(self.window, textvariable=self.var_ET2, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E2.place(x=180, y=200, width=80)

        self.txt_E3 = Entry(self.window, textvariable=self.var_ET3, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E3.place(x=180, y=240, width=80)

        self.txt_E4 = Entry(self.window, textvariable=self.var_ET4, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E4.place(x=180, y=280, width=80)

        self.txt_E5 = Entry(self.window, textvariable=self.var_ET5, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E5.place(x=180, y=320, width=80)

        self.txt_E6 = Entry(self.window, textvariable=self.var_ET6, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E6.place(x=180, y=360, width=80)

        self.txt_E7 = Entry(self.window, textvariable=self.var_ET7, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E7.place(x=180, y=400, width=80)

        self.txt_E8 = Entry(self.window, textvariable=self.var_ET8, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E8.place(x=180, y=440, width=80)

        self.txt_E9 = Entry(self.window, textvariable=self.var_ET9, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E9.place(x=180, y=480, width=80)

        self.txt_E10 = Entry(self.window, textvariable=self.var_ET10, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E10.place(x=280, y=160, width=80)

        self.txt_E11 = Entry(self.window, textvariable=self.var_ET11, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E11.place(x=280, y=200, width=80)

        self.txt_E12 = Entry(self.window, textvariable=self.var_ET12, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E12.place(x=280, y=240, width=80)

        self.txt_E13 = Entry(self.window, textvariable=self.var_ET13, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E13.place(x=280, y=280, width=80)

        self.txt_E14 = Entry(self.window, textvariable=self.var_ET14, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E14.place(x=280, y=320, width=80)

        self.txt_E15 = Entry(self.window, textvariable=self.var_ET15, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E15.place(x=280, y=360, width=80)

        self.txt_E16= Entry(self.window, textvariable=self.var_ET16, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E16.place(x=280, y=400, width=80)

        self.txt_E17 = Entry(self.window, textvariable=self.var_ET17, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E17.place(x=280, y=440, width=80)

        self.txt_E18 = Entry(self.window, textvariable=self.var_ET18, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E18.place(x=280, y=480, width=80)

        self.txt_E19 = Entry(self.window, textvariable=self.var_ET19, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E19.place(x=380, y=160, width=80)

        self.txt_E20 = Entry(self.window, textvariable=self.var_ET20, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E20.place(x=380, y=200, width=80)

        self.txt_E21 = Entry(self.window, textvariable=self.var_ET21, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E21.place(x=380, y=240, width=80)

        self.txt_E22 = Entry(self.window, textvariable=self.var_ET22, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E22.place(x=380, y=280, width=80)

        self.txt_E23 = Entry(self.window, textvariable=self.var_ET23, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E23.place(x=380, y=320, width=80)

        self.txt_E24 = Entry(self.window, textvariable=self.var_ET24, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E24.place(x=380, y=360, width=80)

        self.txt_E25 = Entry(self.window, textvariable=self.var_ET25, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E25.place(x=380, y=400, width=80)

        self.txt_E26= Entry(self.window, textvariable=self.var_ET26, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E26.place(x=380, y=440, width=80)

        self.txt_E27 = Entry(self.window, textvariable=self.var_ET27, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E27.place(x=380, y=480, width=80)

        self.txt_E28 = Entry(self.window, textvariable=self.var_ET28, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E28.place(x=480, y=160, width=80)

        self.txt_E29 = Entry(self.window, textvariable=self.var_ET29, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E29.place(x=480, y=200, width=80)

        self.txt_E30 = Entry(self.window, textvariable=self.var_ET30, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E30.place(x=480, y=240, width=80)

        self.txt_E31= Entry(self.window, textvariable=self.var_ET31, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E31.place(x=480, y=280, width=80)

        self.txt_E32 = Entry(self.window, textvariable=self.var_ET32, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E32.place(x=480, y=320, width=80)

        self.txt_E33 = Entry(self.window, textvariable=self.var_ET33, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E33.place(x=480, y=360, width=80)

        self.txt_E34 = Entry(self.window, textvariable=self.var_ET34, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E34.place(x=480, y=400, width=80)

        self.txt_E35 = Entry(self.window, textvariable=self.var_ET35, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E35.place(x=480, y=440, width=80)

        self.txt_E36 = Entry(self.window, textvariable=self.var_ET36, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E36.place(x=480, y=480, width=80)

        self.txt_E37 = Entry(self.window, textvariable=self.var_ET37, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E37.place(x=580, y=160, width=80)

        self.txt_E38 = Entry(self.window, textvariable=self.var_ET38, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E38.place(x=580, y=200, width=80)

        self.txt_E39 = Entry(self.window, textvariable=self.var_ET39, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E39.place(x=580, y=240, width=80)

        self.txt_E40 = Entry(self.window, textvariable=self.var_ET40, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E40.place(x=580, y=280, width=80)

        self.txt_E41 = Entry(self.window, textvariable=self.var_ET41, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E41.place(x=580, y=320, width=80)

        self.txt_E42 = Entry(self.window, textvariable=self.var_ET42, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E42.place(x=580, y=360, width=80)

        self.txt_E43 = Entry(self.window, textvariable=self.var_ET43, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E43.place(x=580, y=400, width=80)

        self.txt_E44 = Entry(self.window, textvariable=self.var_ET44, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E44.place(x=580, y=440, width=80)

        self.txt_E45 = Entry(self.window, textvariable=self.var_ET45, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E45.place(x=580, y=480, width=80)
        #Calculation
        self.txt_E46 = Entry(self.window, textvariable=self.var_ET46, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E46.place(x=680, y=160, width=80)

        self.txt_E47 = Entry(self.window, textvariable=self.var_ET47, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E47.place(x=680, y=200, width=80)

        self.txt_E48 = Entry(self.window, textvariable=self.var_ET48, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E48.place(x=680, y=240, width=80)

        self.txt_E49 = Entry(self.window, textvariable=self.var_ET49, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E49.place(x=680, y=280, width=80)

        self.txt_E50 = Entry(self.window, textvariable=self.var_ET50, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E50.place(x=680, y=320, width=80)

        self.txt_E51 = Entry(self.window, textvariable=self.var_ET51, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E51.place(x=680, y=360, width=80)

        self.txt_E52 = Entry(self.window, textvariable=self.var_ET52, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E52.place(x=680, y=400, width=80)

        self.txt_E53 = Entry(self.window, textvariable=self.var_ET53, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E53.place(x=680, y=440, width=80)

        self.txt_E54 = Entry(self.window, textvariable=self.var_ET54, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E54.place(x=680, y=480, width=80)

        self.txt_Cs2_1 = Entry(self.window, textvariable=self.var_Cs2_1, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_Cs2_1.place(x=180, y=520, width=80)

        self.txt_Cs2_2 = Entry(self.window, textvariable=self.var_Cs2_2, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_Cs2_2.place(x=280, y=520, width=80)

        self.txt_Cs2_3 = Entry(self.window, textvariable=self.var_Cs2_3, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_Cs2_3.place(x=380, y=520, width=80)

        self.txt_Cs2_4 = Entry(self.window, textvariable=self.var_Cs2_4, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_Cs2_4.place(x=480, y=520, width=80)

        self.txt_Cs2_5 = Entry(self.window, textvariable=self.var_Cs2_5, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_Cs2_5.place(x=580, y=520, width=80)
        #calculation
        self.txt_Cs2_6 = Entry(self.window, textvariable=self.var_Cs2_6, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_Cs2_6.place(x=680, y=520, width=80)









        #Buttons

        self.btn_search=Button(self.window,text='Go',font=("times new roman",15,"bold"),bg="lightgreen",cursor="hand2",command=self.search)
        self.btn_search.place(x=332, y=40,  width=30, height=28)

        self.btn_add=Button(self.window,text='Save',font=("times new roman",15,"bold"),command=self.add,bg="#87d3f8",cursor="hand2")
        self.btn_add.place(x=170,y=600,width=110,height=30)

        self.btn_update = Button(self.window, text='Update', font=("times new roman", 15, "bold"),command=self.update, bg="#87d3f8",cursor="hand2")
        self.btn_update.place(x=310, y=600, width=110, height=30)

        self.btn_add = Button(self.window, text='Delete', font=("times new roman", 15, "bold"),command=self.delete, bg="#87d3f8",cursor="hand2")
        self.btn_add.place(x=450, y=600, width=110, height=30)

        self.btn_clear=Button(self.window,text='clear',font=("times new roman",15,"bold"),command=self.clear_data,bg="#e3f4fe",cursor="hand2")
        self.btn_clear.place(x=650, y=600, width=110, height=30)

        self.btn_cal=Button(self.window,text='calculate',font=("times new roman",15,"bold"),command=self.calculation,bg="#e3f4fe",cursor="hand2")
        self.btn_cal.place(x=650, y=570, width=110, height=30)

        self.btn_delete_all = Button(self.window, text='Delete All', font=("goudy old style", 15, "bold"),command=self.delete_all,cursor="hand2", bg="red")
        self.btn_delete_all.place(x=500, y=700, width=110, height=30)
        self.btn_generate_sheet = Button(self.window, text='Sheet A', font=("goudy old style", 15, "bold"),command=self.mark_sheets,cursor="hand2", bg="lightgreen")
        self.btn_generate_sheet.place(x=330, y=650, width=155, height=30)
        self.enter_file_name = Entry(self.window, textvariable=self.filenam_raw_entry1, font=("goudy old style", 15, "bold"),bg='#e3f4fe')
        self.enter_file_name.place(x=120, y=650, width=200)
        self.btn_generate_sheet = Button(self.window, text='Sheet B', font=("goudy old style", 15, "bold"),command=self.mark_sheets1,cursor="hand2", bg="lightgreen")
        self.btn_generate_sheet.place(x=490, y=650, width=155, height=30)
        self.btn_generate_sheet = Button(self.window, text='Sheet C', font=("goudy old style", 15, "bold"),command=self.mark_sheets2,cursor="hand2", bg="lightgreen")
        self.btn_generate_sheet.place(x=650, y=650, width=155, height=30)
        self.enter_file_name = Entry(self.window, textvariable=self.t_name, font=("goudy old style", 15, "bold"),bg='#e3f4fe')
        self.enter_file_name.place(x=210, y=690, width=200)

        #self.enter_page_no = Entry(self.window, textvariable=self.n, font=("goudy old style", 15, "bold"),bg='#e3f4fe')
        #self.enter_page_no.place(x=120, y=660, width=200)





        lbl_search_roll = Label(self.window, text="Search GRNo", font=("goudy old style", 15, "bold"),bg="#eBffff").place(x=820, y=40, height=30)#452
        self.txt_search_roll = Entry(self.window, textvariable=self.var_roll, font=("goudy old style", 15, "bold"),bg='#e3f4fe')
        self.txt_search_roll.place(x=952, y=40, width=150)#576
        self.btn_search = Button(self.window, text='Search', font=("times new roman", 15, "bold"), command=self.search_marks,bg="lightgreen",cursor="hand2")
        self.btn_search.place(x=1098, y=38, width=90, height=30)#730


        
        #show table
        self.C_frame=Frame(self.window,bd=2,relief=RIDGE)
        self.C_frame.place(x=820,y=75,width=600,height=680)
        scrolly=Scrollbar(self.C_frame,orient=VERTICAL)
        scrollx=Scrollbar(self.C_frame,orient=HORIZONTAL)
        self.marksTable=ttk.Treeview(self.C_frame,columns=("grno","roll","ET1",
        "ET2",
        "ET3",
        "ET4",
        "ET5",
        "ET6",
        "ET7",
        "ET8",
        "ET9",
        "ET10",
        "ET11",
        "ET12",
        "ET13",
        "ET14",
        "ET15",
        "ET16",
        "ET17",
        "ET18",
        "ET19",
        "ET20",
        "ET21",
        "ET22",
        "ET23",
        "ET24",
        "ET25",
        "ET26",
        "ET27",
        "ET28",
        "ET29",
        "ET30",
        "ET31",
        "ET32",
        "ET33",
        "ET34",
        "ET35",
        "ET36",
        "ET37",
        "ET38",
        "ET39",
        "ET40",
        "ET41",
        "ET42",
        "ET43",
        "ET44",
        "ET45",
        "ET46",
        "ET47",
        "ET48",
        "ET49",
        "ET50",
        "ET51",
        "ET52",
        "ET53",
        "ET54",
        "Cs_2_1",
        "Cs_2_2",
        "Cs_2_3",
        "Cs_2_4",
        "Cs_2_5",
        "Cs_2_6",
        "class" ,
         "name",
         "env" ,
           "pe"
              ))
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT, fill=X)
        scrollx.config(command=self.marksTable.xview)
        scrolly.config(command=self.marksTable.yview)
        self.marksTable.heading("grno", text="GRNo.")
        self.marksTable.heading("roll", text="Roll No.")
        self.marksTable.heading("ET1",text="ET1")
        self.marksTable.heading("ET2",text="ET2")
        self.marksTable.heading("ET3",text="ET3")
        self.marksTable.heading("ET4",text="ET4")
        self.marksTable.heading("ET5",text="ET5")
        self.marksTable.heading("ET6", text="ET6")
        self.marksTable.heading("ET7", text="ET7")
        self.marksTable.heading("ET8", text="ET8")
        self.marksTable.heading("ET9", text="ET9")
        self.marksTable.heading("ET10", text="ET10")
        self.marksTable.heading("ET11", text="ET11")
        self.marksTable.heading("ET12", text="ET12")
        self.marksTable.heading("ET13", text="ET13")
        self.marksTable.heading("ET14", text="ET14")
        self.marksTable.heading("ET15", text="ET15")
        self.marksTable.heading("ET16", text="ET16")
        self.marksTable.heading("ET17", text="ET17")
        self.marksTable.heading("ET18", text="ET18")
        self.marksTable.heading("ET19", text="ET19")
        self.marksTable.heading("ET20", text="ET20")
        self.marksTable.heading("ET21", text="ET21")
        self.marksTable.heading("ET22", text="ET22")
        self.marksTable.heading("ET23", text="ET23")
        self.marksTable.heading("ET24", text="ET24")
        self.marksTable.heading("ET25", text="ET25")
        self.marksTable.heading("ET26", text="ET26")
        self.marksTable.heading("ET27", text="ET27")
        self.marksTable.heading("ET28", text="ET28")
        self.marksTable.heading("ET29", text="ET29")
        self.marksTable.heading("ET30", text="ET30")
        self.marksTable.heading("ET31", text="ET31")
        self.marksTable.heading("ET32", text="ET32")
        self.marksTable.heading("ET33", text="ET33")
        self.marksTable.heading("ET34", text="ET34")
        self.marksTable.heading("ET35", text="ET35")
        self.marksTable.heading("ET36", text="ET36")
        self.marksTable.heading("ET37", text="ET37")
        self.marksTable.heading("ET38", text="ET38")
        self.marksTable.heading("ET39", text="ET39")
        self.marksTable.heading("ET40", text="ET40")
        self.marksTable.heading("ET41", text="ET41")
        self.marksTable.heading("ET42", text="ET42")
        self.marksTable.heading("ET43", text="ET43")
        self.marksTable.heading("ET44", text="ET44")
        self.marksTable.heading("ET45", text="ET45")
        self.marksTable.heading("ET46", text="ET46")
        self.marksTable.heading("ET47", text="ET47")
        self.marksTable.heading("ET48", text="ET48")
        self.marksTable.heading("ET49", text="ET49")
        self.marksTable.heading("ET50", text="ET50")
        self.marksTable.heading("ET51", text="ET51")
        self.marksTable.heading("ET52", text="ET52")
        self.marksTable.heading("ET53", text="ET53")
        self.marksTable.heading("ET54", text="ET54")
        self.marksTable.heading("Cs_2_1", text="ET55")
        self.marksTable.heading("Cs_2_2", text="ET56")
        self.marksTable.heading("Cs_2_3", text="ET57")
        self.marksTable.heading("Cs_2_4", text="ET58")
        self.marksTable.heading("Cs_2_5", text="ET59")
        self.marksTable.heading("Cs_2_6", text="ET60")
        self.marksTable.heading("class", text="Class")
        self.marksTable.heading("name", text="Name")
        self.marksTable.heading("env",text="Env")
        self.marksTable.heading("pe",text="PE")




        self.marksTable["show"]='headings'
        self.marksTable.column("grno",width=40)
        self.marksTable.column("roll",width=40)
        self.marksTable.column("ET1", width=30)
        self.marksTable.column("ET2", width=30)
        self.marksTable.column("ET3", width=30)
        self.marksTable.column("ET4", width=30)
        self.marksTable.column("ET5", width=30)
        self.marksTable.column("ET6", width=30)
        self.marksTable.column("ET7", width=30)
        self.marksTable.column("ET8", width=30)
        self.marksTable.column("ET9", width=30)
        self.marksTable.column("ET10",width=30)
        self.marksTable.column("ET11",width=30)
        self.marksTable.column("ET12",width=30)
        self.marksTable.column("ET13",width=30)
        self.marksTable.column("ET14",width=30)
        self.marksTable.column("ET15",width=30)
        self.marksTable.column("ET16",width=30)
        self.marksTable.column("ET17",width=30)
        self.marksTable.column("ET18",width=30)
        self.marksTable.column("ET19",width=30)
        self.marksTable.column("ET20",width=30)
        self.marksTable.column("ET21",width=30)
        self.marksTable.column("ET22",width=30)
        self.marksTable.column("ET23",width=30)
        self.marksTable.column("ET24",width=30)
        self.marksTable.column("ET25",width=30)
        self.marksTable.column("ET26",width=30)
        self.marksTable.column("ET27",width=30)
        self.marksTable.column("ET28",width=30)
        self.marksTable.column("ET29",width=30)
        self.marksTable.column("ET30",width=30)
        self.marksTable.column("ET31",width=30)
        self.marksTable.column("ET32",width=30)
        self.marksTable.column("ET33",width=30)
        self.marksTable.column("ET34",width=30)
        self.marksTable.column("ET35",width=30)
        self.marksTable.column("ET36",width=30)
        self.marksTable.column("ET37",width=30)
        self.marksTable.column("ET38",width=30)
        self.marksTable.column("ET39",width=30)
        self.marksTable.column("ET40",width=30)
        self.marksTable.column("ET41",width=30)
        self.marksTable.column("ET42",width=30)
        self.marksTable.column("ET43",width=30)
        self.marksTable.column("ET44",width=30)
        self.marksTable.column("ET45",width=30)
        self.marksTable.column("ET46",width=30)
        self.marksTable.column("ET47",width=30)
        self.marksTable.column("ET48",width=30)
        self.marksTable.column("ET49",width=30)
        self.marksTable.column("ET50",width=30)
        self.marksTable.column("ET51",width=30)
        self.marksTable.column("ET52",width=30)
        self.marksTable.column("ET53",width=30)
        self.marksTable.column("ET54",width=30)
        self.marksTable.column("Cs_2_1",width=30)
        self.marksTable.column("Cs_2_2",width=30)
        self.marksTable.column("Cs_2_3",width=30)
        self.marksTable.column("Cs_2_4",width=30)
        self.marksTable.column("Cs_2_5",width=30)
        self.marksTable.column("Cs_2_6",width=30)
        self.marksTable.column("class",width=50)
        self.marksTable.column("name",width=50)
        self.marksTable.column("env",width=50)
        self.marksTable.column("pe",width=40)
        self.marksTable.pack(fill=BOTH,expand=1)
        self.marksTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()

        self.de_frame()
        #self.mark_sheets()

    def mark_sheets(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        #n=getint(self.n.get())
        try:
            cur.execute('select * from marksTable where class="A"')
            row = cur.fetchall()
            n=((len(row)//4)+1)
            print(row,"This is AA")

            if row != None:
                #pdf_file = filename+'.pdf'
                #pdf_file=filename+'.pdf'
                packet = io.BytesIO()
                can = canvas.Canvas(packet,pagesize=letter)
                can.setFillColorRGB(0, 0, 0)  # till here everything is okay
                can.setFont("Times-Roman", 12)
                temp=0
                p=0
                for j in range(getint(n)):  #looping for new page in range of pages

                    y=0
                    i=0
                    #print(temp,"hereee",j)
                    while i <len(row) and i+temp<len(row): # loop  content in one page in range of rows of data

                        #for m in range(4):  #looping for
                        print(row[i+temp],i+temp, "alalalaalla")
                        can.drawString(98, 659-y, str(row[i + temp][1]))
                        print("hereerrrr")
                        #if rows!=None and temp+i<len(rows):
                        can.drawString(164, 659-y, str(row[i + temp][-3]))
                        can.drawString(513, 659-y , str(row[i+temp][0]))
                        #sem1
                        can.drawString(115, 625-y, str(row[i+temp][11]))#  math

                        can.drawString(147, 625-y, str(row[i+temp][12]))  # bio
                        can.drawString(178, 625-y, str(row[i+temp][13]))  # phy
                        can.drawString(211, 625-y, str(row[i+temp][14]))  # chm
                        can.drawString(241, 625-y, str(row[i+temp][15]))  # ur
                        can.drawString(269, 625-y, str(row[i+temp][16]))  # eng
                        can.drawString(293, 625-y, str(row[i+temp][17]))  # hin
                        can.drawString(320, 625-y, str(row[i+temp][18]))  # geo
                        can.drawString(347, 625-y, str(getint(row[i+temp][19])+getint(row[i+temp][57]))) # cs1+cs2
                        #print(row[i+temp][19],row[i+temp][58],"mqmqmqmqmqqqmm")
                        #if rows2!=None  and temp+i<len(rows):
                        can.drawString(375, 600-y, str(row[i+temp][-2]))
                        can.drawString(398, 600-y, str(row[i+temp][-1]))

                        #sem2                  -y
                        can.drawString(115, 605-y, str(row[i + temp][29]))#  math

                        can.drawString(147, 605-y, str(row[i + temp][30]))  # bio
                        can.drawString(178, 605-y, str(row[i + temp][31]))  # phy
                        can.drawString(211, 605-y, str(row[i + temp][32]))  # chm
                        can.drawString(241, 605-y, str(row[i + temp][33]))  # ur
                        can.drawString(269, 605-y, str(row[i + temp][34]))  # eng
                        can.drawString(293, 605-y, str(row[i + temp][35]))  # hin
                        can.drawString(320, 605-y, str(row[i + temp][36]))  # geo
                        can.drawString(347, 605-y, str(getint(row[i + temp][37])+getint(row[i+temp][59])) )
                        #print(row[i+temp][37],row[i+temp][60],"mqmqmqmqmqqqmm22222222")

                        #ut1+ut2               -y

                        can.drawString(115, 584-y , str(getint(row[i+temp][2])+getint(row[i + temp][20])))  # MATH

                        can.drawString(147, 584-y , str(getint(row[i+temp][3])+getint(row[i + temp][21])))  # eng
                        can.drawString(178, 584-y, str(getint(row[i+temp][4])+getint(row[i + temp][22])))  # hin
                        can.drawString(211, 584-y, str(getint(row[i+temp][5])+getint(row[i + temp][23])))  # phy
                        can.drawString(241, 584-y, str(getint(row[i+temp][6])+getint(row[i + temp][24])))  # chem
                        can.drawString(269, 584-y, str(getint(row[i+temp][7])+getint(row[i + temp][25])))  # bio
                        can.drawString(293, 584-y, str(getint(row[i+temp][8])+getint(row[i + temp][26])))  # math
                        can.drawString(320, 584-y, str(getint(row[i+temp][9])+getint(row[i + temp][27])))  # geo
                        can.drawString(347, 584-y, str(getint(row[i+temp][10])+getint(row[i+temp][57])+getint(row[i + temp][28])+getint(row[i+temp][59])))  # cs
                        #total*2               -
                        can.drawString(115, 566-y, str(getint(row[i + temp][47])*2))  # math
                        can.drawString(147, 566-y, str(getint(row[i + temp][48])*2))  # eng
                        can.drawString(178, 566-y, str(getint(row[i + temp][49])*2))  # hin
                        can.drawString(211, 566-y, str(getint(row[i + temp][50])*2))  # phy
                        can.drawString(241, 566-y, str(getint(row[i + temp][51])*2))  # chem
                        can.drawString(269, 566-y, str(getint(row[i + temp][52])*2))  # bio
                        can.drawString(293, 566-y, str(getint(row[i + temp][53])*2))  # chem
                        can.drawString(320, 566-y, str(getint(row[i + temp][54])*2))  # chem
                        can.drawString(347, 566-y, str(getint(row[i + temp][55])*2))  # chem
                        #avarage
                        can.drawString(115, 548-y, str(getint(row[i + temp][47])))  # math
                        can.drawString(147, 548-y, str(getint(row[i + temp][48])))  # eng
                        can.drawString(178, 548-y, str(getint(row[i + temp][49])))  # hin
                        can.drawString(211, 548-y, str(getint(row[i + temp][50])))  # phy
                        can.drawString(241, 548-y, str(getint(row[i + temp][51])))  # chem
                        can.drawString(269, 548-y, str(getint(row[i + temp][52])))  # bio
                        can.drawString(293, 548-y, str(getint(row[i + temp][53])))  # chem
                        can.drawString(320, 548-y, str(getint(row[i + temp][54])))  # chem
                        can.drawString(347, 548-y, str(getint(row[i + temp][55])))  # chem
                        y +=151
                        print(i,"iiii")
                        if i>=3 and i%3 == 0:
                            temp=temp+i+1
                            break
                        i+=1
                    p = p + 1
                    can.drawString(540, 40, str(p))
                    can.setFont('Helvetica', 15)
                    can.drawString(370, 750, str('A'))
                    can.drawString(250,718,str(self.t_name.get()))
                    can.showPage()

                can.save()
                #for k in range(n):
                can.showPage()
                #can.showPage()
                #can.showPage()
                #can.showPage()
                #can.save()#existing_pdf = PdfFileReader(open("BKQconsolated8.pdf", "rb"))
                packet.seek(0)
                new_pdf = PdfFileReader(packet)

                # read the existing PDF
                existing_pdf = PdfFileReader(open("SSAmark_sheetsf5.pdf", "rb"))
                output = PdfFileWriter()

                for i in range(n):#len(existing_pdf.pages)
                    page = existing_pdf.getPage(i)
                    page.mergePage(new_pdf.getPage(i))
                    output.addPage(page)
                filename =str(self.filenam_raw_entry1.get())
                myfilename = filename + '.pdf'
                with open(myfilename, 'wb') as f:
                    # outputStream = open("AAAAA.pdf", "wb")
                    output.write(f)
                    f.close()
                    messagebox.showinfo("Success", "Result Generated Successfully", parent=self.window)
                    self.show()
            else:
                messagebox.showerror("Error", "No record found", parent=self.window)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def mark_sheets1(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        #n=getint(self.n.get())
        try:
            cur.execute('select * from marksTable where class="B"')
            row = cur.fetchall()
            n=((len(row)//4)+1)
            print(row,"This is B")
            p=0
            if row != None:
                #pdf_file = filename+'.pdf'
                #pdf_file=filename+'.pdf'
                packet = io.BytesIO()
                can = canvas.Canvas(packet,pagesize=letter)
                can.setFillColorRGB(0, 0, 0)  # till here everything is okay
                can.setFont("Times-Roman", 12)
                temp=0

                for j in range(getint(n)):  #looping for new page in range of pages

                    y=0
                    i=0
                    #print(temp,"hereee",j)
                    while i <len(row) and i+temp<len(row): # loop  content in one page in range of rows of data

                        #for m in range(4):  #looping for
                        print(row[i+temp],i+temp, "alalalaalla")
                        can.drawString(98, 659-y, str(row[i + temp][1]))
                        print("hereerrrr")
                        #if rows!=None and temp+i<len(rows):
                        can.drawString(164, 659-y, str(row[i + temp][-3]))
                        can.drawString(513, 659-y , str(row[i+temp][0]))
                        #sem1
                        can.drawString(115, 625-y, str(row[i+temp][11]))#  math

                        can.drawString(147, 625-y, str(row[i+temp][12]))  # bio
                        can.drawString(178, 625-y, str(row[i+temp][13]))  # phy
                        can.drawString(211, 625-y, str(row[i+temp][14]))  # chm
                        can.drawString(241, 625-y, str(row[i+temp][15]))  # ur
                        can.drawString(269, 625-y, str(row[i+temp][16]))  # eng
                        can.drawString(293, 625-y, str(row[i+temp][17]))  # hin
                        can.drawString(320, 625-y, str(row[i+temp][18]))  # geo
                        can.drawString(347, 625-y, str(getint(row[i+temp][19])+getint(row[i+temp][57]))) # cs1+cs2
                        #print(row[i+temp][19],row[i+temp][58],"mqmqmqmqmqqqmm")
                        #if rows2!=None  and temp+i<len(rows):
                        can.drawString(375, 600-y, str(row[i+temp][-2]))
                        can.drawString(398, 600-y, str(row[i+temp][-1]))

                        #sem2                  -y
                        can.drawString(115, 605-y, str(row[i + temp][29]))#  math

                        can.drawString(147, 605-y, str(row[i + temp][30]))  # bio
                        can.drawString(178, 605-y, str(row[i + temp][31]))  # phy
                        can.drawString(211, 605-y, str(row[i + temp][32]))  # chm
                        can.drawString(241, 605-y, str(row[i + temp][33]))  # ur
                        can.drawString(269, 605-y, str(row[i + temp][34]))  # eng
                        can.drawString(293, 605-y, str(row[i + temp][35]))  # hin
                        can.drawString(320, 605-y, str(row[i + temp][36]))  # geo
                        can.drawString(347, 605-y, str(getint(row[i + temp][37])+getint(row[i+temp][59])) )
                        #print(row[i+temp][37],row[i+temp][60],"mqmqmqmqmqqqmm22222222")

                        #ut1+ut2               -y

                        can.drawString(115, 584-y , str(getint(row[i+temp][2])+getint(row[i + temp][20])))  # MATH

                        can.drawString(147, 584-y , str(getint(row[i+temp][3])+getint(row[i + temp][21])))  # eng
                        can.drawString(178, 584-y, str(getint(row[i+temp][4])+getint(row[i + temp][22])))  # hin
                        can.drawString(211, 584-y, str(getint(row[i+temp][5])+getint(row[i + temp][23])))  # phy
                        can.drawString(241, 584-y, str(getint(row[i+temp][6])+getint(row[i + temp][24])))  # chem
                        can.drawString(269, 584-y, str(getint(row[i+temp][7])+getint(row[i + temp][25])))  # bio
                        can.drawString(293, 584-y, str(getint(row[i+temp][8])+getint(row[i + temp][26])))  # math
                        can.drawString(320, 584-y, str(getint(row[i+temp][9])+getint(row[i + temp][27])))  # geo
                        can.drawString(347, 584-y, str(getint(row[i+temp][10])+getint(row[i+temp][57])+getint(row[i + temp][28])+getint(row[i+temp][59])))  # cs
                        #total*2               -
                        can.drawString(115, 566-y, str(getint(row[i + temp][47])*2))  # math
                        can.drawString(147, 566-y, str(getint(row[i + temp][48])*2))  # eng
                        can.drawString(178, 566-y, str(getint(row[i + temp][49])*2))  # hin
                        can.drawString(211, 566-y, str(getint(row[i + temp][50])*2))  # phy
                        can.drawString(241, 566-y, str(getint(row[i + temp][51])*2))  # chem
                        can.drawString(269, 566-y, str(getint(row[i + temp][52])*2))  # bio
                        can.drawString(293, 566-y, str(getint(row[i + temp][53])*2))  # chem
                        can.drawString(320, 566-y, str(getint(row[i + temp][54])*2))  # chem
                        can.drawString(347, 566-y, str(getint(row[i + temp][55])*2))  # chem
                        #avarage
                        can.drawString(115, 548-y, str(getint(row[i + temp][47])))  # math
                        can.drawString(147, 548-y, str(getint(row[i + temp][48])))  # eng
                        can.drawString(178, 548-y, str(getint(row[i + temp][49])))  # hin
                        can.drawString(211, 548-y, str(getint(row[i + temp][50])))  # phy
                        can.drawString(241, 548-y, str(getint(row[i + temp][51])))  # chem
                        can.drawString(269, 548-y, str(getint(row[i + temp][52])))  # bio
                        can.drawString(293, 548-y, str(getint(row[i + temp][53])))  # chem
                        can.drawString(320, 548-y, str(getint(row[i + temp][54])))  # chem
                        can.drawString(347, 548-y, str(getint(row[i + temp][55])))  # chem
                        y +=151
                        print(i,"iiii")
                        if i>=3 and i%3 == 0:
                            temp=temp+i+1

                            break
                        i+=1
                    p = p + 1
                    can.drawString(540, 40, str(p))
                    can.setFont('Helvetica', 15)
                    can.drawString(370, 750, str('B'))
                    can.drawString(250, 718, str(self.t_name.get()))
                    can.showPage()

                can.save()
                #for k in range(n):
                can.showPage()
                #can.showPage()
                #can.showPage()
                #can.showPage()
                #can.save()#existing_pdf = PdfFileReader(open("BKQconsolated8.pdf", "rb"))
                packet.seek(0)
                new_pdf = PdfFileReader(packet)

                # read the existing PDF
                existing_pdf = PdfFileReader(open("SSAmark_sheetsf5.pdf", "rb"))
                output = PdfFileWriter()

                for i in range(n):#len(existing_pdf.pages)
                    page = existing_pdf.getPage(i)
                    page.mergePage(new_pdf.getPage(i))
                    output.addPage(page)
                filename =str(self.filenam_raw_entry1.get())
                myfilename = filename + '.pdf'
                with open(myfilename, 'wb') as f:
                    # outputStream = open("AAAAA.pdf", "wb")
                    output.write(f)
                    f.close()
                    messagebox.showinfo("Success", "Result Generated Successfully", parent=self.window)
                    self.show()
            else:
                messagebox.showerror("Error", "No record found", parent=self.window)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def mark_sheets2(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        #n=getint(self.n.get())
        try:
            cur.execute('select * from marksTable where class="C"')
            row = cur.fetchall()
            n=((len(row)//4)+1)
            print(row,"This is C")

            if row != None:
                #pdf_file = filename+'.pdf'
                #pdf_file=filename+'.pdf'
                packet = io.BytesIO()
                can = canvas.Canvas(packet,pagesize=letter)
                can.setFillColorRGB(0, 0, 0)  # till here everything is okay
                can.setFont("Times-Roman", 12)
                temp=0
                p=0
                for j in range(getint(n)):  #looping for new page in range of pages

                    y=0
                    i=0
                    #print(temp,"hereee",j)
                    while i <len(row) and i+temp<len(row): # loop  content in one page in range of rows of data
                        print(row[i][-4],row[i],"][][][][][[]")

                        #for m in range(4):  #looping for
                        print(row[i+temp],i+temp, "This is CCCC")
                        can.drawString(98, 659-y, str(row[i + temp][1]))
                        print("hereerrrr")
                        #if rows!=None and temp+i<len(rows):
                        can.drawString(164, 659-y, str(row[i + temp][-3]))
                        can.drawString(513, 659-y , str(row[i+temp][0]))
                        #sem1
                        can.drawString(115, 625-y, str(row[i+temp][11]))#  math

                        can.drawString(147, 625-y, str(row[i+temp][12]))  # bio
                        can.drawString(178, 625-y, str(row[i+temp][13]))  # phy
                        can.drawString(211, 625-y, str(row[i+temp][14]))  # chm
                        can.drawString(241, 625-y, str(row[i+temp][15]))  # ur
                        can.drawString(269, 625-y, str(row[i+temp][16]))  # eng
                        can.drawString(293, 625-y, str(row[i+temp][17]))  # hin
                        can.drawString(320, 625-y, str(row[i+temp][18]))  # geo
                        can.drawString(347, 625-y, str(getint(row[i+temp][19])+getint(row[i+temp][57]))) # cs1+cs2
                        #print(row[i+temp][19],row[i+temp][58],"mqmqmqmqmqqqmm")
                        #if rows2!=None  and temp+i<len(rows):
                        can.drawString(375, 600-y, str(row[i+temp][-2]))
                        can.drawString(398, 600-y, str(row[i+temp][-1]))

                        #sem2                  -y
                        can.drawString(115, 605-y, str(row[i + temp][29]))#  math

                        can.drawString(147, 605-y, str(row[i + temp][30]))  # bio
                        can.drawString(178, 605-y, str(row[i + temp][31]))  # phy
                        can.drawString(211, 605-y, str(row[i + temp][32]))  # chm
                        can.drawString(241, 605-y, str(row[i + temp][33]))  # ur
                        can.drawString(269, 605-y, str(row[i + temp][34]))  # eng
                        can.drawString(293, 605-y, str(row[i + temp][35]))  # hin
                        can.drawString(320, 605-y, str(row[i + temp][36]))  # geo
                        can.drawString(347, 605-y, str(getint(row[i + temp][37])+getint(row[i+temp][59])) )
                        #print(row[i+temp][37],row[i+temp][60],"mqmqmqmqmqqqmm22222222")

                        #ut1+ut2               -y

                        can.drawString(115, 584-y , str(getint(row[i+temp][2])+getint(row[i + temp][20])))  # MATH

                        can.drawString(147, 584-y , str(getint(row[i+temp][3])+getint(row[i + temp][21])))  # eng
                        can.drawString(178, 584-y, str(getint(row[i+temp][4])+getint(row[i + temp][22])))  # hin
                        can.drawString(211, 584-y, str(getint(row[i+temp][5])+getint(row[i + temp][23])))  # phy
                        can.drawString(241, 584-y, str(getint(row[i+temp][6])+getint(row[i + temp][24])))  # chem
                        can.drawString(269, 584-y, str(getint(row[i+temp][7])+getint(row[i + temp][25])))  # bio
                        can.drawString(293, 584-y, str(getint(row[i+temp][8])+getint(row[i + temp][26])))  # math
                        can.drawString(320, 584-y, str(getint(row[i+temp][9])+getint(row[i + temp][27])))  # geo
                        can.drawString(347, 584-y, str(getint(row[i+temp][10])+getint(row[i+temp][57])+getint(row[i + temp][28])+getint(row[i+temp][59])))  # cs
                        #total*2               -
                        can.drawString(115, 566-y, str(getint(row[i + temp][47])*2))  # math
                        can.drawString(147, 566-y, str(getint(row[i + temp][48])*2))  # eng
                        can.drawString(178, 566-y, str(getint(row[i + temp][49])*2))  # hin
                        can.drawString(211, 566-y, str(getint(row[i + temp][50])*2))  # phy
                        can.drawString(241, 566-y, str(getint(row[i + temp][51])*2))  # chem
                        can.drawString(269, 566-y, str(getint(row[i + temp][52])*2))  # bio
                        can.drawString(293, 566-y, str(getint(row[i + temp][53])*2))  # chem
                        can.drawString(320, 566-y, str(getint(row[i + temp][54])*2))  # chem
                        can.drawString(347, 566-y, str(getint(row[i + temp][55])*2))  # chem
                        #avarage
                        can.drawString(115, 548-y, str(getint(row[i + temp][47])))  # math
                        can.drawString(147, 548-y, str(getint(row[i + temp][48])))  # eng
                        can.drawString(178, 548-y, str(getint(row[i + temp][49])))  # hin
                        can.drawString(211, 548-y, str(getint(row[i + temp][50])))  # phy
                        can.drawString(241, 548-y, str(getint(row[i + temp][51])))  # chem
                        can.drawString(269, 548-y, str(getint(row[i + temp][52])))  # bio
                        can.drawString(293, 548-y, str(getint(row[i + temp][53])))  # chem
                        can.drawString(320, 548-y, str(getint(row[i + temp][54])))  # chem
                        can.drawString(347, 548-y, str(getint(row[i + temp][55])))  # chem
                        y +=151
                        print(i,"iiii")
                        if i>=3 and i%3 == 0:
                            temp=temp+i+1

                            break
                        i+=1
                    p = p + 1
                    can.drawString(540, 40, str(p))
                    can.setFont('Helvetica', 15)
                    can.drawString(370, 750, str('C'))
                    can.drawString(250, 718, str(self.t_name.get()))
                    can.showPage()

                can.save()
                #for k in range(n):
                can.showPage()
                #can.showPage()
                #can.showPage()
                #can.showPage()
                #can.save()#existing_pdf = PdfFileReader(open("BKQconsolated8.pdf", "rb"))
                packet.seek(0)
                new_pdf = PdfFileReader(packet)

                # read the existing PDF
                existing_pdf = PdfFileReader(open("SSAmark_sheetsf5.pdf", "rb"))
                output = PdfFileWriter()

                for i in range(n):#len(existing_pdf.pages)
                    page = existing_pdf.getPage(i)
                    page.mergePage(new_pdf.getPage(i))
                    output.addPage(page)
                filename =str(self.filenam_raw_entry1.get())
                myfilename = filename + '.pdf'
                with open(myfilename, 'wb') as f:
                    # outputStream = open("AAAAA.pdf", "wb")
                    output.write(f)
                    f.close()
                    messagebox.showinfo("Success", "Result Generated Successfully", parent=self.window)
                    self.show()
            else:
                messagebox.showerror("Error", "No record found", parent=self.window)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")


    def delete_all(self):
        for record in self.marksTable.get_children():
            self.marksTable.delete(record)
        conn=sqlite3.connect('rms.db')
        c=conn.cursor()
        op = messagebox.askyesno("Confirm", "Do you really wanto to delete?", parent=self.window)
        if op == True:
            #c.execute('DROP TABLE marksTable')
            c.execute('DELETE FROM studentTable')
            messagebox.showinfo("Delete", "Deleted succesfilly", parent=self.window)
        conn.commit()
        conn.close()
        self.clear_data()



    def de_frame(self):

        style = ttk.Style()

        style.theme_use("default")

        style.configure("Treeview", background="D3D3D3", foreground="white", rowheight=45, fieldbackground="white")

        style.map('Treeview', background=[('selected', '#0047AB')])




    def clear_data(self):
        self.show()
        self.var_grno.set(""),
        self.var_roll.set(""),
        self.var_name.set(""),
        self.var_class.set(""),
        self.var_std.set(""),
        self.var_ET1.set(0),
        self.var_ET2.set(0),
        self.var_ET3.set(0),
        self.var_ET4.set(0),
        self.var_ET5.set(0),
        self.var_ET6.set(0),
        self.var_ET7.set(0),
        self.var_ET8.set(0),
        self.var_ET9.set(0),
        self.var_ET10.set(0),
        self.var_ET11.set(0),
        self.var_ET12.set(0),
        self.var_ET13.set(0),
        self.var_ET14.set(0),
        self.var_ET15.set(0),
        self.var_ET16.set(0),
        self.var_ET17.set(0),
        self.var_ET18.set(0),
        self.var_ET19.set(0),
        self.var_ET20.set(0),
        self.var_ET21.set(0),
        self.var_ET22.set(0),
        self.var_ET23.set(0),
        self.var_ET24.set(0),
        self.var_ET25.set(0),
        self.var_ET26.set(0),
        self.var_ET27.set(0),
        self.var_ET28.set(0),
        self.var_ET29.set(0),
        self.var_ET30.set(0),
        self.var_ET31.set(0),
        self.var_ET32.set(0),
        self.var_ET33.set(0),
        self.var_ET34.set(0),
        self.var_ET35.set(0),
        self.var_ET36.set(0),
        self.var_ET37.set(0),
        self.var_ET38.set(0),
        self.var_ET39.set(0),
        self.var_ET40.set(0),
        self.var_ET41.set(0),
        self.var_ET42.set(0),
        self.var_ET43.set(0),
        self.var_ET44.set(0),
        self.var_ET45.set(0),
        self.var_ET46.set(0),
        self.var_ET47.set(0),
        self.var_ET48.set(0),
        self.var_ET49.set(0),
        self.var_ET50.set(0),
        self.var_ET51.set(0),
        self.var_ET52.set(0),
        self.var_ET53.set(0),
        self.var_ET54.set(0),
        self.var_Cs2_1.set(0),
        self.var_Cs2_2.set(0),
        self.var_Cs2_3.set(0),
        self.var_Cs2_4.set(0),
        self.var_Cs2_5.set(0),
        self.var_Cs2_6.set(0) ,
        self.var_env.set(""),
        self.var_pe.set("")



    def delete(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_grno.get()=="":

                messagebox.showerror("Error","GRNo.should be required",parent=self.window)

            else:
                cur.execute("select * from marksTable where grno=?",(self.var_grno.get(),))
                row=cur.fetchone()
                if row==None:

                    messagebox.showerror("Error","please select marksTable from the list first",parent=self.window)

                else:
                    op=messagebox.askyesno("Confirm","Do you really wanto to delete?",parent=self.window)
                    if op==True:

                        cur.execute("delete from marksTable where roll=?",(self.var_grno.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Student's marks deleted succesfilly",parent=self.window)

                        self.clear_data()
        except Exception as ex:
            messagebox.showerror(("Error",f"Error due to{str(ex)}"))



    def get_data(self, ev):
        #self.var_roll.config(state='readonly')

        r=self.marksTable.focus()
        content=self.marksTable.item(r)
        row=content["values"]
        self.var_grno.set(row[0]),
        self.var_roll.set(row[1]),
        #self.var_grp.set(row[1]),
        self.var_ET1.set(row[2]),
        self.var_ET2.set(row[3]),
        self.var_ET3.set(row[4]),
        self.var_ET4.set(row[5]),
        self.var_ET5.set(row[6]),
        self.var_ET6.set(row[7]),
        self.var_ET7.set(row[8]),
        self.var_ET8.set(row[9]),
        self.var_ET9.set(row[10]),
        self.var_ET10.set(row[11]),
        self.var_ET11.set(row[12]),
        self.var_ET12.set(row[13]),
        self.var_ET13.set(row[14]),
        self.var_ET14.set(row[15]),
        self.var_ET15.set(row[16]),
        self.var_ET16.set(row[17]),
        self.var_ET17.set(row[18]),
        self.var_ET18.set(row[19]),
        self.var_ET19.set(row[20]),
        self.var_ET20.set(row[21]),
        self.var_ET21.set(row[22]),
        self.var_ET22.set(row[23]),
        self.var_ET23.set(row[24]),
        self.var_ET24.set(row[25]),
        self.var_ET25.set(row[26]),
        self.var_ET26.set(row[27]),
        self.var_ET27.set(row[28]),
        self.var_ET28.set(row[29]),
        self.var_ET29.set(row[30]),
        self.var_ET30.set(row[31]),
        self.var_ET31.set(row[32]),
        self.var_ET32.set(row[33]),
        self.var_ET33.set(row[34]),
        self.var_ET34.set(row[35]),
        self.var_ET35.set(row[36]),
        self.var_ET36.set(row[37]),
        self.var_ET37.set(row[38]),
        self.var_ET38.set(row[39]),
        self.var_ET39.set(row[40]),
        self.var_ET40.set(row[41]),
        self.var_ET41.set(row[42]),
        self.var_ET42.set(row[43]),
        self.var_ET43.set(row[44]),
        self.var_ET44.set(row[45]),
        self.var_ET45.set(row[46]),

        self.var_ET46.set(row[47]),
        self.var_ET47.set(row[48]),
        self.var_ET48.set(row[49]),
        self.var_ET49.set(row[50]),
        self.var_ET50.set(row[51]),
        self.var_ET51.set(row[52]),
        self.var_ET52.set(row[53]),
        self.var_ET53.set(row[54]),
        self.var_ET54.set(row[55]),

        self.var_Cs2_1.set(row[56]),
        self.var_Cs2_2.set(row[57]),
        self.var_Cs2_3.set(row[58]),
        self.var_Cs2_4.set(row[59]),
        self.var_Cs2_5.set(row[60]),
        self.var_Cs2_6.set(row[61]),
        self.var_class.set(row[-4]),
        self.var_name.set(row[-3]),
        self.var_env.set(row[-2]),
        self.var_pe.set(row[-1]),



    def add(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_grno.get() == "":
                messagebox.showerror("Error", "GRNo should be required", parent=self.window)
            else:
                cur.execute("select *  from marksTable where grno=?", (self.var_grno.get(),))
                row = cur.fetchone()

                if row != None:
                    messagebox.showerror("Error", "GRNo. Already present", parent=self.window)
                else:

                    cur.execute("""insert into marksTable(grno,roll,ET1,ET2,ET3,ET4,ET5,ET6,ET7,ET8,ET9,ET10,ET11,ET12,ET13,ET14,ET15,ET16,ET17,ET18,ET19,ET20,ET21,ET22,ET23,ET24,ET25,ET26,ET27,ET28,ET29,ET30,ET31,ET32,ET33,ET34,ET35,ET36,ET37,ET38,ET39,ET40,ET41,ET42,ET43,ET44,ET45,ET46,ET47,ET48,ET49,ET50,ET51,ET52,ET53,ET54,Cs_2_1,Cs_2_2,Cs_2_3,Cs_2_4,Cs_2_5,Cs_2_6,class,name,env,pe) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",(
                        self.var_grno.get(),
                        self.var_roll.get(),
                        self.var_ET1.get(),
                        self.var_ET2.get(),
                        self.var_ET3.get(),
                        self.var_ET4.get(),
                        self.var_ET5.get(),
                        self.var_ET6.get(),
                        self.var_ET7.get(),
                        self.var_ET8.get(),
                        self.var_ET9.get(),
                        self.var_ET10.get(),
                        self.var_ET11.get(),
                        self.var_ET12.get(),
                        self.var_ET13.get(),
                        self.var_ET14.get(),
                        self.var_ET15.get(),
                        self.var_ET16.get(),
                        self.var_ET17.get(),
                        self.var_ET18.get(),
                        self.var_ET19.get(),
                        self.var_ET20.get(),
                        self.var_ET21.get(),
                        self.var_ET22.get(),
                        self.var_ET23.get(),
                        self.var_ET24.get(),
                        self.var_ET25.get(),
                        self.var_ET26.get(),
                        self.var_ET27.get(),
                        self.var_ET28.get(),
                        self.var_ET29.get(),
                        self.var_ET30.get(),
                        self.var_ET31.get(),
                        self.var_ET32.get(),
                        self.var_ET33.get(),
                        self.var_ET34.get(),
                        self.var_ET35.get(),
                        self.var_ET36.get(),
                        self.var_ET37.get(),
                        self.var_ET38.get(),
                        self.var_ET39.get(),
                        self.var_ET40.get(),
                        self.var_ET41.get(),
                        self.var_ET42.get(),
                        self.var_ET43.get(),
                        self.var_ET44.get(),
                        self.var_ET45.get(),

                        self.var_ET46.get(),
                        self.var_ET47.get(),
                        self.var_ET48.get(),
                        self.var_ET49.get(),
                        self.var_ET50.get(),
                        self.var_ET51.get(),
                        self.var_ET52.get(),
                        self.var_ET53.get(),
                        self.var_ET54.get(),

                        self.var_Cs2_1.get(),
                        self.var_Cs2_2.get(),
                        self.var_Cs2_3.get(),
                        self.var_Cs2_4.get(),
                        self.var_Cs2_5.get(),

                        self.var_Cs2_6.get(),
                        self.var_class.get(),
                        self.var_name.get(),
                        self.var_env.get() ,
                        self.var_pe.get()
                        ))

                    con.commit()
                    messagebox.showinfo("Success", "student Added Successfully", parent=self.window)
                    self.show()
        except Exception as ex:

            messagebox.showerror("Error", f"Error due to  {str(ex)}")

    def update(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_grno.get()=="":

                messagebox.showerror("Error","GRNo. should be required",parent=self.window)
            else:
                cur.execute("select * from marksTable where grno=?",(self.var_grno.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Select marksTable from list",parent=self.window)
                else:
                    cur.execute("update marksTable set roll=?,ET1=?,ET2=?,ET3=?,ET4=?,ET5=?,ET6=?,ET7=?,ET8=?,ET9=?,ET10=?,ET11=?,ET12=?,ET13=?,ET14=?,ET15=?,ET16=?,ET17=?,ET18=?,ET19=?,ET20=?,ET21=?,ET22=?,ET23=?,ET24=?,ET25=?,ET26=?,ET27=?,ET28=?,ET29=?,ET30=?,ET31=?,ET32=?,ET33=?,ET34=?,ET35=?,ET36=?,ET37=?,ET38=?,ET39=?,ET40=?,ET41=?,ET42=?,ET43=?,ET44=?,ET45=?,ET46=?,ET47=?,ET48=?,ET49=?,ET50=?,ET51=?,ET52=?,ET53=?,ET54=?,Cs_2_1=?,Cs_2_2=?,Cs_2_3=?,Cs_2_4=?,Cs_2_5=?,Cs_2_6=?,class=?,name=?,env=?,pe=? where grno=?", (
                        self.var_roll.get(),
                        self.var_ET1.get(),
                        self.var_ET2.get(),
                        self.var_ET3.get(),
                        self.var_ET4.get(),
                        self.var_ET5.get(),
                        self.var_ET6.get(),
                        self.var_ET7.get(),
                        self.var_ET8.get(),
                        self.var_ET9.get(),
                        self.var_ET10.get(),
                        self.var_ET11.get(),
                        self.var_ET12.get(),
                        self.var_ET13.get(),
                        self.var_ET14.get(),
                        self.var_ET15.get(),
                        self.var_ET16.get(),
                        self.var_ET17.get(),
                        self.var_ET18.get(),
                        self.var_ET19.get(),
                        self.var_ET20.get(),
                        self.var_ET21.get(),
                        self.var_ET22.get(),
                        self.var_ET23.get(),
                        self.var_ET24.get(),
                        self.var_ET25.get(),
                        self.var_ET26.get(),
                        self.var_ET27.get(),
                        self.var_ET28.get(),
                        self.var_ET29.get(),
                        self.var_ET30.get(),
                        self.var_ET31.get(),
                        self.var_ET32.get(),
                        self.var_ET33.get(),
                        self.var_ET34.get(),
                        self.var_ET35.get(),
                        self.var_ET36.get(),
                        self.var_ET37.get(),
                        self.var_ET38.get(),
                        self.var_ET39.get(),
                        self.var_ET40.get(),
                        self.var_ET41.get(),
                        self.var_ET42.get(),
                        self.var_ET43.get(),
                        self.var_ET44.get(),
                        self.var_ET45.get(),
                        self.var_ET46.get(),
                        self.var_ET47.get(),
                        self.var_ET48.get(),
                        self.var_ET49.get(),
                        self.var_ET50.get(),
                        self.var_ET51.get(),
                        self.var_ET52.get(),
                        self.var_ET53.get(),
                        self.var_ET54.get(),
                        self.var_Cs2_1.get(),
                        self.var_Cs2_2.get(),
                        self.var_Cs2_3.get(),
                        self.var_Cs2_4.get(),
                        self.var_Cs2_5.get(),
                        self.var_Cs2_6.get(),
                        self.var_class.get(),
                        self.var_name.get(),
                        self.var_env.get(),
                        self.var_pe.get(),
                        self.var_grno.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Student Update Successfully",parent=self.window)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")




    def show(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select * from marksTable")
            rows = cur.fetchall()
            self.marksTable.delete(*self.marksTable.get_children())
            for row in rows:
                self.marksTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
    """def fetch_roll(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select roll from studentTable")
            rows = cur.fetchall()

            if len(rows)>0:
                for row in rows:
                    self.roll_list.append(row[0])


        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")"""
    def fetch_grno(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select * from studentTable")
            rows = cur.fetchall()
            #print(rows)

            if len(rows)>0:
                for row in rows:
                    self.grno_list.append(row[0])

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    """def search(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select name,std,class from studentTable where roll=?", (self.var_roll.get(),))
            row = cur.fetchone()
            if row != None:
                self.var_name.set(row[0])
                self.var_std.set(row[1])
                self.var_class.set(row[2])

            else:
                messagebox.showerror("Error", "No record found", parent=self.window)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")"""
    def search(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            #cur.execute("select students_name,roll_no from bqkTable where grno=?  ", (self.var_grno.get(),))
            #row = cur.fetchone()
            cur.execute("select name,roll,class,std from studentTable where grno=?", (self.var_grno.get(),))
            row = cur.fetchone()
            if row != None:
                self.var_name.set(row[0])
                self.var_roll.set(int(row[1]))
            #if row1 != None:
                self.var_class.set(row[2])
                self.var_std.set(row[3])

            else:
                messagebox.showerror("Error", "No record found", parent=self.window)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
    def calculation(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        cur.execute("select * from marksTable where grno=?",(self.var_grno.get(),))
        row=cur.fetchone()
        v1,v2,v3,v4,v5=1,10,19,28,37
        if row!=None:

            #self.var_ET46.set(getint(row[28]+3))
            var=[self.var_ET46,self.var_ET47,self.var_ET48,self.var_ET49,self.var_ET50,self.var_ET51,self.var_ET52,self.var_ET53,self.var_ET54]



            #print((getint(row[2]),getint(row[11]),getint(row[20]),getint(row[29]),getint(row[38])))
            self.var_ET46.set(math.ceil((getint(row[2])+getint(row[11])+getint(row[20])+getint(row[29])+getint(row[38]))/2))

            #print((getint(row[3]),getint(row[12]),getint(row[21]),getint(row[30]),getint(row[39])))
            self.var_ET47.set(math.ceil((getint(row[3])+getint(row[12])+getint(row[21])+getint(row[30])+getint(row[39]))/2))

            #print((getint(row[4]),getint(row[13]),getint(row[22]),getint(row[31]),getint(row[40])),"lkgggggggggggggg" )
            self.var_ET48.set(math.ceil((getint(row[4])+getint(row[13])+getint(row[22])+getint(row[31])+getint(row[40]))/2))

            #print((getint(row[5]),getint(row[14]),getint(row[23]),getint(row[32]),getint(row[41])))
            self.var_ET49.set(math.ceil((getint(row[5])+getint(row[14])+getint(row[23])+getint(row[32])+getint(row[41]))/2))

            #print((getint(row[6]),getint(row[15]),getint(row[24]),getint(row[33]),getint(row[42])))
            self.var_ET50.set(math.ceil((getint(row[6])+getint(row[15])+getint(row[24])+getint(row[33])+getint(row[42]))/2))

            #print((getint(row[7]),getint(row[16]),getint(row[25]),getint(row[34]),getint(row[43])))
            self.var_ET51.set(math.ceil((getint(row[7])+getint(row[16])+getint(row[25])+getint(row[34])+getint(row[43]))/2))

            #print((getint(row[8]),getint(row[17]),getint(row[26]),getint(row[35]),getint(row[44])))
            self.var_ET52.set(math.ceil((getint(row[8])+getint(row[17])+getint(row[26])+getint(row[35])+getint(row[44]))/2))

            #print((getint(row[9]),getint(row[18]),getint(row[27]),getint(row[36]),getint(row[45])))
            self.var_ET53.set(math.ceil((getint(row[9])+getint(row[18])+getint(row[27])+getint(row[36])+getint(row[45]))/2))

            #print((getint(row[10]),getint(row[19]),getint(row[28]),getint(row[37]),getint(row[46])) )
            self.var_ET54.set(math.ceil((getint(row[10])+getint(row[19])+getint(row[28])+getint(row[37])+getint(row[46]))/2))

            #print((getint(row[56]),getint(row[57]),getint(row[58]),getint(row[59]),getint(row[60])),"ddddddddddddddddddddd")
            self.var_Cs2_6.set(math.ceil((getint(row[56])+getint(row[57])+getint(row[58])+getint(row[59])+getint(row[60]))/2))


        else:
            messagebox.showerror("Error", "No record found", parent=self.window)

    def search_marks(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select * from marksTable where grno=?", (self.var_grno.get(),))
            row = cur.fetchone()
            if row != None:
                self.marksTable.delete(*self.marksTable.get_children())
                self.marksTable.insert('', END, values=row)
            else:
                messagebox.showerror("Error", "No record found", parent=self.window)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

if __name__=="__main__":
    window=Tk()
    obj=class_marks(window)
    window.mainloop()