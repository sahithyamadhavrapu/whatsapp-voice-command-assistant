import pywhatkit

def send_whatsapp_message(command):
    try:
        words = command.split()
        message = " ".join(words[1:])  # Extract message content

        # Modify this part to specify your recipient
        phone_number = "+91XXXXXXXXXX"  # Replace with actual number

        print(f"Sending message: '{message}' to {phone_number}...")
        pywhatkit.sendwhatmsg_instantly(phone_number, message)

    except Exception as e:
        print(f"Error sending message: {e}")
