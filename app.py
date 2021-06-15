from flask import Flask, request, render_template
import re
import pickle
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline

tfidf = pickle.load(open('vectorizer.pickle', 'rb'))

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/classify', methods=['POST'])
def classify():
    if request.method == 'POST':
        algoritmo = request.form['algoritmo']
        title = request.form['user_title']
        content = request.form['user_content']
        total = title + content
        total = re.sub('<[^>]*>', '', total)
        total = re.sub(r'[^\w\s]', '', total)
        total = total.lower()
        data = [total]
        def alg(algoritmo):
            switcher = {
                'svm': 'model_svm.pickle',
                'knn': 'model_knn.pickle',
                'rfc': 'model_rfc.pickle'
            }
            return switcher.get(algoritmo, "Algoritmo no encontrado")
        model_load = alg(algoritmo)
        model = pickle.load(open(model_load, 'rb'))
        pred = model.predict(tfidf.transform(data))[0]
        print(model_load)
    if format(pred[0]) == 'T':
        prediccion = 'Verdadera'
    elif format(pred[0]) == 'F':
        prediccion = 'Falsa'
    else:
        prediccion = 'Error'

    return render_template('index.html', resultado='La noticia es: {}'.format(prediccion))


if __name__ == "__main__":
    app.run(debug=True)