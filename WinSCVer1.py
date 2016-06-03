import os,os.path
import winsound
from PIL import Image as IM
from PIL import ImageTk
from tkinter import *

root = Tk();root.title("WinSC.Ver1")

canvas = Canvas(root,width = 500,height = 600)
canvas.pack()

num = 0

#背景图片和图标
image = ImageTk.PhotoImage((IM.open("D://DeskPicture//F.jpg")).resize((500,600)))
image2 = ImageTk.PhotoImage((IM.open("D://DeskPicture//B.jpg")).resize((500,600)))
image3 = ImageTk.PhotoImage(IM.open("D://DeskPicture//O.jpg").resize((500,600)))
exiticon = ImageTk.PhotoImage(IM.open("D://material//little//exit.png").resize((40,40),IM.ANTIALIAS))

#获取滑块指示的频率和持续时间
def winspeaker():
    duty = scaleduty.get()*10 # max = 1s
    winsound.Beep(scalefre.get(),duty)

"""
重绘canvas时必须指定image在画布上的中心位置，否则导致元组索引越界
IndexError: tuple index out of range
"""
def mousecall(event):
    global num
    num += 1
    if num ==1:
        canvas.create_image((250,300),image = image)#必须指定image中心位置的元组
    elif num == 2:
        canvas.create_image((250,300),image = image2)
    elif num == 3:
        canvas.create_image((250,300),image = image3)
        num = 0
    #print(num)

def sysexit():
    winsound.PlaySound("SystemExit",winsound.SND_ALIAS)
    sys.exit(0)

canvas.create_image((250,300),image = image,anchor = CENTER)
canvas.bind("<Button-3>",mousecall) #绑定鼠标右键

#调节持续时间
scaleduty = Scale(root,from_ = 0,to = 100,resolution = 5,orient = HORIZONTAL,troughcolor = "#00ffff")
scaleduty.config(length = 500,label = "Duty",width = 10,activebackground = "#32cd32",fg = "#0000ff",sliderlength = 20)
scaleduty.place(x = 00,y = 485)
scaleduty.set(50)#设置默认的持续时间：50ms

#调节Beep频率：100-32700Hz
scalefre = Scale(root,from_ = 100,to = 32700)
scalefre.config(resolution = 200,orient = HORIZONTAL,length = 500,label = "Fre")
scalefre.config(activebackground = "#76ee00",troughcolor = "#00ee00",showvalue = True)
scalefre.config(highlightbackground = "#caff70",width = 10,sliderlength = 20,fg = "#76ee00")
scalefre.place(x = 00,y = 543)
scalefre.set(5000)#设置默认频率：5KHz

beep = Button(root,text = "嘟嘟",command = winspeaker,fg = "#ff4500",bg = "#90ee90",cursor = "hand2")
beep.config(highlightcolor = "#c0ff3e")
beep.place(x= 465,y = 410)

Button(root,image = exiticon,command = sysexit,cursor = "hand2").place(x = 460,y = 440)

root.mainloop()



