import customtkinter as ctk 
from tkinter import messagebox

class FlashcardApp:
    def __init__(self, root):
        self.master = {}
        self.root = root
        self.root.title("Flashcard App")
        self.root.geometry("500x400")
        
        self.mode = ctk.StringVar(value="add")

        self.create_widgets()

    def create_widgets(self):
        # Create frame for add flashcard
        self.add_frame = ctk.CTkFrame(self.root)
        self.add_frame.pack(pady=20)

        self.question_label = ctk.CTkLabel(self.add_frame, text="Enter the question:")
        self.question_label.pack(pady=5)
        self.question_entry = ctk.CTkEntry(self.add_frame, width=400)
        self.question_entry.pack(pady=5)

        self.answer_label = ctk.CTkLabel(self.add_frame, text="Enter the answer:")
        self.answer_label.pack(pady=5)
        self.answer_entry = ctk.CTkEntry(self.add_frame, width=400)
        self.answer_entry.pack(pady=5)

        self.add_button = ctk.CTkButton(self.add_frame, text="Add Flashcard", command=self.add_flashcard)
        self.add_button.pack(pady=10)

        # Create frame for quiz
        self.quiz_frame = ctk.CTkFrame(self.root)
        self.quiz_frame.pack(pady=20)

        self.question_display = ctk.CTkLabel(self.quiz_frame, text="", width=400)
        self.question_display.pack(pady=5)
        
        self.answer_entry_quiz = ctk.CTkEntry(self.quiz_frame, width=400)
        self.answer_entry_quiz.pack(pady=5)

        self.submit_button = ctk.CTkButton(self.quiz_frame, text="Submit Answer", command=self.check_answer)
        self.submit_button.pack(pady=10)

        self.result_label = ctk.CTkLabel(self.quiz_frame, text="")
        self.result_label.pack(pady=10)

        # Navigation buttons
        self.switch_button = ctk.CTkButton(self.root, text="Switch to Quiz Mode", command=self.switch_mode)
        self.switch_button.pack(pady=10)

        self.update_mode()

    def update_mode(self):
        if self.mode.get() == "add":
            self.add_frame.pack(pady=20)
            self.quiz_frame.pack_forget()
            self.switch_button.configure(text="Switch to Quiz Mode")
        else:
            self.add_frame.pack_forget()
            self.quiz_frame.pack(pady=20)
            self.switch_button.configure(text="Switch to Add Mode")
            self.start_quiz()

    def switch_mode(self):
        if self.mode.get() == "add":
            self.mode.set("quiz")
        else:
            self.mode.set("add")
        self.update_mode()

    def add_flashcard(self):
        question = self.question_entry.get().strip()
        answer = self.answer_entry.get().strip()
        if question and answer:
            self.master[question] = answer
            messagebox.showinfo("Success", "Flashcard added successfully!")
            self.question_entry.delete(0, 'end')
            self.answer_entry.delete(0, 'end')
        else:
            messagebox.showerror("Error", "Both fields are required!")

    def start_quiz(self):
        self.current_question_index = 0
        self.correct_answers = 0
        self.total_questions = len(self.master)
        self.questions = list(self.master.keys())
        self.next_question()

    def next_question(self):
        if self.current_question_index < self.total_questions:
            self.current_question = self.questions[self.current_question_index]
            self.question_display.configure(text=self.current_question)
            self.answer_entry_quiz.delete(0, 'end')
            self.current_question_index += 1
        else:
            self.display_results()

    def check_answer(self):
        user_answer = self.answer_entry_quiz.get().strip()
        correct_answer = self.master.get(self.current_question, "")
        if user_answer == correct_answer:
            self.correct_answers += 1
        self.next_question()

    def display_results(self):
        accuracy = (self.correct_answers / self.total_questions) * 100
        self.result_label.configure(text=f"QUIZ COMPLETED \nRESULT:\nThe accuracy is {accuracy:.2f}%")
        self.question_display.configure(text="")
        self.answer_entry_quiz.pack_forget()
        self.submit_button.pack_forget()

if __name__ == "__main__":
    root = ctk.CTk()
    app = FlashcardApp(root)
    root.mainloop()