from Tkinter import *
master=Tk()
v=IntVar()
Radiobutton(master,text='one',variable=v,value=1).pack(anchor=W)
Radiobutton(master,text='two',variable=v,value=2).pack(anchor=W)
master.mainloop()