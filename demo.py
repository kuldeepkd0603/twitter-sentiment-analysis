import pickle 
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import re


vector = pickle.load(open('vectorizer', 'rb'))


text_data = ['fuck']
df = pd.DataFrame({'text': text_data})


def stemming(content):
    port_stem = PorterStemmer()
    stemmed_content = re.sub('[^a-zA-Z]',' ',content)
    stemmed_content = stemmed_content.lower()
    stemmed_content = stemmed_content.split()
    stemmed_content = [port_stem.stem(word) for word in stemmed_content if not word in stopwords.words('english')]
    return ' '.join(stemmed_content)


df['text'] = df['text'].apply(stemming)

X_transformed = vector.transform(df['text'])


print("Shape of df:", df.shape)
print("Shape of X_transformed:", X_transformed.shape)


loaded_model = pickle.load(open('trained_model', 'rb'))


predictions = loaded_model.predict(X_transformed)

print(predictions)
