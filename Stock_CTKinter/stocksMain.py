from typing import Any, Tuple
import customtkinter as ctk 
from settings import * 
import yfinance as yf
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

try: 
	from ctypes import windll, byref, sizeof, c_int
except:
	pass

class App(ctk.CTk):
	def __init__(self):
		super().__init__(fg_color = BG_COLOR)
		self.geometry('900x800')
		self.title('Stock')
		self.iconbitmap('stock.png')
		self.title_bar_color()

		# DATA section
		self.input_string = ctk.StringVar(value = 'AAPL')
		self.time_string = ctk.StringVar(value= TIME_OPTIONS[0])
		self.time_string.trace('w', self.create_graph)
		self.has_data= False
			# widgets
		self.graph_panel = None
		InputPanel(self, self.input_string, self.time_string)

		# eventt
		self.bind('<Return>', self.input_handler)


		self.mainloop()
	
	def create_graph(self, *args):
		if self.graph_panel: self.graph_panel.pack_forget()
		if self.has_data:
			match self.time_string.get():
				case 'Max' : data = self.max
				case '1 Year' : data = self.year
				case '6 Months' : data = self.six_month
				case 'Month' : data = self.one_month
				case 'Week' : data = self.one_week


			self.graph_panel = GraphPanel(self, data)

	def input_handler(self, event= None):
		ticker = yf.Ticker(self.input_string.get())
		start = datetime(1950,1,1)
		end = datetime.today()		
		
		self.max = ticker.history(start = start, end = end, period = '1d')

		self.year = self.max.iloc[-260:]
		self.six_month = self.max.iloc[-130:]
		self.one_month = self.max.iloc[-22:]
		self.one_week = self.max.iloc[-5:]
		self.has_data = True
		

		self.create_graph()

	def title_bar_color(self):
		try:
			HWND = windll.user32.GetParent(self.winfo_id())
			windll.dwmapi.DwmSetWindowAttribute(HWND, 35, byref(c_int(TITLE_HEX_COLOR)), sizeof(c_int))
		except:
			pass

class InputPanel(ctk.CTkFrame):
	def __init__(self, parent, input_string, time_string):
		super().__init__(master = parent, fg_color= INPUT_BG_COLOR, corner_radius= 0)
		self.pack(fill = 'both', side = 'bottom')

		# widgets
		ctk.CTkEntry(self, textvariable=input_string, fg_color =BG_COLOR, border_color= TEXT_COLOR, border_width = 1).pack(side= 'left', padx= 10, pady = 10)
		self.buttons = [TextButton(self, text, time_string) for text in TIME_OPTIONS]

		time_string.trace('w', self.unselect_all_buttons)

	def unselect_all_buttons(self, *args):
		for button in self.buttons:
			button.unselect()

class TextButton(ctk.CTkLabel):
	def __init__(self, parent, text, time_string):
		super().__init__(master = parent,text = text, text_color = HIGHLIGHT_COLOR)
		self.pack(side= 'right', padx= 10, pady = 10 )
		self.bind('<Button>', self.select_handler)
	
		self.time_string = time_string
		self.text = text

		if time_string.get() == text:
			self.select_handler()
	
	def select_handler(self, event = None):
		self.time_string.set(self.text)
		self.configure(text_color = HIGHLIGHT_COLOR)
	
	def unselect(self):
		self.configure(text_color = TEXT_COLOR)
	
	"""def selection_handle(self, command, **kw) -> None:
		return super().selection_handle(command, **kw)"""

class GraphPanel(ctk.CTkFrame):
	def __init__(self, parent, data):
		super().__init__(master = parent,fg_color = BG_COLOR)
		self.pack(expand= True, fill = 'both')

		#figure
		figure = plt.Figure()
		figure.subplots_adjust(left= 0, right= 0.99, bottom=0, top= 1)
		figure.patch.set_facecolor(BG_COLOR)

		
		ax = figure.add_subplot(111)
		ax.set_facecolor(BG_COLOR)
		#ax.plot(data['Close'])
		for side in ['top', 'left', 'right', 'bottom']:
			ax.spines[side].set_color(BG_COLOR)
		
		line = ax.plot(data['Close'])[0]
		line.set_color(HIGHLIGHT_COLOR)

		#tick
  
		ax.tick_params(axis = 'x', direction = 'in', pad = -14, colors = TICK_COLOR)
		ax.yaxis.tick_right()
		ax.tick_params(axis = 'y', direction = 'in', pad = -22, colors = HIGHLIGHT_COLOR)


		#widget
		figure_widget = FigureCanvasTkAgg(figure, master = self)
		figure_widget.get_tk_widget().pack(fill='both', expand= True)
  

App()