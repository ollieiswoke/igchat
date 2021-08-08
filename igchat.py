from format import *

#Open ig chat history json at txt file
chat = open("simpler.txt")
fname = "simpler.txt"


def print_history(my_username, username):

    with open(fname, 'r', encoding="ascii", errors="surrogateescape") as f:
        line = f.read()

        #identifies the conversation json
        identifier =  '["' + username + '", "' + my_username + '"],' 
        identifier_flipped =  '["' + my_username + '", "' + username + '"],' 

        #split json by conversation
        conversations = line.split('{"participants": ')
        for conversation in conversations:
            #if right conversation
            if identifier in conversation or identifier_flipped in conversation:
                #split by sender
                conversation_list = conversation.split('{"sender": ')
                for message_json in conversation_list:
                    name = message_json.split(",")[0].replace('"', '')
                    if name == my_username:
                        format_my_message(message_json, name)
                    if name == username:
                        format_their_message(message_json, name)
