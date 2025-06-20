import random

def get_response(user_input):
    user_input = user_input.lower()
    responses = {
        "what is alzheimer": "Alzheimer's is a progressive neurological disorder that causes memory loss and cognitive decline.",
        "symptom": "Common symptoms include memory loss, confusion, difficulty speaking, and changes in behavior.",
        "accuracy": "The model provides a classification with high accuracy, but it's not a replacement for clinical diagnosis.",
        "help": "You can contact a neurologist or visit a hospital for further guidance."
    }
    for key in responses:
        if key in user_input:
            return responses[key]
    return random.choice([
        "I'm here to help you with information about Alzheimer's.",
        "Sorry, I didn't understand that. Can you rephrase?",
        "Please consult a doctor for professional advice."
    ])
