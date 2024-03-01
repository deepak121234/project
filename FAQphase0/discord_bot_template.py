 # i deepak chander sharma certify that this is my work and i havent allowed any body to copy my content.
 # first i will import discord
import discord

class FAQBot(discord.Client):
    def __init__(self, question_file, answer_file):
        """
        it will basically initialize the FAQBot.

        Args:
        question_file (str):it is path to question file
        answer_file (str): it is a pth to answer file
        """
        # it will Configure Discord intents for figuring out the messages
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(intents=intents)

        # it will load questions and answers from provided text files
        self.questions, self.answers = self.load_faq_data(question_file, answer_file)

    def load_faq_data(self, questions_file, answers_file):
        """
        it will load questions and answers from text files.

        Args:
        questions_file (str): provide file path to the questions file.
        answers_file (str): it provides path to the answers file.

        Returns:
        questions (list): A list of questions (in lowercase).
        answers (list): A list of corresponding answers.
        """
        # Open and read the questions and answers from the provided files
        with open(questions_file, 'r') as qf, open(answers_file, 'r') as af:
             # Store questions as lowercase
            questions = [line.strip().lower() for line in qf.readlines()]
            answers = [line.strip() for line in af.readlines()]
        return questions, answers

    def find_answer(self, user_message):
        """
        it will find an answer based on the user's message.

        Args:
        user_message (str): what user typed data

        Returns:
        response (str): The bot's will reply according on the user's data inserted
        """
        # Normalize and clean the user's message for comparison (lowercase and strip)
        user_message = user_message.lower().strip()

        # Iterate through the questions and answers to find a match
        for question, answer in zip(self.questions, self.answers):
            if user_message in question:
                return answer

        # If no matching question is found, provide a default response
        return "Sorry, I don't have an answer for that."

    async def on_ready(self):
        """
        this is Event handler for when the bot is log in.
        """
        # Print a message to the console when the bot is logged in and ready
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        """
        Event handler for when a message is received from user end

        Args:
        message (discord.Message): The received message.
        """
        if message.author == self.user:
            return  # Ignore messages from the bot itself

        # Handle specific greetings
        if message.content.lower() in ["hello", "hi"]:
            await message.channel.send("Hello! I'm an FAQ bot. Ask me a question!")
        elif message.content.lower() in ["goodbye", "bye"]:
            await message.channel.send("Goodbye! Have a nice day!")
        else:
            # For other messages, try to find a relevant answer
            response = self.find_answer(message.content)
            await message.channel.send(response)

# File paths to questions, answers, and bot token
question_file = "questions.txt"
answer_file = "answers.txt"

# Set up and log in the FAQBot using the bot's token
client = FAQBot(question_file, answer_file)
with open("bot_token.txt") as file:
    token = file.read().strip()

client.run(token)
