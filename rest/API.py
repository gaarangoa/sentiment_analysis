from flask import Flask, jsonify, request
from src.sentimentClass import sentiment

app = Flask(__name__)

model = sentiment()

@app.route('/')
def index():
    return jsonify(message = "Rest API for sentiment analysis")

@app.route('/predict/<sentence>', methods=['GET','POST'])
def test(sentence):
        try:
            return jsonify(sentiment=model.predict(sentence));
        except Exception as inst:
            return str(inst);
