from voice_recognition import listen_for_command
from whatsapp_automation import send_message

if __name__ == "__main__":
    command = listen_for_command()
    
    if command:
        print(f"Voice command: {command}")

        # Example: If the user says "send message to Mom"
        if "send message" in command.lower():
            phone_number = "+91XXXXXXXXXX"  # Replace with actual number
            message = "Hello! This is an automated message."
            send_message(phone_number, message)
            print("Message sent!")
    else:
        print("No command recognized.")
