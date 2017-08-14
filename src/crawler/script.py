import json
import praw

DEFAULT_SUBREDDIT = "technology"
AVERAGE_SECONDS_IN_MONTH = (365.25 / 12) * 24 * 60 * 60

reddit = praw.Reddit(client_id="9zOfLO4VGMLYyg",
                     client_secret=None,
                     user_agent="IR Crawler/Paladins")


def fetch_top_posts(subreddit_list=None, limit=10):
    if subreddit_list is None:
        subreddit_list = [DEFAULT_SUBREDDIT]
    complete_data = {}
    for subreddit_name in subreddit_list:
        subreddit_data = []
        subreddit = reddit.subreddit(subreddit_name)
        submissions = subreddit.top(time_filter='all', limit=limit)
        for submission in submissions:
            data = {'title': submission.title,
                    'body': submission.selftext,
                    'created_date': submission.created,
                    'url': submission.url
                    }
            subreddit_data.append(data)
        complete_data[subreddit_name] = subreddit_data
    return complete_data


if __name__ == "__main__":
    subreddit_list = input("Enter a comma separated list of subreddits:\n") or None
    subreddit_list = subreddit_list.split(",") if subreddit_list else None
    try:
        limit = int(input("Enter number of posts to fetch:\n"))
    except (TypeError, ValueError):
        limit = 10
    output_path = input("Enter json output path:\n") or "result.json"
    with open(output_path, "w") as f:
        json.dump(fetch_top_posts(subreddit_list, limit=limit), f, indent=4)
