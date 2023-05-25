import mysql.connector

from subprocess import call
from tkinter import *
from tkinter import messagebox

def OKK():
    mysqldb = mysql.connector.connect(host='localhost', user='root', password="", database='pizzahut')
    mycursor = mysqldb.cursor()
    nam= e1.get()
    ag= e2.get()
    emil=e3.get()
    passwd1=e5.get()

    sql="insert into register (name,age,email,passwrd1) values('%s','%d','%s','%s')"%(nam,int(ag),emil,passwd1)
    sql1="insert into login (username,passwrd) values('%s','%s')"%(nam,passwd1)
    mycursor.execute(sql)
    mycursor.execute(sql1)
    mysqldb.commit()

    messagebox.showinfo("", "Registration Success")
    win.destroy()
    call(['python','Login.py'])

win=Tk()
win.title('Register')
win.geometry('400x300')
win.config(bg='Cadetblue')

global e1
global e2
global e3
global e5

Label(win,text="Name").place(x=10,y=10)
Label(win,text="Age").place(x=10,y=40)
Label(win,text="Email").place(x=10,y=70)
Label(win,text="Create Password").place(x=10,y=100)

e1=Entry(win)
e1.place(x=140,y=10)

e2=Entry(win)
e2.place(x=140,y=40)

e3=Entry(win)
e3.place(x=140,y=70)

e5=Entry(win)
e5.place(x=140,y=100)
e5.config(show='*')

Button(win,text="REGISTER",command=OKK,height=3,width=13).place(x=60,y=200)

win.mainloop()