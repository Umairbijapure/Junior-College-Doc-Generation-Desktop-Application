import sqlite3,csv
from tkinter import *

from tkinter import ttk,messagebox
from PIL import Image, ImageTk

from add11stdA import add11stdA
from course import course
from fillMarks import class_marks
from result import resultClass
#from importcsv import csv_export




class SSA:
    def __init__(self, window):
        self.window = window
        self.window.title("SSA Result Management System")
        self.window.geometry("1350x800+80+50")
        self.window.config(bg="#eBffff")

        # ICONS
        img = (Image.open("logo.png"))
        resized_image = img.resize((60, 60))
        self.logo_dash = ImageTk.PhotoImage(resized_image)
        title = Label(self.window, text="SSA Result Management System", padx=10, compound=LEFT, image=self.logo_dash,font=("goudy old stlye", 20, "bold"), bg="#87CEFA", fg="White").place(x=0, y=0, relwidth=1,height=50)
        #menu
        frame_menu = LabelFrame(self.window, text="Menus", font=("time new roman", 15), bg="#eBffff")
        frame_menu.place(x=10, y=70, width=190, height=508)


        btn_course = Button(frame_menu, text="Add Subjects", font=("goudym old style", 15), bg="#0b5377", fg="white",cursor="hand2", command=self.add_course).place(x=7, y=60, width=170, height=35)
        btn_student = Button(frame_menu, text="Add Student", font=("goudym old style", 15), bg="#0b5377", fg="white",cursor="hand2", command=self.add_student).place(x=7, y=10, width=170, height=35)
        btn_fill_marks = Button(frame_menu, text="Store Marks", font=("goudym old style", 15), bg="#0b5377", fg="white",cursor="hand2", command=self.fill_marks).place(x=7, y=110, width=170, height=35)
        btn_result = Button(frame_menu, text="Result", font=("goudym old style", 15), bg="#0b5377", fg="white",cursor="hand2", command=self.result).place(x=7, y=160, width=170, height=35)
        btn_course = Button(frame_menu, text="Import", font=("goudym old style", 15), bg="#0b5377", fg="white",cursor="hand2", command=self.impo).place(x=7, y=210, width=170, height=35)

        #btn_logout = Button(frame_menu, text="About", font=("goudym old style", 15), bg="#0b5377", fg="white",
                            #cursor="hand2").place(x=7, y=210, width=170, height=35)

        # Image
        self.image1 = Image.open("SSA3.jpg")
        #self.image1 = self.image1.resize((920, 350))
        self.image1 = ImageTk.PhotoImage(self.image1)
        self.label_image1 = Label(self.window, image=self.image1,bg="#eBffff").place(x=370, y=60, width=900, height=800)

        # Content details
        self.label_student = Label(self.window, text="Total Students \n[ 0 ]", font=("goudy old style", 20), bd=10, bg="#eBffff")
        self.label_student.place(x=370, y=585, width=255, height=80)

        #self.label_result = Label(self.window, text="Total Results \n[ 0 ]", font=("goudy old style", 20), bd=10, bg="#eBffff")
        #self.label_result.place(x=716, y=585, width=255, height=80)

        # Footer
        title = Label(self.window,
                      text="SSA Result Management System\nContact US for any technical issue:Umer Bijapure-7020152273",
                      font=("goudy old stlye", 10), bg="#87CEFA", fg="White").pack(side=BOTTOM, fill=X)
        self.total_students()

    def total_students(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select * from studentTable")
            rows1 = cur.fetchall()
            self.label_student.config(text=f"Total Students[{str(len(rows1))}]")
            self.label_student.after(200,self.total_students)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
    def impo(self):
        connection = sqlite3.connect('rms.db')

        cursor = connection.cursor()
        try:

            Table_Query = '''CREATE TABLE if not Exists bqkTablee 
                    (ebc_cast TEXT,age TEXT,mothers_name TEXT,
                    ht TEXT,grno INT,date_of_birth TEXT,roll_no REAL,students_name varchar,B TEXT,C TEXT,D TEXT)'''

            cursor.execute(Table_Query)

            file = open('bkq.csv')

            contents = csv.reader(file)

            insert_records = "INSERT INTO bqkTablee (ebc_cast,age,mothers_name,ht,grno,date_of_birth,roll_no,students_name,B,C,D) VALUES(?, ?,?,?,?,?,?,?,?,?,?)"

            cursor.executemany(insert_records, contents)

            select_all = "SELECT * FROM bqkTablee"
            rows = cursor.execute(select_all).fetchall()

            for r in rows:
                print(r)

            connection.commit()

            connection.close()
            messagebox.showinfo("Success", "Imported  Successfully", parent=self.window)
            #self.show()
        except Exception as ex:
            messagebox.showerror(("Error", f"Error due to{str(ex)}"))


    def add_course(self):
        self.new_win = Toplevel(self.window)
        self.obj1 = course(self.new_win)

    def add_student(self):
        self.new_win = Toplevel(self.window)
        self.obj2 = add11stdA(self.new_win)

    def fill_marks(self):
        self.new_win = Toplevel(self.window)
        self.obj2 = class_marks(self.new_win)

    def result(self):
        self.new_win = Toplevel(self.window)
        self.obj2 = resultClass(self.new_win)

    #def all_students(self):
    #    self.new_win = Toplevel(self.window)
    #   self.obj2 = csv_export(self.new_win)




if __name__ == "__main__":
    window = Tk()
    obj1 = SSA(window)
    window.mainloop()
