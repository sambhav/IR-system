from whoosh.fields import SchemaClass, TEXT, ID, DATETIME
from whoosh.analysis import StemmingAnalyzer


class RedditSchema(SchemaClass):
    url = ID(stored=True)
    title = TEXT(analyzer=StemmingAnalyzer(), stored=True, field_boost=5.0)
    body = TEXT(analyzer=StemmingAnalyzer(), stored=True)
    created = DATETIME(stored=True)
    subreddit = TEXT(stored=True)
