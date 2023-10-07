from flask import Flask, render_template, request
import speech_recognition as sr
from gtts import gTTS

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    text = request.form['text']
    tts = gTTS(text=text, lang='es')
    tts.save('output.mp3')
    return render_template('index.html', text=text)

if __name__ == '__main__':
    app.run(debug=True)
