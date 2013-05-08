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
    shangying_time = Field()
    pingfen = Field()
    imdb_url = Field()
    description = Field()
    

