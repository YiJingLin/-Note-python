import tkinter as tk


height = 500
width = 500
sizeStr = '%sx%s' % (height, width)

window = tk.Tk()
window.title('selection List')
# window.geometry(sizeStr)

####################################
def printSelection():
	text = strList.get(strList.curselection()) #get selection
	varLbl.set(text)

def addE():
	text = addElement.get()
	strList.insert('end',text)
	addElement.delete(0,len(text))

listcontent = ['first','second','third']
listcontent = tuple(listcontent)

#variable
varLbl = tk.StringVar()
varLbl.set('')
varList = tk.StringVar()
varList.set(listcontent)


lbl = tk.Label(window, bg='blue', width=20, textvariable=varLbl)
lbl.pack()

btn = tk.Button(window, text='printSelection', width=20, command=printSelection)
btn.pack()

strList = tk.Listbox(window, listvariable=varList)
strList.pack()

addElement = tk.Entry(window)
addElement.pack()

insrt_Element = tk.Button(window, text='add', width=3, command=addE)
insrt_Element.pack(side=tk.RIGHT)
window.mainloop()