#Simple TODO list
import tkinter
from tkinter import END, ANCHOR

#Build Window
root=tkinter.Tk()
root.title("TO DO List")
root.iconbitmap("./check.ico")
root.geometry("400x400")
root.resizable(0,0)

#fonts and colors to be used further
my_font=("Times New Roman",12)
root_color= "#6c1cbc"
button_color= "#e2cff4"
root.config(bg=root_color)

#define functions
def add_item():
    """add an individual item to the listbox"""
    my_listbox.insert(END, list_entry.get())
    list_entry.delete(0,END)

def remove_item():
    """Remove selected (ANCHOR) item from the listbox"""
    my_listbox.delete(ANCHOR)

def clear_list():
    """Delete all items from the list """
    my_listbox.delete(0,END)

def save_list():
    """Save the list to a TXT file"""
    with open("todolist.txt", "w") as f:
        #listbox.get() returns a tuple
        list_tuple=my_listbox.get(0,END)
        for item in list_tuple:
            if item.endswith("\n"):
                f.write(item)
            else:
                f.write(item+"\n")

def open_list():
    """Open the list if there is one at the start"""
    try:
        with open("todo.txt", "r") as f:
            for line in f:
                my_listbox.insert(END, line)
    except:
        return

#layout
#create frames

input_frame=tkinter.Frame(root, bg=root_color)
output_frame=tkinter.Frame(root, bg=root_color)
button_frame=tkinter.Frame(root, bg=root_color)
input_frame.pack()
output_frame.pack()
button_frame.pack()

#input frame layout
list_entry= tkinter.Entry(input_frame, width=35, borderwidth=3, font=my_font)
list_add_button = tkinter.Button(input_frame,text= "Add Item", borderwidth=2, font=my_font, bg= button_color, command= add_item)
list_entry.grid(row=0, column=0, padx=5, pady=5)
list_add_button.grid(row=0, column=1, padx=5, pady=5, ipadx=5)

#output frame layout
my_scrollbar=tkinter.Scrollbar(output_frame)
my_listbox= tkinter.Listbox(output_frame, height=15, width=45, borderwidth=3, font=my_font, yscrollcommand=my_scrollbar.set)
#link scrollbar to listbox
my_scrollbar.config(command=my_listbox.yview)
my_listbox.grid(row=0, column=0)
my_scrollbar.grid(row=0, column=1, sticky="NS")

#button frame layout
list_remove_button= tkinter.Button(button_frame,text="remove item", borderwidth=2,font=my_font, bg=button_color, command=remove_item)
list_clear_button= tkinter.Button(button_frame,text="Clear List", borderwidth=2,font=my_font, bg=button_color, command=clear_list)
save_button=tkinter.Button(button_frame,text="Save List", borderwidth=2,font=my_font, bg=button_color, command=save_list)
quit_button=tkinter.Button(button_frame,text="QUIT", borderwidth=2,font=my_font, bg=button_color, command=root.destroy)
list_remove_button.grid(row=0, column=0, padx=2, pady=10)
list_clear_button.grid(row=0, column=1, padx=2, pady=10)
save_button.grid(row=0, column=2, padx=2, pady=10, ipadx=10)    
quit_button.grid(row=0, column=3, padx=2, pady=10, ipadx=25)

#Open the previous list if available
open_list()



root.mainloop()