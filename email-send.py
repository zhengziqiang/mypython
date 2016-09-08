from Tkinter import *
from smtplib import *
import string
import tkMessageBox as mes

class loginPage(object):
	def __init__(self,master,info='Mail Send System'):
		self.master=master
		self.mainlabel=Label(master,text=info,justify=CENTER)
		self.mainlabel.grid(row=0,columnspan=3)


		self.user=Label(master,text='username',borderwidth=2)
		self.user.grid(row=1,sticky=W)

		self.pwd=Label(master,text='passwd',borderwidth=2)
		self.pwd.grid(row=2,sticky=W)

		self.userEntry=Entry(master)
		self.userEntry.grid(row=1,column=1,columnspan=2)
		self.userEntry.focus_set()

		self.pwdEntry=Entry(master,show='*')
		self.pwdEntry.grid(row=2,column=1,columnspan=1)

		self.loginButton=Button(master,text='login',borderwidth=2,command=self.login)
		self.loginButton.grid(row=3,column=1)

		self.clearButton=Button(master,text='Clear',borderwidth=2,command=self.clear)
		self.clearButton.grid(row=3,column=2)

	def login(self):
		self.username=self.userEntry.get().strip()
		self.passwd=self.pwdEntry.get().strip()
		if len(self.username) ==0 or len(self.passwd)==0 or '@' not in self.username:
			mes.showwarning('warning','passwd or username is not right')
			self.clear()
			self.userEntry.focus_set()
			return 

		self.get_smtp()
		self.connect()

	def connect(self):
		'this method will try to connect to the smtp server according to the current user'
		HOST='smtp' + self.smtp + '.com'
		try:
			self.mysmtp=SMTP(HOST)
			self.mysmtp.login(self.username,self.passwd)
		except Exception, e:
			mes.showerror('connecting error','%s'%e)
			return 
		self.mySendMail=sendMail(self.master,self.mysmtp,self.username)

	def clear():
		self.userEntry.delete(0,END)
		self.pwdEntry.delete(0,END)

	def get_smtp(self):
		'this method try to obtain the smtp host according the user account'
		firstSplit=self.username.split('@')[1]
		self.smtp=firstSplit.split('.')[0]


class sendMail(object):
	def __init__(self,master,smtp='',sender=''):
		self.smtp=smtp
		self.sender=sender

		self.sendPage=Toplevel(master)

		self.sendToLabel = Label(self.sendPage,text='send to:')
		self.sendToLabel.grid()
		self.sendToEntry = Entry(self.sendPage)
		self.sendToEntry.grid(row=0,column=1)

		self.subjectLabel=Label(self.sendPage,text='subject:')
		self.subjectLabel.grid(row=1,column=0)
		self.subjectEntry=Entry(self.sendPage)
		self.subjectEntry.grid(row=1,column=1)

		self.fromTolabel=Label(self.sendPage,text='from to')
		self.fromTolabel.grid(row=2,column=0)
		self.fromToAdd=Label(self.sendPage,text=self.sender)
		self.fromToAdd.grid(row=2,column=1)

		self.sendText=Text(self.sendPage)
		self.sendText.grid(row=3,column=0,columnspan=2)

		self.newButton=Button(self.sendPage,text='new mail',command=self.newMail)
		self.newButton.grid(row=4,column=1)

	def getMailInfo(self):
		self.sendToAdd=self.sendToEntry.get().strip()
		self.subjectInfo=self.subjectEntry.get().strip()
		self.sendT

		
