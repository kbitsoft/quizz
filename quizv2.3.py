from tkinter import *
from tkinter import messagebox as mb
import json

class Mcq:
    def __init__ (self):
        self.num_of_q = len(questions)
        self.q_no = 0
        self.opt_correct = 0
        self.set_title()
        self.display_question()
        self.opt_selected = IntVar() # Holds integer value that can pass to GUi widget
        self.opts = self.radio_buttons()
        self.display_options()
        self.navigation()

    def set_title(self):
        title = Label(gui, text=quiz_name, width=50, bg="blue", fg="white", font=("ariel",20,"bold"))
        title.place(x=0,y=2)

    def display_question(self):
        qu = Label(gui, text=questions[self.q_no]['question'], width=60, font=('ariel',16,'bold'), anchor='w')
        qu.place(x=70,y=100)
                
    def radio_buttons(self):
        q_container = []
        disp_pos_y = 150
        while len(q_container) < 4:
            radio_btn = Radiobutton(gui, text="", variable=self.opt_selected, value=len(q_container)+1, font=('ariel',14))
            q_container.append(radio_btn)
            radio_btn.place(x=100, y=disp_pos_y)
            disp_pos_y += 40
        return q_container

    def display_options(self):
        self.opt_selected.set(respons[self.q_no])
        for radio_btn, option in zip(self.opts, questions[self.q_no]['options']):
            radio_btn['text'] = option


    def navigation(self):
        next_button = Button(gui, text="Next", command=self.next_click, width=5, bg="black", fg="white", font=("ariel",16,"bold"))
        next_button.place(x=450, y=380)
        back_button = Button(gui, text="Back", command=self.back_click, width=5, bg="black", fg="white", font=("ariel",16,"bold"))
        back_button.place(x=100, y=380)
        close_button = Button(gui, text="Close", command=gui.destroy, width=5, bg="black", fg="white", font=("ariel",16,"bold"))
        close_button.place(x=600, y=50)
                        
    def next_click(self):
        self.check_ans(self.q_no)     
        self.q_no += 1
        if self.q_no == self.num_of_q:
            self.summery_result()
            gui.destroy()
        else:
            self.display_question()
            self.display_options()

    def back_click(self):
        self.check_ans(self.q_no)
        self.q_no -= 1
        self.display_question()
        self.display_options()
                
    def check_ans(self, q_no):
        respons[q_no] = self.opt_selected.get()
        if self.opt_selected.get() == questions[q_no]['answer']:
            mark[q_no] = True
        else:
            mark[q_no] = False
        print(respons)
                        
    def summery_result(self):
        correct_count = mark.count(True)
        correct = f"Correct: {correct_count}"
        wrong_count = self.num_of_q - correct_count
        wrong = f"Wrong: {wrong_count}"
        score = int(correct_count / self.num_of_q * 100)
        result = f"Score: {score}%\n{correct}\n{wrong}"
        

        # show marks for each question
        marks_display = ""
        for i in range(self.num_of_q):
            question = f"{i+1}. {questions[i]['question']}\n"
            options = questions[i]['options']
            response = f"Response: {respons[i]}\n"
            correct = "Correct" if mark[i] else "Wrong"
            options_display = ""
            for j in range(len(options)):
                option_num = j+1
                option = options[j]
                mark_display = ""
                if respons[i] == option_num:
                    mark_display = "X" if mark[i] == False else "✓"
                options_display += f"({option_num}) {option} {mark_display}\n"
            marks_display += f"{question}{options_display}{response}{correct}\n\n"
            marks_display += "Result:"+result
        mb.showinfo("Marks", marks_display)




gui = Tk()
gui.geometry("800x450")
gui.title("Quiz Master")

try:
    with open('library/html quiz.json') as f:
        data = json.load(f)
except Exception as e:
    print(f"Error loading data from JSON file: {e}")
    
questions = data["quiz"]["questions"]
num_of_q = len(questions)
q_no = 0
mark = [0 for i in questions]
respons = [0 for i in questions]
quiz_name=data["quiz"]["name"]
mcq = Mcq()
gui.mainloop()
