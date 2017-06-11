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
    try:
        return jsonify(sentiment=model.predict(sentence));
    except Exception as inst:
        return str(inst);


@app.route('/batchPredict', methods=['GET','POST'])
def batchPredict():
    try:
        sentiment = {'positive':0, 'negative':0}
        # print "Here is the thing"
        data=request.get_json();
        # print request.json
        # return jsonify(data=request.form, data2=request.json, data3=request.data)
        for i in data:
            prediction = model.predict(i)
            sentiment['positive']+=i['positive']
            sentiment['negative']+=i['negative']
        sentiment['positive']=sentiment['positive']/len(data)
        sentiment['negative']=sentiment['negative']/len(data)
        return jsonify(sentiment = sentiment)
    except Exception as inst:
        print 'error: '+str(inst)
        return 'error: '+str(inst)