# lastfm-counter

This is a script that allows me to copy my top played artists for a Twitter post.

See post examples here:

https://twitter.com/joshfinnie/status/1488156977595392001
https://twitter.com/joshfinnie/status/1485612814068817935

To run, fill out a `.env` file and use [Poetry](https://python-poetry.org/):

``` sh
API_KEY=""
LASTFM_SHARED_SECRET=""
LASTFM_USER=""
```

```sh
$ poetry install
$ poetry run python count.py
```

This will print out the data for the tweet like this:

``` shsh
$ poetry run python count.py
♫ My Top 5 played artists in the past 7 days: FKA twigs (14), MØ (6), Almost Vanished (3), Bob Moses (3) & Andy Leech (2). Via #LastFM ♫
```

### Dockerfile

The Docker implementation may or may not work...
