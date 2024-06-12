from tkinter import *
from tkinter import messagebox

from PIL import ImageTk


def login():
    if usernameEntry.get()==''or passwordEntry.get()=='':
        messagebox.showerror('Error','Fields cannot be empty')
    elif usernameEntry.get()=='dev'and passwordEntry.get()=='12345':
        messagebox.showinfo('Success', 'Welcome')
        window.destroy()
        import sms
    else:
        messagebox.showerror('Error', 'Please enter correct Credentials')


window=Tk()
window.geometry('1280x700+0+0')
window.title('Login in Student Management System')
window.resizable(False,False)
backgroundImage=ImageTk.PhotoImage(file='bg.jpg')
bgLabel=Label(window,image=backgroundImage)
bgLabel.place(x=0,y=0)
loginFrame=Frame(window,bg='black')
loginFrame.place(x=400,y=150)
logoImage=PhotoImage(file='logo.png')
logoLabel=Label(loginFrame,image=logoImage,bg='black')
logoLabel.grid(row=0,column=0,columnspan=2)

usernameImage=PhotoImage(file='user.png')
usernameLabel=Label(loginFrame,image=usernameImage,text='Username',compound=LEFT
                    ,font=('vienna',20),bg='black',padx=10,fg='white')
usernameLabel.grid(row=1,column=0,pady=10,padx=20)
usernameEntry=Entry(loginFrame,font=('vienna',20),bd=5,fg='Dodgerblue2')
usernameEntry.grid(row=1,column=1,pady=10,padx=20)

passwordImage=PhotoImage(file='password.png')
passwordLabel=Label(loginFrame,image=passwordImage,text='Password',compound=LEFT
                    ,font=('vienna',20),bg='black',padx=10,fg='white')
passwordLabel.grid(row=2,column=0,pady=10,padx=20)
passwordEntry=Entry(loginFrame,font=('vienna',20),bd=5,fg='Dodgerblue2')
passwordEntry.grid(row=2,column=1,pady=10,padx=20)
loginButton=Button(loginFrame,text='Login' ,font=('vienna',14),width=15,padx=10,fg='white',bg='cornflowerblue'
                   ,activeforeground='white',cursor='hand2',command=login)
loginButton.grid(row=3,column=1,pady=10)



window.mainloop()