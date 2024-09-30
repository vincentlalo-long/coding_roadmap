from tkinter import *

win = Tk()
win.geometry("500x300")
win.config(bg="#4b9ce3")

fr1 = Frame()
fr1.pack()
fr2 =Frame()
fr2.pack()
fr3 = Frame()
fr3.place(x = 1,y = 150)
lb1 = Label(fr1,text = "Đổi từ hệ thập phân sang nhị phân",font=("Arial",12,"bold"),bg = "#4b9ce3")
lb1.pack(side="top")
lb2 = Label(fr2,text = "Số thập phân",font=("Arial",12,"bold"))
lb2.pack(side="left")
def doi():
    b = int(te1.get())
    i = 0
    s = ''
    while b != 0:
        c = b % 2
        b = b // 2
        i = i + 1
        s = s + str(c)
    lb4.config(text = s[::-1])
te1 = Entry(fr2,font=("Arial",12),width=50)
te1.pack()
but1 = Button(win,font = ("Arial",12),text = "Chuyển đổi",command=doi).place(x = 200, y = 90)
lb3 = Label(fr3,text = "Số nhị phân",font=("Arial",12,"bold"))
lb3.pack(side="left")
lb4 = Label(fr3,font=("Arial",12,"bold"))
lb4.pack()
win.mainloop()
