import scrapy
from ..items import CategoryItem


class CategoriesSpider(scrapy.Spider):
    name = 'categories'

    def __init__(self, *args, **kwargs):
        super(CategoriesSpider, self).__init__(*args, **kwargs)
        self.site_url = kwargs['site_url']
        self.site_name = kwargs['site_name']
        self.start_urls = [self.site_url]
        self.config_crawler = kwargs['config_crawler']

    def parse(self, response):
        category = CategoryItem(name=self.site_name, url=self.site_url)
        self.extract_children(category, response, self.config_crawler)
        yield category

    def extract_children(self, item, node, config):
        for child_node in node.css(config['selector']):
            for child in self.extract_items(child_node, config):
                item.add_child(child)

    def extract_items(self, node, config):
        name = node.css(config['name']).get().strip()
        postfix = node.css(config["url"]).get().strip()
        if postfix.startswith("http"):
            prefix = ''
        else:
            prefix = self.site_url
        url = f'{prefix}{postfix}'
        item = CategoryItem(name=name, url=url)
        if 'children' in config.keys():
            child_config = config['children']
            self.extract_children(item, node, child_config)
        yield item
