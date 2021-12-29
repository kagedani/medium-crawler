import feedparser
import logging
import pandas as pd
import json


class Medium:
    # https://github.com/thepracticaldev/dev.to/issues/28#issuecomment-325544385

    def __init__(self):
        self.DEVELOPER_CATEGORY = "developers"
        self.PYTHON_CATEGORY = "python"
        self.PROGRAMMING_CATEGORY = "programming"
        self.CLOUD_CATEGORY = "cloud"
        self.urls = {
            self.CLOUD_CATEGORY: "https://medium.com/feed/tag/cloud",
            self.PYTHON_CATEGORY: "https://medium.com/feed/tag/python",
            self.PROGRAMMING_CATEGORY: "https://medium.com/feed/tag/programming",
            self.DEVELOPER_CATEGORY: "https://medium.com/feed/tag/developer",
        }

    def medium_aggregate(self, category):
        feed = feedparser.parse(self.urls[category])
        logging.debug(f'category entries: {len(feed.entries)}')
        logging.debug(f'### {category} ###')
        df = self.log_feed_entries(feed, category)
        logging.debug(df.to_markdown())
        return df

    @staticmethod
    def log_feed_entries(feed, category):
        element = {}
        entries = {}
        for i in range(len(feed.entries)):
            entry = feed.entries[i]
            logging.debug(f'{entry.title}')
            logging.debug(f'URL: {entry.link}')
            logging.debug('###########################################')
            element = {
                "category": category,
                "title": entry.title,
                "url": entry.link
            }
            entries.update({
                i: element
            })
        logging.debug('-------------------------------------------------------------------------------------')
        df = pd.DataFrame.from_dict(entries, orient="index")
        return df
