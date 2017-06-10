from flask import Flask, jsonify, request
from src.sentimentClass import sentiment
import json

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

@app.route('/batchPredict/', methods=['POST', 'GET'])
def batchPredict():
    # return 'okay'
    try:
        sentiment = {'positive':0, 'negative':0}
        data = request.data;
        print data
        return jsonify(data)

        # for i in data['documents']:
        #     prediction = model.predict(i)
        #     sentiment['positive']+=i['positive']
        #     sentiment['negative']+=i['negative']
        # sentiment['positive']=sentiment['positive']/len(data)
        # sentiment['negative']=sentiment['negative']/len(data)
        # return jsonify(sentiment = sentiment)
    except Exception as inst:
        return str(inst)