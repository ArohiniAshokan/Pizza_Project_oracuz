from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("TODAY'S EXCLUSIVE DEALS....")
root.geometry('1450x1200')
root.config(bg='white')

Total=StringVar()
p1=StringVar()
p2=StringVar()
p3=StringVar()
p4=StringVar()
p5=StringVar()
p6=StringVar()
def generate_bill():
    try: qd1= int(p1.get())
    except: qd1=0
    try: qd2=int(p2.get())
    except: qd2=0
    try: qd3=int(p3.get())
    except: qd3=0
    try: qd4=int(p4.get())
    except: qd4=0
    try: qd5=int(p5.get())
    except: qd5=0
    try: qd6=int(p6.get())
    except: qd6=0

    cost1=qd1*275
    cost2=qd2*285
    cost3=qd3*225
    cost4=qd4*245
    cost5=qd5*315
    cost6=qd6*365
    Totalcost = cost1 + cost2 + cost3 + cost4 + cost5 + cost6
    Label(root, text=f"Thank You for Your Order \n Your Total Amount is Rs {Totalcost}",font=('arial',25,'bold'),fg='red').pack(side=TOP)

image_path = "C:\\Users\\Vinod\\Downloads\\pizzaquote.jpg"
image = Image.open(image_path)
resize_image = image.resize((500, 750))
tk_image = ImageTk.PhotoImage(resize_image)
im1 = Label(image=tk_image).pack(side=LEFT)

image_path1 = "C:\\Users\\Vinod\\Downloads\\pizza1.jpg"
image = Image.open(image_path1)
resize_image1 = image.resize((180, 180))
tk_image1 = ImageTk.PhotoImage(resize_image1)
im2 = Label(image=tk_image1).place(x=600, y=400)

image_path2 = "C:\\Users\\Vinod\\Downloads\\pizza2.jpg"
image = Image.open(image_path2)
resize_image2 = image.resize((180, 180))
tk_image2 = ImageTk.PhotoImage(resize_image2)
im3 = Label(image=tk_image2).place(x=850, y=400)

image_path3 = "C:\\Users\\Vinod\\Downloads\\pizza3.jpg"
image = Image.open(image_path3)
resize_image3 = image.resize((180, 180))
tk_image3 = ImageTk.PhotoImage(resize_image3)
im4 = Label(image=tk_image3).place(x=1100, y=400)

image_path4 = "C:\\Users\\Vinod\\Downloads\\pizza4.jpg"
image = Image.open(image_path4)
resize_image4 = image.resize((180, 180))
tk_image4 = ImageTk.PhotoImage(resize_image4)
im5 = Label(image=tk_image4).place(x=600, y=100)

image_path5 = "C:\\Users\\Vinod\\Downloads\\pizza5.jpg"
image = Image.open(image_path5)
resize_image5 = image.resize((180, 180))
tk_image5 = ImageTk.PhotoImage(resize_image5)
im6 = Label(image=tk_image5).place(x=850, y=100)

image_path6 = "C:\\Users\\Vinod\\Downloads\\pizza6.jpg"
image = Image.open(image_path6)
resize_image6 = image.resize((180, 180))
tk_image6 = ImageTk.PhotoImage(resize_image6)
im7 = Label(image=tk_image6).place(x=1100, y=100)

Label(root, text="Capsicum Chicken  \n Rs 245", font=('Arial', 10, 'bold')).place(x=1125, y=50)
Label(root, text="Cheesy Chicken \n Rs 315", font=('Arial', 10, 'bold')).place(x=885, y=50)
Label(root, text="Chicken Tikka \n Rs 365", font=('Arial', 10, 'bold')).place(x=650, y=50)

Label(root, text="Paneer Tikka \n Rs 275", font=('Arial', 10, 'bold')).place(x=1125, y=350)
Label(root, text="Spicy Mushroom  \n Rs 285", font=('Arial', 10, 'bold')).place(x=885, y=350)
Label(root, text="Cheesy Tomato \n Rs 225", font=('Arial', 10, 'bold')).place(x=650, y=350)


c1 = Label(root,text="Quantity",font=("arial",10,'bold')).place(x=1130,y=550)
e1 = Entry(root,textvariable=p1).place(x=1190,y=550)

c2 = Label(root,text="Quantity",font=("arial",10,'bold')).place(x=885, y=550)
e2 = Entry(root,textvariable=p2).place(x=945,y=550)

c3 = Label(root,text="Quantity",font=("arial",10,'bold')).place(x=650, y=550)
e3 = Entry(root,textvariable=p3).place(x=710,y=550)

c4 = Label(root,text="Quantity",font=("arial",10,'bold')).place(x=1130,y=250)
e4 = Entry(root,textvariable=p4).place(x=1190,y=250)

c5 = Label(root,text="Quantity",font=("arial",10,'bold')).place(x=885, y=250)
e5 = Entry(root,textvariable=p5).place(x=945,y=250)

c6 = Label(root,text="Quantity",font=("arial",10,'bold')).place(x=650, y=250)
e6 = Entry(root,textvariable=p6).place(x=710,y=250)

btn_total=Button(root,bd=4,fg='black',font=('arial',16,'bold'),text="PAY",bg="SteelBlue1",command=generate_bill)
btn_total.place(x=1200,y=650)
root.mainloop()
