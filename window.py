
from tkinter import *
from develop import Employee
import threading
import time

master = Tk()
master.title('良辰刷课')
master.geometry('300x200')
master.resizable(False, False)
Label(master, text="联系邮箱",fg='red').grid(row=1)
Label(master, text="1497367496@qq.com",fg='red').grid(row=1,column=1)
Label(master, text="用户名：").grid(row=2)
Label(master, text="密码：").grid(row=3)
Label(master, text="验证码：").grid(row=4)

username = Entry(master)
password = Entry(master,show='*')
verifycode = Entry(master)
username.grid(row=2, column=1, padx=10, pady=5 )
password.grid(row=3, column=1, padx=10, pady=5)
verifycode.grid(row=4, column=1, padx=10, pady=5)



employee = Employee()

def show():
    # print("作品：《%s》" % username.get())
    # print("passwrod：%s" % password.get())
    # print("code：%s" % verifycode.get())
    # username.delete(0, "end")
    # password.delete(0, "end")
    try:
        employee.login(str(username.get()).strip(),str(password.get()).strip(),str(verifycode.get()).strip())
    except Exception:
        pass
    verifycode.delete(0, "end")

def start():
    employee.start()


def Start():
    try:
        p = threading.Thread(target=start)
        p.start()
    except Exception:
        pass

def Stop():
    try:
        p = threading.Thread(target=stop)
        p.start()
        time.sleep(2)
        # p.join()
    except Exception:
        pass
    exit(0)

def stop():
    employee.stop()
    master.quit()


def speed(value):
    try:
        employee.playSpeed(value)
    except Exception:
        pass

def Mute():
    try:
        p = threading.Thread(target=mute)
        print('..................................')
        p.start()
        p.join()
    except Exception:
        pass

def mute():
    employee.mute()

def Play():
    try:
        p = threading.Thread(target=play)
        print('Play')
        p.start()
        time.sleep(2)
    except Exception:
        pass

def play():
    employee.play()
Button(master, text="登录", width=5, command=show).grid(row=5, column=0, sticky="w", padx=10, pady=5)
Button(master, text="开始", width=5, command=Start).grid(row=5, column=1, sticky="e", padx=45, pady=5)
Button(master, text="退出", width=5, command=Stop).grid(row=5, column=2, sticky="n", padx=10, pady=5)


# Button(master, text="x2", width=5, command=speed(value=2)).grid(row=6, column=0, sticky="w", padx=10, pady=5)
# Button(master, text="x5", width=5, command=speed(value=5)).grid(row=6, column=1, sticky="e", padx=45, pady=5)
# Button(master, text="x10", width=5, command=speed(value=10)).grid(row=6, column=2, sticky="n", padx=10, pady=5)


# Button(master, text="静音", width=5, command=Mute).grid(row=7, column=0, sticky="w", padx=10, pady=5)
# Button(master, text="播放", width=5, command=Play).grid(row=7, column=1, sticky="e", padx=10, pady=5)
# Button(master, text="x10", width=5, command=speed(value=10)).grid(row=6, column=2, sticky="n", padx=10, pady=5)



master.mainloop()