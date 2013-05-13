# Scrapy settings for dirbot project

SPIDER_MODULES = ['mbot.spiders']
NEWSPIDER_MODULE = 'mbot.spiders'
DEFAULT_ITEM_CLASS = 'mbot.items.MovieInfo'

ITEM_PIPELINES = ['mbot.pipelines.SQLiteStorePipeline']
RANDOMIZE_DOWNLOAD_DELAY = True
DOWNLOAD_DELAY = 0.1
CONCURRENT_ITEMS = 100
CONCURRENT_REQUESTS = 16
DNSCACHE_ENABLED = True

HTTPCACHE_ENABLED = True
HTTPCACHE_DIR = 'scrapy-cache'
LOG_LEVEL = "INFO"
DOWNLOAD_TIMEOUT = 5
USER_AGENT = u"Mozilla/5.0 (Windows NT 5.1; rv:20.0) Gecko/20100101 Firefox/20.0"
COOKIES_DEBUG = True

DOWNLOADER_MIDDLEWARES = {
    'mbot.middlewares.DBDownloaderMiddleware': 700,
    'scrapy.contrib.downloadermiddleware.cookies.CookiesMiddleware' : None
#    'scrapy.contrib.downloadermiddleware.defaultheaders.DefaultHeadersMiddleware': None,
    #'scrapy.contrib.downloadermiddleware.cookies.CookiesMiddleware': None,
}

"""
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3',
    "Cookie": 'bid="rBqMIkxG8Q8"; __utma=30149280.549343527.1367506937.1368283525.1368330801.6; __utmz=30149280.1367506937.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); ct=y; __utma=223695111.1425861623.1358599078.1368283525.1368330801.8; __utmz=223695111.1358599078.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); ll="100000"; ue="liuweiky@qq.com"; __utmv=30149280.5318; viewed="1300530_3006309_6011805_3534824"; __utmc=30149280; __utmc=223695111; RT=s=1368333630716&r=http%3A%2F%2Fmovie.douban.com%2Ftag%2F1923',
    "Connection": 'keep-alive'}"""
