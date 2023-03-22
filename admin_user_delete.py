root = Tk()
root.title('Quiz Master')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)

img = PhotoImage(file='sign.png')
Label(root,image=img,bg='white').place(x=50,y=50)

frame = Frame(root,width=350,height=370,bg="white")
frame.place(x=480,y=70)

heading=Label(frame,text='Delete Users', fg='#57a1f8',bg='white',font=('Tahoma',23,'bold'))
heading.place(x=100,y=5)
#--------------------------




#--------------------------
def delete_user():
    # establish connection to database
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="digi_school"
    )
    cursor = db.cursor()

    # get username from entry
    username = uname.get()

    # delete user from database
    query = "DELETE FROM users WHERE username=%s"
    cursor.execute(query, (username,))
    db.commit()

    # display success message
    result_label.config(text="User deleted successfully")
