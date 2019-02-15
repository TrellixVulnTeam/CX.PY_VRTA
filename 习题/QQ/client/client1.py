import tkinter
import socket
import threading
win = tkinter.Tk()
win.title("客户端")
win.geometry("400x400+200+20")

ck = None


def getInfo():
    while True:
        data = ck.recv(1024)
        text.insert(tkinter.INSERT,data.decode("utf-8"))

def connectStrver():
    global ck
    ipStr = eip.get()
    portStr = eport.get()
    userStr = euser.get()
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ipStr, int(portStr)))
    client.send(userStr.encode("utf-8"))
    ck=client
    #等待接收数据
    t = threading.Thread(target=getInfo)
    t.start()

def sendMail():
    friend = efriend.get()
    sendStr = esend.get()
    sendStr = friend + ":" + sendStr

    ck.send(sendStr.encode("utf-8"))

labelUser = tkinter.Label(win,text="userName").grid(row=0,column=0)
euser = tkinter.Variable()
entryUser = tkinter.Entry(win,textvariable = euser).grid(row=0,column=1)

labelIp = tkinter.Label(win,text="ip").grid(row=1,column=0)
eip = tkinter.Variable()
entryIp = tkinter.Entry(win,textvariable = eip).grid(row=1,column=1)

labelPort = tkinter.Label(win,text="port").grid(row=2,column=0)
eport = tkinter.Variable()
entryport = tkinter.Entry(win,textvariable = eport).grid(row=2,column=1)

button = tkinter.Button(win, text="连接", command = connectStrver).grid(row=3,column=0)

text = tkinter.Text(win,width=30, height=5)
text.grid(row=4,column=0)

esend = tkinter.Variable()
entrySend = tkinter.Entry(win,textvariable = esend).grid(row=5,column=0)

efriend = tkinter.Variable()
entryFriend = tkinter.Entry(win,textvariable = efriend).grid(row=6,column=0)

button2 = tkinter.Button(win, text="发送", command = sendMail).grid(row=6,column=1)

win.mainloop()














