import customtkinter
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Platform():

	def __init__(self) -> None:
		
		self.gr = Graph()
		self.Settings()

	def Settings(self):
		customtkinter.set_appearance_mode("System")
		customtkinter.set_default_color_theme("blue")
		self.app = customtkinter.CTk()
		self.app.geometry("720x420")
		self.app.title("Funcion Mapping Platform")

#Clear button
	def ClearButton(self):
		"""
		Adds a clear button when called
		"""
		clear_button = customtkinter.CTkButton(master=self.app, text="Clear", command=self.gr.clear(self.ax, self.canvas))
		clear_button.pack(padx=20, pady=10)

#plot button
	def PlotButton(self):
		"""
		Adds a PLot button when called
		"""
		plot_button = customtkinter.CTkButton(master=self.app, text="Plot", command=self.gr.plot(self.ax, self.canvas))
		plot_button.pack(padx=20, pady=10)

#Graph1
	def GraphSettings(self):
		self.fig, self.ax = plt.subplots()
		self.canvas = FigureCanvasTkAgg(self.fig, master = self.app)
		self.canvas.get_tk_widget().pack()

	def System(self):
		self.GraphSettings()
		self.ClearButton()
		self.PlotButton()
		self.app.mainloop()


class Graph():

	def __init__(self) -> None:
		pass
		
	def clear(self, ax, canvas):
		ax.clear()
		canvas.draw()
		print("clear")

	def plot(self, ax, canvas):
		ax.clear()
		x=np.random.randint(0,10,10)
		y=np.random.randint(0,10,10)
		ax.scatter(x,y)
		canvas.draw()



if __name__ == '__main__':
	appli = Platform()
	appli.System()


# Plotting
# Need to add a bar
# Make the bar share a function to plot
# Add a clearing button 
# Add a Plotting button

