# Your name: Mohymin Islam
# Your student id: 88068007
# Your email: mohymini@umich.edu
# List of who or what you worked with on this homework: No one
# If you used Generative AI, say that you used it and also how you used it.


## Import any necessary modules
import random

## Define class

    ## define the __init__ method
    # def __init__(self, answers):
    #     pass
        

    ## define the __str__ method
    # def __str__(self):
    #    pass

    ## define get_fortune method
    

    ## define play_game method
    

    ## define print_answer_frequencies method
class MagicEightBall:
    def __init__(self, answers):
        self.answers = answers
        self.previous_questions = []
        self.previous_answers = []
    
    def __str__(self):
        if (self.previous_questions.len() == 0):
            return ""
        else:
            return ""
    


    def get_fortune(self, question):
        if question in self.previous_questions:
            return "I've already answered this question"
        else:
            random_ans = random.randint(0, self.answers.len()) # get a random index
            self.previous_answers.append(random_ans) # add the answer index to previous answers
            return self.answers[random_ans] # return random index


        return
    
    def play_game(self):
        user_question = input("Please enter a question: ")
        while (user_question != "done"):
            fortune = self.get_fortune(user_question)
            print(fortune)
            self.previous_questions.append(user_question)
            user_question = input("Please enter the next question:")
            if (user_question == "done"):
                print("Goodbye")
                break

        return


    def print_answer_frequencies(self):
        if (self.previous_answers.len() == 0):
            print("I have not told your fortune yet")
            return
        else:
            for i in range(0, self.answers.len()):
                print("The answer '" + str(self.answers[i]) + "’ has been given ", end="")
                print(str(self.previous_answers.count(i)) + " times")
        return

# Main function
def main():
    # 1. Define the possible answers into a list: 
    # 2. Create a MagicEightBall object
    # 3. Print the MagicEightBall object 
    # 4. Initiate the game play using the play_game() method
    # 5. Call print_answer_frequencies()
    # 6. Print the MagicEightBall object 

    

    return



# Run the main function if the file is executed directly
if __name__ == "__main__":
    main()
   