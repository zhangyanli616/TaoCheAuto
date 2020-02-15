import json
import requests
from xmdAPI.config import config
# from src.test_xmd import xmd_report_help
# from src.test_xmd import xmd_main_help
import random

header = {'Content-Type': "application/json"}

#
# def xmd_report(suite):
#     """
#     封装report，生成小馬達测试报告，返回报告全路径名称
#     :param suite: 需要进行测试的测试集
#     :return: 返回报告全路径名称
#     """
#     return xmd_report_help.build("XMD", suite)
#
#
# def xmd_send_email(report_full_name):
#     """
#     封装send_email,给测试负责人发送测试报告邮件
#     :param report_full_name: 报告全路径名称
#     :return:
#     """
#     xmd_receivers = xmd_config_help.RECEIVERS
#     xmd_main_help.send_email("XMD", xmd_receivers, report_full_name)


def getHeader():
    header = {'Content-Type': "application/json",
              'Authorization': getToken()}
    return header


# 获得token
def getToken():
    result = helpLogin("wb3001", "uat.portal")
    print("token:" + result['data']['token'])
    return result['data']['token']


# 生成手机号
def setPhoneNumber():
    return random.randint(12300000000, 12400000000)


# 登录
def helpLogin(userName,
              userPwd):
    data = json.dumps({'username': userName,
                       'password': userPwd})
    result = requests.post(config.HOME_URL + config.TEST_LOGIN_URL, data=data, headers=header).json()
    return result


# 自建工单
def helpZj(clueChannelName, clueChannelId, customerName, customerPhone, purchaseMode, customerType, carCode, gender,
           sparePhone, remark):
    data = json.dumps({'clueChannelName': clueChannelName,
                       'clueChannelId': clueChannelId,
                       'customerName': customerName,
                       'customerPhone': customerPhone,
                       'purchaseMode': purchaseMode,
                       'customerType': customerType,
                       'carCode': carCode,
                       'gender': gender,
                       'sparePhone': sparePhone,
                       'remark': remark,
                       })
    result = requests.post(config.HOME_URL + config.TEST_ZJ_URL, data=data,
                           headers=getHeader()).json()
    return result


# 工单详情页
# getOrderDetail?isEncrypt=1&orderNo=GD157059077014871
def helpOrderDetail(orderNo):
    result = requests.get(config.HOME_URL + config.TEST_ORDERDETAIL_URL, data=orderNo,
                          headers=getHeader()).json()
    return result


# 工单列表
# https://p-api-test.kanche.com/v1/c2-xmd/bss/getBssOrders
def helpOrderList(pageIndex, pageSize, workTable,myphone,orderStatusMapping):
    data = json.dumps({'pageIndex': pageIndex,
                       'pageSize': pageSize,
                       'workTable': workTable,
                       'keyWord':myphone,
                       'orderStatusMapping':orderStatusMapping
                       })

    result = requests.post(config.HOME_URL + config.TEST_ORDERLIST_URL, data=data,
                           headers=getHeader()).json()
    return result


# 添加接待记录
def helpReserve(carCode,
                followRecordPhotos,
                starLevel,
                taskNo,
                followRecord,
                carStype,
                reservePlace,
                saleOrderNo,
                reserveTime):
    data = json.dumps({'carCode': carCode,
                       'followRecordPhotos': followRecordPhotos,
                       'starLevel': starLevel,
                       'taskNo': taskNo,
                       'followRecord': followRecord,
                       'carStype': carStype,
                       'reservePlace': reservePlace,
                       'saleOrderNo': saleOrderNo,
                       'reserveTime': reserveTime})
    result = requests.post(config.HOME_URL + config.TEST_REVERSE_URL, data=data,
                           headers=getHeader()).json()
    return result


# 订单-电子签（车辆交接确认函）

# "partyBIdCard": "11100000",
# 	"carName": "上汽通用五菱 2019款 1.2L AMT 舒适版",
# 	"partyAName": "刘赛",
# 	"carTransferDate": "2019-09-25",
# 	"vinCode": "L5C13CH7B333H9M8C",
# 	"partyAPhone": "18510169951",
# 	"partyBPhone": "18510168888",
# 	"signDate": "2019-10-23",
# 	"orderId": "20190711145009",
# 	"remark": "政治知识点和谁谁谁谁谁谁谁",
# 	"partyAIdCard": "110222198912223524",
# 	"entrustPurchaseContractId": "QY2019071168766",
# 	"subsidiaryData": "哈哈哈哈我是I了",
# 	"partyBName": "刘赛"

def helpHandoverConfirm(partyBIdCard, carName, partyAName, carTransferDate, vinCode,
                        partyAPhone, partyBPhone, signDate, orderId, remark, partyAIdCard,
                        entrustPurchaseContractId, subsidiaryData, partyBName):
    data = json.dumps({'partyBIdCard': partyBIdCard, 'carName': carName, 'partyAName': partyAName,
                       'carTransferDate': carTransferDate, 'vinCode': vinCode,
                       'partyAPhone': partyAPhone, 'partyBPhone': partyBPhone,
                       'signDate': signDate, 'orderId': orderId, 'remark': remark, 'partyAIdCard': partyAIdCard,
                       'entrustPurchaseContractId': entrustPurchaseContractId,
                       'subsidiaryData': subsidiaryData, 'partyBName': partyBName})
    result = requests.post(config.HOME_URL + config.TEST_LOGIN_URL, data=data,
                           headers=getHeader()).json()
    return result


# 订单-线下签（车辆交接确认函）
def helpSignoffline(orderId, make, model, latitude, cdn,
                    source, longitude, type):
    images = [{'make': make, 'model': model, 'latitude': latitude,
               'cdn': cdn, 'source': source, 'longitude': longitude}]
    data = json.dumps({'orderId': orderId, 'images': images, 'type': type})
    result = requests.post(xmd_config_help.HOME_URL + xmd_config_help.TEST_PAPERSIGN_URL, data=data,
                           headers=getHeader()).json()
    return result


# 订单-电子签（保真协议）
'''
{
	"carMileage": "111100",
	"orderId": "20190711145009",
	"partyAPhone": "18510169951",
	"carName": "上汽通用五菱 2019款 1.2L AMT 舒适版",
	"agreementTakeEffectDate": "2020-11-23",
	"partyAName": "刘赛",
	"vinCode": "L5C13CH7B333H9M8C",
	"partyAIdCard": "110222198912223524",
	"dealPrice": "32000"
}
'''