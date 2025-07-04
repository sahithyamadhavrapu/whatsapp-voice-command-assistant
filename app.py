from flask import Flask, render_template_string
from voice_engine import get_command
from whatsapp_bot import send_message

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
    if "send" in command and "to" in command:
        result = send_message(command)
        return f"<p>{result}</p>"
    else:
        return "No valid command detected."

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
    
