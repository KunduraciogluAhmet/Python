from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root = Tk()
root.title = ('BMI Calculator')
root.geometry("470x580+300+100")
root.resizable(0,0)
root.configure(bg="#f5f1f0")

def BMI():
    h= float(Height.get())
    w=float(weight.get())

    # convert height into meter
    bmi = round(float(w/(h/100)**2), 1)
    label1.config(text=bmi)

    if bmi <= 18.5:
        label2.config(text="Underweight")
        label3.config(text="You have lower weight than a normal body!!!")

    elif bmi >= 18.5 and bmi<= 25:
        label2.config(text="Normal")
        label3.config(text="You have balanced height&weight !!!")
        
    elif bmi >= 25 and bmi<= 30:
        label2.config(text="Overweight")
        label3.config(text="You have a bit over weight than a normal body, \n maybe you should apply a diet and take some exercises!!!")
    
    else:
        label2.config(text="OBES")
        label3.config(text="Your health may be under risk \n you must immiditly start a diet program!!!")

        
#icon
Image_icon = PhotoImage(file = "Images/icon.png")
root.iconphoto(False, Image_icon)

#top 
top = PhotoImage(file="Images/top.png")
top_image = Label(root, image=top, background="#f0f1f5")
top_image.place(x= -10, y=-10)

# bottom box
Label(root, width= 72, height=18, bg = "lightblue").pack(side=BOTTOM)

# two boxes
box = PhotoImage(file="Images/box.png")
Label(root, image=box).place(x=20, y= 100)
Label(root, image=box).place(x= 240, y= 100)

# scale image (ruler)
scale = PhotoImage(file= "Images/scale.png")
Label(root, image=scale, bg="lightblue").place(x=20, y=310)

##################################### slider1
current_value = tk.DoubleVar()
def get_current_value():
    return '{: .2f}'.format(current_value.get())


def slider_changed(event):
    Height.set(get_current_value())

    size = int(float(get_current_value()))
    img = (Image.open("Images/man.png"))
    resized_image= img.resize((50,10+size))
    photo2 = ImageTk.PhotoImage(resized_image)
    secondimage.config(image=photo2)
    secondimage.place(x=70, y=550-size)
    secondimage.image= photo2

# command to change BG color of scale
style = ttk.Style()
style.configure("TScale", background= "white")
slider= ttk.Scale(root, from_=0, to= 240, orient='horizontal', style="TScale", command=slider_changed, variable=current_value)
slider.place(x=80, y=255)

###############################################

##################################### slider2

current_value2 = tk.DoubleVar()

def get_current_value2():
    return '{: .2f}'.format(current_value2.get())


def slider_changed2(event):
    Weight.set(get_current_value2())

# command to change BG color of scale
style2 = ttk.Style()
style2.configure("TScale", background= "white")
slider2= ttk.Scale(root, from_=0, to= 200, orient='horizontal', style="TScale", command=slider_changed2, variable=current_value2)
slider2.place(x=280, y=255)

###############################################

#entry box

Height = StringVar()
Weight = StringVar()
height = Entry(root, textvariable=Height, width = 5, font='arial 50', bg="#fff", fg="#000", bd=0, justify=CENTER)
height.place(x=35, y= 160)
Height.set(get_current_value())

weight = Entry(root, textvariable=Weight, width = 5, font='arial 50', bg="#fff", fg="#000", bd=0, justify=CENTER)
weight.place(x=255, y= 160)
Weight.set(get_current_value2())

# Man image
secondimage = Label(root, bg= "lightblue")
secondimage.place(x=70, y= 530)


Button(root,text="View report", width= 15, height=2, font="arial 10 bold", bg= "#1f6e6B", fg ="#fff", command= BMI).place(x=300, y=340)

label1 = Label(root, font="arial 60 bold", bg= "lightblue", fg= "#fff")
label1.place(x= 125, y= 305)

label2 = Label(root, font="arial 20 bold", bg= "lightblue", fg= "#3b3b3b")
label2.place(x= 180, y= 430)

label3 = Label(root, font="arial 10 bold", bg= "lightblue")
label3.place(x= 100, y= 500)




root.mainloop()

