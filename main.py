from tkinter import *
from PIL import ImageTk                    #to import jpg images
window=Tk()

#Screen resolution
window.geometry('1280x700')
window.resizable(False,False)             #Remove the resize button


#Background image
bg=ImageTk.PhotoImage(file='bg.jpg') 
bglabel=Label(window,image=bg)            #image label
bglabel.place(x=0,y=0)                    #image location

#Frame login 
img=ImageTk.PhotoImage(file='back.jpg')
Login=Frame(window)
Login.place(x=900,y=150)



Logo=ImageTk.PhotoImage(file='user.jpg')
Logolabel=Label(Login,image=Logo)
Logolabel.grid(row=0,column=0,columnspan=2) #columnspan takes2 column space

usernameimg=PhotoImage(file='user.png')
usernameLabel=Label(Login,image=usernameimg,text='Username',font=('times new roman',20),compound=LEFT)
usernameLabel.grid(row=1,column=0)

usernamefield=Entry(Login)
usernamefield.grid(row=1,column=1)

window.mainloop()
