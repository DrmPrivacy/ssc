import httphelper
import config
import csvhelper as csv
def getCompanyInfo(companyName):
    try:
        pageUrl = config.SearchCompanyInfo
        requestBody = {"keyword":str(companyName),"searchType":21,"pageIndex":1,"pageSize":20}
        print(requestBody)
        response = httphelper.request(pageUrl, requestBody)
        companyInfo = response['data'][0]
        return companyInfo
    except Exception as ex:
        return None
#查询股东信息
def getStockInfo(companyId):
    try:
        pageUrl = config.SearchCompanyInfo
        requestBody =  {"pageSize":10,"pageIndex":1,"isHistory":0,"companyId":companyId}
        response = httphelper.request(pageUrl, requestBody)
        return response['data']
    except Exception as ex:
        return None
#查询历史主要人员
def getMainPersonInfo(companyId):
    try:
        pageUrl = config.SearchHistoryPerson
        requestBody =  {"pageSize":20,"pageIndex":1,"isHistory":1,"companyId":companyId}
        response = httphelper.request(pageUrl, requestBody)
        return response['data']
    except Exception as ex:
        return None
#查询历史对外投资s
def getInvestmentAbroadInfo(companyId):
    try:
        pageUrl = config.SearchInvestment
        requestBody =  {"pageSize":20,"pageIndex":1,"isHistory":1,"companyId":companyId}
        response = httphelper.request(pageUrl, requestBody)
        return response['data']
    except Exception as ex:
        return None

compaines = []
for company in config.CompanyList:
    companyInfo = getCompanyInfo(company)
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
    stockInfo = getStockInfo(companyId)
    if stockInfo is not None:
        stocks = ''
        for stock in stockInfo:
            stocks+=stock['stockName']+'-'
        currentCompany['stockPerson'] = stocks
        print(stocks)
    #获取主要人员
    mainPersons = getMainPersonInfo(companyId)
    person = ''
    if mainPersons is not None:
        for mainPerson in mainPersons:
            person+=mainPerson['employeeName']+'-'
        currentCompany['mainPerson'] = person
    investmentAbroads = getInvestmentAbroadInfo(companyId=companyId)
    if investmentAbroads is not None:
        investment = ''
        for investmentAbroad in investmentAbroads:
            investment += investmentAbroad['investmentCompanyName']+ '-'
        currentCompany['investmentAbroad'] = investment
    compaines.append(currentCompany)

header = '公司名称,统一信用代码,登记状态,法人,成立时间,注册地址,股东信息,主要人员,对外投资'
csv.writetoscv(header,compaines, "output.csv")