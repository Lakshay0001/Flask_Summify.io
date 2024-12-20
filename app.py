from flask import Flask,render_template,request,jsonify, send_from_directory
from textSummary import summarizer
# from pyttsx3 import *
from gtts import *
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze',methods=['GET','POST'])
def analyze():
    if request.method=='POST':
        rawtext=request.form['rawtext']
        summary,originalText,lenOriginalText,lenSummary=summarizer(rawtext)
    
    return render_template('summary.html',summary=summary,originalText=originalText,lenOriginalText=lenOriginalText,lenSummary=lenSummary)

@app.route('/speak',methods=['POST'])
def speak():
    data = request.get_json()
    text = data.get('text', '')

    if not text:
        return jsonify({'status': 'error', 'message': 'No text provided'}), 400

    try:
        tts = gTTS(text, lang='en')
        audio_file = "speech.mp3"
        tts.save(audio_file)
        return jsonify({'status': 'success', 'audio': audio_file})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500
    
@app.route('/speech.mp3')
def get_audio():
    return send_from_directory('.', 'speech.mp3')



if __name__ == "__main__":
    app.run(debug = True)












# from flask import Flask,render_template,request,jsonify
# from textSummary import summarizer
# from pyttsx3 import *

# app = Flask(__name__)
# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/analyze',methods=['GET','POST'])
# def analyze():
#     if request.method=='POST':
#         rawtext=request.form['rawtext']
#         summary,originalText,lenOriginalText,lenSummary=summarizer(rawtext)
    
#     return render_template('summary.html',summary=summary,originalText=originalText,lenOriginalText=lenOriginalText,lenSummary=lenSummary)

# @app.route('/speak',methods=['POST'])
# def speak():
#     data = request.get_json()
#     text = data.get('text', '')

#     if not text:
#         return jsonify({"error": "No text provided"}), 400

#     engine = init()

#     rate = engine.getProperty('rate')
#     engine.setProperty('rate', rate - 50)

#     engine.say(text)
#     engine.runAndWait()



# if __name__ == "__main__":
#     app.run(debug = True)
