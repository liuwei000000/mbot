# Scrapy settings for dirbot project

SPIDER_MODULES = ['dirbot.spiders']
NEWSPIDER_MODULE = 'dirbot.spiders'
DEFAULT_ITEM_CLASS = 'dirbot.items.MovieInfo'

ITEM_PIPELINES = ['dirbot.pipelines.SQLiteStorePipeline']
DOWNLOAD_DELAY = 0.07
HTTPCACHE_ENABLED = True
HTTPCACHE_DIR = 'C:/scrapy-cache/filedbm'
LOG_LEVEL = "INFO"
DOWNLOAD_TIMEOUT = 5