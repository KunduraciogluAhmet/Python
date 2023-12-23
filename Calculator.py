#simple calculator
import tkinter
from tkinter import RIGHT, END, DISABLED, NORMAL

#Building window
root= tkinter.Tk()
root.title('Calculator')
root.iconbitmap('calc.ico')
root.geometry('300x400')
root.resizable(0,0)

#colors and fonts to be used
dark_green= '#93af22'
light_green='#acc253'
white_green='#edefe0'
button_font= ('arial',18)
display_font=('Arial',30)

#defining the functions 
def submit_number(number):
    """add a number to the display box"""
    #insert the number or decimal pressed to the end of the display
    display.insert(END, number)

    #if decimal was pressed disable the decimal button so it cannot be pressed twice
    if "." in display.get():
        decimal_button.config(state=DISABLED)

def operate(operator):
    """store the 1st number of the expression and the operation to be used"""
    global first_number
    global operation
    
    #get the operator pressed and the current value of the display. This is the first number in the calculation
    operation = operator
    first_number= display.get()

    #delete the value (first number) from entry display
    display.delete(0,END)

    #disable all operator buttons until equal or clear is pressed.
    add_button.config(state=DISABLED)
    substract_button.config(state=DISABLED)
    multiply_button.config(state=DISABLED)
    divide_button.config(state=DISABLED)
    exponent_button.config(state=DISABLED)
    inverse_button.config(state=DISABLED)
    square_button.config(state=DISABLED)
    
    #return decimal button to normal state
    decimal_button.config(state= NORMAL)

def equal():
    """run the stored operation for two number"""
    #perform the desired math op
    if operation=="add":
        value=float(first_number)+ float(display.get())
    elif operation=="substract":
        value= float(first_number)-float(display.get())
    elif operation== "multiply":
        value= float(first_number)*float(display.get())
    elif operation== "divide":
        if display.get()== "0":
            value =" ERROR"
        else:
            value= float(first_number) / float(display.get())
    elif operation =="exponent":
        value= (first_number) ** float(display.get())
    
    #remove the current value of the display and update it with the answer
    display.delete(0, END)
    display.insert(0, value)

    #returns buttons to normal state
    enable_buttons()

def enable_buttons():
    """Enable buttons for new operations"""
    decimal_button.config(state= NORMAL)
    add_button.config(state= NORMAL)
    substract_button.config(state= NORMAL)
    multiply_button.config(state= NORMAL)
    divide_button.config(state= NORMAL)
    exponent_button.config(state= NORMAL)
    inverse_button.config(state= NORMAL)
    square_button.config(state= NORMAL)

def clear():
    """clear the display box"""
    display.delete(0, END)

    #return buttons to normal state
    enable_buttons()

def inverse():
    """Calculate the 1/x"""
    #don't allow 1/0
    if display.get()=="0":
        value=="ERROR"
    else:
        value== 1/float(display.get())
    
    #Remove the current value in the display box and update it w/ answer
    display.delete(0, END)
    display.insert(0,value)

def square():
    """Calculate the square of a given number"""
    value=float(display.get())**2

    #Remove the current value in the displaybox and update it w answer
    display.delete(0, END)
    display.insert(0,value)

def negate():
    value= -1*float(display.get())

    #Remove the current value in the displaybox and update it w answer
    display.delete(0, END)
    display.insert(0,value)

#Building the GUI Layout
#Define frames
display_frame= tkinter.LabelFrame(root)
button_frame=tkinter.LabelFrame(root)
display_frame.pack(padx=2, pady=(5,20))
button_frame.pack(padx=2, pady=5)

#Layout for the display frame
display=tkinter.Entry(display_frame, width=50, font=display_font, bg= white_green, borderwidth=5, justify=RIGHT)
display.pack(padx=5, pady=5)

#Layout for the button frame
clear_button=tkinter.Button(button_frame, text="Clear", font= button_font,bg=dark_green, command= clear)
quit_button= tkinter.Button(button_frame, text = "QUIT", font= button_font, bg= dark_green, command=root.destroy)

inverse_button = tkinter.Button(button_frame,text="1/x", font=button_font, bg=light_green, command=inverse)
square_button = tkinter.Button(button_frame,text="x^2", font=button_font, bg=light_green, command=square)
exponent_button = tkinter.Button(button_frame,text="x^n", font=button_font, bg=light_green, command=lambda:operate('exponent'))
divide_button = tkinter.Button(button_frame,text="/", font=button_font, bg=light_green, command=lambda:operate('divide'))
multiply_button = tkinter.Button(button_frame,text="X", font=button_font, bg=light_green, command=lambda:operate('multiply'))
substract_button = tkinter.Button(button_frame,text="-", font=button_font, bg=light_green, command=lambda:operate('substract'))
add_button = tkinter.Button(button_frame,text="+", font=button_font, bg=light_green, command=lambda:operate('add'))
equal_button = tkinter.Button(button_frame,text="=", font=button_font, bg=light_green, command=equal)
decimal_button = tkinter.Button(button_frame,text=".", font=button_font, bg=light_green, command=lambda:submit_number("."))
negate_button = tkinter.Button(button_frame,text="+/-", font=button_font, bg=light_green, command=negate)

nine_button=tkinter.Button(button_frame, text="9", font= button_font,bg="black",fg="white",command=lambda:submit_number(9))
eight_button=tkinter.Button(button_frame, text="8", font= button_font,bg="black",fg="white",command=lambda:submit_number(8))
seven_button=tkinter.Button(button_frame, text="7", font= button_font,bg="black",fg="white",command=lambda:submit_number(7))
six_button=tkinter.Button(button_frame, text="6", font= button_font,bg="black",fg="white",command=lambda:submit_number(6))
five_button=tkinter.Button(button_frame, text="5", font= button_font,bg="black",fg="white",command=lambda:submit_number(5))
four_button=tkinter.Button(button_frame, text="4", font= button_font,bg="black",fg="white",command=lambda:submit_number(4))
three_button=tkinter.Button(button_frame, text="3", font= button_font,bg="black",fg="white",command=lambda:submit_number(3))
two_button=tkinter.Button(button_frame, text="2", font= button_font,bg="black",fg="white",command=lambda:submit_number(2))
one_button=tkinter.Button(button_frame, text="1", font= button_font,bg="black",fg="white",command=lambda:submit_number(1))
zero_button=tkinter.Button(button_frame, text="0", font= button_font,bg="black",fg="white",command=lambda:submit_number(0))

#first row of the frame
clear_button.grid(row=0,column=0, pady=1, sticky="WE")
quit_button.grid(row=0,column=1, pady=1, sticky="WE")

#second row for the buttons
inverse_button.grid(row=1, column=0, pady=1,sticky="WE")
square_button.grid(row=1, column=1, pady=1,sticky="WE")
exponent_button.grid(row=1, column=2, pady=1,sticky="WE")
divide_button.grid(row=1, column=3, pady=1,sticky="WE")
#third row for the buttons (use padding to create the size of the columns)
seven_button.grid(row=2, column=0,  pady=1,sticky="WE", ipadx=20)
eight_button.grid(row=2, column=1, pady=1,sticky="WE", ipadx=20)
nine_button.grid(row=2, column=2, pady=1,sticky="WE", ipadx=20)
multiply_button.grid(row=2, column=3, pady=1, sticky="WE", ipadx=20)
#fourth row for the number buttons
four_button.grid(row=3, column=0,  pady=1,sticky="WE")
five_button.grid(row=3, column=1, pady=1,sticky="WE")
six_button.grid(row=3, column=2, pady=1,sticky="WE")
substract_button.grid(row=3, column=3, pady=1, sticky="WE")
#fifth row for the number buttons
one_button.grid(row=4, column=0,  pady=1,sticky="WE")
two_button.grid(row=4, column=1, pady=1,sticky="WE")
three_button.grid(row=4, column=2, pady=1,sticky="WE")
add_button.grid(row=4, column=3, pady=1, sticky="WE")
#sixth row for the number buttons
negate_button.grid(row=5, column=0,  pady=1,sticky="WE")
zero_button.grid(row=5, column=1, pady=1,sticky="WE")
decimal_button.grid(row=5, column=2, pady=1,sticky="WE")
equal_button.grid(row=5, column=3, pady=1, sticky="WE")

















root.mainloop()
    