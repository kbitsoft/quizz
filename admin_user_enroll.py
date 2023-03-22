from tkinter import *
from tkinter import messagebox
import mysql.connector
import hashlib

root = Tk()
root.title('Quiz Master')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)

img = PhotoImage(file='sign.png')
Label(root,image=img,bg='white').place(x=50,y=50)

frame = Frame(root,width=350,height=370,bg="white")
frame.place(x=480,y=70)

heading=Label(frame,text='Enroll Student', fg='#57a1f8',bg='white',font=('Tahoma',23,'bold'))
heading.place(x=100,y=5)
#--------------------------




#--------------------------

def enroll_user():
    # establish connection to database
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="digi_school"
    )
    cursor = db.cursor()

    # get user details from entries
    username = uname.get()
    mcq_id = mcq.get()

    # enroll user for MCQ in database
    query = "INSERT INTO mcq_enrollment (username, mcq_id) VALUES (%s, %s)"
    values = (username, mcq_id)
    cursor.execute(query, values)
    db.commit()

    # display success message
    result_label.config(text="User enrolled successfully")
root.mainloop()
