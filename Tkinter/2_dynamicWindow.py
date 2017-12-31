# radio button, sacle bar, check button
# radio button : change bg color
# scale bar : change window height and width
# check button : show label or not

###################################
import tkinter as tk
mainX = 800; mainY = 800

# main window 
height = 300
width = 300
sizeMain = '%sx%s+%s+%s' % (height, width, mainX, mainY)

window = tk.Tk()
window.title('Dynamic Window. (main)')
window.geometry(sizeMain)

#sub window
sub_height = sub_width = 100
sizeSub = '%sx%s+%s+%s' % (sub_height, sub_width, 100 ,100)
windowSub = tk.Tk()
windowSub.title('child Window.')

####################################
def updateWindowSize(size):
	sizeSub = '%sx%s+%s+%s' % (size, size, 100 ,100)
	tkVar_size.set(size)
	if tkVar_show.get()=='1':
		windowSub.title('child Window '+str((size, size)))
	windowSub.geometry(sizeSub)

def startSetting(): # start and add new component to window
	tkBtn_start.destroy()
	tkScale_subSize.pack()
	tkRadio_blueBG.pack()
	tkRadio_yellowBG.pack()
	tkCheck_showSize.pack()

def updatelabelBG():
	tkLabel_subLabel.config(bg=tkVar_color.get())

def updateSubTitle():
	size = tkVar_size.get()

	if tkVar_show.get()=='1' :
		windowSub.title('child Window '+str((size, size)))
	else:
		windowSub.title('child Window ')

def destroySub():
	windowSub.destroy()
####################################

## Main
tkVar_color = tk.StringVar()
tkVar_show = tk.StringVar()
tkVar_show.set(0)
tkVar_size = tk.StringVar()
tkVar_size.set(100)

tkBtn_start = tk.Button(window, text='start !', command=startSetting)
tkBtn_start.pack()

tkScale_subSize = tk.Scale(window, from_=100, to=500,
				orient=tk.HORIZONTAL, length=200, showvalue=0,
				tickinterval=200, resolution=10, command=updateWindowSize)

tkRadio_blueBG = tk.Radiobutton(window, text='blue background',
				  variable=tkVar_color, value='blue', command=updatelabelBG)
tkRadio_yellowBG = tk.Radiobutton(window, text='yellow background',
				 variable=tkVar_color, value='yellow', command=updatelabelBG)

tkCheck_showSize = tk.Checkbutton(window, text='show size on title',
					variable=tkVar_show, onvalue=1, offvalue=0, command=updateSubTitle)

## Sub
tkLabel_subLabel = tk.Label(windowSub, text='im label in child window')
tkLabel_subLabel.pack()


tkBtn_subDestroy = tk.Button(windowSub, text='destroy', command=destroySub)
tkBtn_subDestroy.pack()
####################################

window.mainloop()
# windowSub.mainloop()