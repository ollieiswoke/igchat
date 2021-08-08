
def get_date(message_json):
    created_at = message_json.split(",")[1].replace('"', '')
    date = created_at.split(":")[1][:11]
    return date

def get_text(message_json):
    text = message_json.split('"text":')[1]
    text = text[2:-5]
    return text

def get_post(message_json):
    owner = message_json.split('"media_owner":')[1]
    owner = owner.split(',')[0]
    owner = owner[2:-1]
    return "sent a post by "+owner

def get_profile(message_json):
    profile = message_json.split('"profile_share_username":')[1]
    profile = profile.split(',')[0]
    profile = profile[2:-1]
    return "sent a profile: "+profile

def format_message(message_json):
    if '"text":' in message_json:
        message = get_text(message_json)
    elif '"url":' in message_json:
        message = "sent a gif"
    elif '"media":' in message_json or '"media_url":' in message_json:
        message = "sent an image"
    elif '"media_owner":' in message_json:
        message = get_post(message_json)
    elif '"heart":' in message_json:
        message = "❤️"
    elif '"profile_share_username":' in message_json:
        message = get_profile(message_json)
    elif '"voice_media":' in message_json:
        message = "shared a voice clip"
    elif '"video_call_action":' in message_json:
        message = "started a video call"
    else:
        raise "unhandled message type. json dump: "+message_json
    return message
    #print(get_text(message_json))
    #print(message_json)
    #print("==================")

def format_my_message(message_json, name):
    print(f"{name}: {format_message(message_json)}")


def format_their_message(message_json, name):
    print("||||||" + f"{name}: {format_message(message_json)}")
def format_gif():
    pass
def format_image():
    pass