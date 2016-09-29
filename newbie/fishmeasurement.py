import wx
import tkFileDialog
import Image
#codeing=gbk
def read(event):
    #filename = tkFileDialog.askdirectory()
    filename = tkFileDialog.askopenfilename()
    #im=Image.open(filename)
    #im.show()
    
   # panel=wx.Panel(win)
    image=wx.Image(filename,wx.BITMAP_TYPE_BMP)
    temp=image.ConvertToBitmap()
   #win.panel=wx.Panel(win)
    size=temp.GetWidth(),temp.GetHeight()
    win.bmp=wx.StaticBitmap(parent=contents,bitmap=temp)
    #sizer=wx.BoxSizer()
    #sizer.Add(win.panel,1,wx.EXPAND)
    #win.SetSizerAndFit(sizer)
    win.Centre()
   # win.SetClientSize(size)
  
    print filename

def load(event):
    file=open(filename.GetValue())
    contents.SetValue(file.read())
    file.close()

def save(event):
    file=open(filename.GetValue(),'w')
    file.write(contents.GetValue())
    file.close()

def __init__(self): 
    wx.Frame.__init__(self, None, -1, "My Frame", size=(300, 300)) 
    panel = wx.Panel(self, -1) 
    panel.Bind(wx.EVT_MOTION,  self.OnMove) 
    wx.StaticText(panel, -1, "Pos:", pos=(10, 12)) 
    self.posCtrl = wx.TextCtrl(panel, -1, "", pos=(40, 10)) 
    
def OnMove(self, event): 
    pos = event.GetPosition() 
    self.posCtrl.SetValue("%s, %s" % (pos.x, pos.y)) 

    print pos.x,pos.y

    
app=wx.App()
win=wx.Frame(None,title="FishMeasurement",size=(1500,1000))
bkg=wx.Panel(win)

Button1=wx.Button(bkg,label='¿¿')
Button1.Bind(wx.EVT_BUTTON,read)

Button2=wx.Button(bkg,label='¿¿')
Button3=wx.Button(bkg,label='¿¿')
Button3.Bind(wx.EVT_BUTTON,OnMove)



Button4=wx.Button(bkg,label='¿¿')

Button5=wx.Button(bkg,label='¿¿')
Button5.Bind(wx.EVT_BUTTON,save)



Button6=wx.Button(bkg,label='ÉÏÒ»·ù')
Button7=wx.Button(bkg,label='ÏÂÒ»·ù')
#filename=wx.TextCtrl(bkg)
contents=wx.TextCtrl(bkg,style=wx.TE_MULTILINE|wx.HSCROLL)

hbox=wx.BoxSizer()
#hbox.Add(filename,proportion=1,flag=wx.EXPAND)
hbox.Add(Button1,proportion=0,flag=wx.LEFT,border=80)
hbox.Add(Button2,proportion=0,flag=wx.LEFT,border=80)
hbox.Add(Button3,proportion=0,flag=wx.LEFT,border=80)
hbox.Add(Button4,proportion=0,flag=wx.LEFT,border=80)
hbox.Add(Button5,proportion=0,flag=wx.LEFT,border=80)
hbox.Add(Button6,proportion=0,flag=wx.LEFT,border=80)
hbox.Add(Button7,proportion=0,flag=wx.LEFT,border=80)

vbox=wx.BoxSizer(wx.VERTICAL)
vbox.Add(hbox,proportion=0,flag=wx.EXPAND|wx.ALL,border=5)
vbox.Add(contents,proportion=1,flag=wx.EXPAND|wx.LEFT|wx.BOTTOM|wx.RIGHT,border=5)


bkg.SetSizer(vbox)
win.Show()

app.MainLoop()
