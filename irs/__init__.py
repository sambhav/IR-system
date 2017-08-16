import json
import click
from irs.crawler.script import fetch_top_posts
from irs.search.indexer import (create_index as _create_index,
                                index_documents as _index_documents)
from irs.flaskapp.app import app


@click.group()
def cli():
    pass


@cli.command()
def run():
    app.run(host='0.0.0.0', debug=True)


@cli.command()
def crawl():
    subreddit_list = click.prompt("Enter a comma separated list of subreddits", default="technology")
    subreddit_list = [s.strip() for s in subreddit_list.split(",")] if subreddit_list else None
    limit = click.prompt("Enter number of posts (per subreddit) to fetch", default=10, type=int)
    output_path = click.prompt("Enter json output path:", default="result.json", type=click.Path())
    click.echo("Fetching posts. Please wait...")
    with open(output_path, "w") as f:
        json.dump(fetch_top_posts(subreddit_list, limit=limit), f, indent=4)
    click.echo("Done!")


@cli.command()
def create_index():
    click.echo("Creating index dir...")
    _create_index()
    click.echo("Done!")


@cli.command()
@click.argument('json_path', type=click.Path(exists=True))
def index_documents(json_path):
    _index_documents(json_path)
