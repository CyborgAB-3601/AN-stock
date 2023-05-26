from tkinter import *
from tkinter import messagebox
from PIL import ImageTk                    #to import jpg images
window=Tk()

def login():
    if usernamefield.get()=='' or passwordfield.get()=='':
        messagebox.showerror('Error','Blank fields are not accepted')
    elif usernamefield.get()=='Abhinav' and passwordfield.get()=='3601':
        messagebox.showinfo('Authorized','Welcome')


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

usernameimg=PhotoImage(file='user.png') #usename field
usernameLabel=Label(Login,image=usernameimg,text='Username',font=('times new roman',20),compound=LEFT)
usernameLabel.grid(row=1,column=0,padx=20)
usernamefield=Entry(Login)
usernamefield.grid(row=1,column=1,padx=20)
passwordimg=PhotoImage(file='user.png') #Password field
passwordLabel=Label(Login,image=usernameimg,text='Password',font=('times new roman',20),compound=LEFT)
passwordLabel.grid(row=2,column=0,padx=20)
passwordfield=Entry(Login)
passwordfield.grid(row=2,column=1,padx=20)

loginbutton=Button(Login,text='LOGIN',font=('mono space',20),pady=10,bg='cornflowerblue',fg='white',activebackground='cornflowerblue',activeforeground='white',command=login)
loginbutton.grid(row=3,column=1,pady=10)

window.mainloop()

