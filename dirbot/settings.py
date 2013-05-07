# Scrapy settings for dirbot project

SPIDER_MODULES = ['dirbot.spiders']
NEWSPIDER_MODULE = 'dirbot.spiders'
DEFAULT_ITEM_CLASS = 'dirbot.items.Website'

ITEM_PIPELINES = ['dirbot.pipelines.FilterWordsPipeline']
DOWNLOAD_DELAY = 0.05
HTTPCACHE_ENABLED = True
HTTPCACHE_DIR = 'C:/scrapy-cache/filedbm'