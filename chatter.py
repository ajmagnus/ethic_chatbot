import chatterbot
def main():
	print("Python main func");
	from chatterbot import ChatBot
	chatbot = ChatBot("Trump");
	reponse = chatbot.get_response("Good morn");
	print(response);




if __name__ == '__main__':
	main()
