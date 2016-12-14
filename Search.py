# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from lxml import etree
from urllib import request
import re
class UrlSearch:
    def parseContent(self,content):
        #存储内容网址
        print("正在解析页面url")
        content_urls = []
        tree = etree.HTML(content)
        records = tree.xpath("//div[@id = 'content_left']/div[@id]/h3/a/@href")#获得url
        if(records == None):
            print("records is NoneType")
        for record in records:
            content_urls.append(record)
        return content_urls
    
    def parsePage(self,content):
        #存储页面网址
        page_urls = []
        tree = etree.HTML(content)
        records = tree.xpath("//div[@id = 'page']/a/@href")#获得url
        if(type(records) is None or records == None):
            print("records is NoneType")
        for record in records:
            page_urls.append(record)
        return page_urls