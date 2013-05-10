# -*- coding: utf-8 -*-
import sqlite3
from os import path
 
from scrapy import signals
from scrapy.xlib.pydispatch import dispatcher


class SQLiteStorePipeline(object):
    """A pipeline for filtering out items which contain certain words in their
    description"""
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
 
    def create_table(self, filename):
        conn = sqlite3.connect(filename)
        #conn.execute(u"create table moive( id int identity(1, 1) not null primary key, 名字  text, 导演  text, 豆瓣链接  text, 描述  text)")
        #conn.commit()
        return conn

    def sql_dianying_yinren(self, dianying_id, list_yingren):
        for item in list_yingren:
            x = conn.execute(u'select "演员id" from "演员id-姓名" where "姓名"%s";' % item).fetchone()
            if x:
                pass
            
    def insert_dianying(self, item):
        self.conn.execute(u'insert into 电影信息(名称,豆瓣链接,发行地区,语言,描述,封面链接,上映日期,时长,评分,评分人数) \
          values(?,?,?,?,?,?,?,?,?,?)',(item["name"], item["douban_url"], item["quyu"], item["yuyan"], item["description"],\
                                          item["imgae_url"], item["date"], item["runtime"], item["pingfen"], item["ping_num"])).fetchone()
        x = self.conn.execute("select last_insert_rowid()").fetchone()
        if x:
            return x[0]
        else:
            exit()
        

    def process_item(self, item, spider):
        item.pr()
        dianying_id = self.insert_dianying(item)
        #处理影人
        
        #
        
        
        return item


"""
CREATE TABLE "电影信息" (
  [id] INTEGER PRIMARY KEY AUTOINCREMENT, 
  [名称] VARCHAR(256) NOT NULL, 
  [豆瓣链接] VARCHAR(1024) NOT NULL, 
  [发行地区] VARCHAR(64), 
  [语言] VARCHAR(64), 
  [描述] VARCHAR, 
  [封面链接] VARCHAR(1024), 
  [上映日期] DATE, 
  [时长] INT, 
  [评分] DECIMAL, 
  [评分人数] INT);

CREATE INDEX [豆瓣链接索引] ON "电影信息" ([豆瓣链接]);


CREATE TABLE "别名-电影id" (
  [电影名称] VARCHAR(256) NOT NULL, 
  [电影id] BIGINT NOT NULL REFERENCES [电影信息]([id]));

CREATE INDEX [电影名称索引] ON "别名-电影id" ([电影名称]);


CREATE TABLE "影人信息" (
  [id] INTEGER PRIMARY KEY AUTOINCREMENT, 
  [出生年月] DATE);


CREATE TABLE "演员id-姓名" (
  [演员id] BIGINT NOT NULL REFERENCES "影人信息"([id]), 
  [姓名] VARCHAR(256) NOT NULL);

CREATE INDEX [姓名索引] ON "演员id-姓名" ([姓名]);


CREATE TABLE "电影id-导演id" (
  [电影id] BIGINT REFERENCES [电影信息]([id]) NOT NULL, 
  [导演id] BIGINT REFERENCES [影人信息]([id]) NOT NULL);


CREATE TABLE "电影id-演员id" (
  [电影id] BIGINT REFERENCES "电影信息"([id]) NOT NULL, 
  [演员id] BIGINT REFERENCES "影人信息"([id]) NOT NULL);


CREATE TABLE "电影id-编剧id" (
  [电影id] BIGINT REFERENCES [电影信息]([id]) NOT NULL, 
  [编剧id] BIGINT REFERENCES [影人信息]([id]) NOT NULL);


CREATE TABLE "类型-电影id" (
  [类型] VARCHAR(64) NOT NULL, 
  [电影id] BIGINT NOT NULL REFERENCES [电影信息]([id]));

CREATE INDEX [类型索引] ON "类型-电影id" ([类型]);

"""