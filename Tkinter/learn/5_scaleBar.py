import tkinter as tk
import numpy as np

height = 100
width = 200
sizeStr = '%sx%s' % (height, width)

window = tk.Tk()
window.title('scale bar ')
# window.geometry(sizeStr)

####################################

def updateLabel(num):
	tkLabel_output.config(text='num : '+num)

####################################

tkLabel_output = tk.Label(window, width=20, text='empty')
tkLabel_output.pack()

tkScale = tk.Scale(window, from_=0, to=10, orient=tk.HORIZONTAL,
				length=200, showvalue=0, tickinterval=5, resolution=0.1,
				command=updateLabel)
tkScale.pack()
####################################

window.mainloop()