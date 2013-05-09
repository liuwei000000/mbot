# Scrapy settings for dirbot project

SPIDER_MODULES = ['mbot.spiders']
NEWSPIDER_MODULE = 'mbot.spiders'
DEFAULT_ITEM_CLASS = 'mbot.items.MovieInfo'

ITEM_PIPELINES = ['mbot.pipelines.SQLiteStorePipeline']
DOWNLOAD_DELAY = 0.07
HTTPCACHE_ENABLED = True
HTTPCACHE_DIR = 'scrapy-cache'
LOG_LEVEL = "INFO"
DOWNLOAD_TIMEOUT = 5