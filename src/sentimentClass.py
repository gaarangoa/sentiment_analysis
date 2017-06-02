from nltk.tokenize import TweetTokenizer
from SentimentModel import load
import json
import unicodedata
from tflearn.data_utils import to_categorical, pad_sequences
import os,sys

BASE_PATH = "/".join(os.getcwd().split('/')[:-1])
sys.path.append(BASE_PATH)

import config

class sentiment():
    #
    def __init__(self):
        self.tokenizer = TweetTokenizer(strip_handles=True, reduce_len=True)
        self.dict, self.rev_dict = json.load(open(config.rootdir+'/data/dict.json'))
        self.model = load();
    #
    def remove_accents(self, input_str):
        nfkd_form = unicodedata.normalize('NFKD', input_str)
        only_ascii = nfkd_form.encode('ASCII', 'ignore')
        return only_ascii
    #
    def word2num(self, doc):
        raw =  doc.lower();
        raw = self.remove_accents(raw);
        tokens = self.tokenizer.tokenize(raw);
        tk=[]
        for k in tokens:
            try:
                tk.append(self.dict[k])
            except:
                pass
        return tk
    #
    def predict(self, str):
        wn = self.word2num(str)
        pn = pad_sequences([wn], maxlen=20, value=0.0)
        prediction = self.model.predict(pn);
        # print "Positive score: ", prediction[0][1]*100, "\nNegative score: ", prediction[0][0]*100
        return {'positive':round(prediction[0][1]*100, 1), 'negative':round(prediction[0][0]*100,1)}


