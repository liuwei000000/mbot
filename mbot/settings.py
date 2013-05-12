# Scrapy settings for dirbot project

SPIDER_MODULES = ['mbot.spiders']
NEWSPIDER_MODULE = 'mbot.spiders'
DEFAULT_ITEM_CLASS = 'mbot.items.MovieInfo'

ITEM_PIPELINES = ['mbot.pipelines.SQLiteStorePipeline']
DOWNLOAD_DELAY = 0.05
#HTTPCACHE_ENABLED = True
#HTTPCACHE_DIR = 'scrapy-cache'
LOG_LEVEL = "INFO"
DOWNLOAD_TIMEOUT = 5
USER_AGENT = u"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; AskTB5.6)"

