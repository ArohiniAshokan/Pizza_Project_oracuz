import mysql.connector

from subprocess import call
from tkinter import *
from tkinter import messagebox

def OK():
    mysqldb=mysql.connector.connect(host='localhost',user='root',password="",database='pizzahut')
    mycursor=mysqldb.cursor()
    username=e1.get()
    passwrd=e2.get()

    sql="select * from login where username=%s and passwrd=%s"
    mycursor.execute(sql,[(username),(passwrd)])
    results= mycursor.fetchall()
    mysqldb.commit()
    if results:
        messagebox.showinfo("","Login Success")
        top.destroy()
        call(['python','home.py'])
        return True
    else:
        messagebox.showinfo("","Incorrect Username and Password")
        return False

top=Tk()
top.title('Login')
top.geometry('300x200')
top.config(bg='cadetblue')

global e1
global e2

Label(top,text="Username",bg='pink').place(x=10,y=10)
Label(top,text="Password",bg='pink').place(x=10,y=40)

e1=Entry(top)
e1.place(x=140,y=10)

e2=Entry(top)
e2.place(x=140,y=40)
e2.config(show='*')

Button(top,text="LOGIN",bg='pink',command=OK,height=3,width=13).place(x=60,y=100)
top.mainloop()