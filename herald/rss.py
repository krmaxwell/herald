from rss_parser import Parser


class Feed:
    def __init__(self, rss_file: str) -> None:
        with open(rss_file, "rb") as f:
            self.rss = f.read()

        self._parser = Parser(xml=self.rss)
        self.feed = self._parser.parse()

        self.title = self.feed.title
        self.items = self.feed.feed


if __name__ == "__main__":
    feed = Feed("sample.xml")
    print(feed.title)
