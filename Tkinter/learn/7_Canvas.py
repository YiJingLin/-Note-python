import tkinter as tk
mainX = 800; mainY = 800

# main window 
height = 300
width = 300
sizeMain = '%sx%s+%s+%s' % (height, width, mainX, mainY)

window = tk.Tk()
window.title('Canvas')
window.geometry(sizeMain)

####################################

# def


####################################

tkCanvas = tk.Canvas(window, bg='yellow',
		height=500, width=500)
tkCanvas.pack()

x0, y0, x1, y1= 100, 100, 200, 200
tkCanvas.create_line(x0, y0, x1, y1)
tkCanvas.create_line(100, 200, 200, 100)

tkCanvas.create_oval(x0, y0, x1, y1, fill='red')  #创建一个圆，填充色为`red`红色
tkCanvas.create_oval(x0+10, y0+10, x1, y1, fill='blue')

tkCanvas.create_arc(x0+30, y0+30, x1+30, y1+30, start=0, extent=180)  #创建一个扇形
tkCanvas.create_arc(x0+30, y0+30, x1+30, y1+30, start=0, extent=-10)  #创建一个扇形

tkCanvas.create_polygon(0, 0, 0, 100, 100, 100)
####################################

window.mainloop()
