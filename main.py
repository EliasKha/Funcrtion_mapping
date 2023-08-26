import tkinter
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Platform():

	def __init__(self) -> None:
		
		self.gr = Graph()
		self.Settings()

	def Settings(self):
		self.app = tkinter.Tk()
		self.app.geometry("1000x900")
		self.app.title("Funcion Mapping Platform")

	#Clear button
	def ClearButton(self):
		"""
		Adds a clear button when called
		"""
		clear_button = tkinter.Button(master=self.app, text="Clear", command=lambda: self.gr.clear(self.canvas))
		return clear_button

	#plot button
	def PlotButton(self):
		"""
		Adds a PLot button when called
		"""
		plot_button = tkinter.Button(master=self.app, text="Plot", command=lambda: self.gr.plot(self.canvas, self.entry.get()))
		return plot_button

	def Entry(self):
		entry = tkinter.Entry(master=self.app)
		return entry

	#Graph1
	def GraphSettings(self):
		self.canvas = FigureCanvasTkAgg(self.gr.fig, master = self.app)
		self.canvas.get_tk_widget().pack()
	
	
	def System(self):
		self.entry = self.Entry()
		self.entry.pack()
		self.GraphSettings()
		self.ClearButton().pack()
		self.PlotButton().pack()
		self.app.mainloop()


class Graph():

	def __init__(self) -> None:
		self.plot_length = [-5, 5, -100, 100]
		self.fig, self.ax = plt.subplots()
		self.ax.axis(self.plot_length)
		self.ax.grid(True)
		
	def clear(self, canvas):
		self.ax.clear()
		self.ax.axis(self.plot_length)
		self.ax.grid(True)
		canvas.draw()
		print("clear")

	def plot(self, canvas, entry):
		self.ax.clear()
		self.ax.axis(self.plot_length)
		self.ax.grid(True)
		x = np.arange(-50,50.0,1)
		y = self.calculator(x, entry)


		self.ax.plot(x,y)
		canvas.draw()
		print("plot")
	
	def calculator(self,input_list, entry):
		output_list = []
		for x in input_list:
			output_list.append(eval(entry))
		return output_list



if __name__ == '__main__':
	appli = Platform()
	appli.System()

