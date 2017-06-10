from flask import Flask, jsonify, request
from src.sentimentClass import sentiment
import json
import base64

app = Flask(__name__)

model = sentiment()

@app.route('/')
def index():
    return jsonify(message = "Rest API for sentiment analysis")

@app.route('/predict/<sentence>', methods=['GET','POST'])
def test(sentence):
    data = json.loads(base64.b64decode(sentence))
    try:
        for i in data:
            prediction = model.predict(i)
            sentiment['positive']+=i['positive']
            sentiment['negative']+=i['negative']
        sentiment['positive']=sentiment['positive']/len(data)
        sentiment['negative']=sentiment['negative']/len(data)
        return jsonify(sentiment = sentiment)
    except Exception as inst:
        return str(inst);

