import os
from flask import Flask, render_template, request, json

app = Flask(__name__)


# Search page
@app.route('/')
def searchpage():
    return render_template('search.html')


# Search API
@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    tfidf_result = tfidf_results(query)
    bm25_result = bm25_results(query)
    return json.dumps({'tfidf': tfidf_result, 'bm25': bm25_result})


if __name__ == "__main__":
    app.run(host='0.0.0.0')
