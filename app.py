from flask import Flask, render_template_string
from voice_engine import get_command
from whatsapp_bot import send_message, send_file

app = Flask(__name__)

@app.route("/")
def index():
    return render_template_string("""
        <h2>🎙️ WhatsApp Voice Assistant</h2>
        <form action="/send">
            <button type="submit">Start Listening</button>
        </form>
    """)

@app.route("/send")
def send():
    command = get_command()

    if "send file" in command:
        result = send_file(command)
    elif "send message" in command or "send" in command:
        result = send_message(command)
    else:
        result = "No valid command detected."

    return f"<p>{result}</p>"

if __name__ == "__main__":
    app.run(debug=True)

    
