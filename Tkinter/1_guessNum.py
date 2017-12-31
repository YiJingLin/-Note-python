import tkinter as tk
import numpy as np

height = 100
width = 200
sizeStr = '%sx%s' % (height, width)

window = tk.Tk()
window.title('Game1. pickNum')
# window.geometry(sizeStr)

####################################
win_count = 0
lose_count = 0
numList = [idx for idx in range(1,7)]

####################################

def com_randomChoose():
	num = np.random.choice(numList)
	print(num)
	return num

def user_pickNum():
	num = tkList_selection.get(tkList_selection.curselection())
	return num

def update():
	global win_count, lose_count
	
	com_num = com_randomChoose()
	user_num = user_pickNum()

	if com_num == user_num:
		win_count+=1
	else:
		lose_count+=1;

	score_desc = 'win : %s , lose : %s. (COM pick %s)' % (win_count, lose_count, com_num)
	tkVar_score.set(score_desc)
####################################

tkVar_score = tk.StringVar()
tkVar_score.set('')

tkList_selection = tk.StringVar()
tkList_selection.set(tuple(numList))
#####################################

tkLbl_title = tk.Label(window, text='pick a number from 1 to 6')
tkLbl_title.pack()

#score board
tkLbl_score = tk.Label(window, textvariable=tkVar_score)
tkLbl_score.pack()

# decision button
tkBtn_decision = tk.Button(window, text='compare', command=update)
tkBtn_decision.pack()

# selection list
tkList_selection = tk.Listbox(window, listvariable=tkList_selection)
tkList_selection.pack()

#####################################

window.mainloop()