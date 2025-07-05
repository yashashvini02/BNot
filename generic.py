import re

def get_str_from_food_dict(food_dict: dict):
    return ", ".join([f"{int(value)} {key}" for key, value in food_dict.items()])

def extract_session_id(session_str: str):
    """
    Extracts session ID from session path.
    Works for both Dialogflow console and Messenger.
    """
    if not session_str:
        return ""

    parts = session_str.split("/sessions/")
    if len(parts) < 2:
        return ""

    # Handle optional /contexts
    after_sessions = parts[1]
    session_id = after_sessions.split("/contexts/")[0]
    return session_id

if __name__=="__main__" :
    print(extract_session_id("projects/yt-chatbot-jc9a/agent/sessions/295ce436-83f8-ad78-af7b-0011c2342141/contexts/ongoing-order"))
    print(extract_session_id("projects/yt-chatbot-jc9a/agent/sessions/295ce436-83f8-ad78-af7b-0011c2342141"))
    print(get_str_from_food_dict({"Pizza": 2, "Mango Lassi": 1}))


def normalize_repeats(text):
    """
    Replace any letter repeated more than twice in a row with just two of that letter.
    E.g. Hiiiiii -> Hii
         Hellooooo -> Helloo
         Heyyyyyy -> Heyy
    """
    return re.sub(r'(.)\1{2,}', r'\1\1', text)
