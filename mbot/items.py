# -*- coding: utf-8 -*-
from scrapy.item import Item, Field

class MovieInfo(Item):
    """str2name = {\
        "douban_url":u"豆瓣链接"，\
        "name":u"名称" ,\
                }"""
    douban_url = Field()
    name = Field()
    other_name = Field()
    daoyan = Field()
    bianju = Field()
    zhuyan = Field()
    leixing = Field()
    quyu = Field()
    yuyan = Field()
    date = Field()
    runtime = Field()
    pingfen = Field()
    imgae_url = Field()
    imdb_url = Field()
    description = Field()
    ping_num = Field()
    
    def pr(self):
        print '==================================='
        for k in self:
            if isinstance(self[k], list):
                print "%s :" % k,
                for i in self[k]:
                    print i.encode('gb18030'), ";" ,
                print
            else:
                print "%s :"% k, self[k].encode('gb18030')
        print '####################################'
    

