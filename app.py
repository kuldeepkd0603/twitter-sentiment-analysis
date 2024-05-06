from flask import Flask, render_template, request, jsonify
import pickle
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import re

app = Flask(__name__)

vectorizer = pickle.load(open('vectorizer', 'rb'))
loaded_model = pickle.load(open('trained_model', 'rb'))

def stemming(content):
    port_stem = PorterStemmer()
    stemmed_content = re.sub('[^a-zA-Z]',' ',content)
    stemmed_content = stemmed_content.lower()
    stemmed_content = stemmed_content.split()
    stemmed_content = [port_stem.stem(word) for word in stemmed_content if not word in stopwords.words('english')]
    return ' '.join(stemmed_content)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    text_data = request.form['text']
    preprocessed_text = stemming(text_data)
    X_transformed = vectorizer.transform([preprocessed_text])
    prediction = loaded_model.predict(X_transformed)
    sentiment = "Negative" if prediction[0] == 0 else "Positive"
    return render_template('index.html', prediction=sentiment)

if __name__ == '__main__':
    app.run(debug=True)
