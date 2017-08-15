import json
import os
from datetime import datetime
from os.path import dirname, realpath
from whoosh import index
from schema import RedditSchema 

PROJECT_DIR = dirname(dirname(dirname(realpath(__file__))))
INDEX_DIR = os.path.join(PROJECT_DIR, "indexdir")

def create_index():
    if not os.path.exists(INDEX_DIR):
        os.mkdir(INDEX_DIR)
    ix = index.create_in(INDEX_DIR, RedditSchema, indexname="reddit")


def index_documents():
    ix = index.open_dir(INDEX_DIR, indexname="reddit")
    writer = ix.writer()
    documents = None
    with open(os.path.join(PROJECT_DIR, "sample_data", "dump.json")) as f:
        documents = json.load(f)
    for subreddit in documents:
        for doc in documents[subreddit]:
            writer.add_document(title=doc['title'], body=doc["body"],
                                created=datetime.fromtimestamp(int(doc["created_date"])), url=doc["url"],
                                subreddit=subreddit)    


if __name__ == '__main__':
    create_index()
    index_documents()