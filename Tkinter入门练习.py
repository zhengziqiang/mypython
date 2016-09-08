from Tkinter import *
def processok():
	print ("OK buttom is clicked")
def processcancel():
	print ("cancel buttom is clicked")


window=Tk()
btok=Button(window,text = "OK",fg='red',command=processok)
btcan=Button(window,text = "cancel",bg='green',command=processcancel)
btok.pack()
btcan.pack()
window.mainloop()
