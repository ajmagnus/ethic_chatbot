from chatterbot import ChatBot
def main():
	from chatterbot import ChatBot
	chatbot = ChatBot("Trump");
	msg = 'hello!';
	print(msg);
	while msg != 'bye':
		msg = input(':');
		print(msg);
		#response = chatbot.get_response(msg);
		#print(response);

	print('bye!');

if __name__ == '__main__':
	main()
