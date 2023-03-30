import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import openai

openai.api_type = "azure"
openai.api_base = os.getenv("OPENAI_API_BASE") 
openai.api_version = "2023-03-15-preview"
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)
CORS(app)
app.debug = True

@app.route('/app/', methods=['POST'])
def chat():
    data = request.json
    prompt = data.get('prompt')

    response = openai.ChatCompletion.create(
        engine = os.getenv("OPENAI_ENGINE"),
        messages = [
            {"role": "user", "content": prompt},
        ],
        temperature=0.5,
        max_tokens=800,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None
    )
    return jsonify({"response": response['choices'][0]['message']['content']})

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')