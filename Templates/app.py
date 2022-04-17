from flask import Flask, escape, request, render_template
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

#initilise Tfidvectorizer
vector = TfidfVectorizer(stop_words = 'english',max_df = 0.7)

model = pickle.load(open("finalized_model.pkl",'rb'))

app = Flask(__name__)

@app.route('/')
def home():

     return render_template("index.html")

@app.route('/')
def prediction():

     return render_template("index.html")

     

if __name__ == '__main__':
    app.run()