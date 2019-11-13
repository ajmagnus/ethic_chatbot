from chatterbot import ChatBot
def main():
	print("Python main func");
	from chatterbot import ChatBot
	chatbot = ChatBot("Trump");
	response = chatbot.get_response("Good morn");
	print(response);




if __name__ == '__main__':
	main()
