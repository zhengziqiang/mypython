#!/usr/bin/env python  
#coding=utf-8  
      
      
from smtplib import *  
from Tkinter import *  
import tkMessageBox  
import string  
      

class loginPage(object):  
      
      
    def __init__(self, main, info='Mail Send System'):  
            self.main = main  
            self.mainlabel = Label(main, text=info, justify=CENTER)  
            self.mainlabel.grid(row=0, columnspan=3)  
      
      
            self.user = Label(main, text='username', borderwidth=2)  
            self.user.grid(row=1, sticky=W)  
      
      
            self.pwd = Label(main, text='password', borderwidth=2)  
            self.pwd.grid(row=2, sticky=W)  
      
      
            self.userEntry = Entry(main)  
            self.userEntry.grid(row=1, column=1, columnspan=2)  
            self.userEntry.focus_set()  
      
      
            self.pwdEntry = Entry(main, show='*')  
            self.pwdEntry.grid(row=2, column=1, columnspan=2)  
      
      
            self.loginButton = Button(main, text='Login', borderwidth=2, command=self.login)  
            self.loginButton.grid(row=3, column=1)  
      
      
            self.clearButton = Button(main, text='Clear', borderwidth=2, command=self.clear)  
            self.clearButton.grid(row=3, column=2)  
      
      
    def login(self):  
            self.username = self.userEntry.get().strip()  
            self.passwd = self.pwdEntry.get().strip()  
            if len(self.username) == 0 or len(self.passwd) == 0 or '@' not in self.username:  
                tkMessageBox.showwarning('警告', '用户名或者密码为空或邮件格式不正确')  
      
      
                self.clear()  
                self.userEntry.focus_set()  
                return  
      
      
            self.getSmtpHost()  
            self.connect()  
      
      
    def connect(self):  
            'this method will try to connet the SMTP server according the current user'  
            HOST = 'smtp.' + self.smtp +'.com'  
            try:  
                self.mySMTP = SMTP(HOST)  
                self.mySMTP.login(self.username, self.passwd)  
            #except SMTPConnectError:  
            except Exception, e:  
                tkMessageBox.showerror('连接错误', '%s' % e)  
                return  
            self.mySendMail = sendMail(self.main, self.mySMTP, self.username)  
      
      
    def clear(self):  
            self.userEntry.delete(0, END)  
            self.pwdEntry.delete(0, END)  
      
      
    def getSmtpHost(self):  
            'this method try to obtian the SMTP HOST according the user account'  
            firstSplit = self.username.split('@')[1]  
            self.smtp = firstSplit.split('.')[0]  
      
      
      
      
class sendMail(object):  
    'my sendemail class'  
    def __init__(self, main, smtp='', sender=''):  
            self.smtp = smtp  
            self.sender = sender  
      
      
            self.sendPage = Toplevel(main)  
      
      
            self.sendToLabel = Label(self.sendPage, text='send to:')  
            self.sendToLabel.grid()  
            self.sendToEntry = Entry(self.sendPage)  
            self.sendToEntry.grid(row=0, column=1)  
      
      
            self.subjectLabel = Label(self.sendPage, text='subject:')  
            self.subjectLabel.grid(row=1, column=0)  
            self.subjectEntry = Entry(self.sendPage)  
            self.subjectEntry.grid(row=1, column=1)  
      
      
            self.fromToLabel = Label(self.sendPage, text='from to:')  
            self.fromToLabel.grid(row=2, column=0)  
            self.formToAdd = Label(self.sendPage, text=self.sender)  
            self.formToAdd.grid(row=2, column=1)  
      
      
            self.sendText = Text(self.sendPage)  
            self.sendText.grid(row=3, column=0, columnspan=2)  
      
      
            self.sendButton = Button(self.sendPage, text='send', command=self.sendMail)  
            self.sendButton.grid(row=4, column=0)  
      
      
            self.newButton = Button(self.sendPage, text='new mail', command=self.newMail)  
            self.newButton.grid(row=4, column=1)  
      
      
    def getMailInfo(self):  
            self.sendToAdd = self.sendToEntry.get().strip()  
            self.subjectInfo = self.subjectEntry.get().strip()  
            self.sendTextInfo = self.sendText.get(1.0, END)  
      
      
    def sendMail(self):  
            self.getMailInfo()  
            body = string.join(("From: %s" % self.sender, "To: %s" % self.sendToAdd, "Subject: %s" % self.subjectInfo, "", self.sendTextInfo), "\r\n")  
            try:  
                self.smtp.sendmail(self.sender, [self.sendToAdd], body)  
            except Exception, e:  
                tkMessageBox.showerr('发送失败', "%s" % e)  
                return  
            tkMessageBox.showinfo('提示', '邮件已发送成功！')  
      
      
    def newMail(self):  
            self.sendToEntry.delete(0, END)  
            self.subjectEntry.delete(0, END)  
            self.sendText.delete(1.0, END)  
      
      
if __name__ == '__main__':  
      
      
        root = Tk()  
        root.title('简易发送邮件程序')  
      
      
        myLogin = loginPage(root)  
      
      
        #root.wait_window(myLogin.mySendMail.sendPage)  
        mainloop()  