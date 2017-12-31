# TKinter button and change window 
import tkinter as tk


height = 100
width = 200
sizeStr = '%sx%s' % (height, width)

window = tk.Tk()
window.title('Button click')
window.geometry(sizeStr)

####################################

count = 0
lbl_txt = tk.StringVar()
lbl_txt.set('')

def update_lbl_txt():
	global lbl_txt, count
	count +=1
	lbl_txt.set('Button click :' + str(count))

label = tk.Label(window, textvariable = lbl_txt, bg='blue', width = 20, height = 10)
label.pack()

btn = tk.Button(window, text='update click times', width=20, height=2, command=update_lbl_txt)
btn.pack()


window.mainloop()