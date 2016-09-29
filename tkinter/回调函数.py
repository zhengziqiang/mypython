from Tkinter import *
master=Tk()
MODES=[
	("monchrome","1"),
	("grayscale","L"),
	("True color","RGB"),
	("color separation","CMYK"),
]
v=StringVar()
v.set("L")
for text,mode in MODES:
	b=Radiobutton(master,text=text,variable=v,value=mode)
	b.pack(anchor=W)
mainloop()