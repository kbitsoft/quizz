from tkinter import *
from tkinter import messagebox
import mysql.connector
import hashlib#encrypt password
import subprocess #to open another process
    
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
    # Hash the password using SHA256
    password = hashlib.sha256(password.encode()).hexdigest()
    # execute query to retrieve user info from database
    query = "SELECT * FROM users WHERE username=%s and password=%s"
    cursor.execute(query, (username,password))
    user = cursor.fetchone()
    

    if user is not None:
         # check the role of the user
        if user[2] == 'student':
            # redirect to quizv2.3.py
            root.destroy() # close the login window
            subprocess.Popen(["python", "quizv2.3.py"])# import and run the quizv2.3 module
        elif user[2] == 'admin':
            # redirect to fileupload.py
            root.destroy() # close the login window
            subprocess.Popen(["python", "admin_dash_board.py"]) # import and run the fileupload module
    else:
        result_label.config(text="Invalid username or password")
    
Button(frame,width=39,pady=7,text='Log In', command=login, bg='#57a1f8',fg='white',border=0).place(x=35,y=204)

root.mainloop()
