import tkinter as tk
import numpy as np

height = 100
width = 200
sizeStr = '%sx%s' % (height, width)

window = tk.Tk()
window.title('Game1. pickNum')
# window.geometry(sizeStr)

####################################

def updateLabel():
	text = tkVar_radioValue.get()
	tkLabel_output.config(text='you have selected ' + text)

####################################

tkVar_radioValue = tk.StringVar()

tkLabel_output = tk.Label(window, width=20, text='empty')
tkLabel_output.pack()

# hint: parameter:varaible is used to store radiobutton's value
tkRadio_optionA = tk.Radiobutton(window, text='Option A', value='A',
				 variable=tkVar_radioValue, command=updateLabel)
tkRadio_optionA.pack()

tkRadio_optionB = tk.Radiobutton(window, text='Option B', value='B',
				 variable=tkVar_radioValue, command=updateLabel)
tkRadio_optionB.pack()

tkRadio_optionC = tk.Radiobutton(window, text='Option C', value='C',
				 variable=tkVar_radioValue, command=updateLabel)
tkRadio_optionC.pack()
####################################

window.mainloop()