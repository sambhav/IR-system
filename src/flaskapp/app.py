from flask import Flask, request, render_template
from search.search import doc_search

app = Flask(__name__)


# Home page
@app.route('/', methods=['GET'])
def homepage():
    if 'search' not in request.args:
        return render_template('search.html')
    query = request.args.get('search')
    tfidf = doc_search(query, "TFIDF")
    bm25 = doc_search(query, "BM25")
    if len(tfidf) > 10:
        tfidf = tfidf[:10]
    if len(bm25) > 10:
        bm25 = bm25[:10]
    return render_template('search.html', tfidf=tfidf, bm25=bm25)
