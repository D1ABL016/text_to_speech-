from pathlib import Path
from openai import OpenAI
from flask import Flask, request, jsonify
from flask_cors import CORS
import pyttsx3
# import pytesseract
# from PIL import Image
import io

import pygame
from gtts import gTTS

app = Flask(__name__)
CORS(app)

@app.route('/play', methods=['POST'])
def play_text():
    content = request.json
    text = content.get("text", "")
    
    if text == "":
        return jsonify({"error": "No text to read"})
    
    # engine = pyttsx3.init()
    # newVoiceRate = 145
    # engine.setProperty('rate',newVoiceRate)
    # engine.say(text)
    # engine.runAndWait()
    
    
    # tts = gTTS(text, lang='en')

    # # Save the audio to a bytes buffer
    # audio_buffer = io.BytesIO()
    # tts.write_to_fp(audio_buffer)
    # audio_buffer.seek(0)

    # # Initialize pygame mixer
    # pygame.mixer.init()
    
    # # Load the audio buffer into pygame
    # pygame.mixer.music.load(audio_buffer, 'mp3')

    # # Play the audio
    # pygame.mixer.music.play()

    # # Wait for the audio to finish playing
    # while pygame.mixer.music.get_busy():
    #     pygame.time.Clock().tick(10)
    
    
    
    client = OpenAI(api_key = "sk-None-qtasBwsX64N7R1eEDknAT3BlbkFJXf8TXAuoWW8KrB9FbR1T")

    speech_file_path = Path(__file__).parent / "speech.mp3"
    response = client.audio.speech.create(
  model="tts-1",
  voice="alloy",
  input="Today is a wonderful day to build something people love!"
)

    # response.stream_to_file(speech_file_path)
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(debug=True)
