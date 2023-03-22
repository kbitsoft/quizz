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

heading=Label(frame,text='Edit Users', fg='#57a1f8',bg='white',font=('Tahoma',23,'bold'))
heading.place(x=100,y=5)
#--------------------------


#---------------------------
user = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Tahoma',11))
user.place(x=30,y=80)
user.insert(0,'Full Name')

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)
#---------------------------
# Define the options for the usertype dropdown
usertype_options = ["admin", "student"]

# Create a StringVar to hold the selected usertype
selected_usertype = StringVar()

# Set the initial value of the StringVar to the first option
selected_usertype.set(usertype_options[1])

# Create the usertype dropdown
usertype_dropdown = OptionMenu(frame, selected_usertype, *usertype_options)
usertype_dropdown.config(width=32,fg='black',border=0,bg="white",font=('Tahoma',11))
usertype_dropdown['menu'].config(bg='white', font=('Tahoma', 11), border=0)
usertype_dropdown.place(x=27, y=150)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)
#-----------------------------
Entry1 = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Tahoma',11))
Entry1.place(x=30,y=220)
Entry1.insert(0,'Username')

Frame(frame,width=295,height=2,bg='black').place(x=25,y=247)
#-----------------------------------------------------
Entry2 = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Tahoma',11))
Entry2.place(x=30,y=290)
Entry2.insert(0,'Password')

Frame(frame,width=295,height=2,bg='black').place(x=25,y=317)



def update_user():
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
    password = code.get()
    role = usertype.get()

    # update user information in database
    query = "UPDATE users SET password=%s, role=%s WHERE username=%s"
    values = (password, role, username)
    cursor.execute(query, values)
    db.commit()

    # display success message
    result_label.config(text="User information updated successfully")
root.mainloop()
