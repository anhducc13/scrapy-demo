import os

config_category = {
    'site_name': 'Điện máy chợ lớn',
    'site_url': 'https://dienmaycholon.vn',
    'settings': {
        'FILENAME': './scrapy_project/results/category/dienmaycholon_categories.json',
        'ITEM_PIPELINES': {
            'scrapy_project.pipelines.JsonWriterPipeline': 200
        }
    },
    'config_crawler': {
        'selector': 'ul.nav_maincate > li',
        'name': 'a::attr(title)',
        'url': 'a::attr(href)',
        'children': {
            'selector': 'div.menu_child > ul > li',
            'name': 'a::text',
            'url': 'a::attr(href)'
        }
    }
}

config_product = {
    'site_name': 'Điện máy chợ lớn',
    'site_url': 'https://dienmaycholon.vn',
    'file_category': os.path.join(os.path.dirname(__file__), 'dienmaycholon_sample.json'),
    'settings': {
        'FILENAME': './scrapy_project/results/product/dienmaycholon_products.json',
        'ITEM_PIPELINES': {
            'scrapy_project.pipelines.JsonWriterPipeline': 200
        }
    },
    'config_crawler': {
        'next_page': 'div.paging > a::text*="Next"::attr(href)',
        'link_product': 'div.item_product > div.pro_infomation > a::attr(href)',
        'fields': {
            'name': 'h1.product_name::text',
            'price': 'div.box_price > strong.price_sale::text',
            'original_price': 'div.box_price > strong.price_market::text',
            'image': 'div.img_main > a.zoom_main > img::attr(val)'
        }
    }
}
