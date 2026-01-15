from flask import Flask, render_template, request
import pickle
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer

# Ensure NLTK data is downloaded
nltk.download('punkt')
nltk.download('stopwords')

app = Flask(__name__)
ps = PorterStemmer()

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

# Load model and vectorizer
tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    message = None
    if request.method == 'POST':
        message = request.form['message']
        # 1. preprocess
        transformed_sms = transform_text(message)
        # 2. vectorize
        vector_input = tfidf.transform([transformed_sms])
        # 3. predict
        prediction = model.predict(vector_input)[0]
        # 4. Display
        if prediction == 1:
            result = "Smishing"
        else:
            result = "Not Smishing"
            
    return render_template('index.html', result=result, message=message)

if __name__ == '__main__':
    app.run(debug=True)
