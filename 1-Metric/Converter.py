import tkinter
from tkinter import ttk, END, StringVar
#from tkinter import 

# MAIN WINDOW

root = tkinter.Tk()
root.title('Unit Converter')
root.iconbitmap('ruler.ico')
root.geometry('400x200')
root.resizable(0,0)

# colors and fonts
field_font =('Cambria', 10)
bg_color= "#c75c5c"
button_color= "#f5cf87"
root.config(bg=bg_color)

# FUNCTIONS
def convert():
    metric_values = {
        'femto' : 10**-15,
        'pico' : 10**-12,
        'nano' : 10**-9,
        'micro' : 10**-6,
        'mili' : 10**10-3,
        'centi' : 10**-2,
        'deci' : 10**-1,
        'base value' :1,
        'deca': 10,
        'hecto' : 10**2,
        'kilo' :10**3,
        'mega' :10**6,
        'giga' : 10**9,
        'tera' : 10**12,
        'peta' : 10**15
    }

    output_field.delete(0,END)
    start_value = float(input_field.get())
    start_prefix= input_combobox.get()
    end_prefix= output_combobox.get()

    base_value = start_value*metric_values[start_prefix]
    end_value = base_value/metric_values[end_prefix]

    output_field.insert(0, str(end_value))



# LAYOUTS
    # INPUT AND OUTPUT AREAS

input_field= tkinter.Entry(root, width= 20, font= field_font, borderwidth=3)
output_field= tkinter.Entry(root, width=20, font= field_font, borderwidth=3)
equal_label= tkinter.Label(root, text="=", font="field_font", bg=bg_color)

input_field.grid(row=0, column=0, padx=10, pady=10)
output_field.grid(row=0, column=2, padx=10, pady=10)
equal_label.grid(row=0, column=1, padx=10, pady=10)

input_field.insert(0, 'Enter Your Quantity')
metric_list= ['femto', 'pico', 'micro', 'mili', 'centi', 'deci', 'base value', 'deca', 'hecto', 'kilo', 'mega', 'giga', 'tera', 'peta']
input_combobox= ttk.Combobox(root, value= metric_list,font=field_font, justify='center')
output_combobox=ttk.Combobox(root, value= metric_list,font=field_font, justify='center')
to_label = tkinter.Label(root, text = "to", font = field_font, bg= bg_color )
input_combobox.grid(row=1, column=0, padx=10, pady=10)
output_combobox.grid(row=1, column=2, padx=10, pady=10)
to_label.grid(row=1,column=1, padx=10, pady=10)
input_combobox.set('base value')
output_combobox.set('base value')
input_choice = StringVar()
output_choice= StringVar()

# combobox



""" DROPDOWN
input_dropdown = tkinter.OptionMenu(root, input_choice, *metric_list)
output_dropdown = tkinter.OptionMenu(root, output_choice, *metric_list)
to_label = tkinter.Label(root, text = "to", font = field_font, bg= bg_color )

input_dropdown.grid(row=1, column=0)
to_label.grid(row=1,column=1)
output_dropdown.grid(row=1, column=2)
"""
input_choice.set('base value')
output_choice.set('base value')

# CONVERSION BUTTON

convert_button = tkinter.Button(root, text='convert', font=field_font, bg=button_color, command=convert)
convert_button.grid(row=2, column=0, columnspan=3, padx=10, pady=10, ipadx=50)



root.mainloop()
