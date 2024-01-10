from tkinter import *
root = Tk()
root.title("Calculator V2.0")
root.geometry("380x550+750+150")
root.resizable(0,0)


result=0
result_list=[]

########## functions #############
def enterNumber(x):
    if entry_box.get() =="O":
        entry_box.delete(0,"end")
        entry_box.insert(0,str(x))
    else:
        length= len(entry_box.get())
        entry_box.insert(length,str(x))

def enterOperator(x):
    if entry_box.get()!="O":
        length = len(entry_box.get())
        entry_box.insert(length, btn_operator[x]["text"])
    

def funcClear():
    entry_box.delete(0,END)
    entry_box.insert(0,"O")
    

def funcOperator():
    content = entry_box.get()
    result= eval(content)
    entry_box.delete(0,"end")
    entry_box.insert(0, str(result))

    result_list.append(content)
    result_list.reverse()
    statusBar.configure(text="Operations: " + "|".join(result_list[:5]), font="verdana 10 bold" )



def funcDelete():
    length=len(entry_box.get())
    entry_box.delete(length-1,"end")
    if length==1:
        entry_box.insert(0,"O")



#Input-entry field
entry_box=Entry(font="Verdana 14 bold", width=20, bg="#e6e6fa", bd=5, justify=RIGHT)
entry_box.insert(0,"O")
entry_box.place(x=20, y=10)

#######Buttons for Numbers######
btn_numbers=[]

for i in range(10):
    btn_numbers.append(Button(width=4, text=str(i), font="times 15 bold", bd=5, command= lambda x=i:enterNumber(x)))

btn_text=1
for i in range(0,3):
    for j in range(0,3):
        btn_numbers[btn_text].place(x=30+j*90,y=70+i*70)
        btn_text+=1

############Operator_Buttons################
btn_operator = []    
for i in range(4):
    btn_operator.append(Button(width=4, font="times 15 bold", bd=5, command=lambda x=i:enterOperator(x)))

btn_operator[0]["text"]="+"
btn_operator[1]["text"]="-"
btn_operator[2]["text"]="*"
btn_operator[3]["text"]="/"

for i in range(4):
    btn_operator[i].place(x=290, y=(i+1)*70)

############Other_Buttons################
btn_zero =Button(width=19, text="0", font="times 15 bold", bd=5, command=lambda x=0:enterNumber(x))
btn_zero.place(x=30, y=280)
btn_clear = Button(width=4, text="C", font="times 15 bold", bd=5, command=funcClear)
btn_clear.place(x=30, y=340)
btn_dot = Button(width=4, text=".", font="times 15 bold", bd=5, command= lambda x=".": enterNumber(x))
btn_dot.place(x=115, y=340)
btn_equal = Button(width=4, text="=", font="times 15 bold", bd=5, command= funcOperator)
btn_equal.place(x=205, y=340)
icon=PhotoImage(file="Arrowback32.png")
btn_delete= Button(width=60, height=35,  font="times 15 bold", bd=5, image= icon, command=funcDelete)
btn_delete.place(x=290, y=340)

##################History Bar###################
statusBar =Label(root, text="Operators: ", relief=SUNKEN, height=3, anchor=W, font="verdana 11 bold")
statusBar.pack(side= BOTTOM, fill=X)






root.mainloop()