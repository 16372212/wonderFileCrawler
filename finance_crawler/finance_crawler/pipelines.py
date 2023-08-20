import pymysql

from finance_crawler.items import PbcPolicyItem, EastMoneyFundItem


class FinanceCrawlerPipeline:

    def open_spider(self, spider):
        self.connection = pymysql.connect(
            host='localhost', user='root', password='password', db='finance_db'
        )
        self.cursor = self.connection.cursor()

    def close_spider(self, spider):
        self.connection.close()

    def process_item(self, item, spider):
        if isinstance(item, PbcPolicyItem):
            # save to pbc_policy_table
            pass
        elif isinstance(item, EastMoneyFundItem):
            # save to eastmoney_fund_table
            pass
        return item
