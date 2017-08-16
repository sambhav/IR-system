import click
import praw
import prawcore


DEFAULT_SUBREDDIT = "technology"
AVERAGE_SECONDS_IN_MONTH = (365.25 / 12) * 24 * 60 * 60

reddit = praw.Reddit(client_id="9zOfLO4VGMLYyg",
                     client_secret=None,
                     user_agent="IR Crawler/Paladins")


def fetch_top_posts(subreddit_list=None, limit=10):
    if subreddit_list is None:
        subreddit_list = [DEFAULT_SUBREDDIT]
    complete_data = {}
    with click.progressbar(subreddit_list) as bar:
        for subreddit_name in bar:
            subreddit_data = []
            subreddit = reddit.subreddit(subreddit_name)
            submissions = subreddit.top(time_filter='all', limit=limit)
            try:
                for submission in submissions:
                    data = {'title': submission.title,
                            'body': submission.selftext,
                            'created_date': submission.created,
                            'url': submission.url
                            }
                    subreddit_data.append(data)
            except (prawcore.exceptions.NotFound, prawcore.exceptions.Redirect):
                pass
            else:
                complete_data[subreddit_name] = subreddit_data
    return complete_data
