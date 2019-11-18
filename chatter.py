from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.logic import LogicAdapter
from chatterbot import utils
def main():
	chatbot = ChatBot(
			"Trump", 
			read_only=False,
			logic_adapters=[
				{
					"import_path": "chatterbot.logic.BestMatch",
				#	"response_selection_method": "chatterbot.response_selection.get_random_response"
				}
			]
	)
	
	#chatbot.logic_adapters = [ {"response_selection_method": chatterbot.response_selection.get_random_response} ]
	#trainer = ChatterBotCorpusTrainer(chatbot)
	#trainer.train(
	#    "chatterbot.corpus.trump"
	#)

	chatbot.read_only=True
	
	#have conversation
	msg = 'hello!'
	print(msg);
	while msg != 'bye':
		msg = input(':')
		#print(msg)
		response = chatbot.get_response(msg)
		print(response)

	print('bye!')

if __name__ == '__main__':
	main()
