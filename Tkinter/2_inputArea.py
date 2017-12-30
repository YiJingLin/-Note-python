# text input 
import tkinter as tk

height =100
width = 200
sizeStr = '%sx%s' % (height, width)

window = tk.Tk()
window.title('Input')

####################################
e = tk.Entry(window, show='*') #password format
e.pack()

def insert():
	global e
	var = e.get()
	txt.insert('insert', var) # concat new string from Entry input area
	e.delete(0,	len(var)) # clear variable value from index 0 to len(var)

txt = tk.Text(window, height=2)
txt.pack()

btn = tk.Button(window, text=' btn', width=20, height=2, command=insert)
btn.pack()

window.mainloop()