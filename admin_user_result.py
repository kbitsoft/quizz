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

heading=Label(frame,text='Student Result', fg='#57a1f8',bg='white',font=('Tahoma',23,'bold'))
heading.place(x=100,y=5)
#--------------------------


#---------------------------




def get_result():
    # get the username from entry
    username = uname.get()
    # establish connection to database
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="digi_school"
    )
    cursor = db.cursor()
    # execute query to get the result of the user
    query = "SELECT score FROM quiz WHERE username=%s"
    cursor.execute(query, (username,))
    result = cursor.fetchone()
    # update the result label with the user's score
    if result:
        result_label.config(text=f"User {username} scored {result[0]} points")
    else:
        result_label.config(text=f"No results found for user {username}")
		
root.mainloop()
