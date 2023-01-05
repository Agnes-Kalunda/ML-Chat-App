from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

my_bot = ChatBot(name='PyBot', read_only =True)

small_talk = ['Hello!',
                'Hi', 'How are you today?', 'Sorry to hear that', 'Glad to hear that!']