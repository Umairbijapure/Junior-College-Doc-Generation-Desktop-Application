import os
import numpy as np
import pandas as pd
from tkinter import *
from tkinter import filedialog
from tkinter import ttk,messagebox
import sqlite3
import csv
#con = sqlite3.connect(database="rms.db")
#cur = con.cursor()
#cur.execute("CREATE TABLE IF NOT EXISTS bqkTablee(grno INTEGER PRIMARY KEY AUTOINCREMENT,ebc_caste varchar, age float, mothers_name varchar, ht_wt float, date_of_birth varchar, roll_no int, students_name varchar)")
#con.commit()
Table_Query = '''CREATE TABLE if not Exists bqkTablee 
            (ebc_cast TEXT,age TEXT,mothers_name TEXT,
            ht TEXT,grno INT,date_of_birth TEXT,roll_no REAL,students_name varchar,B TEXT,C TEXT,D TEXT)'''

            # 2. create database
con = sqlite3.connect(database='rms.db')
cur = con.cursor()
# 3. execute table query to create table
cur.execute(Table_Query)
con.commit()


class csv_export:

    def __init__(self,window):
        self.window=window
        self.window.title("Import Data")
        self.window.geometry("1350x800+80+50")
        self.window.config(bg="#a0cff8")
        self.window.focus_force()
        title = Label(self.window, text="Note:Columns of the excel sheet should be in this format> ebc_caste , age , mothers_name, ht_wt , grno , date_of_birth , roll_no , students_name", padx=10,font=("goudy old stlye", 10), bg="#87CEFA", fg="red").place(x=44, y=650,height=50)
        btn_course = Button(self.window, text="Import Excel file", font=("goudym old style", 15), bg="#0b5377", fg="white",cursor="hand2",command=self.file_open).place(x=500, y=700, width=180, height=35)

        #variables
        self.var_cast = StringVar()
        self.var_age = StringVar()
        self.var_mother = StringVar()
        self.var_ht_wt = StringVar()
        self.var_grno=StringVar()
        self.var_dob = StringVar()
        self.var_roll=StringVar()
        self.var_name=StringVar()

        self.btn_delete_all = Button(self.window, text='Delete All', font=("goudy old style", 15, "bold"),command=self.delete_all, bg="red")
        self.btn_delete_all.place(x=300, y=700, width=110, height=30)


        self.my_frame=Frame(window)
        #my_frame.pack(padx=20,pady=20,ipadx=200,ipady=200)
        self.my_frame.place(x=50,y=50,width=1385,height=595)
        scrolly = Scrollbar(self.my_frame, orient=VERTICAL)

        scrollx = Scrollbar(self.my_frame, orient=HORIZONTAL)

        self.bqkTablee=ttk.Treeview(self.my_frame,column=("ebc_cast","age","mothers_name", "ht_wt" , "grno" , "date_of_birth" , "roll_no" , "students_name","B","C","D"))
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.bqkTablee.xview)
        scrolly.config(command=self.bqkTablee.yview)
        self.bqkTablee.pack(fill=BOTH,expand=1)
        self.bqkTablee.bind("<ButtonRelease-1>",self.get_data)

        self.show()

    def get_data(self, ev):
        r=self.bqkTablee.focus()
        content=self.bqkTablee.item(r)
        row=content["values"]
        #print(list[row],"kkkkkkkkhhhhh")
        self.var_cast.set(row[0])
        self.var_age.set(row[1])
        self.var_mother.set(row[2])
        self.var_ht_wt.set(row[3])
        self.var_grno.set(row[4])
        self.var_dob.set(row[5])
        self.var_roll.set(row[6])
        self.var_name.set(row[7])
    def delete_all(self):

        conn=sqlite3.connect('rms.db')
        c=conn.cursor()
        op = messagebox.askyesno("Confirm", "Do you really wanto to delete?", parent=self.window)
        if op == True:
            c.execute('DROP TABLE bqkTablee')
            for record in self.bqkTablee.get_children():
                self.bqkTablee.delete(record)
            c.execute('DELETE FROM studentTable')
            messagebox.showinfo("Delete", "Deleted succesfilly", parent=self.window)
        conn.commit()
        conn.close()



    def file_open(self):
        try:
            filename = filedialog.askopenfilename(
                initialdir="Downloads",
                title="Open A File",
                filetype=(("xlsx files", "*.xlsx"), ("All files", "*.*"))
            )
            if filename:
                try:
                    filename = r"{}".format(filename)
                    df = pd.read_csv(filename)
                    # df = pd.read_excel('bkq.xlsx')
                    #df.to_csv('bkq11.csv', header=df.columns, index=False)
                    #df = pd.DataFrame(pd.read_csv("bkq11.csv"))
                    self.clean(df)
                    df.to_sql('bqkTablee', con, if_exists='replace', index=False)
                    cur.execute('select * from bqkTablee ')
                    row = cur.fetchall()
                    self.bqkTablee["column"] = list(df.columns)
                    self.bqkTablee["show"] = "headings"
                    # loop throu clmn list
                    for column in self.bqkTablee["column"]:
                        self.bqkTablee.heading(column, text=column)
                    # put data in treeview
                    self.df_rows = df.to_numpy().tolist()
                    i=0
                    for row in self.df_rows:
                        self.bqkTablee.insert("", "end", values=row)
                        messagebox.showinfo("Success", "Imported  Successfully"+str(i)+str(row), parent=self.window)
                        self.show()
                        i+=1
                    self.bqkTablee.pack()
                    con.commit()
                    messagebox.showinfo("Success", "Imported  Successfully", parent=self.window)
                    self.show()



                except ValueError:
                    my_label.config(text="FIle Couldnt Be Opened..")
                except FileNotFoundError:
                    my_label.config(text="FIle Couldnt Be found..")
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")


        '''self.bqkTablee["column"] = list(df.columns)
        self.bqkTablee["show"] = "headings"
        # loop throu clmn list
        for column in self.bqkTablee["column"]:
            self.bqkTablee.heading(column, text=column)
        # put data in treeview
        self.df_rows = df.to_numpy().tolist()
        for row in self.df_rows:
            self.bqkTablee.insert("", "end", values=row)
        self.bqkTablee.pack()'''

    def clean(self,df):
        df.columns=[x.lower().replace(" ","_").replace("?","").replace("-","_").replace(r"/","_").replace("\\","_").replace("%","").replace(")","").replace(r"(","").replace("$","").replace(r"'","").replace("__","_").replace(".","") for x in df.columns]
        replacements={
            'object':'varchar',
            'float64':'float',
            'int64':'int',
            'datetime64':'timestamp',
            'timedelta64[ns]':'varchar'
        }
        col_str=', '.join("{} {}".format(n,d)for n,d in zip(df.columns,df.dtypes.replace(replacements)))

    def show(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select * from bqkTablee")
            rows = cur.fetchall()
            self.bqkTablee.delete(*self.bqkTablee.get_children())
            for row in rows:
                self.bqkTablee.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")










if __name__=="__main__":
    window=Tk()
    obj1=csv_export(window)
    my_label = Label(window, text=20)
    obj1.show()
    window.mainloop()
