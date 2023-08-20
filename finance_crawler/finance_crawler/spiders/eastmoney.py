import scrapy
from finance_crawler.items import EastMoneyFundItem


class EastMoneySpider(scrapy.Spider):
    name = 'eastmoney'
    login_url = 'http://eastmoney.com/login'  # 这是一个示例URL，实际URL可能不同
    start_urls = ['http://eastmoney.com/funds']  # 同上

    def start_requests(self):
        return [scrapy.FormRequest(
            self.login_url,
            formdata={'username': 'YOUR_USERNAME', 'password': 'YOUR_PASSWORD'},
            callback=self.after_login
        )]

    def after_login(self, response):
        # 检查是否登录成功，这通常是检查某些特定文本或URL重定向
        if "login success" in response.text:  # 示例文本
            for url in self.start_urls:
                yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        item = EastMoneyFundItem()
        # 使用XPath或CSS选择器来提取信息
        # ...
        yield item
