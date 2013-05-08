# -*- coding: utf-8 -*-
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request

from dirbot.items import MovieInfo

movie_link_xpath="//div[@class='pl2']/a/@href"      #search movie url
this_page_num_xpath = "//span[@class='thispage']/text()"

class DmozSpider(BaseSpider):
    name = "douban"
    allowed_domains = []
    startYear = 1922
    #endYear = 1980
    endYear = 1921
    #start_urls =  ['http://movie.douban.com/tag/'+str(i) for i in range(startYear, endYear,-1)]
    start_urls =  ['http://movie.douban.com/subject/2127034/','http://movie.douban.com/subject/6021916/']    
    allruls = [];

    def creat_item(self, hxs, url):
        item = MovieInfo()
        item["douban_url"] = url
        item["name"]= hxs.select("//h1/span/text()").extract()[0]
        infos = hxs.select("//div[@id='info']/span").extract()
        item["daoyan"] = hxs.select(u"//*[text()='导演']/following-sibling::*/text()").extract()
        item["bianju"] = hxs.select(u"//*[text()='编剧']/following-sibling::*/text()").extract()
        item["zhuyan"] = hxs.select(u"//*[text()='主演']/following-sibling::*/text()").extract()
        
        #hxs.select(u"//*[text()='类型:']/following-sibling::*")
        
        
        return item

    def parse(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html

        @scrapes name
        """
        
        hxs = HtmlXPathSelector(response)
        if 'http://movie.douban.com/subject' in response.url:
            print response.url
            yield self.creat_item(hxs, response.url)
        
        if 'http://movie.douban.com/tag' in response.url:
            """
            from tag dir to movie url
            """
            #或者所有电影的链接
            sites = hxs.select(movie_link_xpath).extract()
            for site in sites:
                yield Request(url=site, callback=self.parse_detail)
        
            #获取下一页的分类页面链接
            thispage = hxs.select(this_page_num_xpath).extract()
            if thispage != []:
                next_url_xpath = "//div[@class='paginator']/a[text()>" + str(thispage[0]) + "]/@href"
                next_url = hxs.select(next_url_xpath).extract() 
                if next_url != []:
                    yield Request(url=next_url[0], callback=self.parse)
        
    def parse_detail(self, response):
       """
       parse movie info
       """
       if 'http://movie.douban.com/subject' not in response.url:
           return
       
       hxs = HtmlXPathSelector(response)
       print response.url
       yield creat_item(hxs, response.url)

