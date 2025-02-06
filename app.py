from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('ankl.html')

@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    comment = request.form['comment']
    analysis = TextBlob(comment)
    sentiment = 0 if analysis.sentiment.polarity >= 0 else 1  # 0 for positive, 1 for negative
    return render_template('ankl.html', sentiment=sentiment)

if __name__ == '__main__':
    app.run(debug=True)