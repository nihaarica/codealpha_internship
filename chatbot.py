import random

# Define some conversation patterns and responses
patterns = {
    'hi|hello|hey': ['Hello!', 'Hi there!', 'Hey!'],
    'how are you?': ['I am doing well, thank you!', 'I\'m good, thanks for asking.'],
    'what\'?s your name?': ['I am a chatbot.', 'My name is Chatbot.'],
    'what can you do?': ['I can have conversations with you.', 'I can answer your questions.'],
    'who are you?': ['I am a chatbot designed to assist you.', 'I\'m your friendly chatbot.'],
    'what time is it?': ['I do not have access to real-time information.', 'I cannot provide the current time.'],
    'how old are you?': ['I do not age, as I am a program.', 'Age is just a number for me.'],
    'where are you from?': ['I exist in the digital world.', 'I don\'t have a physical location.'],
    'thank you': ['You\'re welcome!', 'No problem.', 'Anytime!'],
    'good morning': ['Good morning!', 'Morning!', 'Hello!'],
    'good afternoon': ['Good afternoon!', 'Afternoon!', 'Hello!'],
    'good evening': ['Good evening!', 'Evening!', 'Hello!'],
    'how\'s it going?': ['It\'s going well, thank you!', 'Everything\'s good, thanks.'],
    'what\'s up?': ['Not much, just chatting with you!', 'Just here, ready to help.'],
    'tell me a joke': ['Why don\'t scientists trust atoms? Because they make up everything!', 
                       'Did you hear about the mathematician who’s afraid of negative numbers? He’ll stop at nothing to avoid them.'],
    'how was your day?': ['It was good, thanks for asking!', 'It was productive, thank you.'],
    'have a good day': ['You too!', 'Thanks, you too.'],
    'how\'s the weather?': ['I cannot provide real-time weather updates.', 'You might want to check a weather website for that.'],
    'do you have any hobbies?': ['My hobby is chatting with users like you!', 'I enjoy helping users like you.'],
    'what are your interests?': ['I am interested in technology and helping users.', 'I enjoy learning and interacting with users.'],
    'how can I help you?': ['You can ask me questions or chat about anything you like.', 'Feel free to tell me what you need assistance with.'],
    'do you dream?': ['I am not capable of dreaming, as I am a computer program.', 'Dreaming is not within my capabilities.'],
    'where do you live?': ['I exist in the digital realm.', 'I don\'t have a physical address.'],
    'what\'s your favorite color?': ['I don\'t have preferences like humans do.', 'I don\'t have the ability to perceive colors.'],
    'what\'s your favorite food?': ['I don\'t eat, as I am a program.', 'I don\'t have the capability to taste food.'],
    'are you a robot?': ['I am a chatbot, which is a type of program.', 'I am a virtual assistant designed to help users.'],
    'do you sleep?': ['I don\'t sleep, as I am a computer program.', 'Sleep is not necessary for me.'],
    'can you learn?': ['I am constantly learning from interactions with users.', 'Yes, I can adapt and improve over time.'],
    'are you human?': ['No, I am a chatbot programmed to assist users.', 'I am a virtual assistant, not a human.'],
    'what\'s the meaning of life?': ['The meaning of life is subjective and varies from person to person.', 'That\'s a profound question!'],
}
def chatbot_respond(user_input):
    for pattern, responses in patterns.items():
        if user_input.lower() in pattern:
            return random.choice(responses)
    return "I'm sorry, I don't understand."

def run_chatbot():
    print("Welcome to the chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        response = chatbot_respond(user_input)
        print("Chatbot:", response)
        if user_input.lower() in ['quit', 'exit']:
            break

if __name__ == "__main__":
    run_chatbot()
