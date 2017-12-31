import tkinter as tk

height = 100
width = 200
sizeStr = '%sx%s' % (height, width)

window = tk.Tk()
window.title('check button')
# window.geometry(sizeStr)

####################################
def updateLabel():
	var1 = tkVar_check1.get()
	var2 = tkVar_check2.get()
	tkLabel_output.config(text=var1 +':'+ var2)
	
####################################

tkVar_check1 = tk.StringVar()
tkVar_check1.set('0')
tkVar_check2 = tk.StringVar()
tkVar_check2.set('0')

tkLabel_output = tk.Label(window, width=20, text='empty')
tkLabel_output.pack()


tkCheck_check1 = tk.Checkbutton(window, text='Python', variable=tkVar_check1,
				onvalue=1, offvalue=0, command=updateLabel)
tkCheck_check1.pack()

tkCheck_check2 = tk.Checkbutton(window, text='C++', variable=tkVar_check2,
				onvalue=1, offvalue=0, command=updateLabel)
tkCheck_check2.pack()

####################################

window.mainloop()