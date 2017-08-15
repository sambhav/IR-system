import whoosh
from pprint import pprint
from whoosh.scoring import BM25F, TF_IDF
from whoosh.index import open_dir
from whoosh.qparser import MultifieldParser
from indexer import INDEX_DIR

def print_results(results):
    for i, result in enumerate(results):
        print("="*50)
        print(str(i), result['title'] )
        print(result['subreddit'])
        print(result['url'])
        print("-"*50)
        print(result['body'])
        print("-"*50)
        print("="*50)

def doc_search(query, scoring_method="BM25F"):
    ix=open_dir(INDEX_DIR, indexname="reddit")
    if scoring_method == "TF-IDF":
        searcher = ix.searcher(weighting=TF_IDF)
    else:
        searcher = ix.searcher(weighting=BM25F) 
    qp = MultifieldParser(['title','body'], ix.schema).parse(query)
    results = [dict(result) for result in searcher.search(qp, limit=10)]
    return results

if __name__ == "__main__":
    print_results(doc_search("linux"))
    print_results(doc_search("linux", scoring_method="TF-IDF"))