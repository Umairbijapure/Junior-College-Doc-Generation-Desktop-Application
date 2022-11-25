
from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import csv
import sqlite3
from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from datetime import datetime
class exportClass():
    def __init__(self, window):
        self.window=window
        self.window.title("Storing Data Locally")
        self.window.geometry("500x500+550+150")
        self.window.config(bg="#eBffff")
        self.window.focus_force()
        #variables
        self.filenam_raw_entry=StringVar()

        #Export
        #Export Database
        lbl_select = Label(self.window, text="File name:", font=("goudy old style", 15, "bold"), bg='white').place(x=20, y=100, height=50)

        self.txt_filename = Entry(self.window, textvariable=self.filenam_raw_entry, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_filename.place(x=140, y=110, width=150)

        self.btn_csv=Button(self.window,text='Generate CSV',font=("times new roman",15,"bold"),command=self.export_as_csv,bg="red",cursor="hand2")
        self.btn_csv.place(x=300, y=110, width=150, height=30)

        #self.button_export3=Button(self.window,text="To XLS",width=12,bg='#03A9F4',fg='#fff',command=self.export_as_xls)
        #self.button_export3.grid(row=3,column=2,padx=10,pady=10)

    def export_as_csv(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        filename = str(self.filenam_raw_entry.get())
        myfilename = filename + '.csv'
        with open(myfilename, 'w') as f:
            writer = csv.writer(f)
            cur.execute('SELECT*FROM resultTable')

            data = cur.fetchall()
            writer.writerow(["roll", "Std", "Class", "Grn", "Math", "Bio", "Phy", "Chem", "Urdu", "Eng", "Hin", "Geo","Cs1","Cs2","env","pe","date","result","grandtotal","perc","grade","name","adress","reop"])
            writer.writerows(data)
            messagebox.showinfo(title="Registrasion", message='"Exported As {}'.format(myfilename))

    def export_as_xls(self):
        pass


if __name__=="__main__":
    window=Tk()
    obj=exportClass(window)
    window.mainloop()