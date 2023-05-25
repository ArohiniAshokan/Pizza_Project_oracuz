#PROJECT - PIZZA HUT

from subprocess import call
from tkinter import *
from PIL import ImageTk,Image

root=Tk()

root.title("WELCOME.........")
root.geometry('1450x1200')
root.config(bg='white')

def login_form():
    call(['python','Login.py'])

def register_form():
    call(['python', 'Register.py'])

image_path = "C:\\Users\\Vinod\\Downloads\\pizza-g8b6d9c9f8_1920.jpg"
image = Image.open(image_path)
resize_image = image.resize((600,450))
tk_image = ImageTk.PhotoImage(resize_image)
im1=Label(image=tk_image).pack(side=LEFT)

t1=Label(root,text="VINTOOS PIZZA HUT",bg='yellow',fg='red',font=('Arial',60,'bold')).place(x=420,y=200)

log_btn=Button(root,text="LOGIN",bg='sky blue',fg='black',activebackground='coral',padx=40,pady=30,font=('Arial',20,'bold'),command=login_form).place(x=650,y=400)

reg_btn=Button(root,text="REGISTER",bg='sky blue',fg='black',activebackground='coral',padx=40,pady=30,font=('Arial',20,'bold'),command=register_form).place(x=900,y=400)

root.mainloop()