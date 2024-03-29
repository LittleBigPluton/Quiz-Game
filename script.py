import load_data as ld
import random

class play_game(ld.read_data):

    # Randomly choose questions to the game
    def set_question_parameters(self):
        question_number = random.randint(1,self.questions.shape[0]-1)
        self.question_row = self.questions.iloc[question_number]
        self.current_question = self.question_row["Question"]
        self.category = self.question_row["Category"]
        self.options ={
            "A": self.question_row["Option A"],
            "B": self.question_row["Option B"],
            "C": self.question_row["Option C"],
            "D": self.question_row["Option D"]
        }
        self.answer = self.question_row["Answer"]

    def get_options(self):
        for option, value in self.options.items():
            print(f"{option}) {value}")


    def get_question(self):
        print(f"Category: {self.category}")
        print(f"Question: {self.current_question}")

    def get_answer(self):
        print(f"Answer: {self.answer}")

    def check_answer(self,user_option):
        try:
            user_option = user_option.upper()
            if self.options[user_option] == self.answer:
                print("Correct")
                return True
            else:
                print("Wrong")
                print(f"The correct answer is {self.answer}")
                return False
        except KeyError:
            print("Invalid option. Please try again.")
            return None
