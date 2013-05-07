from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from dirbot.items import Website


class DmozSpider(BaseSpider):
    name = "douban"
    allowed_domains = []
    startYear = 2013
    endYear = 1980
    start_urls =  ['http://movie.douban.com/tag/'+str(i) for i in range(startYear, endYear,-1)]

    def parse(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html

        @url http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
        @scrapes name
        """
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('//ul[@class="directory-url"]/li')
        items = []

        for site in sites:
            item = Website()
            item['name'] = site.select('a/text()').extract()
            item['url'] = site.select('a/@href').extract()
            item['description'] = site.select('text()').re('-\s([^\n]*?)\\n')
            items.append(item)

        return items
