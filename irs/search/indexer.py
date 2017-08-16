import json
import os
from datetime import datetime
from os.path import dirname, realpath
from click import progressbar, echo
from whoosh import index
from irs.search.schema import RedditSchema

PROJECT_DIR = dirname(dirname(dirname(realpath(__file__))))
INDEX_DIR = os.path.join(PROJECT_DIR, "indexdir")


def create_index():
    if not os.path.exists(INDEX_DIR):
        os.mkdir(INDEX_DIR)
    index.create_in(INDEX_DIR, RedditSchema, indexname="reddit")


def index_documents(json_path):
    ix = index.open_dir(INDEX_DIR, indexname="reddit")
    writer = ix.writer()
    documents = None
    with open(json_path) as f:
        documents = json.load(f)

    with progressbar(documents, label="Total Indexing Progress") as bar:
        for subreddit in bar:
            for doc in documents[subreddit]:
                timestamp = datetime.fromtimestamp(int(doc["created_date"]))
                writer.add_document(title=doc['title'],
                                    body=doc["body"],
                                    created=timestamp,
                                    url=doc["url"],
                                    subreddit=subreddit)
    echo("Committing Index. Please wait...")
    writer.commit()
    echo("Done!")
