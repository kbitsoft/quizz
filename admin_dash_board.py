from tkinter import *
from tkinter import ttk
import mysql.connector
import subprocess #to open another process

root = Tk()
root.title("Quiz Master")
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)

img = PhotoImage(file='dashboard.png')
Label(root, image=img, bg='white').place(x=50, y=50)

frame = Frame(root, width=700, height=350, bg="")
frame.place(x=30, y=5)

heading = Label(frame, text='Admin Dashboard', fg='#57a1f8', bg='white', font=('Tahoma',23,'bold'))
heading.place(x=180, y=2)


# function to add new user into database
def add_user():
 subprocess.Popen(["python", ""]) 

# function to update user information
def update_user():
 subprocess.Popen(["python", "admin_user_edit.py"]) 

# function to delete user information
def delete_user():
 subprocess.Popen(["python", "admin_user_delete.py"])     

# function to enroll user for MCQ
def enroll_user():
 subprocess.Popen(["python", "admin_user_enroll.py"])    

# function to get user result
def get_result():
 subprocess.Popen(["python", "admin_user_result.py"])     
       
Button(frame,width=39,pady=7,text='Add Users', command=add_user, bg='#57a1f8',fg='white',border=0).place(x=180,y=50)
Button(frame,width=39,pady=7,text='Update Users', command=update_user, bg='#57a1f8',fg='white',border=0).place(x=180,y=90)
Button(frame,width=39,pady=7,text='Delete Users', command=delete_user, bg='#57a1f8',fg='white',border=0).place(x=180,y=130)
Button(frame,width=39,pady=7,text='Enroll Users', command=enroll_user, bg='#57a1f8',fg='white',border=0).place(x=180,y=170)
Button(frame,width=39,pady=7,text='User\'s Results', command=get_result, bg='#57a1f8',fg='white',border=0).place(x=180,y=210)
root.mainloop()
