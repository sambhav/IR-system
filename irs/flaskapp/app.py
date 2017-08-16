from os.path import dirname, abspath, join as join_path
from flask import Flask, request, render_template
from irs.search.search import doc_search

TEMPLATE_FOLDER = join_path(dirname(abspath(__file__)), 'templates')

app = Flask(__name__, template_folder=TEMPLATE_FOLDER)


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
