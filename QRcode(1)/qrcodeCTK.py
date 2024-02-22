import tkinter as tk
from tkinter import filedialog
from typing import Tuple
import customtkinter as ctk
from PIL import Image, ImageTk
import qrcode

class App(ctk.CTk):
	def __init__(self):
		# Window Setup
		ctk.set_appearance_mode('light')
		super().__init__(fg_color = 'white')

		self.title('QR Code Gen')
		self.iconbitmap('images/empty.ico')
		
		self.geometry('400x400')
		self.resizable(0,0)
		
        # Entry field
		self.entry_string= ctk.StringVar(value="text")
		self.entry_string.trace("w", self.create_qr)
		EntryField(self, self.entry_string, self.save)
		
        # event 
		self.bind('<Return>', self.save)

		# QR Code
		raw_image= Image.open("images/placeholder.png").resize((200,200))
		tk_image= ImageTk.PhotoImage(raw_image)
		self.qr_image=QrImage(self)
		self.qr_image.update_image(tk_image)
		
		# QrImage(self) this line become self.qr_image= QrImage(self)

        # Running the APP
		self.mainloop()
		
	def create_qr(self, *args):
		current_text= self.entry_string.get()
		if current_text:
			self.raw_image= qrcode.make(current_text).resize((200,200))
			self.tk_image=ImageTk.PhotoImage(self.raw_image)
			self.qr_image.update_image(self.tk_image)
		else:
			self.qr_image.clear()
			self.raw_image = None
			self.tk_image = None
			
	def save(self, event = ''):
		if self.raw_image:
			file_path= filedialog.asksaveasfilename()
			if file_path:
				self.raw_image.save(file_path + '.jpg')
          		
			
			
		
			

class EntryField(ctk.CTkFrame):
	def __init__(self, parent, entry_string,save_func):
		super().__init__(master = parent, corner_radius = 20, fg_color= '#021FB3')
		self.place(relx= 0.5, rely = 1, relwidth = 1, relheight = 0.4, anchor = "center")

        #grid layout
		self.rowconfigure((0,1), weight=1, uniform='a')
		self.columnconfigure(0, weight=1, uniform='a')
		
        #widgets
		self.frame=ctk.CTkFrame(self, fg_color='transparent')
		self.frame.columnconfigure(0, weight=1,uniform='b')
		self.frame.columnconfigure(1, weight=4,uniform='b')
		self.frame.columnconfigure(2, weight=2,uniform='b')
		self.frame.columnconfigure(3, weight=1,uniform='b')
		self.frame.grid(row = 0, column = 0)
		
		entry= ctk.CTkEntry(self.frame, textvariable= entry_string, fg_color="#2E54E8", border_width=0, text_color="white")
		entry.grid(row=0, column=1, sticky="nsew")
		
		button= ctk.CTkButton(self.frame, command=  save_func, text= "SAVE",fg_color="#2E54E8", border_width=1, text_color="white", hover_color="#4266F1")
		button.grid(row=0, column=2, sticky="nsew", padx= 10)
		
class QrImage(tk.Canvas):
	def __init__(self, parent):
		super().__init__(master= parent, background="#eeeeee", bd=1, highlightthickness=2, relief="ridge")
		self.place(relx=0.5, rely=0.4, width=200, height= 200, anchor= "center")
	def update_image(self, image_tk):
		self.clear()
		self.create_image(0,0, image = image_tk, anchor="nw")
		
	def clear(self):
		self.delete("all") 
	
App()