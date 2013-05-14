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

class DmozSpider(BaseSpider):
    name = "db"
    allowed_domains = []
    startYear = 2013
    #endYear = 1980
    endYear = 1800
   
    tables = [u'\u7231\u60c5',
 u'\u559c\u5267',
 u'\u52a8\u753b',
 u'\u7ecf\u5178',
 u'\u79d1\u5e7b',
 u'\u52a8\u4f5c',
 u'\u5267\u60c5',
 u'\u9752\u6625',
 u'\u60ac\u7591',
 u'\u60ca\u609a',
 u'\u72af\u7f6a',
 u'\u7eaa\u5f55\u7247',
 u'\u6587\u827a',
 u'\u52b1\u5fd7',
 u'\u641e\u7b11',
 u'\u6050\u6016',
 u'\u6218\u4e89',
 u'\u77ed\u7247',
 u'\u9b54\u5e7b',
 u'\u9ed1\u8272\u5e7d\u9ed8',
 u'\u52a8\u753b\u77ed\u7247',
 u'\u60c5\u8272',
 u'\u4f20\u8bb0',
 u'\u7ae5\u5e74',
 u'\u611f\u4eba',
 u'\u66b4\u529b',
 u'\u97f3\u4e50',
 u'\u540c\u5fd7',
 u'\u9ed1\u5e2e',
 u'\u5973\u6027',
 u'\u6d6a\u6f2b',
 u'\u5bb6\u5ead',
 u'\u53f2\u8bd7',
 u'\u7ae5\u8bdd',
 u'cult',
 u'\u70c2\u7247',
 u'\u7f8e\u56fd',
 u'\u9999\u6e2f',
 u'\u65e5\u672c',
 u'\u4e2d\u56fd',
 u'\u82f1\u56fd',
 u'\u6cd5\u56fd',
 u'\u97e9\u56fd',
 u'\u53f0\u6e7e',
 u'\u610f\u5927\u5229',
 u'\u5fb7\u56fd',
 u'\u5185\u5730',
 u'\u6cf0\u56fd',
 u'\u897f\u73ed\u7259',
 u'\u5370\u5ea6',
 u'\u6b27\u6d32',
 u'\u52a0\u62ff\u5927',
 u'\u6fb3\u5927\u5229\u4e9a',
 u'\u4fc4\u7f57\u65af',
 u'\u4f0a\u6717',
 u'\u4e2d\u56fd\u5927\u9646',
 u'\u745e\u5178',
 u'\u5df4\u897f',
 u'\u7231\u5c14\u5170',
 u'\u6ce2\u5170',
 u'\u6377\u514b',
 u'\u4e39\u9ea6',
 u'\u963f\u6839\u5ef7',
 u'\u6bd4\u5229\u65f6',
 u'\u58a8\u897f\u54e5',
 u'\u5965\u5730\u5229',
 u'\u8377\u5170',
 u'\u5308\u7259\u5229',
 u'\u571f\u8033\u5176',
 u'\u65b0\u52a0\u5761',
 u'\u65b0\u897f\u5170',
 u'\u4ee5\u8272\u5217',
 u'\u5bab\u5d0e\u9a8f',
 u'\u5468\u661f\u9a70',
 u'\u738b\u5bb6\u536b',
 u'JohnnyDepp',
 u'\u5ca9\u4e95\u4fca\u4e8c',
 u'\u6881\u671d\u4f1f',
 u'\u5f20\u56fd\u8363',
 u'\u5c3c\u53e4\u62c9\u65af\xb7\u51ef\u5947',
 u'\u5f20\u827a\u8c0b',
 u'\u5218\u5fb7\u534e',
 u'\u51af\u5c0f\u521a',
 u'\u65af\u76ae\u5c14\u4f2f\u683c',
 u'\u6210\u9f99',
 u'\u675c\u742a\u5cf0',
 u'\u674e\u8fde\u6770',
 u'\u59dc\u6587',
 u'\u5f90\u514b',
 u'\u674e\u5b89',
 u'\u5468\u8fc5',
 u'TimBurton',
 u'\u6842\u7eb6\u9541',
 u'\u5468\u6da6\u53d1',
 u'\u5965\u9edb\u4e3d\xb7\u8d6b\u672c',
 u'\u91d1\u57ce\u6b66',
 u'\u5f90\u9759\u857e',
 u'\u8212\u6dc7',
 u'AnneHathaway',
 u'\u5434\u5f66\u7956',
 u'JimCarrey',
 u'\u5f6d\u6d69\u7fd4',
 u'bradpitt',
 u'\u6c64\u59c6\xb7\u6c49\u514b\u65af',
 u'WillSmith',
 u'\u9ed1\u6cfd\u660e',
 u'\u5e0c\u533a\u67ef\u514b',
 u'\u5f20\u67cf\u829d']
        
    #start_urls =  [u'http://movie.douban.com/tag/cult']
    #start_urls = ['http://movie.douban.com/subject/4132890/']
    #start_urls =  ['http://movie.douban.com/tag/'+str(i) for i in range(startYear, endYear,-1)]
    start_urls =  ['http://movie.douban.com/tag/'+ t for t in tables]
    #start_urls =  ['http://movie.douban.com/subject/2127034/','http://movie.douban.com/subject/6021916/']    
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
            names = names.replace(u"(港/台)", "") #注意数据中的含有该字段的数据,要删除
            item["other_name"].extend(names.split(" / "))
        
        item["description"] = ""
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
            print response.url ,
            yield self.creat_item(hxs, response.url)
        
        if 'http://movie.douban.com/tag' in response.url:
            """
            from tag dir to movie url
            """
            print response.url
            #或者所有电影的链接
            sites = hxs.select(movie_link_xpath).extract()
            for site in sites:
                print site ,
                if not self.conn.execute(u'select * from "电影信息" where "豆瓣链接"="%s";' % site).fetchone():
                    print
                    yield Request(url=site, callback=self.parse_detail)
                else:
                    print "Exsit!"
        
            #获取下一页的分类页面链接
            next_url = hxs.select("//span[@class='next']/a/@href").extract()
            if next_url:
                yield Request(url=next_url[0], callback=self.parse)
        
    def parse_detail(self, response):
        """
        parse movie info
        """
        if 'http://movie.douban.com/subject' not in response.url:
            return

        if self.conn.execute(u'select * from "电影信息" where "豆瓣链接"="%s";' % response.url).fetchone():
            print response.url , "Exsit!"
            return
       
        hxs = HtmlXPathSelector(response)
        print response.url
        yield self.creat_item(hxs, response.url)

