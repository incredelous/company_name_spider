# -*- coding: utf-8 -*-
class CompanyNameRecord:
    def GainCompanyName(self,file_name):
        company_names = []
        with open(file_name,'r',encoding = 'utf-8') as f:
            for line in f:
                if line == '\n':
                    continue
                else:
                    record = line.replace('\n',' ')
                    record = record.strip()
                    company_names.append(record)
        f.close()
        return company_names
            
