import index as processor
import config
import csvhelper as csv
def main():
    compaines = []
    header = '公司名称,统一信用代码,登记状态,法人,成立时间,注册地址,股东信息,主要人员,对外投资'
    for company in config.CompanyList:
        companyInfo = processor.getCompanyInfo(company)
        if companyInfo is None:
            continue
        currentCompany = {
            'companyId':companyInfo['companyId'], # 公司Id
            'creditNo':companyInfo['creditNo'], #统一信用代码
            'companyName':companyInfo['companyNameTag'], # 公司名称
            'Status': companyInfo['statusFlag'], #登记状态
            'legalPerson': companyInfo['legalPersonFlag'],#法人
            'establishmentTime':companyInfo['establishmentTime'], #成立时间
            'registerAddress':companyInfo['addressTag'], #注册地址
            'stockPerson':'', #股东信息
            'historyStockPerso':'', #历史股东信息
            'mainPerson':'', #主要人员
            'investmentAbroad':'', #对外投资
        }
        companyId = companyInfo['companyId']
        #获取股东信息
        stockInfo = processor.getStockInfo(companyId)
        if stockInfo is not None:
            stocks = ''
            for stock in stockInfo:
                stocks+=stock['stockName']+'-'
            currentCompany['stockPerson'] = stocks
            print(stocks)
        #获取主要人员
        mainPersons = processor.getMainPersonInfo(companyId)
        person = ''
        if mainPersons is not None:
            for mainPerson in mainPersons:
                person+=mainPerson['employeeName']+'-'
            currentCompany['mainPerson'] = person
        investmentAbroads = processor.getInvestmentAbroadInfo(companyId=companyId)
        if investmentAbroads is not None:
            investment = ''
            for investmentAbroad in investmentAbroads:
                investment += investmentAbroad['investmentCompanyName']+ '-'
            currentCompany['investmentAbroad'] = investment
        compaines.append(currentCompany)
        csv.writeOnetoscv(header,currentCompany, "outputone.csv")

if __name__ == "__main__":
    main()