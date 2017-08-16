import whoosh
from pprint import pprint
from whoosh.scoring import BM25F, TF_IDF
from whoosh.index import open_dir
from whoosh.qparser import MultifieldParser
try:
    from search.indexer import INDEX_DIR
except:
    from indexer import INDEX_DIR


def doc_search(query, scoring_method="BM25"):
    ix=open_dir(INDEX_DIR, indexname="reddit")
    if scoring_method == "TFIDF":
        searcher = ix.searcher(weighting=TF_IDF)
    else:
        searcher = ix.searcher(weighting=BM25F) 
    qp = MultifieldParser(['title','body'], ix.schema).parse(query)
    results = [dict(result) for result in searcher.search(qp, limit=10)]
    return results
