from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
import PyPDF2
from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
#from datetime import datetime
from menu.export import  exportClass
import math



class resultClass():
    def __init__(self, window):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        cur.execute(
            "CREATE TABLE IF NOT EXISTS resultTable(grno INTEGER PRIMARY KEY AUTOINCREMENT,roll text,Std text,Class text,Math text,Bio text,Phy text,Chem text,Urdu text,Eng text,Hin text,Geo text,Cs1 text,Cs2 text,env text,pe text,date text,result text,grandtotal text,perc text,grade text,name text,adress text,reop text)")
        con.commit()
        con.close()
        self.window=window
        self.window.title("Generate Results")
        self.window.geometry("1350x800+80+50")
        self.window.config(bg="#eBffff")
        self.window.focus_force()
        #Variables
        self.var_grno=StringVar()
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_std = StringVar()
        self.var_class=StringVar()
        self.var_search=StringVar()
        self.grno_list=[]
        self.fetch_grno()
        self.var_math=StringVar()
        self.var_bio =StringVar()
        self.var_phy=StringVar()
        self.var_chem=StringVar()
        self.var_ur=StringVar()
        self.var_eng=StringVar()
        self.var_Hin=StringVar()
        self.var_geo=StringVar()
        self.var_cs1=StringVar()
        self.var_cs2=StringVar()
        self.var_ET46=StringVar()
        self.var_ET47=StringVar()
        self.var_ET48=StringVar()
        self.var_ET49=StringVar()
        self.var_ET50=StringVar()
        self.var_ET51=StringVar()
        self.var_ET52=StringVar()
        self.var_ET53=StringVar()
        self.var_ET54=StringVar()
        self.var_Cs2_6 = StringVar()
        self.var_year=StringVar()
        self.var_result=StringVar()
        self.var_grandtotal=StringVar()
        self.var_grade=StringVar()
        self.var_perc=StringVar()
        self.var_adress=StringVar()
        self.var_reopening=StringVar()
        self.var_env=StringVar()
        self.var_pe=StringVar()
        self.no_of_pages=StringVar()


        #self.generate_btn = QPushButton("Generate PDF")
        #self.generate_btn.pressed.connect(self.generate)

        #Grace variables
        self.var_ET461=IntVar()
        self.var_ET471=IntVar()
        self.var_ET481=IntVar()
        self.var_ET491=IntVar()
        self.var_ET501=IntVar()
        self.var_ET511=IntVar()
        self.var_ET521=IntVar()
        self.var_ET531=IntVar()
        self.var_ET541=IntVar()
        self.var_Cs2_61 = IntVar()
        self.f=False
        #labels
        lbl_select = Label(self.window, text="GRNo:", font=("goudy old style", 15, "bold"), bg='#eBffff').place(x=20,y=32,height=50)
        lbl_std = Label(self.window, text="Std:", font=("goudy old style", 15, "bold"), bg='#eBffff').place(x=20,y=70,height=50)
        lbl_class = Label(self.window, text="Class:", font=("goudy old style", 15, "bold"), bg='#eBffff').place(x=200,y=70,height=50)
        lbl_adress = Label(self.window, text="Address:", font=("goudy old style", 15, "bold"), bg='#eBffff').place(x=390,y=70,height=50)
        lbl_roll = Label(self.window, text="Roll no:", font=("goudy old style", 15, "bold"), bg='#eBffff').place(x=14,y=103,height=40)
        lbl_name = Label(self.window, text="Name:", font=("goudy old style", 15, "bold"), bg='#eBffff').place(x=200,y=105,height=40)
        lbl_year = Label(self.window, text="Year:", font=("goudy old style", 15, "bold"), bg='#eBffff').place(x=395,y=168,height=50)
        lbl_result = Label(self.window, text="Result:", font=("goudy old style", 15, "bold"), bg='#eBffff').place(x=395, y=205,height=50)
        lbl_grand = Label(self.window, text="Grand Total:", font=("goudy old style", 15, "bold"), bg='#eBffff').place(x=395,y=240,height=50)
        lbl_perc = Label(self.window, text="Percentage:", font=("goudy old style", 15, "bold"), bg='#eBffff').place(x=395,y=275,height=50)
        lbl_grade = Label(self.window, text="Grade:", font=("goudy old style", 15, "bold"), bg='#eBffff').place(x=395,y=310,height=50)
        lbl_env = Label(self.window, text="Environent:", font=("goudy old style", 15, "bold"), bg='#eBffff').place(x=395,y=345,height=50)
        lbl_pe = Label(self.window, text="PE:", font=("goudy old style", 15, "bold"), bg='#eBffff').place(x=395,y=380,height=50)
        lbl_reopning = Label(self.window, text="Reopening:", font=("goudy old style", 15, "bold"), bg='#eBffff').place(x=395,y=415,height=50)
        lbl_grace = Label(self.window, text="Grace marks", font=("goudy old style", 10, "bold"), bg='#eBffff').place(x=298, y=122,height=50)
        #lbl_final = Label(self.window, text="Final marks", font=("goudy old style", 10, "bold"), bg='#eBffff').place(x=200, y=122, height=50)
        #lbl_math = Label(self.window, text="Mathematics:", font=("goudy old style", 15, "bold"), bg='#eBffff').place(x=20,y=160,height=50)
        self.txt_E46 = Entry(self.window, textvariable=self.var_math, font=("goudy old style", 15,"bold"),bg='#e3f4fe',state='readonly')
        self.txt_E46.place(x=20, y=160, width=100)

        #lbl_bio = Label(self.window, text="biology:", font=("goudy old style", 15, "bold"), bg='#eBffff').place(x=20,y=200,height=50)
        self.txt_E47 = Entry(self.window, textvariable=self.var_bio, font=("goudy old style", 15,"bold"),bg='#e3f4fe',state='readonly')
        self.txt_E47.place(x=20, y=200, width=100)

        #lbl_phy = Label(self.window, text="Physics:", font=("goudy old style", 15, "bold"), bg='#eBffff').place(x=20,y=240,height=50)
        self.txt_E48 = Entry(self.window, textvariable=self.var_phy, font=("goudy old style", 15,"bold"),bg='#e3f4fe',state='readonly')
        self.txt_E48.place(x=20, y=240, width=100)


        #lbl_chem = Label(self.window, text="Chemistry:", font=("goudy old style", 15, "bold"), bg='#eBffff').place(x=20,y=280,height=50)
        self.txt_E49 = Entry(self.window, textvariable=self.var_chem, font=("goudy old style", 15,"bold"),bg='#e3f4fe',state='readonly')
        self.txt_E49.place(x=20, y=280, width=100)


        #lbl_urdu = Label(self.window, text="Urdu:", font=("goudy old style", 15, "bold"), bg='#eBffff').place(x=20,y=320,height=50)
        self.txt_E50 = Entry(self.window, textvariable=self.var_ur, font=("goudy old style", 15,"bold"),bg='#e3f4fe',state='readonly')
        self.txt_E50.place(x=20, y=320, width=100)

        #lbl_eng = Label(self.window, text="English:", font=("goudy old style", 15, "bold"), bg='#eBffff').place(x=20,y=360,height=50)
        self.txt_E51 = Entry(self.window, textvariable=self.var_eng, font=("goudy old style", 15,"bold"),bg='#e3f4fe',state='readonly')
        self.txt_E51.place(x=20, y=360, width=100)

        #lbl_hindi = Label(self.window, text="Hindi:", font=("goudy old style", 15, "bold"), bg='#eBffff').place(x=20,y=400,height=50)
        self.txt_E52 = Entry(self.window, textvariable=self.var_Hin, font=("goudy old style", 15,"bold"),bg='#e3f4fe',state='readonly')
        self.txt_E52.place(x=20, y=400, width=100)

        #lbl_geo = Label(self.window, text="Geography:", font=("goudy old style", 15, "bold"), bg='#eBffff').place(x=20,y=440,height=50)
        self.txt_E53 = Entry(self.window, textvariable=self.var_geo, font=("goudy old style", 15,"bold"),bg='#e3f4fe',state='readonly')
        self.txt_E53.place(x=20, y=440, width=100)

        #lbl_cs1 = Label(self.window, text="CS1:", font=("goudy old style", 15, "bold"), bg='#eBffff').place(x=20,y=480,height=50)
        self.txt_E54 = Entry(self.window, textvariable=self.var_cs1, font=("goudy old style", 15,"bold"),bg='#e3f4fe',state='readonly')
        self.txt_E54.place(x=20, y=480, width=100)


        #lbl_cs2 = Label(self.window, text="CS2:", font=("goudy old style", 15, "bold"), bg='#eBffff').place(x=20,y=520,height=50)
        self.txt_Cs2_6 = Entry(self.window, textvariable=self.var_cs2, font=("goudy old style", 15,"bold"),bg='#e3f4fe',state='readonly')
        self.txt_Cs2_6.place(x=20, y=520, width=100)


        #Entriies
        self.txt_student = ttk.Combobox(self.window, textvariable=self.var_grno,values=self.grno_list, font=("goudy old style", 15, "bold"), justify=CENTER)
        self.txt_student.place(x=90, y=40, width=150)
        self.txt_student.set("Select")

        self.txt_name = Entry(self.window, textvariable=self.var_name, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_name.place(x=280, y=110, width=400)

        self.txt_std = Entry(self.window, textvariable=self.var_std, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_std.place(x=90, y=80, width=100)

        self.txt_class = Entry(self.window, textvariable=self.var_class, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_class.place(x=280, y=80, width=100)

        self.txt_adress = Entry(self.window, textvariable=self.var_adress, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_adress.place(x=500 , y=80, width=300)

        self.txt_roll = Entry(self.window, textvariable=self.var_roll, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_roll.place(x=90, y=110, width=100)

        self.txt_E46 = Entry(self.window, textvariable=self.var_ET46, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E46.place(x=200, y=160, width=80)

        self.txt_E47 = Entry(self.window, textvariable=self.var_ET47, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E47.place(x=200, y=200, width=80)

        self.txt_E48 = Entry(self.window, textvariable=self.var_ET48, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E48.place(x=200, y=240, width=80)

        self.txt_E49 = Entry(self.window, textvariable=self.var_ET49, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E49.place(x=200, y=280, width=80)

        self.txt_E50 = Entry(self.window, textvariable=self.var_ET50, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E50.place(x=200, y=320, width=80)

        self.txt_E51 = Entry(self.window, textvariable=self.var_ET51, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E51.place(x=200, y=360, width=80)

        self.txt_E52 = Entry(self.window, textvariable=self.var_ET52, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E52.place(x=200, y=400, width=80)

        self.txt_E53 = Entry(self.window, textvariable=self.var_ET53, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E53.place(x=200, y=440, width=80)

        self.txt_E54 = Entry(self.window, textvariable=self.var_ET54, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E54.place(x=200, y=480, width=80)

        self.txt_Cs2_6 = Entry(self.window, textvariable=self.var_Cs2_6, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_Cs2_6.place(x=200, y=520, width=80)
        #Grace
        self.txt_E461 = Entry(self.window, textvariable=self.var_ET461, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E461.place(x=300, y=160, width=80)

        self.txt_E471 = Entry(self.window, textvariable=self.var_ET471, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E471.place(x=300, y=200, width=80)

        self.txt_E481 = Entry(self.window, textvariable=self.var_ET481, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E481.place(x=300, y=240, width=80)

        self.txt_E491 = Entry(self.window, textvariable=self.var_ET491, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E491.place(x=300, y=280, width=80)

        self.txt_E501 = Entry(self.window, textvariable=self.var_ET501, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E501.place(x=300, y=320, width=80)

        self.txt_E511 = Entry(self.window, textvariable=self.var_ET511, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E511.place(x=300, y=360, width=80)

        self.txt_E521 = Entry(self.window, textvariable=self.var_ET521, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E521.place(x=300, y=400, width=80)

        self.txt_E531 = Entry(self.window, textvariable=self.var_ET531, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E531.place(x=300, y=440, width=80)

        self.txt_E541 = Entry(self.window, textvariable=self.var_ET541, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E541.place(x=300, y=480, width=80)

        self.txt_Cs2_61 = Entry(self.window, textvariable=self.var_Cs2_61, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_Cs2_61.place(x=300, y=520, width=80)

        #column2
        self.txt_year = Entry(self.window, textvariable=self.var_year, font=("goudy old style", 15, "bold"),bg='#e3f4fe')
        self.txt_year.place(x=520, y=178, width=200)

        self.txt_result = Entry(self.window, textvariable=self.var_result, font=("goudy old style", 15, "bold"),bg='#e3f4fe')
        self.txt_result.place(x=520, y=215, width=200)

        self.txt_grandtotal = Entry(self.window, textvariable=self.var_grandtotal, font=("goudy old style", 15, "bold"),bg='#e3f4fe')
        self.txt_grandtotal.place(x=520, y=250, width=200)

        self.txt_perc = Entry(self.window, textvariable=self.var_perc, font=("goudy old style", 15, "bold"),bg='#e3f4fe')
        self.txt_perc.place(x=520, y=285, width=200)

        self.txt_grade = Entry(self.window, textvariable=self.var_grade, font=("goudy old style", 15, "bold"),bg='#e3f4fe')
        self.txt_grade.place(x=520, y=320, width=200)

        self.txt_env = Entry(self.window, textvariable=self.var_env, font=("goudy old style", 15, "bold"),bg='#e3f4fe')
        self.txt_env.place(x=520, y=355, width=200)

        self.txt_pe = Entry(self.window, textvariable=self.var_pe, font=("goudy old style", 15, "bold"),bg='#e3f4fe')
        self.txt_pe.place(x=520, y=390, width=200)


        self.txt_reopening = Entry(self.window, textvariable=self.var_reopening, font=("goudy old style", 15, "bold"),bg='#e3f4fe')
        self.txt_reopening.place(x=520, y=425, width=200)

        lbl_select = Label(self.window, text="File Name:", font=("goudy old style", 15, "bold"), bg='#eBffff').place(x=20, y=687, height=50)
        self.filenam_raw_entry1=StringVar()
        self.txt_filename = Entry(self.window, textvariable=self.filenam_raw_entry1, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_filename.place(x=149, y=700, width=180)

        self.btn_result=Button(self.window,text='Get Result',font=("times new roman",15,"bold"),command=self.generate_pdf,bg="#89CFF0",cursor="hand2")
        self.btn_result.place(x=348, y=698, width=150, height=30)
        self.filenam_raw_entry2=StringVar()

        lbl_file_name = Label(self.window, text="File Name:", font=("goudy old style", 15, "bold"), bg='#eBffff').place(x=20, y=640, height=50)
        self.txt_no_of_pages = Entry(self.window, textvariable=self.filenam_raw_entry2, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_no_of_pages.place(x=149, y=650, width=180)
        self.btn_result=Button(self.window,text='Get Conso',font=("times new roman",15,"bold"),command=self.create_pdf,bg="#89CFF0",cursor="hand2")
        self.btn_result.place(x=348, y=650, width=150, height=30)






        #Buttons
        self.btn_search=Button(self.window,text='Go',font=("times new roman",15,"bold"),command=self.search,bg="lightgreen",cursor="hand2")
        self.btn_search.place(x=240, y=40, width=30, height=28)
        self.btn_getresult=Button(self.window,text='Get Result',font=("times new roman",15,"bold"),command=self.main_result,bg="lightgreen",cursor="hand2")
        self.btn_getresult.place(x=520, y=462, width=110, height=30)
        #self.btn_search=Button(self.window,text='Generate Result',font=("times new roman",15,"bold"),command=self.generate_pdf,bg="red",cursor="hand2")
        #self.btn_search.place(x=400, y=700, width=160, height=30)
        self.btn_csv=Button(self.window,text='Generate CSV',font=("times new roman",15,"bold"),command=self.generate_csv,bg="#89CFF0",cursor="hand2")
        self.btn_csv.place(x=600, y=698, width=160, height=30)
        lbl_search_roll=Label(self.window,text="Search GRNo:",font=("goudy old style",15,"bold"),bg="#eBffff").place(x=860,y=32,height=50)
        self.txt_search_roll=Entry(self.window,textvariable=self.var_search,font=("goudy old style",15,"bold"),bg='#e3f4fe')
        self.txt_search_roll.place(x=990, y=40, width=200)
        self.btn_search1=Button(self.window,text='Search',font=("times new roman",15,"bold"),command=self.search1,bg="lightgreen")
        self.btn_search1.place(x=1195, y=39, width=110, height=30)

        #Frame
        self.C_frame = Frame(self.window, bd=2, relief=RIDGE)
        self.C_frame.place(x=810, y=80, width=600,height=680)
        scrolly = Scrollbar(self.C_frame, orient=VERTICAL)
        scrollx = Scrollbar(self.C_frame, orient=HORIZONTAL)
        self.resultTable = ttk.Treeview(self.C_frame, columns=("grno","roll", "Std", "Class","Math", "Bio", "Phy", "Chem", "Urdu", "Eng", "Hin", "Geo","Cs1","Cs2","env","pe","date","result","grandtotal","perc","grade","name","adress","reop"))
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=X)
        scrollx.config(command=self.resultTable.xview)
        scrolly.config(command=self.resultTable.yview)
        self.resultTable.heading("grno", text="GRNo.")
        self.resultTable.heading("roll", text="Roll")
        self.resultTable.heading("Std", text="Std")
        self.resultTable.heading("Class", text="Class")
        self.resultTable.heading("Math", text="Math")
        self.resultTable.heading("Bio", text="Biology")
        self.resultTable.heading("Phy", text="physics")
        self.resultTable.heading("Chem", text="Chemistry")
        self.resultTable.heading("Urdu", text="Urdu")
        self.resultTable.heading("Eng", text="English")
        self.resultTable.heading("Hin", text="Hindi")
        self.resultTable.heading("Geo", text="Geograpy")
        self.resultTable.heading("Cs1", text="CS1")
        self.resultTable.heading("Cs2", text="CS2")
        self.resultTable.heading("env", text="Environment")
        self.resultTable.heading("pe", text="P.E.")
        self.resultTable.heading("date",text="Year")
        self.resultTable.heading("result",text="Result")
        self.resultTable.heading("grandtotal",text="grandtotal")
        self.resultTable.heading("perc",text="percentage")
        self.resultTable.heading("grade",text="grade")
        self.resultTable.heading("name",text="Name")
        self.resultTable.heading("adress",text="Address")
        self.resultTable.heading("reop", text="Reopening")


        self.resultTable["show"] = 'headings'
        self.resultTable.column("grno", width=60)
        self.resultTable.column("roll", width=60)
        self.resultTable.column("Std", width=60)
        self.resultTable.column("Class", width=60)
        self.resultTable.column("Math", width=60)
        self.resultTable.column("Bio", width=60)
        self.resultTable.column("Phy", width=60)
        self.resultTable.column("Chem", width=60)
        self.resultTable.column("Urdu", width=60)
        self.resultTable.column("Eng", width=60)
        self.resultTable.column("Hin", width=60)
        self.resultTable.column("Geo", width=60)
        self.resultTable.column("Cs1", width=60)
        self.resultTable.column("Cs2", width=60)
        self.resultTable.column("env", width=60)
        self.resultTable.column("pe", width=60)
        self.resultTable.column("date", width=60)
        self.resultTable.column("result",width=60)
        self.resultTable.column("grandtotal",width=60)
        self.resultTable.column("perc",width=60)
        self.resultTable.column("grade",width=80)
        self.resultTable.column("name",width=180)
        self.resultTable.column("adress",width=180)
        self.resultTable.column("reop", width=180)
        self.resultTable.pack(fill=BOTH, expand=1)
        self.resultTable.bind("<ButtonRelease-1>", self.get_data)
        self.show()

        #buttons
        self.btn_add=Button(self.window,text='Save',font=("goudy old style",15,"bold"),command=self.add,bg="#87d3f8")
        self.btn_add.place(x=150,y=600,width=110,height=30)
        self.btn_update = Button(self.window, text='Update', font=("goudy old style", 15, "bold"),command=self.update, bg="#87d3f8")
        self.btn_update.place(x=270, y=600, width=110, height=30)
        self.btn_add = Button(self.window, text='Delete', font=("goudy old style", 15, "bold"),command=self.delete, bg="#87d3f8")
        self.btn_add.place(x=390, y=600, width=110, height=30)
        self.btn_clear = Button(self.window, text='Clear', font=("goudy old style", 15, "bold"),command=self.clear_data, bg="#87d3f8")
        self.btn_clear.place(x=510, y=600, width=110, height=30)

        self.btn_delete_all = Button(self.window, text='Delete All', font=("goudy old style", 15, "bold"),command=self.delete_all, bg="red")
        self.btn_delete_all.place(x=600, y=745, width=110, height=30)



        self.de_frame()





    def delete_all(self):
        for record in self.resultTable.get_children():
            self.resultTable.delete(record)
        conn=sqlite3.connect('rms.db')
        c=conn.cursor()
        op = messagebox.askyesno("Confirm", "Do you really wanto to delete?", parent=self.window)
        if op == True:
            #c.execute('DROP TABLE resultTable')
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





    def search1(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select * from courseTable where grno=?", (self.var_search.get(),))
            row = cur.fetchone()
            if row != None:
                self.resultTable.delete(*self.resultTable.get_children())
                self.resultTable.insert('', END, values=row)
            else:
                messagebox.showerror("Error", "No record found", parent=self.window)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")




    def fetch_grno(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select grno from studentTable")
            rows = cur.fetchall()

            if len(rows)>0:
                for row in rows:
                    self.grno_list.append(row[0])

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def search(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select * from courseTable where grno=?", (self.var_grno.get(),))
            row = cur.fetchone()
            #cur.execute("select roll,name,class,address,std from studentTable where grno=?", (self.var_grno.get(),))
            #row2 = cur.fetchone()
            cur.execute("select roll_no,students_name from bqkTablee where grno=?", (self.var_grno.get(),))
            row2 = cur.fetchone()
            cur.execute("select ET46,ET47,ET48,ET49,ET50,ET51,ET52,ET53,ET54,Cs_2_6,env,pe from marksTable where grno=?", (self.var_grno.get(),))
            row3 = cur.fetchone()



            if row != None:
                print(row,"lll")
                #if row3 !=None:
                #    for j in range(len(row3)):

                #       if row[j+3]=='1' and row3[j]==0:
                #            self.var_result.set("Fail")
                #            self.f=True
                #            break

                if row[6]=="1":
                    self.var_math.set("Math")
                else:
                    self.var_math.set("-")
                if row[7]=="1":
                    self.var_bio.set("Biology")
                else:
                    self.var_bio.set("-")
                if row[4]=="1":
                    self.var_phy.set("Physics")
                else:
                    self.var_phy.set("-")
                if row[5]=="1":
                    self.var_chem.set("Chemistry")
                else:
                    self.var_chem.set("-")
                if row[9]=="1":
                    self.var_ur.set("Urdu")
                else:
                    self.var_ur.set("-")
                if row[3]=="1":
                    self.var_eng.set("English")
                else:
                    self.var_eng.set("-")
                if row[10]=="1":
                    self.var_Hin.set("Hindi")
                else:
                    self.var_Hin.set("-")
                if row[8]=="1":
                    self.var_geo.set("Geography")
                else:
                    self.var_geo.set("-")
                if row[11]=="1":
                    self.var_cs1.set("CS1")
                    self.var_cs2.set("CS2")
                else:
                    self.var_cs1.set("-")
                #if row[12]=="1":
                #    self.var_cs2.set("CS2")
                #else:
                #    self.var_cs2.set("-")

            """if row2!=None:
                self.var_roll.set(int(row2[0]))
                self.var_name.set(row2[1])
                self.var_class.set(row2[2])
                self.var_adress.set(row2[3])
                self.var_std.set(row2[4])"""
            if row2 != None:
                self.var_roll.set(int(row2[0]))
                self.var_name.set(row2[1])


                #self.var_mother.set(2)
            if row3!=None:
                #print(row3,"oooooodddddd")
                self.var_env.set(row3[-2])
                self.var_pe.set(row3[-1])
                if row[6]=="1":
                    self.var_ET46.set(row3[0])
                    if float(row3[0])<35:
                        #print(35-float(row3[0]),"hereee")
                        self.var_ET461.set(35-math.ceil(row3[0]))
                else:
                    self.var_ET46.set("-")
                    self.var_ET461.set("-")
                if row[7]=="1":
                    self.var_ET47.set(row3[1])
                    if float(row3[1])<35:
                        self.var_ET471.set(35-math.ceil(row3[1]))
                else:
                    self.var_ET47.set("-")
                    self.var_ET471.set("-")
                if row[4]=="1":
                    self.var_ET48.set(row3[2])
                    if float(row3[2])<35:
                        self.var_ET481.set(35-math.ceil(row3[2]))
                else:
                    self.var_ET48.set("-")
                    self.var_ET481.set("-")
                if row[5]=="1":
                    self.var_ET49.set(row3[3])

                    if float(row3[3])<35:
                        self.var_ET491.set(35-math.ceil(row3[3]))
                else:
                    self.var_ET49.set("-")
                    self.var_ET491.set("-")
                if row[9]=="1":
                    self.var_ET50.set(row3[4])
                    if float(row3[4])<35:
                        self.var_ET501.set(35-math.ceil(row3[4]))
                else:
                    self.var_ET50.set("-")
                    self.var_ET501.set("-")
                if row[3]=="1":
                    self.var_ET51.set(row3[5])
                    if float(row3[5])<35:
                        self.var_ET511.set(35-math.ceil(row3[5]))
                else:
                    self.var_ET51.set("-")
                    self.var_ET511.set("-")
                if row[10]=="1":
                    self.var_ET52.set(row3[6])
                    if float(row3[6])<35:
                        self.var_ET521.set(35-math.ceil(row3[6]))
                else:
                    self.var_ET52.set("-")
                    self.var_ET521.set("-")
                if row[8]=="1":
                    self.var_ET53.set(row3[7])
                    if float(row3[7])<35:
                        self.var_ET531.set(35-math.ceil(row3[7]))
                else:
                    self.var_ET53.set('-')
                    self.var_ET531.set('-')
                if row[11]=="1":
                    self.var_ET54.set(row3[8])
                    self.var_Cs2_6.set(row3[9])
                    if float(row3[8])<35:
                        self.var_ET541.set(35-math.ceil(row3[8]))
                    if float(row3[9])<35:
                        self.var_Cs2_61.set(35-math.ceil(row3[9]))

                else:

                    self.var_ET54.set("-")
                    self.var_Cs2_6.set("-")
                    self.var_ET541.set("-")
                    self.var_Cs2_61.set("-")


            else:
                messagebox.showerror("Error", "No record found", parent=self.window)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def clear_data(self):
        self.show()
        self.var_grno.set("Select")
        self.var_roll.set(""),
        self.var_class.set(""),
        self.var_std.set(""),

        self.var_math.set(""),
        self.var_bio.set(""),
        self.var_phy.set(""),
        self.var_chem.set(""),
        self.var_ur.set(""),
        self.var_eng.set(""),
        self.var_Hin.set(""),
        self.var_geo.set(""),
        self.var_cs1.set(""),
        self.var_cs2.set(""),
        self.var_ET46.set(""),
        self.var_ET47.set(""),
        self.var_ET48.set(""),
        self.var_ET49.set(""),
        self.var_ET50.set(""),
        self.var_ET51.set(""),
        self.var_ET52.set(""),
        self.var_ET53.set(""),
        self.var_ET54.set(""),
        self.var_Cs2_6.set(""),
        self.var_year.set(""),
        self.var_result.set(""),
        self.var_grandtotal.set(""),
        self.var_perc.set(""),
        self.var_grade.set(""),
        self.var_ET461.set(""),
        self.var_ET471.set(""),
        self.var_ET481.set(""),
        self.var_ET491.set(""),
        self.var_ET501.set(""),
        self.var_ET511.set(""),
        self.var_ET521.set(""), 
        self.var_ET531.set(""),
        self.var_ET541.set(""),
        self.var_Cs2_61.set(""),
        self.var_name.set(""),
        self.var_adress.set(""),
        self.var_env.set(""),
        self.var_pe.set(""),
        self.var_reopening.set("")


    def get_data(self, ev):
        #self.var_roll.config(state='readonly')

        r=self.resultTable.focus()
        content=self.resultTable.item(r)
        row=content["values"]
        self.var_grno.set(row[0]),
        self.var_roll.set(row[1]),
        self.var_class.set(row[3]),
        self.var_std.set(row[2]),

        #self.var_sub.set(row[4])
#        self.var_math.set(row[4]),
#        self.var_bio.set(row[5]),
#        self.var_phy.set(row[6]),
#        self.var_chem.set(row[7]),
#        self.var_ur.set(row[8]),
#        self.var_eng.set(row[9]),
#        self.var_Hin.set(row[10]),
#        self.var_geo.set(row[11]),
#        self.var_cs1.set(row[12])
#        self.var_cs2.set(row[13])
        self.var_ET46.set(row[4]),
        self.var_ET47.set(row[5]),
        self.var_ET48.set(row[6]),
        self.var_ET49.set(row[7]),
        self.var_ET50.set(row[8]),
        self.var_ET51.set(row[9]),
        self.var_ET52.set(row[10]),
        self.var_ET53.set(row[11]),
        self.var_ET54.set(row[12]),
        self.var_Cs2_6.set(row[13]),
        self.var_env.set(row[14]),
        self.var_pe.set(row[15])
        self.var_year.set(row[16]),
        self.var_result.set(row[17]),
        self.var_grandtotal.set(row[18]),
        self.var_perc.set(row[19]),
        self.var_grade.set(row[20]),
        self.var_name.set(row[21]),
        self.var_adress.set(row[22]),
        self.var_reopening.set(row[23])


    def delete(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_grno.get()=="":

                messagebox.showerror("Error","GRNo.should be required",parent=self.window)

            else:
                cur.execute("select * from resultTable where grno=?",(self.var_grno.get(),))
                row=cur.fetchone()
                if row==None:

                    messagebox.showerror("Error","please select resultTable from the list first",parent=self.window)

                else:
                    op=messagebox.askyesno("Confirm","Do you really wanto to delete?",parent=self.window)
                    if op==True:

                        cur.execute("delete from resultTable where grno=?",(self.var_grno.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Student deleted succesfilly",parent=self.window)

                        self.clear_data()
        except Exception as ex:
            messagebox.showerror(("Error",f"Error due to{str(ex)}"))



    def add(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_grno.get() == "":
                messagebox.showerror("Error", "GRNo. should be required", parent=self.window)
            else:
                cur.execute("select *  from resultTable where grno=?", (self.var_grno.get(),))
                row = cur.fetchone()

                if row != None:
                    messagebox.showerror("Error", "GRNo. Already present", parent=self.window)
                else:

                    cur.execute("insert into resultTable(grno,roll,Std,Class,Math,Bio,Phy,Chem,Urdu,Eng,Hin,Geo,Cs1,Cs2,env,pe,date,result,grandtotal,perc,grade,name,adress,reop) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(
                           self.var_grno.get(),
                           self.var_roll.get(),
                           self.var_std.get(),
                           self.var_class.get(),

                           self.var_ET46.get(),
                           self.var_ET47.get(),
                           self.var_ET48.get(),
                           self.var_ET49.get(),
                           self.var_ET50.get(),
                           self.var_ET51.get(),
                           self.var_ET52.get(),
                           self.var_ET53.get(),
                           self.var_ET54.get(),
                           self.var_Cs2_6.get(),
                           self.var_env.get(),
                           self.var_pe.get(),
                           #self.var_math.get(),
                           #self.var_bio.get(),
                           #self.var_phy.get(),
                           #self.var_chem.get(),
                           #self.var_ur.get(),
                           #self.var_eng.get(),
                           #self.var_Hin.get(),
                           #self.var_geo.get(),
                           #self.var_cs1.get(),
                           #self.var_cs2.get(),
                           self.var_year.get(),
                           self.var_result.get(),
                           self.var_grandtotal.get(),
                           self.var_perc.get(),
                           self.var_grade.get(),
                           self.var_name.get(),
                           self.var_adress.get(),
                           self.var_reopening.get()



                    ) )

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
                cur.execute("select * from resultTable where grno=?",(self.var_grno.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Select resultTable from list",parent=self.window)
                else:
                    cur.execute("update resultTable set roll=?,Std=?,Class=?,Math=?,Bio=?,Phy=?,Chem=?,Urdu=?,Eng=?,Hin=?,Geo=?,Cs1=?,Cs2=?,env=?,pe=?,date=?,result=?,grandtotal=?,perc=?,grade=?,name=?,adress=?,reop=? where grno=?", (
                        self.var_roll.get(),
                        self.var_std.get(),
                        self.var_class.get(),

                        self.var_ET46.get(),
                        self.var_ET47.get(),
                        self.var_ET48.get(),
                        self.var_ET49.get(),
                        self.var_ET50.get(),
                        self.var_ET51.get(),
                        self.var_ET52.get(),
                        self.var_ET53.get(),
                        self.var_ET54.get(),
                        self.var_Cs2_6.get(),
                        self.var_env.get(),
                        self.var_pe.get(),
                        #self.var_math.get(),
                        #self.var_bio.get(),
                        #self.var_phy.get(),
                        #self.var_chem.get(),
                        #self.var_ur.get(),
                        #self.var_eng.get(),
                        #self.var_Hin.get(),
                        #self.var_geo.get(),
                        #self.var_cs1.get(),
                        #self.var_cs2.get(),
                        self.var_year.get(),
                        self.var_result.get(),
                        self.var_grandtotal.get(),
                        self.var_perc.get(),
                        self.var_grade.get(),
                        self.var_name.get(),
                        self.var_adress.get(),
                        self.var_reopening.get(),
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
            cur.execute("select * from resultTable")
            rows = cur.fetchall()
            self.resultTable.delete(*self.resultTable.get_children())
            for row in rows:
                self.resultTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
    def main_result(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select Math,Bio,Phy,Chem,Urdu,Eng,Hin,Geo,Cs1,Cs2 from resultTable where grno=?", (self.var_grno.get(),))
            row = cur.fetchone()
            if row != None:
                sum=0
                for r in row:

                    if r!='-':
                        sum=sum+float(r)
                self.var_grandtotal.set(math.ceil(sum))
                perc=(sum/600)*100
                self.var_perc.set(round(perc,2))
                #print(perc,"ooo")
                #print(self.f,"falsss")
                if 100>=perc>=75 and self.f==False:
                    self.var_grade.set("Ist Class with Distinction")
                    self.var_result.set("Pass")
                elif 75>perc>=60 and self.f==False:
                    self.var_grade.set("I Class")
                    self.var_result.set("Pass")
                elif 60>perc>=45 and self.f==False:
                    self.var_grade.set("II Class")
                    self.var_result.set("Pass")
                elif perc<35:
                    self.var_result.set("Fail")


            else:
                messagebox.showerror("Error", "No record found", parent=self.window)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def generate_pdf(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select * from resultTable where grno=?", (self.var_grno.get(),))
            row = cur.fetchone()
            #print(row,"lllllll")
            if row != None:
                self.var_name.set(row[21])

            else:
                messagebox.showerror("Error", "No record found", parent=self.window)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
        try:
            packet = io.BytesIO()
            can = canvas.Canvas(packet, pagesize=letter)
            can.setFillColorRGB(0, 0, 0)
            can.setFont("Times-Roman", 14)
            can.drawString(174,627, str(row[21]))  #Name
            print(row)
            can.drawString(135, 592, str(row[2]+'-'+row[3])) #stdanddiv
            can.drawString(140, 552, str(row[1]))#roll
            can.drawString(450, 589, str(row[0])) #grno
            can.drawString(345, 691, str(row[16]))#year
            can.drawString(450, 552, str(row[23]))#reopenning
            can.drawString(468,477, str(row[4])) #1
            can.drawString(468,450, str(row[5])) #2
            can.drawString(468,430, str(row[6])) #3
            can.drawString(468,410, str(row[7])) #4
            can.drawString(468,387, str(row[8])) #5
            can.drawString(468,365, str(row[9])) #6
            can.drawString(468,345, str(row[10])) #7
            can.drawString(468,325, str(row[11])) #8
            if row[12]!='-':
                can.drawString(468,305, str(math.ceil(float(row[12])+float(row[13])))) #9
            else:
                can.drawString(468, 305, str("-"))
            can.drawString(468,285, str(row[14]))  # 10
            can.drawString(468,265 , str(row[15]))  # 11
            can.drawString(138, 215, str(row[19]))  # 12
            can.drawString(138,180, str(row[18])) #13
            can.drawString(115, 144, str(row[17]))  # 14
            can.drawString(115, 108, str(row[20]))  # 15


            can.save()
            packet.seek(0)
            new_pdf = PdfFileReader(packet)
            existing_pdf = PdfFileReader(open("SSAreport.pdf", "rb"))#SSA3f
            output = PdfFileWriter()
            page = existing_pdf.getPage(0)
            page.mergePage(new_pdf.getPage(0))
            output.addPage(page)
            filename = str(self.filenam_raw_entry1.get())
            myfilename = filename + '.pdf'
            with open(myfilename, 'wb') as f:

                #outputStream = open("AAAAA.pdf", "wb")
                output.write(f)
                f.close()
                messagebox.showinfo("Success", "Result Generated Successfully", parent=self.window)
                self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def create_pdf(self):#filename,n
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        #n=getint(self.no_of_pages.get())
        try:
            cur.execute("select * from resultTable")
            row = cur.fetchall()

            n=math.ceil(len(row)/18)
            print(n,len(row),"lllllkkkkkkkkkkkkkkkkk")
            if row != None:
                #pdf_file = filename+'.pdf'
                #pdf_file=filename+'.pdf'
                packet = io.BytesIO()
                can = canvas.Canvas(packet,pagesize=letter)
                can.setFillColorRGB(0, 0, 0)  # till here everything is okay
                can.setFont("Times-Roman", 12)

                temp=0
                for j in range(getint(n)):
                    i=0
                    y=0
                    print(temp,"hereee",j)
                    while i <len(row) and i+temp<len(row):
                        print(row[i+temp], "alalalaalla")
                        can.drawString(45, 470 - y, str(row[i+temp][1]))
                        can.drawString(82, 470 - y, str(row[i+temp][8]))  # urdu
                        can.drawString(115, 470 - y, str(row[i+temp][9]))  # eng
                        can.drawString(155, 470 - y, str(row[i+temp][10]))  # hin
                        can.drawString(195, 470 - y, str(row[i+temp][6]))  # phy
                        can.drawString(232, 470 - y, str(row[i+temp][7]))  # chem
                        can.drawString(270, 470 - y, str(row[i+temp][5]))  # bio
                        can.drawString(307, 470 - y, str(row[i+temp][4]))  # math
                        can.drawString(345, 470 - y, str(row[i+temp][11]))  # geo
                        can.drawString(388, 470 - y, str(row[i+temp][14]))  # env
                        can.drawString(420, 470 - y, str(row[i+temp][15]))  # pe
                        can.drawString(458, 470 - y, str(row[i+temp][18]))  # grandtotal
                        can.drawString(490, 470 - y, str(row[i+temp][19]))  # percent
                        # can.drawString(545, 470, str(row[8]))  # rank
                        can.drawString(583, 470 - y, str(row[i+temp][20]))  # grade
                        y += 25
                        print(i,"iiii")
                        if i>=17 and i%17 == 0:
                            temp=temp+i+1
                            break
                        i+=1
                    #if j>=len(row):
                    #    break
                    print(i,j,temp)
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
                existing_pdf = PdfFileReader(open("SSAconsolidated.pdf", "rb"))
                output = PdfFileWriter()

                for i in range(n):#len(existing_pdf.pages)
                    page = existing_pdf.getPage(i)
                    page.mergePage(new_pdf.getPage(i))
                    output.addPage(page)
                filename = str(self.filenam_raw_entry2.get())
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

    def copy_pdfs(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select * from resultTable")
            row = cur.fetchall()
            if row != None:
                packet = io.BytesIO()
                #pdf_file = str(self.filenam_raw_entry1.get())
                can = canvas.Canvas(packet, pagesize=letter)  # packet, pagesize=letter
                can.setFillColorRGB(0, 0, 0)  # till here everything is okay
                can.setFont("Times-Roman", 12)
                can.save()

                packet.seek(0)
                new_pdf = PdfFileReader(packet)
                existing_pdf = PdfFileReader(open("SSAmark_sheetsf4.pdf", "rb"))
                output = PdfFileWriter()
                page = existing_pdf.getPage(0)
                page.mergePage(new_pdf.getPage(0))
                for i in range(33):#getint((self.no_of_pages).get())
                    output.addPage(page)

                filename = 'SSAmark_sheetsf5'#str(self.filenam_raw_entry1.get())
                myfilename = filename + '.pdf'
                with open(myfilename, 'wb') as f:
                    output.write(f)
                    f.close()
                    messagebox.showinfo("Success", "Result Generated Successfully", parent=self.window)
                    self.show()

            else:
                messagebox.showerror("Error", "No record found", parent=self.window)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")


    def generate_csv(self):
        self.new_win=Toplevel(self.window)
        self.obj1=exportClass(self.new_win)




if __name__=="__main__":
    window=Tk()
    obj=resultClass(window)
    window.mainloop()