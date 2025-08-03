from flask import Flask, render_template, request
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    dream_text = request.form['dream']
    analyzer = SentimentIntensityAnalyzer()
    scores = analyzer.polarity_scores(dream_text)
    compound = scores['compound']

    print(f"VADER Score: {compound}")  # debug score

    if compound >= 0.5:
        emotion = "Very Positive 😄"
    elif 0.2 <= compound < 0.5:
        emotion = "Positive 🙂"
    elif -0.2 < compound < 0.2:
        emotion = "Neutral 😐"
    elif -0.5 < compound <= -0.2:
        emotion = "Negative 😟"
    else:
        emotion = "Very Negative 😢"

    return render_template('results.html', dream=dream_text, emotion=emotion, polarity=compound)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')  # allow phone to connect

