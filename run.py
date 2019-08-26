import copy
from scrapy.crawler import CrawlerProcess
from scrapy.utils import project
from scrapy_project.spiders.category import CategoriesSpider
from scrapy_project.spiders.product import ProductsSpider
from scrapy_project.constants import dienmaycholon, anphatpc


def run_categories():
    config_category = copy.deepcopy(anphatpc.config_category)
    settings = project.get_project_settings()
    settings.update(config_category.pop('settings', {}))
    process = CrawlerProcess(
        settings=settings
    )
    process.crawl(CategoriesSpider, **config_category)
    process.start()


def run_products():
    config_product = copy.deepcopy(anphatpc.config_product)
    settings = project.get_project_settings()
    settings.update(config_product.pop('settings', {}))
    process = CrawlerProcess(
        settings=settings
    )
    process.crawl(ProductsSpider, **config_product)
    process.start()


if __name__ == "__main__":
    run_products()
