import scrapy
from myscraper.items import MyscraperItem
from scrapy.http import Request

URL = 'http://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=230&page=%s'
start_page = 1

class MybotsSpider(scrapy.Spider):
    name = 'mybot'
    allowed_domains = ['naver.com']
    start_urls = [URL % start_page]
    
    def start_requests(self):
        
        for i in range(6): # 0, 1 ~ 9 -> 1 ~ 10
            yield Request(url=URL % (i + start_page), callback=self.parse)

    def parse(self, response):
        titles = response.xpath('//*[@id="main_content"]/div[2]/ul/li/dl/dt[2]/a/text()').extract()
        writers = response.css('.writing::text').extract()
        previews = response.css('.lede::text').extract()
        

        items = []
        # items에 XPATH, CSS를 통해 추출한 데이터를 저장 
        for idx in range(len(titles)):
            item = MyscraperItem()
            item['title'] = titles[idx].strip()
            item['writer'] = writers[idx]
            item['preview'] = previews[idx]

            items.append(item)

        return items