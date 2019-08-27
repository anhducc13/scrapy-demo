import copy
from scrapy.crawler import CrawlerProcess
from scrapy.utils import project
from scrapy_project.constants import dienmaycholon, anphatpc


def run_crawler(spider, config):
    c_config = copy.deepcopy(config)
    settings = project.get_project_settings()
    settings.update(c_config.pop('settings', {}))
    process = CrawlerProcess(
        settings=settings
    )
    process.crawl(spider, **c_config)
    process.start()


if __name__ == "__main__":
    # run_crawler('category', dienmaycholon.config_category)
    run_crawler('product', anphatpc.config_product)
