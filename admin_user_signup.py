from tkinter import *
from tkinter import messagebox
import mysql.connector
import hashlib

root = Tk()
root.title("Quiz Master")
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)

img = PhotoImage(file='sign.png')
Label(root,image=img,bg='white').place(x=50,y=50)

frame = Frame(root,width=350,height=370,bg="white")
frame.place(x=480,y=70)

heading=Label(frame,text='Sign Up', fg='#57a1f8',bg='white',font=('Tahoma',23,'bold'))
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




# Connect to the database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="digi_school"
)
# Define a function to insert the data to the database
def register():
    fullname = user.get()
    usertype = selected_usertype.get()
    username = Entry1.get()
    password = Entry2.get()
    # Hash the password using SHA256
    password = hashlib.sha256(password.encode()).hexdigest()
    # Check if the username already exists in the database
    cursor = mydb.cursor()
    cursor.execute("SELECT username FROM users WHERE username = %s", (username,))
    result = cursor.fetchone()
    if result is not None:
        # Show an error message if the username already exists
        messagebox.showerror('Error', 'Username already exists!')
        return
    # Prepare the SQL query
    sql = "INSERT INTO users (fullname, usertype, username, password) VALUES (%s, %s, %s, %s)"
    values = (fullname, usertype, username, password)
    
    # Execute the query
    cursor.execute(sql, values)
    mydb.commit()
    
    # Show a message box to inform the user
    messagebox.showinfo('Success', 'Data inserted successfully!')
    
Button(frame,width=39,pady=7,text='Register', bg='#57a1f8',fg='white',border=0, command=register).place(x=35,y=334)
root=mainloop()
