#!/usr/bin/env python

import pytest

from herald import rss

feed = rss.Feed(rss_file="sample.xml")


def test_feed_title():
    assert feed.title == "FeedForAll Sample Feed"


def test_feed_item_count():
    assert len(feed.items) == 9
