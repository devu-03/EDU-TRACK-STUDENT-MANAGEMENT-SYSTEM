from tkinter import *
import time
import ttkthemes
from tkinter import ttk, messagebox
import pymysql
#fuctionality Part
def update_student():

    def update_data():
        query='update student set name=%s, mobile=%s, email=%s, address=%s, gender=%s, dob=%s, date=%s, time=%s where id=%s'
        mycursor.execute(query,(nameEntry.get(), phoneEntry.get(), emailEntry.get(),
                                addressEntry.get(), genderEntry.get(), dobEntry.get(),date,currenttime,idEntry.get()))
        con.commit()
        messagebox.showinfo('Success',f'Id {idEntry.get()} is modified successfully',parent=update_window)
        update_window.destroy()
        show_student()

    update_window = Toplevel()
    update_window.title('Update Student')
    update_window.grab_set()
    update_window.resizable(0, 0)
    idLabel = Label(update_window, text='Id', font=('arial', 18))
    idLabel.grid(row=0, column=0, padx=20, pady=15, sticky=W)
    idEntry = Entry(update_window, font=('Courier', 16), width=24)
    idEntry.grid(row=0, column=1, padx=20, pady=15)

    nameLabel = Label(update_window, text='Name', font=('arial', 18))
    nameLabel.grid(row=1, column=0, padx=20, pady=15, sticky=W)
    nameEntry = Entry(update_window, font=('Courier', 16), width=24)
    nameEntry.grid(row=1, column=1, padx=20, pady=15)

    phoneLabel = Label(update_window, text='Phone', font=('arial', 18))
    phoneLabel.grid(row=2, column=0, padx=20, pady=15, sticky=W)
    phoneEntry = Entry(update_window, font=('Courier', 16), width=24)
    phoneEntry.grid(row=2, column=1, padx=20, pady=15)

    emailLabel = Label(update_window, text='Email', font=('arial', 18))
    emailLabel.grid(row=3, column=0, padx=20, pady=15, sticky=W)
    emailEntry = Entry(update_window, font=('Courier', 16), width=24)
    emailEntry.grid(row=3, column=1, padx=20, pady=15)

    addressLabel = Label(update_window, text='Address', font=('arial', 18))
    addressLabel.grid(row=4, column=0, padx=20, pady=15, sticky=W)
    addressEntry = Entry(update_window, font=('Courier', 16), width=24)
    addressEntry.grid(row=4, column=1, padx=20, pady=15)

    genderLabel = Label(update_window, text='Gender', font=('arial', 18))
    genderLabel.grid(row=5, column=0, padx=20, pady=15, sticky=W)
    genderEntry = Entry(update_window, font=('Courier', 16), width=24)
    genderEntry.grid(row=5, column=1, padx=20, pady=15)

    dobLabel = Label(update_window, text='D.O.B', font=('arial', 18))
    dobLabel.grid(row=6, column=0, padx=20, pady=15, sticky=W)
    dobEntry = Entry(update_window, font=('Courier', 16), width=24)
    dobEntry.grid(row=6, column=1, padx=20, pady=15)

    update_student_button = ttk.Button(update_window, text='UPDATE',command=update_data)
    update_student_button.grid(row=7, columnspan=2, pady=15)

    indexing=studentTable.focus()
    content=studentTable.item(indexing)
    listdata=content['values']
    idEntry.insert(0,listdata[0])
    nameEntry.insert(0, listdata[1])
    phoneEntry.insert(0, listdata[2])
    emailEntry.insert(0, listdata[3])
    addressEntry.insert(0, listdata[4])
    genderEntry.insert(0, listdata[5])
    dobEntry.insert(0, listdata[6])




def show_student():
    query = 'select * from student'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('', END, values=data)
def delete_student():
    indexing=studentTable.focus()
    content=studentTable.item(indexing)
    content_id=content['values'][0]
    query='delete from student where id=%s'
    mycursor.execute(query,content_id)
    con.commit()
    messagebox.showinfo('Deleted',f'Id {content_id} is deleted successfully')
    query='select * from student'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('',END,values=data)

def search_student():
    def search_data():
        query='select * from student where id=%s or name=%s or mobile=%s or email=%s or address=%s or gender=%s or dob=%s'
        mycursor.execute(query,(idEntry.get(), nameEntry.get(), phoneEntry.get(), emailEntry.get(),
                                addressEntry.get(), genderEntry.get(), dobEntry.get()))
        studentTable.delete(*studentTable.get_children())
        fetched_data = mycursor.fetchall()
        for data in fetched_data:
            studentTable.insert('',END,values=data)

    search_window = Toplevel()
    search_window.title('Search Student')
    search_window.grab_set()
    search_window.resizable(0, 0)
    idLabel = Label(search_window, text='Id', font=('arial', 18))
    idLabel.grid(row=0, column=0, padx=20, pady=15, sticky=W)
    idEntry = Entry(search_window, font=('Courier', 16), width=24)
    idEntry.grid(row=0, column=1, padx=20, pady=15)

    nameLabel = Label(search_window, text='Name', font=('arial', 18))
    nameLabel.grid(row=1, column=0, padx=20, pady=15, sticky=W)
    nameEntry = Entry(search_window, font=('Courier', 16), width=24)
    nameEntry.grid(row=1, column=1, padx=20, pady=15)

    phoneLabel = Label(search_window, text='Phone', font=('arial', 18))
    phoneLabel.grid(row=2, column=0, padx=20, pady=15, sticky=W)
    phoneEntry = Entry(search_window, font=('Courier', 16), width=24)
    phoneEntry.grid(row=2, column=1, padx=20, pady=15)

    emailLabel = Label(search_window, text='Email', font=('arial', 18))
    emailLabel.grid(row=3, column=0, padx=20, pady=15, sticky=W)
    emailEntry = Entry(search_window, font=('Courier', 16), width=24)
    emailEntry.grid(row=3, column=1, padx=20, pady=15)

    addressLabel = Label(search_window, text='Address', font=('arial', 18))
    addressLabel.grid(row=4, column=0, padx=20, pady=15, sticky=W)
    addressEntry = Entry(search_window, font=('Courier', 16), width=24)
    addressEntry.grid(row=4, column=1, padx=20, pady=15)

    genderLabel = Label(search_window, text='Gender', font=('arial', 18))
    genderLabel.grid(row=5, column=0, padx=20, pady=15, sticky=W)
    genderEntry = Entry(search_window, font=('Courier', 16), width=24)
    genderEntry.grid(row=5, column=1, padx=20, pady=15)

    dobLabel = Label(search_window, text='D.O.B', font=('arial', 18))
    dobLabel.grid(row=6, column=0, padx=20, pady=15, sticky=W)
    dobEntry = Entry(search_window, font=('Courier', 16), width=24)
    dobEntry.grid(row=6, column=1, padx=20, pady=15)

    search_student_button = ttk.Button(search_window, text='SEARCH', command=search_data)
    search_student_button.grid(row=7, columnspan=2, pady=15)
def add_student():
    def add_data():
        if idEntry.get()=='' or nameEntry.get()=='' or phoneEntry.get()=='' or emailEntry.get()=='' or addressEntry.get()=='' or genderEntry.get()=='' or dobEntry.get()=='':
            messagebox.showerror('Error','All FieldS are required', parent=add_window)
        else:
            try:
              query='insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
              mycursor.execute(query,(idEntry.get(), nameEntry.get(), phoneEntry.get(), emailEntry.get(),
                                        addressEntry.get(), genderEntry.get(), dobEntry.get(),date,currenttime))
              con.commit()
              result=messagebox.askyesno('Confirm','Data added successfully. Do you want to clean the form?',parent=add_window)
              if result:
                 idEntry.delete(0,END)
                 nameEntry.delete(0, END)
                 phoneEntry.delete(0, END)
                 emailEntry.delete(0,END)
                 addressEntry.delete(0, END)
                 genderEntry.delete(0, END)
                 dobEntry.delete(0, END)
              else:
                  pass
            except:
               messagebox.showerror('Error','Id cannot be repeated',parent=add_window)
               return

            query='select * from student'
            mycursor.execute(query)
            fetched_data=mycursor.fetchall()
            studentTable.delete(*studentTable.get_children())
            for data in fetched_data:
                studentTable.insert('',END,values=data)
    add_window=Toplevel()
    add_window.grab_set()
    add_window.resizable(0,0)
    idLabel=Label(add_window,text='Id',font=('arial', 18))
    idLabel.grid(row=0,column=0,padx=20,pady=15,sticky=W)
    idEntry=Entry(add_window,font=('Courier',16),width=24)
    idEntry.grid(row=0,column=1,padx=20,pady=15)

    nameLabel = Label(add_window, text='Name', font=('arial', 18))
    nameLabel.grid(row=1, column=0, padx=20, pady=15,sticky=W)
    nameEntry = Entry(add_window, font=('Courier', 16), width=24)
    nameEntry.grid(row=1, column=1, padx=20, pady=15)

    phoneLabel = Label(add_window, text='Phone', font=('arial', 18))
    phoneLabel.grid(row=2, column=0, padx=20, pady=15,sticky=W)
    phoneEntry = Entry(add_window, font=('Courier', 16), width=24)
    phoneEntry.grid(row=2, column=1, padx=20, pady=15)

    emailLabel = Label(add_window, text='Email', font=('arial', 18))
    emailLabel.grid(row=3, column=0, padx=20, pady=15,sticky=W)
    emailEntry = Entry(add_window, font=('Courier', 16), width=24)
    emailEntry.grid(row=3, column=1, padx=20, pady=15)

    addressLabel = Label(add_window, text='Address', font=('arial', 18))
    addressLabel.grid(row=4, column=0, padx=20, pady=15,sticky=W)
    addressEntry = Entry(add_window, font=('Courier', 16), width=24)
    addressEntry.grid(row=4, column=1, padx=20, pady=15)

    genderLabel = Label(add_window, text='Gender', font=('arial', 18))
    genderLabel.grid(row=5, column=0, padx=20, pady=15,sticky=W)
    genderEntry = Entry(add_window, font=('Courier', 16), width=24)
    genderEntry.grid(row=5, column=1, padx=20, pady=15)

    dobLabel = Label(add_window, text='D.O.B', font=('arial', 18))
    dobLabel.grid(row=6, column=0, padx=20, pady=15,sticky=W)
    dobEntry = Entry(add_window, font=('Courier', 16), width=24)
    dobEntry.grid(row=6, column=1, padx=20, pady=15)

    add_student_button=ttk.Button(add_window,text='ADD STUDENT',command=add_data)
    add_student_button.grid(row=7, columnspan=2, pady=15)
def connect_database():
    def connect():
        global mycursor,con
        try:
           con = pymysql.connect(host='localhost', user='root', password='T#9758@qlph')
           mycursor = con.cursor()
        except:
            messagebox.showerror('Error','Invalid Details',parent=connectWindow)
            return
        try:
            query='create database studentmanagementsystem'
            mycursor.execute(query)
            query='use studentmanagementsystem'
            mycursor.execute(query)
            query = 'create table student(Id int not null primary key, name varchar(30), mobile varchar(10), email varchar(30), address varchar(100), gender varchar(20), dob varchar(20), date varchar(50), time varchar(50))'
            mycursor.execute(query)
        except:
          query='use studentmanagementsystem'
          mycursor.execute(query)
        messagebox.showinfo('Success', 'Database Connection id Successful', parent=connectWindow)
        connectWindow.destroy()
        addstudentButton.config(state=NORMAL)
        searchstudentButton.config(state=NORMAL)
        deletestudentButton.config(state=NORMAL)
        updatestudentButton.config(state=NORMAL)
        showstudentButton.config(state=NORMAL)
        exportstudentButton.config(state=NORMAL)
        exitButton.config(state=NORMAL)

    connectWindow = Toplevel()
    connectWindow.grab_set()
    connectWindow.geometry('500x250+730+230')
    connectWindow.title('Database Connection')
    connectWindow.resizable(0,0)

    hostnameLabel=Label(connectWindow,text='Host Name',font=('arial',18))
    hostnameLabel.grid(row=0,column=0,padx=20)
    hostEntry=Entry(connectWindow,font=('Courier',16),bd=2)
    hostEntry.grid(row=0,column=1,padx=40,pady=20)

    UsernameLabel = Label(connectWindow, text='User Name', font=('arial', 18))
    UsernameLabel.grid(row=1, column=0, padx=20)
    UserEntry = Entry(connectWindow, font=('Courier', 16), bd=2)
    UserEntry.grid(row=1, column=1, padx=40, pady=20)

    passwordLabel = Label(connectWindow, text='Password', font=('arial', 18))
    passwordLabel.grid(row=2, column=0, padx=20)
    passwordEntry = Entry(connectWindow, font=('Courier', 16), bd=2)
    passwordEntry.grid(row=2, column=1, padx=40, pady=20)

    connectButton=ttk.Button(connectWindow,text='CONNECT', command=connect)
    connectButton.grid(row=3,columnspan=2)

count=0
text=''
def slider():
    global text,count
    if count==len(s):
        count=0
        text=""
    text=text+s[count]
    sliderLable.config(text=text)
    count+=1
    sliderLable.after(90, slider)
def clock():
    global date,currenttime
    date=time.strftime('%d/%m/%Y')
    currenttime=time.strftime('%H:%M:%S')
    datetimeLabel.config(text=f'  Date:{date}\nTime:{currenttime}')
    datetimeLabel.after(1000,clock)
#GUI Part
root=ttkthemes.ThemedTk()
root.get_themes()
root.set_theme('radiance')
root.geometry('1174x720+50+0')
root.title('Student Management System')

datetimeLabel=Label(root,font=('Courier',15))
datetimeLabel.place(x=5,y=5)
clock()
s='STUDENT MANAGEMENT SYSTEM'
sliderLable = Label(root,text=s,font=('Candara Light',32),width=30)
sliderLable.place(x=215,y=0)
slider()

connectButton=ttk.Button(root, text='Connect Database', command=connect_database)
connectButton.place(x=1000, y=0)

leftFrame=Frame(root)
leftFrame.place(x=50,y=80,width=300,height=600)

logo_image=PhotoImage(file='student.png')
logo_Label=Label(leftFrame,image=logo_image)
logo_Label.grid(row=0,column=0)

addstudentButton=ttk.Button(leftFrame,text='Add Student',width=25,state=DISABLED,command=add_student)
addstudentButton.grid(row=1,column=0,pady=20)

searchstudentButton=ttk.Button(leftFrame,text='Search Student',width=25,state=DISABLED,command=search_student)
searchstudentButton.grid(row=2,column=0,pady=20)

deletestudentButton=ttk.Button(leftFrame,text='Delete Student',width=25,state=DISABLED,command=delete_student)
deletestudentButton.grid(row=3,column=0,pady=20)

updatestudentButton=ttk.Button(leftFrame,text='Update Student',width=25,state=DISABLED,command=update_student)
updatestudentButton.grid(row=4,column=0,pady=20)

showstudentButton=ttk.Button(leftFrame,text='Show Student',width=25,state=DISABLED,command=show_student)
showstudentButton.grid(row=5,column=0,pady=20)

exportstudentButton=ttk.Button(leftFrame,text='Export Student',width=25,state=DISABLED)
exportstudentButton.grid(row=6,column=0,pady=20)

exitButton=ttk.Button(leftFrame,text='Exit',width=25,state=DISABLED)
exitButton.grid(row=7,column=0,pady=20)

rightFrame=Frame(root)
rightFrame.place(x=350,y=80,width=820,height=600)

scrollBarX=Scrollbar(rightFrame,orient=HORIZONTAL)
scrollBarY=Scrollbar(rightFrame,orient=VERTICAL)

studentTable=ttk.Treeview(rightFrame,columns=('Id','Name','Mobile No','Email Address','Address','Gender','D.O.B','Added Date','Added Time')
                          ,xscrollcommand=scrollBarX.set,yscrollcommand=scrollBarY.set)
scrollBarX.config(command=studentTable.xview)
scrollBarY.config(command=studentTable.yview)
scrollBarX.pack(side=BOTTOM,fill=X)
scrollBarY.pack(side=RIGHT,fill=Y)

studentTable.pack(fill=BOTH,expand=1)

studentTable.heading('Id',text='ID')
studentTable.heading('Name',text='Name')
studentTable.heading('Mobile No',text='Mobile No')
studentTable.heading('Email Address',text='Email Address')
studentTable.heading('Address',text='Address')
studentTable.heading('Gender',text='Gender')
studentTable.heading('D.O.B',text='D.O.B')
studentTable.heading('Added Date',text='Added Date')
studentTable.heading('Added Time',text='Added Time')

studentTable.column('Id',width=50,anchor=CENTER)
studentTable.column('Name',width=200,anchor=CENTER)
studentTable.column('Email Address',width=200,anchor=CENTER)
studentTable.column('Mobile No',width=200,anchor=CENTER)
studentTable.column('Address',width=100,anchor=CENTER)
studentTable.column('Gender',width=100,anchor=CENTER)
studentTable.column('D.O.B',width=100,anchor=CENTER)
studentTable.column('Added Date',width=150,anchor=CENTER)
studentTable.column('Added Time',width=150,anchor=CENTER)
style=ttk.Style()
style.configure('Treeview',rowheight=40,font=('arial',13))
style.configure('Treeview.Heading',font=('arial',13),foreground='red4')

studentTable.config(show='headings')

root.mainloop()