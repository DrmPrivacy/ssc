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
        pageUrl = config.SearchStockInfo
        requestBody =  {"pageSize":10,"pageIndex":1,"isHistory":0,"companyId":companyId}
        response = httphelper.request(pageUrl, requestBody)
        print(response)
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