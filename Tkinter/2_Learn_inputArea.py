# text input 
import tkinter as tk

height =100
width = 200
sizeStr = '%sx%s' % (height, width)

window = tk.Tk()
window.title('Input')
window.geometry(sizeStr)

####################################
e = tk.Entry(window, show='*') #password format
e.pack()

def insert():
	global e
	var = e.get()

	# txt.insert(2.2, var) # insert string from Entry input area to index: (2,2)
	# txt.insert('end', var) # concat
	txt.insert('insert', var) # insert string from Entry input area to specified index

	e.delete(0,	len(var)) # clear variable value from index 0 to len(var)


txt = tk.Text(window, height=2)
txt.pack()

btn = tk.Button(window, text=' btn', width=20, height=2, command=insert)
btn.pack()

window.mainloop()