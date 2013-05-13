# -*- coding: utf-8 -*-
import random
from scrapy.contrib.downloadermiddleware.cookies import CookiesMiddleware

class DBDownloaderMiddleware(CookiesMiddleware):
    
    cookie_list =[\
                  'bid="W8zbiQYf1HE"; __utma=30149280.1106066029.1346389592.1368000298.1368410197.13;  __utmz=30149280.1368000298.12.7.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=sql%20no%20sql; __utmv=30149280.7246;  ll="108288"; viewed="1439694_3440402"; __utma=223695111.819414762.1355465623.1355465623.1355705472.2;  __utmz=223695111.1355465623.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmb=30149280.26.10.1368410197;  __utmc=30149280; dbcl2="72467264:jqkHFCI+DB0"; ck="MRr6"',
                  'bid="W8zbiQYf1HE"; __utma=30149280.1106066029.1346389592.1368000298.1368410197.13;  __utmz=30149280.1368000298.12.7.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=sql%20no%20sql; __utmv=30149280.7246;  ll="108288"; viewed="1439694_3440402"; __utma=223695111.819414762.1355465623.1355465623.1355705472.2;  __utmz=223695111.1355465623.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmb=30149280.30.10.1368410197;  __utmc=30149280; dbcl2="72467338:w9SdKscmt0A"; ck="rcnM"',
                  'bid="W8zbiQYf1HE"; __utma=30149280.1106066029.1346389592.1368000298.1368410197.13; __utmz=30149280.1368000298.12.7.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=sql%20no%20sql; __utmv=30149280.7246; ll="108288"; viewed="1439694_3440402"; __utmb=30149280.36.10.1368410197; __utmc=30149280; dbcl2="72467898:rGx9zyfZkXM"; ck="rcnM"',
                  'bid="W8zbiQYf1HE"; __utma=30149280.1106066029.1346389592.1368000298.1368410197.13; __utmz=30149280.1368000298.12.7.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=sql%20no%20sql; __utmv=30149280.7246; ll="108288"; viewed="1439694_3440402"; __utmb=30149280.38.10.1368410197; __utmc=30149280; dbcl2="72468329:mnebpinfBVw"; ck="2ckS"',
                  'bid="W8zbiQYf1HE"; __utma=30149280.1106066029.1346389592.1368000298.1368410197.13; __utmz=30149280.1368000298.12.7.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=sql%20no%20sql; __utmv=30149280.7246; ll="108288"; viewed="1439694_3440402"; __utmb=30149280.40.10.1368410197; __utmc=30149280; dbcl2="72468383:C+9El+gs7KY"; ck="45oG"',
                  'bid="W8zbiQYf1HE"; __utma=30149280.1106066029.1346389592.1368000298.1368410197.13; __utmz=30149280.1368000298.12.7.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=sql%20no%20sql; __utmv=30149280.7246; ll="108288"; viewed="1439694_3440402"; __utmb=30149280.42.10.1368410197; __utmc=30149280; dbcl2="72468495:NqwOKUT08Fw"; ck="qd66"',
                  'bid="W8zbiQYf1HE"; __utma=30149280.1106066029.1346389592.1368000298.1368410197.13; __utmz=30149280.1368000298.12.7.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=sql%20no%20sql; __utmv=30149280.7246; ll="108288"; viewed="1439694_3440402"; __utmb=30149280.44.10.1368410197; __utmc=30149280; dbcl2="72468544:LH3ZyGpSLqU"; ck="ofa0"',
                  'bid="W8zbiQYf1HE"; __utma=30149280.1106066029.1346389592.1368000298.1368410197.13; __utmz=30149280.1368000298.12.7.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=sql%20no%20sql; __utmv=30149280.7246; ll="108288"; viewed="1439694_3440402"; __utmb=30149280.46.10.1368410197; __utmc=30149280; dbcl2="72468587:RnuB14ngbkA"; ck="B8mt"',
                  'bid="W8zbiQYf1HE"; __utma=30149280.1106066029.1346389592.1368000298.1368410197.13; __utmz=30149280.1368000298.12.7.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=sql%20no%20sql; __utmv=30149280.7246; ll="108288"; viewed="1439694_3440402"; __utmb=30149280.52.10.1368410197; __utmc=30149280; dbcl2="72468697:JilfnFALuro"; ck="ho4u"; RT=s=1368413185321&r=http%3A%2F%2Fmovie.douban.com%2Fsubject%2F6973376%2F',
                  'bid="W8zbiQYf1HE"; __utma=30149280.1106066029.1346389592.1368000298.1368410197.13; __utmz=30149280.1368000298.12.7.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=sql%20no%20sql; __utmv=30149280.7246; ll="108288"; viewed="1439694_3440402"; __utmb=30149280.56.10.1368410197; __utmc=30149280; dbcl2="72468742:YbOD471pXjY"; ck="XasE"; RT=s=1368413185321&r=http%3A%2F%2Fmovie.douban.com%2Fsubject%2F6973376%2F',
                  ]
    
    def process_request(self, request, spider):
        request.headers.setdefault('Cookie', random.choice(self.cookie_list))
    

