# coding:utf8
import requests
import random
from lxml import etree
import time
import csv
import codecs
# 提供ua信息的的包
from fake_useragent import UserAgent


class LianjiaSpider(object):
    def __init__(self):
        self.url = 'https://sh.lianjia.com/ershoufang/chongming/pg{}/'
        # 计数，请求一个页面的次数，初始值为1
        self.blog = 1

    # 随机取一个UA
    def get_header(self):
        # 实例化ua对象
        ua = UserAgent()
        headers = {'User-Agent': ua.random}
        return headers

    # 发送请求
    def get_html(self, url):
        # 在超时间内，对于失败页面尝试请求三次
        if self.blog <= 3:
            try:
                res = requests.get(url=url, headers=self.get_header(), timeout=3)
                html = res.text
                return html
            except Exception as e:
                print(e)
                self.blog += 1
                self.get_html(url)

    # 解析提取数据
    def parse_html(self, url):
        html = self.get_html(url)
        if html:
            p = etree.HTML(html)
            # 基准xpath表达式-30个房源节点对象列表
            h_list = p.xpath('//ul[@class="sellListContent"]/li[@class="clear LOGVIEWDATA LOGCLICKDATA"]')
            # 所有列表节点对象
            for h in h_list:
                item = {}
                # 名称
                name_list = h.xpath('.//a[@data-el="region"]/text()')
                # 判断列表是否为空
                item['name'] = name_list[0] if name_list else None
                # 户型+面积+方位+是否精装..['2室1厅 | 88.62平米 | 北 南 | 简装 | 顶层(共6层) | 2004年建 | 板楼']
                info_list = h.xpath('.//div[@class="houseInfo"]/text()')
                # 判断列表是否为空
                if info_list:
                    L = info_list[0].split('|')
                    # ['2室1厅 ', ' 88.62平米 ', ' 北 南 ', ' 简装 ', ' 顶层(共6层) ', ' 2004年建 ', ' 板楼']
                    if len(L) >= 5:
                        item['model'] = L[0].strip()
                        item['area'] = L[1].strip()
                        item['direction'] = L[2].strip()
                        item['fitment'] = L[3].strip()
                        item['floor'] = L[4].strip()
                # 区域+总价+单价
                address_list = h.xpath('.//div[@class="positionInfo"]/a/text()')
                # item['address'] = address_list[1].strip() if address_list else None
                item['address'] = '崇明'
                total_list = h.xpath('.//div[@class="totalPrice totalPrice2"]/span/text()')
                item['total_list'] = total_list[0].strip() if total_list else None
                price_list = h.xpath('.//div[@class="unitPrice"]/span/text()')
                item['price_list'] = price_list[0].strip() if price_list else None
                print(item)
                data = [item]
                data_write_csv('ershoufang.csv', data)

    # 入口函数
    def run(self):
        try:
            for i in range(1, 13):
                url = self.url.format(i)
                self.parse_html(url)
                time.sleep(random.randint(1, 3))
                # 每次抓取一页要初始化一次self.blog
                self.blog = 1
        except Exception as e:
            print('发生错误', e)


def data_write_csv(file_name, datas):
    # name,model,area,direction,fitment,floor,address,total_list,price_list
    header = ['name', 'model', 'area', 'direction', 'fitment', 'floor', 'address', 'total_list', 'price_list']
    with open(file_name, 'a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=header)  # 提前预览列名，当下面代码写入数据时，会将其一一对应。
        # writer.writeheader()  # 写入列名
        writer.writerows(datas)  # 写入数据


if __name__ == '__main__':
    spider = LianjiaSpider()
    spider.run()
