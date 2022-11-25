from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3


class course:
    def __init__(self,window):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        cur.execute(
            "CREATE TABLE IF NOT EXISTS courseTable(grno INTEGER PRIMARY KEY AUTOINCREMENT,roll text,Class text,English text,Physics text,Chemistry text,Maths text,Biology text,Geo text,Urdu text,Hindi text,CS text)")
        con.commit()
        con.close()
        self.window=window
        self.window.title("Add Subjects")
        self.window.geometry("1350x800+80+50")
        self.window.config(bg="white")
        self.window.focus_force()
        #variables
        self.var_roll=StringVar()
        self.var_class=StringVar()
        self.var_grno=StringVar()
        self.var_name=StringVar()
        self.tkvar1 =IntVar()
        self.tkvar2 =IntVar()
        self.tkvar3 = IntVar()
        self.tkvar4 = IntVar()
        self.tkvar5 = IntVar()
        self.tkvar6 = IntVar()
        self.tkvar7 = IntVar()
        self.tkvar8 = IntVar()
        self.tkvar9 = IntVar()

        self.class_list=["Select",'Class A',"Class B","Class C"]
        self.grno_list = []
        self.fetch_grno()
        #Labels
        title = Label(self.window, text="Add Subjects to a Student ", padx=10, font=("goudy old stlye", 15, "bold"),bg="#87CEFA", fg="white").place(x=0, y=0, relwidth=1, height=30)
        lbl_grn = Label(self.window, text="GRNo:", font=("goudy old style", 15, "bold"), bg='white').place(x=20,y=85,height=50)
        lbl_class = Label(self.window, text="Class:", font=("goudy old style", 15, "bold"), bg='white').place(x=20,y=125,height=50)
        lbl_roll = Label(self.window, text="Roll no:", font=("goudy old style", 15, "bold"), bg='white').place(x=20,y=230,height=50)
        lbl_sub = Label(self.window, text="Name:", font=("goudy old style", 15, "bold"), bg='white').place(x=20,y=285,height=50)
        self.image1 = Image.open("11thA.jpg")
        #self.image1 = self.image1.resize((920, 350))
        self.image1 = ImageTk.PhotoImage(self.image1)
        self.label_image1 = Label(self.window, image=self.image1,bg="#eBffff").place(x=100, y=30, width=800, height=800)

        #Entriess
        self.txt_student = ttk.Combobox(self.window, textvariable=self.var_grno, values=self.grno_list,font=("goudy old style", 15, "bold"), justify=CENTER)
        self.txt_student.place(x=180, y=85, width=200)
        self.txt_student.set("Select")

        self.txt_class = Entry(self.window, textvariable=self.var_class, font=("goudy old style", 15, "bold"),bg='#e3f4fe')
        self.txt_class.place(x=180, y=125, width=100)
        #self.txt_class = ttk.Combobox(self.window, textvariable=self.var_class, values=self.class_list,font=("goudy old style", 15, "bold"), state='readonly', justify=CENTER)
        #self.txt_class.place(x=180, y=125, width=200)
        #self.txt_class.set("Select")

        self.txt_roll = Entry(self.window, textvariable=self.var_roll, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_roll.place(x=180, y=230, width=100)

        self.txt_name = Entry(self.window, textvariable=self.var_name, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_name.place(x=180, y=285, width=400)
        #buton
        self.btn_search = Button(self.window, text='Go', font=("times new roman", 15, "bold"), command=self.search2,bg="lightgreen",cursor="hand2")
        self.btn_search.place(x=383, y=83, width=30, height=28)
        self.var_search=StringVar()
        lbl_search_roll=Label(self.window,text="Search GRNo:",font=("goudy old style",15,"bold"),bg="white").place(x=820,y=44,height=50)#710
        self.txt_search_roll=Entry(self.window,textvariable=self.var_search,font=("goudy old style",15,"bold"),bg='#e3f4fe')
        self.txt_search_roll.place(x=955, y=50, width=200)#860
        self.btn_search=Button(self.window,text='Search',font=("times new roman",15,"bold"),command=self.search1,bg="lightgreen",cursor="hand2")
        self.btn_search.place(x=1160, y=48, width=90, height=30)#1070
        #frame
        self.C_frame=Frame(self.window,bd=2,relief=RIDGE)
        self.C_frame.place(x=815,y=105,width=650,height=680)
        scrolly=Scrollbar(self.C_frame,orient=VERTICAL)
        scrollx=Scrollbar(self.C_frame,orient=HORIZONTAL)
        self.courseTable=ttk.Treeview(self.C_frame,columns=("grno","roll","Class","English","Physics","Chemistry","Maths","Biology","Geo","Urdu","Hindi","CS"))
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT, fill=X)
        scrollx.config(command=self.courseTable.xview)
        scrolly.config(command=self.courseTable.yview)
        self.courseTable.heading("grno", text="GRNo")
        self.courseTable.heading("roll",text="Roll")
        self.courseTable.heading("Class", text="Class")
        self.courseTable.heading("English",text="English")
        self.courseTable.heading("Physics",text="Physics")
        self.courseTable.heading("Chemistry",text="Chemistry")
        self.courseTable.heading("Maths",text="Maths")
        self.courseTable.heading("Biology",text="Biology")
        self.courseTable.heading("Geo",text="Geography")
        self.courseTable.heading("Urdu",text="Urdu")
        self.courseTable.heading("Hindi",text="Hindi")
        self.courseTable.heading("CS",text="Computer Science")
        self.courseTable["show"]='headings'
        self.courseTable.column("grno", width=60)
        self.courseTable.column("roll",width=60)
        self.courseTable.column("Class", width=60)
        self.courseTable.column("English",width=60)
        self.courseTable.column("Physics",width=60)
        self.courseTable.column("Chemistry",width=60)
        self.courseTable.column("Maths",width=60)
        self.courseTable.column("Biology",width=60)
        self.courseTable.column("Geo",width=60)
        self.courseTable.column("Urdu",width=60)
        self.courseTable.column("Hindi",width=60)
        self.courseTable.column("CS",width=60)
        self.courseTable.pack(fill=BOTH,expand=1)
        self.courseTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()

        self.c1 = Checkbutton(window, text='English', variable=self.tkvar1, onvalue=1, offvalue=0, command=self.selection,bg='#aadefc').place(x=600,y=85,width=150,height=50)
        #self.c1.pack()
        self.c2 = Checkbutton(window, text='Physics', variable=self.tkvar2, onvalue=1, offvalue=0, command=self.selection,bg='#e3e7fe').place(x=600,y=150,width=150,height=50)
        #self.c2.pack()

        self.c3 = Checkbutton(window, text='Chemistry', variable=self.tkvar3, onvalue=1, offvalue=0, command=self.selection,bg='#71c7fa').place(x=600,y=210,width=150,height=50)
        #self.c2.pack()
        self.c4 = Checkbutton(window, text='Maths', variable=self.tkvar4, onvalue=1, offvalue=0, command=self.selection,bg='#fefbe3').place(x=600,y=270,width=150,height=50)
        #self.c2.pack()
        self.c5 = Checkbutton(window, text='Biology', variable=self.tkvar5, onvalue=1, offvalue=0, command=self.selection,bg='#fee3f4').place(x=600,y=330,width=150,height=50)
        #self.c2.pack()
        self.c6 = Checkbutton(window, text='Geography', variable=self.tkvar6, onvalue=1, offvalue=0, command=self.selection,bg='#feede3').place(x=600,y=390,width=150,height=50)
        #self.c2.pack()
        self.c7 = Checkbutton(window, text='Urdu', variable=self.tkvar7, onvalue=1, offvalue=0, command=self.selection,bg='#e3fefb').place(x=600,y=450,width=150,height=50)
        #self.c2.pack()
        self.c8 = Checkbutton(window, text='Hindi', variable=self.tkvar8, onvalue=1, offvalue=0, command=self.selection,bg='#f6f3ec').place(x=600,y=510,width=150,height=50)
        #self.c2.pack()
        self.c9 = Checkbutton(window, text='CS', variable=self.tkvar9, onvalue=1, offvalue=0, command=self.selection,bg='#e3f4fe').place(x=600,y=570,width=150,height=50)
        #self.c2.pack()
        self.btn_add=Button(self.window,text='Save',font=("goudy old style",15,"bold"),command=self.add,bg="#87d3f8")
        self.btn_add.place(x=120,y=510,width=110,height=30)
        self.btn_update = Button(self.window, text='Update', font=("goudy old style", 15, "bold"),command=self.update, bg="#87d3f8")
        self.btn_update.place(x=240, y=510, width=110, height=30)
        self.btn_add = Button(self.window, text='Delete', font=("goudy old style", 15, "bold"),command=self.delete, bg="#87d3f8")
        self.btn_add.place(x=360, y=510, width=110, height=30)
        self.btn_clear = Button(self.window, text='Clear', font=("goudy old style", 15, "bold"),command=self.clear_data, bg="#87d3f8")
        self.btn_clear.place(x=480, y=510, width=110, height=30)

        self.btn_delete_all = Button(self.window, text='Delete All', font=("goudy old style", 15, "bold"),command=self.delete_all, bg="red")
        self.btn_delete_all.place(x=490, y=745, width=110, height=30)

        self.de_frame()

    def delete_all(self):
        for record in self.courseTable.get_children():
            self.courseTable.delete(record)
        conn=sqlite3.connect('rms.db')
        c=conn.cursor()
        op = messagebox.askyesno("Confirm", "Do you really wanto to delete?", parent=self.window)
        if op == True:
            #c.execute('DROP TABLE courseTable')
            c.execute('DELETE FROM courseTable')
            messagebox.showinfo("Delete", "Deleted succesfilly", parent=self.window)
        conn.commit()
        conn.close()
        self.clear_data()

    def de_frame(self):

        style = ttk.Style()

        style.theme_use("default")

        style.configure("Treeview", background="D3D3D3", foreground="white", rowheight=45, fieldbackground="white")

        style.map('Treeview', background=[('selected', '#0047AB')])

    def search2(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            #cur.execute("select students_name,roll_no from studentTable where grno=?  ", (self.var_grno.get(),))
            #row = cur.fetchone()
            cur.execute("select name,roll,class from studentTable where grno=?", (self.var_grno.get(),))
            row = cur.fetchone()
            if row != None:
                self.var_name.set(row[0])
                self.var_roll.set(int(row[1]))

                self.var_class.set(row[2])

            else:
                messagebox.showerror("Error", "No record found", parent=self.window)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")



    def search1(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select * from courseTable where grno=?", (self.var_search.get(),))
            row = cur.fetchone()
            if row != None:
                self.courseTable.delete(*self.courseTable.get_children())
                self.courseTable.insert('', END, values=row)
            else:
                messagebox.showerror("Error", "No record found", parent=self.window)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")





    def clear_data(self):
        self.show()
        self.var_roll.set(""),
        self.var_class.set(""),
        self.var_grno.set("Select"),
        #self.var_sub.set(row[4])
        self.tkvar1.set(0),
        self.tkvar2.set(0),
        self.tkvar3.set(0),
        self.tkvar4.set(0),
        self.tkvar5.set(0),
        self.tkvar6.set(0),
        self.tkvar7.set(0),
        self.tkvar8.set(0),
        self.tkvar9.set(0),
        self.var_name.set("")
                                                    
    def delete(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_grno.get()=="":

                messagebox.showerror("Error","GRNo.should be required",parent=self.window)

            else:
                cur.execute("select * from courseTable where grno=?",(self.var_grno.get(),))
                row=cur.fetchone()
                if row==None:

                    messagebox.showerror("Error","please select courseTable from the list first",parent=self.window)

                else:
                    op=messagebox.askyesno("Confirm","Do you really wanto to delete?",parent=self.window)
                    if op==True:

                        cur.execute("delete from courseTable where grno=?",(self.var_grno.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Student deleted succesfilly",parent=self.window)

                        self.clear_data()
        except Exception as ex:
            messagebox.showerror(("Error",f"Error due to{str(ex)}"))



    def get_data(self, ev):
        #self.var_roll.config(state='readonly')

        r=self.courseTable.focus()
        content=self.courseTable.item(r)
        row=content["values"]
        if row!=None:
            self.var_roll.set(row[1]),

            self.var_class.set(row[2]),

            self.var_grno.set(row[0]),

            #self.var_sub.set(row[4])
            self.tkvar1.set(row[3]),
            self.tkvar2.set(row[4]),
            self.tkvar3.set(row[5]),
            self.tkvar4.set(row[6]),
            self.tkvar5.set(row[7]),
            self.tkvar6.set(row[8]),
            self.tkvar7.set(row[9]),
            self.tkvar8.set(row[10]),
            self.tkvar9.set(row[11])

    def selection(self):
        lis=[self.tkvar1.get(),
             self.tkvar2.get(),
             self.tkvar3.get(),
             self.tkvar4.get(),
             self.tkvar5.get(),
             self.tkvar6.get(),
             self.tkvar7.get(),
             self.tkvar8.get(),
             self.tkvar9.get()]
        #print(lis)





    def add(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_grno.get() == "":
                messagebox.showerror("Error", "GRNo.. should be required", parent=self.window)
            else:
                cur.execute("select *  from courseTable where grno=?", (self.var_roll.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "Roll no. Already present", parent=self.window)
                else:

                    cur.execute("insert into courseTable(grno,roll,Class,English,Physics,Chemistry,Maths,Biology,Geo,Urdu,Hindi,CS) values(?,?,?,?,?,?,?,?,?,?,?,?)",(
                           self.var_grno.get(),
                           self.var_roll.get(),
                           self.var_class.get(),
                           self.tkvar1.get(),
                           self.tkvar2.get(),
                           self.tkvar3.get(),
                           self.tkvar4.get(),
                           self.tkvar5.get(),
                           self.tkvar6.get(),
                           self.tkvar7.get(),
                           self.tkvar8.get(),
                           self.tkvar9.get()
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
                cur.execute("select * from courseTable where grno=?",(self.var_grno.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Select courseTable from list",parent=self.window)
                else:
                    cur.execute("update courseTable set roll=?,Class=?,English=?,Physics=?,Chemistry=?,Maths=?,Biology=?,Geo=?,Urdu=?,Hindi=?,CS=? where grno=?", (
                        self.var_roll.get(),

                        self.var_class.get(),

                        self.tkvar1.get(),
                        self.tkvar2.get(),
                        self.tkvar3.get(),
                        self.tkvar4.get(),
                        self.tkvar5.get(),
                        self.tkvar6.get(),
                        self.tkvar7.get(),
                        self.tkvar8.get(),
                        self.tkvar9.get(),
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
            cur.execute("select * from courseTable")
            rows = cur.fetchall()
            self.courseTable.delete(*self.courseTable.get_children())
            for row in rows:
                self.courseTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

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
                    #self.class_list.append(row[8])


        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")










if __name__=="__main__":
    window=Tk()
    obj1=course(window)
    window.mainloop()
