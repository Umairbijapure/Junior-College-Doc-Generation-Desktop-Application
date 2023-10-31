from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
from tkinter import colorchooser
import sqlite3


class add11stdA:

    def __init__(self,window):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        cur.execute(
            "CREATE TABLE IF NOT EXISTS studentTable(grno INTEGER PRIMARY KEY AUTOINCREMENT,roll text,name text,email text,gender text,dob text,contact text,mother text,class text,std text,city text,state text,pin text,address text)")
        con.commit()
        con.close()
        self.window=window
        self.window.title("Add Student")
        self.window.geometry("1350x800+80+50")
        self.window.config(bg="#a0cff8")
        #title = Label(self.window, text="Add Student", padx=10,font=("goudy old stlye", 20, "bold"), bg="#87CEFA", fg="White").place(x=0, y=0, relwidth=1,height=20)
        title = Label(self.window, text="Please Fill Student Details", padx=10,font=("goudy old stlye", 15, "bold"), bg="#87CEFA", fg="White").place(x=0, y=0, relwidth=1,height=30)
        self.image1 = Image.open("assets/cloud.jpeg")
        # self.image1 = self.image1.resize((920, 350))
        self.image1 = ImageTk.PhotoImage(self.image1)
        self.label_image1 = Label(self.window, image=self.image1, bg="#eBffff").place(x=0, y=30, width=300,
                                                                                      height=800)

        self.label_image1 = Label(self.window, image=self.image1, bg="#eBffff").place(x=300, y=30, width=300,
                                                                                      height=800)
        self.label_image1 = Label(self.window, image=self.image1, bg="#eBffff").place(x=600, y=30, width=300,
                                                                                      height=800)
        self.label_image1 = Label(self.window, image=self.image1, bg="#eBffff").place(x=900, y=30, width=300,
                                                                                      height=800)
        self.label_image1 = Label(self.window, image=self.image1, bg="#eBffff").place(x=1200, y=30, width=300,
                                                                                   height=800)
        self.var_grno=StringVar()
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_address = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_contact = StringVar()
        self.var_class = StringVar()
        self.var_mother = StringVar()
        self.var_state = StringVar()
        self.var_city = StringVar()
        self.var_pin = StringVar()
        self.var_std = StringVar()
        self.var_search = StringVar()
        self.grno_list = []
        self.fetch_grno()


        #info details:column1
        lbl_grno=Label(self.window,text="GRNo:",font=("goudy old style",15,"bold"),bg='#a0cff8').place(x=20, y=105,height=30)
        lbl_roll=Label(self.window,text="Roll No:",font=("goudy old style",15,"bold"),bg='#a0cff8').place(x=20, y=48,height=30)
        lbl_name = Label(self.window, text="Name:", font=("goudy old style", 15, "bold"), bg='#a0cff8').place(x=20,y=145,height=30)
        lbl_email = Label(self.window, text="Email:", font=("goudy old style", 15, "bold"), bg='#a0cff8').place(x=20,y=195,height=30)
        lbl_address = Label(self.window, text="Address:", font=("goudy old style", 15, "bold"), bg='#a0cff8').place(x=20,y=400,height=30)
        lbl_gender = Label(self.window, text="Gender:", font=("goudy old style", 15, "bold"), bg='#a0cff8').place(x=20, y=240,height=30)#20 296 50
        lbl_sate = Label(self.window, text="State:", font=("goudy old style", 15, "bold"), bg='#a0cff8').place(x=20,y=300,height=30)
        lbl_city = Label(self.window, text="City:", font=("goudy old style", 15, "bold"), bg='#a0cff8').place(x=20,y=350,height=30)

        self.txt_state = Entry(self.window, textvariable=self.var_state, font=("goudy old style", 15, "bold"),bg='#e3f4fe')
        self.txt_state.place(x=125, y=352, width=200)#125,301

        self.txt_city = Entry(self.window, textvariable=self.var_city, font=("goudy old style", 15, "bold"),bg='#e3f4fe')
        self.txt_city.place(x=125, y=301, width=200)


        #info entry:column1
        #self.txt_grno=Entry(self.window,textvariable=self.var_grno,font=("goudy old style",15,"bold"),bg='#e3f4fe')
        #self.txt_grno.place(x=125,y=105,width=200)
        self.txt_grno = ttk.Combobox(self.window, textvariable=self.var_grno, values=self.grno_list,font=("goudy old style", 15, "bold"), justify=CENTER)
        self.txt_grno.place(x=125, y=105, width=160)
        self.txt_grno.set("Select")

        #self.txt_roll=Entry(self.window,textvariable=self.var_roll,font=("goudy old style",15,"bold"),bg='#e3f4fe')
        #self.txt_roll.place(x=125,y=50,width=200)
        self.txt_Roll = Entry(self.window, textvariable=self.var_roll, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_Roll.place(x=125, y=50, width=200)

        self.txt_name = Entry(self.window, textvariable=self.var_name, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_name.place(x=125, y=145, width=250)

        self.txt_email = Entry(self.window, textvariable=self.var_email, font=("goudy old style", 15, "bold"),bg='#e3f4fe')
        self.txt_email.place(x=125, y=195, width=200)

        self.txt_gender = ttk.Combobox(self.window, textvariable=self.var_gender,values=("Select","Male","Female","Other"),font=("goudy old style", 15, "bold"), state='readonly', justify=CENTER)
        self.txt_gender.place(x=125, y=240, width=200)
        self.txt_gender.current(0)






        #TEXT Fields

        self.txt_address = Text(self.window, font=("goudy old style", 15, "bold"),bg='#e3f4fe')
        self.txt_address.place(x=125, y=400, width=573,height=96)



        # info entry:column2
        lbl_dob = Label(self.window, text="DOB:", font=("goudy old style", 15, "bold"), bg='#a0cff8').place(x=375,y=48,height=20)
        lbl_contact = Label(self.window, text="Contact:", font=("goudy old style", 15, "bold"), bg='#a0cff8').place(x=375, y=108,height=20)
        lbl_mother = Label(self.window, text="Mother's Name:", font=("goudy old style", 15, "bold"), bg='#a0cff8').place(x=330,y=176,height=20)
        lbl_class = Label(self.window, text="Class:", font=("goudy old style", 15, "bold"), bg='#a0cff8').place(x=375,y=228,height=20)
        lbl_std = Label(self.window, text="Std:", font=("goudy old style", 15, "bold"), bg='#a0cff8').place(x=375,y=288,height=20)
        lbl_pin = Label(self.window, text="Pin Code:", font=("goudy old style", 15, "bold"), bg='#a0cff8').place(x=375,y=349,height=20)

        self.course_list=["Select","A","B","C"]
        self.std_list=["Select","XI","XII"]
        #self.fetch_details()
        self.txt_dob = Entry(self.window, textvariable=self.var_dob, font=("goudy old style", 15, "bold"),bg='#e3f4fe')
        self.txt_dob.place(x=495, y=50, width=200)

        self.txt_contact = Entry(self.window, textvariable=self.var_contact, font=("goudy old style", 15, "bold"),bg='#e3f4fe')
        self.txt_contact.place(x=495, y=110, width=200)

        self.txt_mother = Entry(self.window, textvariable=self.var_mother, font=("goudy old style", 15, "bold"),bg='#e3f4fe')
        self.txt_mother.place(x=495, y=170, width=200)

        self.txt_class = ttk.Combobox(self.window, textvariable=self.var_class,values=(self.course_list),font=("goudy old style", 15, "bold"), state='readonly', justify=CENTER)
        self.txt_class.place(x=495, y=230, width=200)  # 150 300 200
        self.txt_class.current(0)

        #self.txt_std = Entry(self.window, textvariable=self.var_std, font=("goudy old style", 15, "bold"),bg='#e3f4fe')
        #self.txt_std.place(x=495, y=288, width=200)
        self.txt_std = ttk.Combobox(self.window, textvariable=self.var_std,values=(self.std_list),font=("goudy old style", 15, "bold"), state='readonly', justify=CENTER)
        self.txt_std.place(x=495, y=288, width=200)  # 150 300 200
        self.txt_std.current(0)


        self.txt_pin = Entry(self.window, textvariable=self.var_pin, font=("goudy old style", 15, "bold"),bg='#e3f4fe')
        self.txt_pin.place(x=495, y=348, width=200)



        #buttons oparation
        self.btn_add=Button(self.window,text='Save',font=("goudy old style",15,"bold"),command=self.add,bg="#87d3f8")
        self.btn_add.place(x=150,y=510,width=110,height=30)
        self.btn_update = Button(self.window, text='Update', font=("goudy old style", 15, "bold"),command=self.update, bg="#87d3f8")
        self.btn_update.place(x=270, y=510, width=110, height=30)
        self.btn_delete = Button(self.window, text='Delete', font=("goudy old style", 15, "bold"),command=self.delete, bg="#87d3f8")
        self.btn_delete.place(x=390, y=510, width=110, height=30)
        self.btn_clear = Button(self.window, text='Clear', font=("goudy old style", 15, "bold"),command=self.clear_data, bg="#87d3f8")
        self.btn_clear.place(x=510, y=510, width=110, height=30)
        self.btn_delete_all = Button(self.window, text='Delete All', font=("goudy old style", 15, "bold"),command=self.delete_all, bg="red")
        self.btn_delete_all.place(x=510, y=700, width=110, height=30)
        self.btn_imp_csv = Button(self.window, text='Go', font=("goudy old style", 15, "bold"),command=self.search3, bg="Lightgreen")
        self.btn_imp_csv.place(x=285, y=105, width=40, height=28)






        #SEARCH section
        lbl_search_roll=Label(self.window,text="Search GRNo",font=("goudy old style",15,"bold"),bg="#a0cff8").place(x=720,y=55,height=20)
        self.txt_search_roll=Entry(self.window,textvariable=self.var_search,font=("goudy old style",15,"bold"),bg='#e3f4fe')
        self.txt_search_roll.place(x=850, y=50, width=200)
        self.btn_search=Button(self.window,text='Search',font=("times new roman",15,"bold"),command=self.search,bg="lightgreen")
        self.btn_search.place(x=1060, y=50, width=110, height=30)
        #show table
        self.C_frame=Frame(self.window,bd=2,relief=RIDGE)
        self.C_frame.place(x=720,y=100,width=700,height=680)

        scrolly=Scrollbar(self.C_frame,orient=VERTICAL)
        scrollx=Scrollbar(self.C_frame,orient=HORIZONTAL)

        self.studentTable=ttk.Treeview(self.C_frame,columns=("grno","roll","name","email","gender","dob","contact","mother","class","std","state","city","pin","address"))
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT, fill=X)
        scrollx.config(command=self.studentTable.xview)
        scrolly.config(command=self.studentTable.yview)
        self.studentTable.heading("grno", text="GRNo")
        self.studentTable.heading("roll",text="Roll")
        self.studentTable.heading("name",text="Name")
        self.studentTable.heading("email",text="Email")
        self.studentTable.heading("gender",text="Gender")
        self.studentTable.heading("dob",text="DOB")
        self.studentTable.heading("contact",text="Contact")
        self.studentTable.heading("mother",text="mother")
        self.studentTable.heading("class",text="Class")
        self.studentTable.heading("std", text="Std")
        self.studentTable.heading("state",text="state")
        self.studentTable.heading("city",text="City")
        self.studentTable.heading("pin",text="Pin")
        self.studentTable.heading("address",text="Address")
        self.studentTable["show"]='headings'
        self.studentTable.column("grno",width=100)
        self.studentTable.column("roll",width=100)
        self.studentTable.column("name",width=100)
        self.studentTable.column("email",width=100)
        self.studentTable.column("gender",width=100)
        self.studentTable.column("dob",width=100)
        self.studentTable.column("contact",width=100)
        self.studentTable.column("mother",width=100)
        self.studentTable.column("class",width=100)
        self.studentTable.column("std", width=100)
        self.studentTable.column("state",width=100)
        self.studentTable.column("city",width=100)
        self.studentTable.column("pin",width=100)
        self.studentTable.column("address",width=200)
        self.studentTable.pack(fill=BOTH,expand=1)
        self.studentTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
        #self.fetch_details()
        self.de_frame()

    def search3(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select students_name,roll_no,date_of_birth,mothers_name from bqkTablee where grno=?", (self.var_grno.get(),))
            row = cur.fetchone()
            #print(row,"llllllllll")
            if row != None:
                self.var_name.set(row[0])
                self.var_roll.set(int(row[1]))
                self.var_dob.set(row[2])
                self.var_mother.set(row[3])
                #self.var_std.set(row[1])
                #self.var_class.set(row[2])

            else:
                messagebox.showerror("Error", "No record found", parent=self.window)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def fetch_grno(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select * from bqkTablee")
            rows = cur.fetchall()
            #print(rows)

            if len(rows)>0:
                for row in rows:
                    self.grno_list.append(row[4])

                    #self.class_list.append(row[8])



        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")




    def delete_all(self):
        for record in self.studentTable.get_children():
            self.studentTable.delete(record)
        conn=sqlite3.connect('rms.db')
        c=conn.cursor()
        op = messagebox.askyesno("Confirm", "Do you really wanto to delete?", parent=self.window)
        if op == True:
            #c.execute('DROP TABLE studentTable')
            c.execute('DELETE FROM studentTable')

            messagebox.showinfo("Delete", "Deleted succesfilly", parent=self.window)
        conn.commit()
        conn.close()
        self.clear_data()

    def de_frame(self):
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview", background="D3D3D3", foreground="#F4F7F9", rowheight=45, fieldbackground="#F4F7F9")
        style.map('Treeview', background=[('selected', '#0047AB')])

        #global count
        #count = 0
        #con = sqlite3.connect(database="rms.db")
        #cur = con.cursor()
        #cur.execute("select * from studentTable")
        #rows = cur.fetchall()
        #self.studentTable.tag_configure('oddrow',background='white')
        #self.studentTable.tag_configure('evenrow', background='lightblue')
        #for row in rows:

            #if count % 2 == 0:
            #self.studentTable.insert(parent='',index='0',text='', values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12]),iid=count,tags=('evenrow',))
            #else:
                #self.studentTable.insert(parent='', index='0', values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12]),iid=count,tags=('oddrow',))
        #    count+=1






    def clear_data(self):
        self.show()
        self.var_grno.set("Select")
        self.var_roll.set(""),
        self.var_name.set(""),
        self.var_email.set(""),
        self.var_gender.set("Select"),
        self.var_dob.set(""),
        self.var_contact.set(""),
        self.var_mother.set(""),
        self.var_class.set("Select"),
        self.var_std.set("Select"),
        self.var_state.set(""),
        self.var_city.set(""),
        self.var_pin.set(""),
        self.txt_address.delete("1.0", END)
        #self.txt_r.config(state=NORMAL)
        self.var_search.set("")

    def delete(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_grno.get()=="":

                messagebox.showerror("Error","Roll no.should be required",parent=self.window)

            else:
                cur.execute("select * from studentTable where grno=?",(self.var_grno.get(),))
                row=cur.fetchone()
                if row==None:

                    messagebox.showerror("Error","please select studentTable from the list first",parent=self.window)

                else:
                    op=messagebox.askyesno("Confirm","Do you really wanto to delete?",parent=self.window)
                    if op==True:

                        cur.execute("delete from studentTable where grno=?",(self.var_grno.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Student deleted succesfilly",parent=self.window)

                        self.clear_data()
        except Exception as ex:
            messagebox.showerror(("Error",f"Error due to{str(ex)}"))

    def get_data(self, ev):
        #self.txt_roll.config(state='readonly')

        r=self.studentTable.focus()
        content=self.studentTable.item(r)
        row=content["values"]
        self.var_grno.set(row[0]),
        self.var_roll.set(row[1]),
        self.var_name.set(row[2]),
        self.var_email.set(row[3]),
        self.var_gender.set(row[4]),
        self.var_dob.set(row[5]),
        self.var_contact.set(row[6]),
        self.var_mother.set(row[7]),
        self.var_class.set(row[8]),
        self.var_std.set(row[9]),
        self.var_state.set(row[11]),
        self.var_city.set(row[10]),
        self.var_pin.set(row[12]),
        self.txt_address.delete("1.0", END),
        self.txt_address.insert(END,row[13])





    def add(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_grno.get() == "":
                messagebox.showerror("Error", "GRNO. should be required", parent=self.window)
            else:
                cur.execute("select *  from studentTable where grno=?", (self.var_grno.get(),))
                row = cur.fetchone()

                if row != None:
                    messagebox.showerror("Error", "Roll no. Already present", parent=self.window)
                else:

                    cur.execute("insert into studentTable(grno,roll,name,email,gender,dob,contact,mother,class,std,state,city,pin,address) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(
                           self.var_grno.get(),
                           self.var_roll.get(),
                           self.var_name.get(),
                           self.var_email.get(),
                           self.var_gender.get(),
                           self.var_dob.get(),
                           self.var_contact.get(),
                           self.var_mother.get(),
                           self.var_class.get(),
                           self.var_std.get(),
                           self.var_state.get(),
                           self.var_city.get(),
                           self.var_pin.get(),
                           self.txt_address.get("1.0", END)))

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
                cur.execute("select * from studentTable where grno=?",(self.var_grno.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Select studentTable from list",parent=self.window)
                else:
                    cur.execute("update StudentTable set roll=?,name=?,email=?,gender=?,dob=?,contact=?,mother=?,class=?,std=?,state=?,city=?,pin=?,address=? where grno=?", (
                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_mother.get(),
                        self.var_class.get(),
                        self.var_std.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_pin.get(),
                        self.txt_address.get("1.0", END),
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
            cur.execute("select * from studentTable")
            rows = cur.fetchall()
            self.studentTable.delete(*self.studentTable.get_children())
            for row in rows:
                self.studentTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    """def fetch_details(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select * from studentTable")
            rows = cur.fetchall()
            print(rows)

            if len(rows)>0:
                for row in rows:
                    self.course_list.append(row[0])


        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")"""











    def search(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select * from studentTable where grno=?", (self.var_search.get(),))
            row = cur.fetchone()
            if row != None:
                self.studentTable.delete(*self.studentTable.get_children())
                self.studentTable.insert('', END, values=row)
            else:
                messagebox.showerror("Error", "No record found", parent=self.window)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")










if __name__=="__main__":
    window=Tk()
    obj1=add11stdA(window)
    window.mainloop()
