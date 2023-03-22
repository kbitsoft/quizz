from tkinter import *
from tkinter import filedialog
import os
import json

class FileUpload(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Quiz Master")
        self.master.geometry("800x500")
        self.master.config(bg="#f2f2f2")
        self.pack(expand=True, fill=BOTH)
        self.create_widgets()

    def create_widgets(self):
        self.title = Label(self, text="MCQ Uploading", width=800, bg="#2c3e50", fg="white", font=("arial", 20, "bold"))
        self.title.pack(fill=X)
        self.file_label = Label(self, text="Choose File to Upload:", font=("arial", 12), bg="#f2f2f2")
        self.file_label.pack(pady=20)
        self.upload_button = Button(self, text="Upload File", command=self.upload_file, font=("arial", 12), bg="#2c3e50", fg="white", width=20, height=2)
        self.upload_button.pack(pady=10)
        self.quit_button = Button(self, text="Quit", command=self.master.destroy, font=("arial", 12), bg="red", fg="white", width=20, height=2)
        self.quit_button.pack(pady=10)
        self.status_bar = Label(self, text="", font=("arial", 12), bg="#f2f2f2", fg="green")
        self.status_bar.pack(pady=20)

    def upload_file(self):
        filepath = filedialog.askopenfilename()
        if not filepath:
            return
        filename = os.path.basename(filepath)
        self.status_bar.config(text="Uploading file...", fg="green")
        self.master.update()
        # Check for duplicate file name
        if self.check_duplicate_file(filename):
            # Show error message
            self.status_bar.config(text="Error: File already exists!", fg="red")
            return
        # Check json structure
        if not self.check_quiz_file(filepath):
            # Show error message
            self.status_bar.config(text="Error: File format is not correct!", fg="red")
            return
        # If file is not a duplicate, continue with upload
        with open(filepath, "rb") as f:
            data = f.read()
        with open(f"library/{filename}", "wb") as f:
            f.write(data)
        # Show success message
        self.status_bar.config(text="File uploaded successfully!", fg="green")

    def check_duplicate_file(self, filename):
        """Check if the uploaded file already exists in the library."""
        if os.path.exists("library/" + filename):
            return True
        return False
    

    def check_quiz_file(self, filepath):
        print("Check file extension")
        if not filepath.endswith(".json"):
            return False
        # Load JSON data from file
        try:
            with open(filepath, "r") as f:
                data = json.load(f)
        except json.JSONDecodeError:
            return False
        # Check data structure
        if "quiz" not in data or "name" not in data["quiz"] or "questions" not in data["quiz"]:
            return False
        for question in data["quiz"]["questions"]:
            if "question" not in question or "options" not in question or "answer" not in question:
                return



if __name__ == "__main__":
    root = Tk()
    app = FileUpload(master=root)
    app.mainloop()

