#工单详情页case

from xmdAPI.base import Base
from xmdAPI.test_yd_api.common_fuc import helpOrderDetail


class TestORDERINFOCase(Base):

    def test_getSuccess(self):
        #自建工单
        #跟进手机号获取工单列表
        #
        result = helpOrderDetail("GD156974124870815")
        print(result)