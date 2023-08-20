# 在 finance_crawler/spiders/pbc.py 中

import scrapy

class PbcSpider(scrapy.Spider):
    name = 'pbc'
    start_urls = ['http://www.pbc.gov.cn/redianzhuanti/118742/118714/119413/index.html']

    def parse(self, response):
        # 抓取页面上的信贷政策链接，并跟随这些链接
        # http://www.pbc.gov.cn/jinrongshichangsi/118742/118714/119413/index.html
        policy_links = response.css('a[href*="/jinrongshichangsi/147160/147289/"]::attr(href)').extract()

        # policy_links = response.css('a[href*="/jinrongshichangsi/147160/147289/"]:not([onclick="void(0)"])::attr(href)').extract()
        print("==========policy_links==========")
        print(response.text)
        print(policy_links)
        for link in policy_links:
            print("========link=======", link)
            yield response.follow(link, self.parse_policy)

    def parse_policy(self, response):
        title = response.css('title::text').extract_first().strip()
        source = response.css('#laiyuan::text').extract_first().strip()
        date_str = response.css('meta[name="页面生成时间"]::attr(content)').extract_first().strip().split(' ')[0]

        yield {
            'title': title,
            'source': source,
            'date': date_str
        }
