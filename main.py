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
	def PlotButton(self, entry):
		"""
		Adds a PLot button when called
		"""
		plot_button = tkinter.Button(master=self.app, text="Plot", command=lambda: self.gr.plot(self.canvas, entry))
		return plot_button

	def SearchBar(self):
		search_bar = tkinter.Entry(master=self.app)
		return search_bar

	#Graph1
	def GraphSettings(self):
		self.canvas = FigureCanvasTkAgg(self.gr.fig, master = self.app)
		self.canvas.get_tk_widget().pack()
	
	
	def System(self):
		self.SearchBar().pack()
		self.GraphSettings()
		self.ClearButton().pack()
		self.PlotButton(self.SearchBar().get()).pack()
		self.app.mainloop()


class Graph():

	def __init__(self) -> None:
		self.fig, self.ax = plt.subplots()
		
	def clear(self, canvas):
		self.ax.clear()
		canvas.draw()
		print("clear")

	def plot(self, canvas, entry):
		self.ax.clear()
		x=np.random.randint(0,10,10)
		y=np.random.randint(0,10,10)
		self.ax.scatter(x,y)
		canvas.draw()
		print("plot")
		print(entry)



if __name__ == '__main__':
	appli = Platform()
	appli.System()


# Plotting
# Need to add a bar
# Make the bar share a function to plot
# Add a clearing button 
# Add a Plotting button

