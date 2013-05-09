# -*- coding: utf-8 -*-
import sqlite3
from os import path
 
from scrapy import signals
from scrapy.xlib.pydispatch import dispatcher


class SQLiteStorePipeline(object):
    """A pipeline for filtering out items which contain certain words in their
    description"""
    filename = 'data.db'
 
    def __init__(self):
        self.conn = None
        dispatcher.connect(self.initialize, signals.engine_started)
        dispatcher.connect(self.finalize, signals.engine_stopped)
        
    def initialize(self):
        if path.exists(self.filename):
            self.conn = sqlite3.connect(self.filename)
        else:
            self.conn = self.create_table(self.filename)
 
    def finalize(self):
        if self.conn is not None:
            self.conn.commit()
            self.conn.close()
            self.conn = None
 
    def create_table(self, filename):
        conn = sqlite3.connect(filename)
        #conn.execute(u"create table moive( id int identity(1, 1) not null primary key, 名字  text, 导演  text, 豆瓣链接  text, 描述  text)")
        #conn.commit()
        return conn

    def process_item(self, item, spider):
        item.pr()
        
        
        return item
