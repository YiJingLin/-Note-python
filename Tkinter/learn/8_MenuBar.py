import tkinter as tk
mainX = 800; mainY = 800

# main window 
height = 300
width = 300
sizeMain = '%sx%s+%s+%s' % (height, width, mainX, mainY)

window = tk.Tk()
window.title('Menu bar')
window.geometry(sizeMain)

####################################
def menuCmd():
	print('Event Triggered')

####################################
tkMenuBar = tk.Menu(window)

# create new column entity
tkMenu = tk.Menu(tkMenuBar, tearoff=0)

tkMenuBar.add_cascade(label='File', menu=tkMenu)
tkMenu.add_command(label='New', command=menuCmd)
tkMenu.add_command(label='Save', command=menuCmd)
tkMenu.add_separator()
tkMenu.add_command(label='Exit', command=window.quit)


# create another column entity
tkSecMenu = tk.Menu(tkMenu)
tkMenu.add_cascade(label='Import', menu=tkSecMenu, underline=0)
tkSecMenu.add_command(label='submenu1', command=menuCmd)
tk


####################################
window.config(menu=tkMenuBar)
window.mainloop()