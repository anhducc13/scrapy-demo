import scrapy
from .utils import gen_uuid


class DotNotation(scrapy.Item):
    def __getattr__(self, name):
        return self[name]

    def __setattr__(self, name, value):
        if not name.startswith('_'):
            self[name] = value
        else:
            super(DotNotation, self).__setattr__(name, value)


class CategoryItem(DotNotation):
    id = scrapy.Field()
    name = scrapy.Field()
    url = scrapy.Field()
    children = scrapy.Field()

    def __init__(self, name, url):
        super(CategoryItem, self).__init__(name=name, url=url)
        self.id = gen_uuid(self.url)
        self.children = []
        self._parent = None

    def add_child(self, children):
        self.children.append(children)
        children._parent = self

    def to_dict(self):
        dic = {
            'id': self.id,
            'name': self.name,
            'url': self.url,
        }
        children = [child.to_dict() for child in self.children]
        dic.update({'children': children})
        return dic
