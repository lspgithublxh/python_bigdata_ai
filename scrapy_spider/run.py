from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from spiders.no1spider import no1spider
from spiders.no2spider import no2spider

settings = get_project_settings()
process = CrawlerProcess(settings=settings)
# process.crawl(no1spider)
process.crawl(no2spider)
process.start()
