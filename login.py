from tkinter import *
from tkinter import messagebox
import mysql.connector


    
root = Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)

img = PhotoImage(file='login.png')
Label(root,image=img,bg='white').place(x=50,y=50)

frame = Frame(root,width=350,height=350,bg="white")
frame.place(x=480,y=70)

heading=Label(frame,text='Log in', fg='#57a1f8',bg='white',font=('Tahoma',23,'bold'))
heading.place(x=100,y=5)
#---------------------------
uname = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Tahoma',11))
uname.place(x=30,y=80)
uname.insert(0,'Username')

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)
#---------------------------
code = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Tahoma',11))
code.place(x=30,y=150)
code.insert(0,'Password')

Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)
# Result label
result_label = Label(frame, text="",fg="Orange",font=('Tahoma',11))
result_label.place(x=30,y=250)

def login():
    # establish connection to database
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="digi_school"
    )
    cursor = db.cursor()

    # get username and password from entries
    username = uname.get()
    password = code.get()

    # execute query to retrieve user info from database
    query = "SELECT * FROM users WHERE username=%s"
    cursor.execute(query, (username,))
    user = cursor.fetchone()

    if user is not None and user[3] == password:
        result_label.config(text="Login successful!")
    else:
        result_label.config(text="Invalid username or password")

    # close database connection
    db.close()
    
Button(frame,width=39,pady=7,text='Log In', command=login, bg='#57a1f8',fg='white',border=0).place(x=35,y=204)

root=mainloop()
