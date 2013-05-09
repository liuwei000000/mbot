# -*- coding: utf-8 -*-
from scrapy.item import Item, Field

class MovieInfo(Item):

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
    
    def pr(self):
        print '==================================='
        for k in self:
            if isinstance(self[k], list):
                print "%s :"% k,
                for i in self[k]:
                    print i,
                print
            else:
                print "%s :"% k, self[k]
        print '####################################'
    

