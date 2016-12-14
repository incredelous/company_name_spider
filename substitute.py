# -*- coding: utf-8 -*-
from CompanyName import CompanyNameRecord
fp = open('filter_data.txt','r',encoding = 'utf-8')#打开已过滤文件
if fp == None:
    print("can't open filter_data file")
    exit()
fs = open('substitute_data.txt','a',encoding = 'utf-8')#替换数据
if fs == None:
    print("can't open substitute_data file")
    exit()
file_name = "substitute_company_name.txt"
substitute_company_names = []#替换的公司名称
company_names = []#被替换的公司名名称
sc = CompanyNameRecord()
substitute_company_names = sc.GainCompanyName(file_name)
ok = 0
for line in fp:
    if line == '\n':
        ok = 0
    else:
        if ok == 0:#公司名称所在行
            line = line.replace('\n',' ')
            line = line.strip()
            company_names.append(line)
            ok = 1
        else:
            continue
rate = 1
for substitute_company_name in substitute_company_names:    
    out_rate = rate/len(substitute_company_names)*100
    rate += 1
    print("正在替换...完成{0:.3f}%".format(out_rate))
    fp.seek(0)
    count = 0
    ok = 0
    fs.write(substitute_company_name + '\n')
    for line in fp:
        if line == '\n':
            ok = 0
            count += 1
        else:
            if ok == 0:#公司名称
                ok = 1
            else:
                sentence = line.replace(company_names[count],substitute_company_name)
                fs.write(sentence)
    fs.write('\n')