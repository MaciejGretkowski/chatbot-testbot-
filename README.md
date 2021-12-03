# chatbot-testbot-
A Machine Learned chatbot capable of answering questions by picking up intents.

This chatbot is created using machine learning, it has learned from a .json file that has some basic intents and the pre-determined responses to them.

Currently it has a few issues such as: the model having some dirty intents which causes the bot to provide wrong answers, it reads intents file from my local specified location, GUI having a few weird spacing issues and not being sizeable.

With a little more time the GUI issues would be solved but I'm happy with how it's currently implemented. As for the intents having dirty data if it were to be adjusted for a real life application there would be much more effort for this agent to be applicable for it's inteded purpose. Reading from a specific location would be solved with just using "/intents.json" code but it caused me some issues earlier as I had it in a different folder, it's a 2 minute fix if I were to organise my folder structure :D

Model was trained with NLTK and it utlised tensorflow.
