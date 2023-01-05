from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

my_bot = ChatBot(name='PyBot', read_only =True)

small_talk = ['Hello!',
                'Hi', 'How are you today?', 'Sorry to hear that', 'Glad to hear that!']

math_talk_1 = ['pythagorean theorem', 'a squared plus b squared equals c squared.']

math_talk_2 = ['law of cosines', 'c**2 = a**2 + b**2 - 2*a*b*cos(gamma)']

list_trainer = ListTrainer(my_bot)

for item in (small_talk, math_talk_1, math_talk_2):
    list_trainer.train(item)