import pywhatkit
import json
import datetime
import os

def load_contacts():
    with open("contacts.json") as file:
        return json.load(file)

def handle_command(command):
    contacts = load_contacts()
    name = ""
    for key in contacts:
        if key in command:
            name = key
            break

    if not name:
        return "❌ Contact not found."

    number = contacts[name]

    # Detect if it's a file
    if ".pdf" in command or ".png" in command or ".jpg" in command:
        for word in command.split():
            if word.endswith((".pdf", ".jpg", ".png")):
                file_name = word
                break
        if not os.path.exists(file_name):
            return f"❌ File '{file_name}' not found."
        pywhatkit.sendwhats_image(number, file_name, f"Here's the file: {file_name}")
        return f"✅ File '{file_name}' sent to {name.title()}!"
    
    # Otherwise, treat it as message
    message = extract_message_text(command, name)
    hour = datetime.datetime.now().hour
    minute = datetime.datetime.now().minute + 1
    pywhatkit.sendwhatmsg(number, message, hour, minute)
    return f"✅ Message sent to {name.title()}: '{message}'"

def extract_message_text(command, name):
    # You can improve this logic later with NLP
    words = command.split()
    msg_start = words.index("to") + 1
    if name in words:
        msg_start = words.index(name) + 1
    message = " ".join(words[msg_start:]) or "Hello from Sahithya’s assistant"
    return message
