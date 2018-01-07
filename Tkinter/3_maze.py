import tkinter as tk
import numpy as np

height = 100
width = 200
sizeStr = '%sx%s' % (height, width)

window = tk.Tk()
window.title('control window')
window.geometry(sizeStr)

#sub window
sub_height = sub_width = 100
sub_size = '%sx%s+%s+%s' % (sub_height, sub_width, 100 ,100)
sub_window = tk.Tk()
sub_window.title('game window')
sub_window.geometry(sub_size)
#########################################
def updateGameWindow(action):
	tkVar_lbltxt.set(action)

#########################################
tkVar_lbltxt = tk.StringVar()
tkVar_lbltxt.set('')

tkBtn_up = tk.Button(window, text='- up -', command=lambda: updateGameWindow(action=0)).pack()
tkBtn_down = tk.Button(window, text='-down-', command=lambda: updateGameWindow(action=1)).pack()
tkBtn_left = tk.Button(window, text='-left-', command=lambda: updateGameWindow(action=2)).pack()
tkBtn_right = tk.Button(window, text='-right-', command=lambda: updateGameWindow(action=3)).pack()

tkLabel = tk.Label(window, textvariable = tkVar_lbltxt).pack()

####################################

window.mainloop()
# sub_window.mainloop()