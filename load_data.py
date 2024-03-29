import pandas as pd

class read_data():
    #Read question and rule file
    def __init__(self,filepath_welcome_message,filepath_rules,filepath_questions):
        # Save the paths
        self.filepath_welcome_message = filepath_welcome_message
        self.filepath_rules = filepath_rules
        self.filepath_questions = filepath_questions

        # Initialize the class variables
        self.welcome = None
        self.rules = None
        self.questions = None
        self.player = None

        # Initialize the question parameters
        self.question_row = None
        self.current_question = None
        self.category = None
        self.options = None
        self.answer = None

    # Read predefined welcome message from txt file
    def load_welcome_message(self):
        with open(self.filepath_welcome_message, 'r') as file:
            self.welcome = file.read()

    # Load question data set
    def load_questions(self):
        with open(self.filepath_rules, 'r') as file:
            self.rules = file.read()

    # Load rules from the txt file
    def load_rules(self):
        self.questions = pd.read_csv(self.filepath_questions,sep=",")

    # Print out welcome message on the screen
    def get_welcome_screen(self):
        print(self.welcome)

    # Get username from the player
    def get_username(self):
        self.player = str(input("Please enter your name: "))
        print(f"Welcome {self.player}. This is the Quiz game.")

    # Print out the rules on the screen
    def get_rules(self):
        print(f"Rules... are just simple {self.player}")
        print(self.rules)
