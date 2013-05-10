# -*- coding: utf-8 -*-
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from mbot.items import MovieInfo

import sqlite3
from os import path
from scrapy import signals
from scrapy.xlib.pydispatch import dispatcher
import re

movie_link_xpath="//div[@class='pl2']/a/@href"      #search movie url
this_page_num_xpath = "//span[@class='thispage']/text()"

class DmozSpider(BaseSpider):
    name = "db"
    allowed_domains = []
    startYear = 2013
    #endYear = 1980
    endYear = 2000
    #start_urls =  ['http://movie.douban.com/tag/'+str(i) for i in range(startYear, endYear,-1)]
    start_urls =  ['http://movie.douban.com/subject/2127034/','http://movie.douban.com/subject/6021916/']    
    allruls = [];    
    filename = '-data.db'
 
    def __init__(self):
        self.conn = None
        dispatcher.connect(self.initialize, signals.engine_started)
        dispatcher.connect(self.finalize, signals.engine_stopped)
        
    def initialize(self):
        self.conn = sqlite3.connect(self.filename)
 
    def finalize(self):
        if self.conn is not None:
            self.conn.commit()
            self.conn.close()
            self.conn = None

    def set_item(self, i, s, v):
        if v:
            i[s] = v[0]
        else:
            i[s] = ""

    def creat_item(self, hxs, url):
        item = MovieInfo()
        item["douban_url"] = url
        item["name"] = hxs.select("//h1/span/text()").extract()[0]
        item["imgae_url"] = hxs.select(u"//div[@id='mainpic']//img/@src").extract()[0]
        #infos = hxs.select("//div[@id='info']/span").extract()
        item["daoyan"] = hxs.select(u"//*[text()='导演']/following-sibling::*/text()").extract()
        item["bianju"] = hxs.select(u"//*[text()='编剧']/following-sibling::*/text()").extract()
        item["zhuyan"] = hxs.select(u"//*[text()='主演']/following-sibling::*/text()").extract()
        item["leixing"] = hxs.select(u"//*[@id='info']/* \
        [position() > (count(//*[text()='类型:']/preceding-sibling::*) + 1) and \
        position() < count(//*[text()='类型:']/following-sibling::br[1]/preceding-sibling::*)+1 ]/text()").extract()
        self.set_item(item, "quyu", hxs.select(u"//div[@id='info']").re(u'制片国家/地区:</span>([^<]*)'))
        self.set_item(item, "yuyan", hxs.select(u"//div[@id='info']").re(u'语言:</span>([^<]*)'))
        self.set_item(item, "date", hxs.select(u"//div[@id='info']/span[@property='v:initialReleaseDate']/@content").extract())
        self.set_item(item, "runtime", hxs.select(u"//div[@id='info']/span[@property='v:runtime']/@content").extract())
        self.set_item(item, "pingfen", hxs.select(u"//strong[@property='v:average']/text()").extract())
        self.set_item(item, "ping_num", hxs.select(u"//span[@property='v:votes']/text()").extract())
         
        item["other_name"] = []
        result = re.match("([^A-Za-z ]*) (.*)", item["name"])
        if result and result.groups() >= 2:
            item["other_name"].append(result.groups()[0])
            item["other_name"].append(result.groups()[1])
        names_list = hxs.select(u"//div[@id='info']").re(u'又名:</span>([^<]*)')
        #处理多个名字
        if names_list :   
            names = names_list[0]
            names = names.replace(u"(港)", "")
            names = names.replace(u"(台)", "")
            item["other_name"].extend(names.split(" / "))
        
        disp = hxs.select(u"//span[@property='v:summary']").extract()
        if disp :
            item["description"] = disp[0]
        disp = hxs.select(u"//span[@class='all hidden']").extract()
        if disp :
            item["description"] = disp[0]       
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
            if thispage:
                next_url_xpath = "//div[@class='paginator']/a[text()>" + str(thispage[0]) + "]/@href"
                next_url = hxs.select(next_url_xpath).extract() 
                if next_url:
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

