from xmdAPI.test_yd_api.test_zj_case import TestZJCase
from xmdAPI.test_yd_api.test_orderList_case import TestORDERLISTCase


def getOrderNumber(self):
    # 自建工单
    zj_phone = TestZJCase.get_zj_phone(self)
    # 通过手机号查询工单
    orderList = TestORDERLISTCase.test_getListSuccess(self, zj_phone)
    orderNumber = orderList['data']['c2Orders'][0]['orderNo']
    return orderNumber




