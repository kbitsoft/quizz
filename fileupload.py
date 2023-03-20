import os
import shutil

from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("File Upload GUI")
root.geometry("400x200")
root.resizable(False, False)

def upload():
    file_path = filedialog.askopenfilename()
    destination_path = os.path.join(os.path.dirname(__file__)+"/librarry/", os.path.basename(file_path),)
    shutil.copyfile(file_path, destination_path)
    print("File uploaded to:", destination_path)

label1=Label(root,text="Upload your mcq file here:")
label1.pack()
upload_btn = Button(root, text="Upload File", command=upload)
upload_btn.pack(pady=20)

root.mainloop()

