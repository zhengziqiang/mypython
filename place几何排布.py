from Tkinter import *
root=Tk();root.title("logging")
root['width']=200;root['height']=80
Label(root,text='username',width=6).place(x=1,y=1)
Entry(root,width=20).place(x=45,y=1)
Label(root,text='passwd',width=6).place(x=1,y=20)
Entry(root,width=20,show='*').place(x=45,y=20)
Button(root,text='log',width=8).place(x=40,y=40)
Button(root,text='cancel',width=8).place(x=110,y=40)
root.mainloop()