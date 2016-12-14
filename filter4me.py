# -*- coding: utf-8 -*-
import re
def IsContainBranch(string,company_name):#句子中是否包含该公司的分公司
        pattern = company_name + "[\s\S]*(分公司|区公司)$"
        prog = re.compile(pattern)
        result = prog.match(string)
        if result == None:
            return 0
        else:
            return 1
            
def StripLabel(string):#去标签
    new_string = ""
    ok = 0
    for char in string:
        if char == "<":
            ok = 1
            continue
        if char == ">":
            ok = 0
            continue
        if ok == 0:
            new_string = new_string + char
    return new_string
    
def IsNotContain(company_name,sentence):#句子中是否包含公司名
    for i in range(len(sentence) - len(company_name) + 1):
       if sentence[i] == company_name[0]:
            ok = 0
            for j in range(len(company_name)):
                try:
                    char = sentence[i + j]
                except:
                    print("exceed index")
                if char == company_name[j]:
                    continue
                else:
                    ok = 1
                    break
            if ok == 0:
                return 0
    return 1
    
def IsShorter(sentence,company_name):
    if len(sentence) <= len(company_name):
        return 1
    else:
        return 0

def filters(sentence,company_name):
    pattern = '[\.\-\!\/_,:$%^*()?+\"\'[\]<>]+|[+——！，。？、：；~@#￥%……&*“”（）]+'
    sentence = re.sub(pattern,'',sentence)
    if sentence == '':
        return None
    if IsShorter(sentence,company_name):
        return None
    if IsNotContain(sentence,company_name):
        return None
    return sentence 
        
company_names = []
fp = open('filter_data.txt','w',encoding = 'utf-8')#过滤数据后的文件
if fp == None:
    print("can't open fliter_data file")
    exit()
fs = open('extend_company_name.txt','w',encoding = 'utf-8')#存储分公司名的文件
if fs == None:
    print("can't open extend_company_name.txt")
    exit()
ok = 0
with open('raw_data.txt','r',encoding = 'utf-8') as f:#打开待过滤数据文件，找到所有公司名称，为找出分公司做准备
    for line in f:
        if line == '\n':
            ok = 0
        else:
            if ok == 0:
                line = line.replace('\n',' ')
                line = line.strip()
                company_names.append(line)
                ok = 1
            else:
                continue
f.close()
for company_name in company_names:
    print(company_name)
count = 0
sentences = set()
with open('raw_data.txt','r',encoding = 'utf-8') as f:#打开待过滤数据文件，准备开始过滤
    for line in f:
        if line == '\n':
            fp.write('\n')
            count += 1
            sentences.clear()
        else:
            sentence = line
            chunks = re.split('[。，——：？！；]|[,:?\.\!\/]')
            for chunk in chunks:
                chunk = filters(chunk,company_name[count])
                if IsContainBranch(chunk,company_name[count]):
                   fs.write(chunk + '\n')
                
                   
            sentence = re.sub(pattern,'',line)#去除标点符号
            if sentence in sentences:
                continue
            else:
                sentences.add(sentence)
            fp.write(sentence + '\n')
f.close()
fs.close()
fp.close()