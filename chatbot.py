from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# ساخت ربات چت
chatbot = ChatBot(
    'Assistant',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.MathematicalEvaluation'
    ],
    database_uri='sqlite:///database.db'
)

# آموزش دادن ربات با داده‌های آماده انگلیسی
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

# شروع گفتگو
print("Hi, I'm your chatbot assistant. Type 'exit' to end the chat.")
while True:
    user_input = input("You: ")

    if user_input.lower() == 'exit':
        print("Goodbye!")
        break

    response = chatbot.get_response(user_input)
    print("Chatbot:", response)
