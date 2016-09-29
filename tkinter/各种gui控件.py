from Tkinter import *
class widgetsDemo:
	def __init__(self):
		window=Tk()
		window.title("Widgets Demo")

		frame1=Frame(window)
		frame1.pack()
		self.v1=IntVar()
		cbtBold=Checkbutton(frame1,text="bold",variable=self.v1,command=self.processCheckbutton)
		self.v2=IntVar()

		rbred=Radiobutton(frame1,text="Red",bg='red',variable=self.v2,value=1,command=self.processRadiobutton)

		rbyellow=Radiobutton(frame1,text="Yellow",bg='yellow',variable=self.v2,value=2,command=self.processRadiobutton)
		
		frame2=Frame(window)
		frame2.pack()
		label=Label(frame2,text="Enter your name:")
		self.name=StringVar()
		entryName=Entry(frame2,textvariable=self.name)
		btGetName=Button(frame2,text="get name",command=self.processButton)

		message=Message(frame2,text="It is a widget demo")

		label.grid(row=1,column=1)
		entryName.grid(row=1,column=2)
		btGetName.grid(row=1,column=3)
		message.grid(row=1,column=4)

		text=Text(window)
		text.pack()
		text.insert(END,"Tip\nthe best way to learn tkinter is to read")
		text.insert(END,"these carefully designed examples and use them")
		text.insert(END,"to create your application")

		window.mainloop()
	def processCheckbutton(self):
		print ("check button is:"+("check" if self.v1.get()==1 else "Unchecked"))
	def processRadiobutton(self):
		print (("red" if self.v2.get()==1 else "Yellow")+"is selected")
	def processButton(self):
		print ("your name is"+ self.name.get())
widgetsDemo()


