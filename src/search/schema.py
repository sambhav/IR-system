from whoosh.fields import SchemaClass, TEXT, ID, DATETIME
from whoosh.analysis import StemmingAnalyzer


class RedditSchema(SchemaClass):
    url = ID
    title = TEXT(analyzer=StemmingAnalyzer(), stored=True)
    body = TEXT(analyzer=StemmingAnalyzer(), stored=True)
    created = DATETIME
    subreddit = TEXT
