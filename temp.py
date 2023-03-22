from tkinter import *

root = Tk()
root.geometry('925x500+300+200')

canvas = Canvas(root, width=700, height=350, highlightthickness=0)
canvas.place(x=30, y=5)

# create a transparent rectangle on the canvas
canvas.create_rectangle(0, 0, 700, 350, fill="#00000000", outline="")

heading = Label(canvas, text='Admin Dashboard', fg='#57a1f8', bg='white', font=('Tahoma',23,'bold'))
heading.place(x=180, y=2)

img = PhotoImage(file='dashboard.png')
Label(root, image=img, bg='white').place(x=50, y=50)

root.mainloop()
