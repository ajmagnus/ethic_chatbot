from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import chatterbot
def main():
	from chatterbot import ChatBot
	chatbot = ChatBot(
			"Trump", 
			read_only=False,
			#logic_adapters=[
			#	{
			#		"response_selection_method": chatterbot.response_selection.get_random_response
			#	}
			#]
	)
		
	#train the chatbot
	trainer = ChatterBotCorpusTrainer(chatbot)
	#trainer.train(
	#	"convo.yml"
	#)

	trainer.train(
	    "chatterbot.corpus.trump"
	)

		

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
