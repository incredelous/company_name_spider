# -*- coding: utf-8 -*-
from Spider import SentenceSpider
from Search import UrlSearch
from CompanyName import CompanyNameRecord
from Visit import VisitByBrowser
from urllib import parse
import time
company_name_file = "company_name.txt"
fp = open("raw_data.txt","a",encoding='utf-8')
if fp == None:
    print("open file data.txt error")        
sc = CompanyNameRecord()
vb = VisitByBrowser()
company_names = sc.GainCompanyName(company_name_file)
for company_name in company_names:
    print("目前正在搜索：" + company_name + "...")
    print("公司名称长度为" + str(len(company_name)))
    page = 1#页码
    search_word = company_name
    search_field = {'ie':'utf-8','wd':search_word}
    base_url = "http://www.baidu.com"
    search_url = base_url + "/s?" + parse.urlencode(search_field)
    content = vb.openurl(search_url)
    if content == None:
        continue
    us = UrlSearch()
    page_urls = us.parsePage(content)#找寻page页url
    print("第" + str(page) + "页")
    content_urls = us.parseContent(content)#找寻content页url
    for page_url in page_urls:
        page += 1
        print("第" + str(page) + "页")
        time.sleep(1)
        url = base_url + page_url
        content = vb.openurl(url)
        if content == None:
            continue
        content_urls.extend(us.parseContent(content))       
    print("content_urls列表中共有" + str(len(content_urls)) + "项")
    fp.write(company_name + '\n')
    count = 0
    ss = SentenceSpider()#开始爬取包含公司名称的句子
    for url in content_urls[:min(len(content_urls),30)]:#解析至多30个页面
        content = vb.openurl(url)
        if content == None:
            continue
        count += 1
        print("正在查找第" + str(count) + "个页面的内容...")
        ss.parse(content,company_name,fp)        
        print(url) 
        time.sleep(2)#2秒后再搜索
    fp.write('\n')
    ddd
fp.close()