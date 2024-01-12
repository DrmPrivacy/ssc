import csv
import json
import codecs

def writetoscv(header, message, filename):
    # 打开CSV文件并创建writer对象
    with codecs.open(filename, 'w', 'utf-8-sig') as file:
        header = ['公司名称','统一信用代码','登记状态','法人','成立时间','注册地址','股东信息','主要人员','对外投资']
        #'公司名称,统一信用代码,登记状态,法人,成立时间,注册地址,股东信息,主要人员,对外投资'
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()
        for row in message:
            print(str(row['companyName']).replace('<em>','').replace('<em>','</em>'))
            companyName = str(row['companyName']).replace('<em>','').replace('</em>','')
            writer.writerow({'公司名称':companyName,
                             '统一信用代码':str(row['creditNo']),
                             '登记状态':  str(row['Status']),
                             '法人':str(row['legalPerson']),
                             '成立时间':str(row['establishmentTime']),
                             '注册地址':str(row['registerAddress']),
                             '股东信息':str(row['stockPerson']),
                             '主要人员':str(row['mainPerson']),
                             '对外投资':str(row['investmentAbroad']),
                             })
def writeOnetoscv(header, row, filename):
    # 打开CSV文件并创建writer对象
    with codecs.open(filename, 'a', 'utf-8-sig') as file:
        header = ['公司名称','统一信用代码','登记状态','法人','成立时间','注册地址','股东信息','主要人员','对外投资']
        #'公司名称,统一信用代码,登记状态,法人,成立时间,注册地址,股东信息,主要人员,对外投资'
        writer = csv.DictWriter(file, fieldnames=header)
        companyName = str(row['companyName']).replace('<em>','').replace('</em>','')
        writer.writerow({'公司名称':companyName,
                            '统一信用代码':str(row['creditNo']),
                            '登记状态':  str(row['Status']),
                            '法人':str(row['legalPerson']),
                            '成立时间':str(row['establishmentTime']),
                            '注册地址':str(row['registerAddress']),
                            '股东信息':str(row['stockPerson']),
                            '主要人员':str(row['mainPerson']),
                            '对外投资':str(row['investmentAbroad']),
                            })
