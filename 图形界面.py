from Tkinter import *
import tkMessageBox as mes
# class Application(Frame):
# 	def __init__(self,master=None):
# 		Frame.__init__(self,master)
# 		self.pack()
# 		self.createWidgets()
# 	def createWidgets(self):
# 		self.hellolabel=Label(self,text='hello World')
# 		self.hellolabel.pack()
# 		self.quitButton=Button(self,text='Quit',command=self.quit)
# 		self.quitButton.pack()
	
class App1(Frame):
	def __init__(self,master=None):
		Frame.__init__(self,master)
		self.pack()
		self.createWidgets()
	def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.alertButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        mes.showinfo('Message', 'Hello, %s' % name)
app=Application()
app.master.title('Hello World')
app.mainloop()
app1=App1()
app1.master.title("hello")
app1.mainloop()