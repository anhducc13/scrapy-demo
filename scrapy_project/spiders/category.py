import scrapy
from ..items import CategoryItem
from ..utils import gen_uuid


class CategoriesSpider(scrapy.Spider):
    name = 'category'

    def __init__(self, *args, **kwargs):
        super(CategoriesSpider, self).__init__(*args, **kwargs)
        self.site_url = kwargs.get('site_url', '')
        self.site_name = kwargs.get('site_name', '')
        self.config_crawler = kwargs.get('config_crawler', dict())
        self.start_urls = [self.site_url]

    def parse(self, response):
        category = CategoryItem(
            id=gen_uuid(self.site_url),
            name=self.site_name,
            url=self.site_url,
            children=[]
        )
        self.extract_children(category, response, self.config_crawler)
        yield category

    def extract_children(self, item, node, config):
        for child_node in node.css(config['selector']):
            for child in self.extract_items(child_node, config):
                item['children'].append(child)

    def extract_items(self, node, config):
        name = node.css(config['name']).get().strip()
        postfix = node.css(config["url"]).get().strip()
        if postfix.startswith("http"):
            prefix = ''
        else:
            prefix = self.site_url
        url = f'{prefix}{postfix}'
        item = CategoryItem(
            id=gen_uuid(url),
            name=name,
            url=url,
            children=[]
        )
        if 'children' in config.keys():
            child_config = config['children']
            self.extract_children(item, node, child_config)
        yield item
