# i deepak chander sharma certify that this is my work and i havent allowed any body to copy my content.
# Import the file_input function from a file named file_input.py
from file_input import file_input

def load_FAQ_data():
    """
    This function will help me to  loads questions and answers from files and returns them as lists.

    Returns:
    questions (list):it will showcase a list of questions.
    answers (list):it will show  a list of corresponding answers.
    """
    # Load questions from "questions.txt" file
    questions = file_input("questions.txt")
    # Load answers from "answers.txt" file
    answers = file_input("answers.txt")
    return questions, answers

def understand(utterance, questions):
    """
    This function will check which content of user match the question

    Args:
    utterance (str): The user's input utterance.
    questions (list): A list of questions available in text to compare with the input

    Returns:
    int:will return the index value of question i  the file if it doesnot matches it will show -1
    """
    try:
        # Converting  the utterance to lowercase and find its index in the questions list
        return questions.index(utterance.lower())
    except ValueError:
        # If no match is found, return -1
        return -1

def generate(intent, answers):
    """
    This functionwill basically  provide  a response based on the user's intent.

    Args:
    intent (int):the index of the question matched to the content
    answers (list): A list of relevant answers.

    Returns:
    str: An appropriate response based on the user's intent.
    """
    if intent == -1:
        # If no intent was matched, return a default response
        return "Sorry, I don't know the answer to that!"
    # Return the corresponding answer based on the intent
    return answers[intent]

def main():
    """
    This function will help to implements a chat session in the shell.

    """
    #it will  Load questions and answers from files
    questions, answers = load_FAQ_data()
    print("Hello! I know stuff about chat bots. When you're done talking, just say 'goodbye'.")

    while True:
        utterance = input(">>> ").strip()
        if utterance.lower() == "goodbye":
            print("Goodbye! Have a great day!")
            break

        # it checka  the user's intent based on their input
        intent = understand(utterance, questions)
        # provide a relevanmt answer  based on the user's intent
        response = generate(intent, answers)
        # Print the response to the user
        print(response)

if __name__ == "__main__":
    # Run the main function
    main()
