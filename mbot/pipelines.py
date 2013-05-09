# -*- coding: utf-8 -*-
from scrapy.xlib.pydispatch import dispatcher
from scrapy.exceptions import DropItem


class SQLiteStorePipeline(object):
    """A pipeline for filtering out items which contain certain words in their
    description"""

    def process_item(self, item, spider):
        print '==================================='
        for k in item:
            if isinstance(item[k], list):
                print "%s :"% k,
                for i in item[k]:
                    print i,
                print
            else:
                print "%s :"% k, item[k]
        print '####################################'
        
        
        return item
