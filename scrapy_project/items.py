import scrapy


class CategoryItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    url = scrapy.Field()
    children = scrapy.Field()

    def to_dict(self):
        return {
            'id': self['id'],
            'name': self['name'],
            'url': self['url'],
            'children': [child.to_dict() for child in self['children']]
        }


class ProductItem(scrapy.Item):
    id = scrapy.Field()
    cat_id = scrapy.Field()
    url = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    original_price = scrapy.Field()
    image = scrapy.Field()

    def to_dict(self):
        return {
            'id': self['id'],
            'cat_id': self['name'],
            'url': self['url'],
            'name': self['name'],
            'price': self['price'],
            'original_price': self['original_price'],
            'image': self['image'],
        }
