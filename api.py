from flask import Flask, request, jsonify
import pickle
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import re

app = Flask(__name__)


vector = pickle.load(open('vectorizer', 'rb'))


loaded_model = pickle.load(open('trained_model', 'rb'))


def stemming(content):
    port_stem = PorterStemmer()
    stemmed_content = re.sub('[^a-zA-Z]',' ',content)
    stemmed_content = stemmed_content.lower()
    stemmed_content = stemmed_content.split()
    stemmed_content = [port_stem.stem(word) for word in stemmed_content if not word in stopwords.words('english')]
    return ' '.join(stemmed_content)

@app.route('/predict', methods=['POST'])
def predict():
    
    text_data = request.json['text']

    
    preprocessed_text = stemming(text_data)

    
    X_transformed = vector.transform([preprocessed_text])

    
    prediction = loaded_model.predict(X_transformed)[0]

    
    sentiment = "positive" if prediction == 1 else "negative"

    
    return jsonify({'sentiment': sentiment})

if __name__ == '__main__':
    app.run(debug=True)
