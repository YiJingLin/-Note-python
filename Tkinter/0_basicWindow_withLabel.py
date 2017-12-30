
# coding: utf-8

# In[ ]:

import tkinter as tk


# In[ ]:

# 
height = 100
width = 200
sizeStr = '%sx%s' % (height, width)

window = tk.Tk()
window.title('GUI window')
window.geometry(sizeStr)



# In[ ]:

label = tk.Label(window,
                text = 'this is a test',
                bg='green',
                width=20, height=10
                )

label.pack()


# In[ ]:

# 这里是窗口的内容
window.mainloop()

