import re
import json
import scrapy
from ..utils import gen_uuid
from ..items import ProductItem


class ProductsSpider(scrapy.Spider):
    name = 'product'

    def __init__(self, *args, **kwargs):
        super(ProductsSpider, self).__init__(*args, **kwargs)
        self.site_url = kwargs.get('site_url', '')
        self.site_name = kwargs.get('site_name', '')
        self.file_category = kwargs.get('file_category', '')
        self.config_crawler = kwargs.get('config_crawler', dict())

    def start_requests(self):
        with open(self.file_category) as cats:
            category_tree = json.load(cats)
        yield from self.visit_category_tree(category_tree)

    def visit_category_tree(self, category_tree):
        for category in category_tree:
            cat_child = category.get('children', [])
            if len(cat_child) > 0:
                yield from self.visit_category_tree(cat_child)
            else:
                yield scrapy.Request(
                    category['url'],
                    callback=self.visit_first_page,
                    cb_kwargs=dict(
                        cat_id=category['id']
                    )
                )

    def visit_first_page(self, response, cat_id):
        list_product_link = response.css(self.config_crawler['link_product']).getall()
        for product_link in list_product_link:
            yield scrapy.Request(
                f'{self.site_url}{product_link}',
                callback=self.parse,
                meta={
                    'cat_id': cat_id
                }
            )

    def parse(self, response):
        fields = self.config_crawler['fields']
        p_id = gen_uuid(response.url)
        cat_id = response.meta['cat_id']
        name = response.css(fields['name']).get()
        price = response.css(fields['price']).get()
        if isinstance(price, str):
            try:
                price = int(re.sub(r'[^0-9]', '', price))
            except ValueError:
                price = None
        else:
            price = None

        original_price = response.css(fields['original_price']).get()
        if isinstance(original_price, str):
            try:
                original_price = int(re.sub(r'[^0-9]', '', original_price))
            except ValueError:
                original_price = None
        else:
            original_price = None
        image = f'{self.site_url}{response.css(fields["image"]).get()}'
        yield ProductItem(
            id=p_id,
            cat_id=cat_id,
            url=response.url,
            name=name,
            price=price,
            original_price=original_price,
            image=image
        )
