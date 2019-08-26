import json


class JsonWriterPipeline(object):
    def __init__(self, filename):
        self.filename = filename

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            filename=crawler.settings.get('FILENAME'),
        )

    def open_spider(self, spider):
        self.items = []

    def close_spider(self, spider):
        with open(self.filename, 'w') as f:
            data = json.dumps(self.items)
            f.write(data)
            f.close()

    def process_item(self, item, spider):
        if not isinstance(item, dict):
            self.items.append(item.to_dict())
        else:
            self.items.append(item)
        return item