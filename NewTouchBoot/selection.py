from time import sleep
import wx
import subprocess
from threading import Thread
from os import system as fileopen
from time import sleep

width=800
height=480

def scale_bitmap(bitmap, widther, heighter):
    image = wx.ImageFromBitmap(bitmap)
    image = image.Scale(widther, heighter, wx.IMAGE_QUALITY_HIGH)
    result = wx.BitmapFromImage(image)
    return result        
        
class PanelOne(wx.Panel):
    """"""
    global width
    global height
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent=parent)

class PanelTwo(wx.Panel):
    """"""
    global width
    global height
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent=parent)

class PanelThree(wx.Panel):
    """"""
    global width
    global height
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent=parent)

class MyForm(wx.Frame):

    global width
    global height

    def __init__(self, *args, **kw):
        super(MyForm, self).__init__(*args, **kw) 
        
        self.InitUI()

    def InitUI(self):  
        # self.panel_two = PanelTwo(self)
        self.panel_one = PanelOne(self)
        self.panel_three = PanelThree(self)
        self.SetSize((width, height))
        self.SetTitle('Starting Your Entertainment Experience')
        self.Centre()
        self.panel_one.SetSize((width, height))
        # self.panel_two.SetSize((width, height))
        self.panel_three.SetSize((width, height))
        
        rpbmp = wx.Bitmap("/opt/retropie/configs/all/NewTouchBoot/retro.jpg", wx.BITMAP_TYPE_ANY)
        rpbmp = scale_bitmap(rpbmp, width/2, height/2)
        kbbmp = wx.Bitmap("/opt/retropie/configs/all/NewTouchBoot/kodi.jpg", wx.BITMAP_TYPE_ANY)
        kbbmp = scale_bitmap(kbbmp, width/2, height/2)
        rbbmp = wx.Bitmap("/opt/retropie/configs/all/NewTouchBoot/Debian.jpg", wx.BITMAP_TYPE_ANY)
        rbbmp = scale_bitmap(rbbmp, width/2, height/2)
        tbbmp = wx.Bitmap("/opt/retropie/configs/all/NewTouchBoot/terminal.png", wx.BITMAP_TYPE_ANY)
        tbbmp = scale_bitmap(tbbmp, width/2, height/2)

        self.panel_one.rpb = wx.BitmapButton(self.panel_one, bitmap=rpbmp, pos=(0,0), size=(width/2,height/2))
        self.panel_one.kb = wx.BitmapButton(self.panel_one, bitmap=kbbmp, pos=(width/2, 0), size=(width/2,height/2))
        self.panel_one.rb = wx.BitmapButton(self.panel_one, bitmap=rbbmp, pos=(0, height/2), size=(width/2,height/2))
        self.panel_one.tb = wx.BitmapButton(self.panel_one, bitmap=tbbmp, pos=(width/2, height/2), size=(width/2,height/2))
        
        self.panel_one.rpb.Bind(wx.EVT_BUTTON, self.Pressedrpb)
        self.panel_one.kb.Bind(wx.EVT_BUTTON, self.Pressedkb)
        self.panel_one.rb.Bind(wx.EVT_BUTTON, self.Pressedrb)
        self.panel_one.tb.Bind(wx.EVT_BUTTON, self.Pressedtb)

        self.SetSize((width, height))
        self.SetTitle('Starting Your Entertainment Experience')
        self.Centre()
        self.Show(True)
    
    def Pressedrpb(self, e):
        self.panel_one.Hide()
        self.panel_three.Show()

    def Pressedkb(self, e):

        fileopen('/opt/retropie/configs/all/NewTouchBoot/mounts')
        sleep(0.1)
        f = open("/opt/retropie/configs/all/NewTouchBoot/checknum","w")
        f.write("num=2")
        f.close()
        exit()

    def Pressedrb(self, e):

        fileopen('/opt/retropie/configs/all/NewTouchBoot/mounts')
        sleep(0.1)
        f = open("/opt/retropie/configs/all/NewTouchBoot/checknum","w")
        f.write("num=3")
        f.close()
        exit()

    def Pressedtb(self, e):

        fileopen('/opt/retropie/configs/all/NewTouchBoot/mounts')
        sleep(0.1)
        f = open("/opt/retropie/configs/all/NewTouchBoot/checknum","w")
        f.write("num=4")
        f.close()
        exit()
 
    #----------------------------------------------------------------------
 
    #----------------------------------------------------------------------

 
# Run the program
if __name__ == "__main__":
    # cmd = ['xrandr']
    # cmd2 = ['grep', '*']
    # p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    # p2 = subprocess.Popen(cmd2, stdin=p.stdout, stdout=subprocess.PIPE)
    # p.stdout.close()
    # resolution_string, junk = p2.communicate()
    # resolution = resolution_string.split()[0]
    # strwidth, strheight = resolution.split('x')
    width=800
    height=480
    ex = wx.App()
    MyForm(None)
    ex.MainLoop() 