import os

config_category = {
    'site_name': 'An Phát PC',
    'site_url': 'https://www.anphatpc.com.vn',
    'settings': {
        'FILENAME': './scrapy_project/results/category/anphatpc_categories.json',
        'ITEM_PIPELINES': {
            'scrapy_project.pipelines.JsonWriterPipeline': 200
        }
    },
    'config_crawler': {
        'selector': 'div#nav_vertical > ul > li',
        'name': 'a::text',
        'url': 'a::attr(href)',
        'children': {
            'selector': 'div.sub_nav > div.box_cate',
            'name': 'a.sub1::text',
            'url': 'a.sub1::attr(href)',
            'children': {
                'selector': 'a.sub2',
                'name': '::text',
                'url': '::attr(href)',
            }
        }
    }
}

config_product = {
    'site_name': 'An Phát PC',
    'site_url': 'https://www.anphatpc.com.vn',
    'file_category': os.path.join(os.path.dirname(__file__), 'anphatpc_sample.json'),
    'settings': {
        'FILENAME': './scrapy_project/results/product/anphatpc_products.json',
        'ITEM_PIPELINES': {
            'scrapy_project.pipelines.JsonWriterPipeline': 200
        }
    },
    'config_crawler': {
        'next_page': '',
        'link_product': 'div.product-list-2019 > div > div.p-container-2019 > a::attr(href)',
        'fields': {
            'name': 'div#product_detail > div:first-child > h1::text',
            'price': 'div#product_detail > div:first-child > div#overview > div.price-detail b.price::text',
            'original_price': 'div#product_detail > div:first-child > div#overview > div.price-detail span.old-price::text',
            'image': 'div#product_detail > div:first-child > div#widget div#img_large > a::attr(href)'
        }
    }
}
