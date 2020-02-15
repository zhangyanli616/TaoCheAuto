#工单列表case
#工单列表字段均未校验，无需测试

from xmdAPI.base import Base
from xmdAPI.test_yd_api.common_fuc import helpOrderList


class TestORDERLISTCase(Base):
    '''
    {
    	"userNo": ["acbcc66a37594f6d9e3daa045a5e8876"],
    	"pageIndex": 1,
    	"pageSize": 20,
    	"workTable": "xmd_yd_sales"
    	"blankQueryKey":"关键字"
    	"orderStatusMapping":["c2_sale_order_status_mapping_dfp","c2_sale_order_status_mapping_dyy","c2_sale_order_status_mapping_djd","c2_sale_order_status_mapping_dkc"]
    }
    '''
    #参数未校验
    def test_getListSuccess(self,myPhone):
        result = helpOrderList(1,20,"xmd_yd_sales",myPhone,["c2_sale_order_status_mapping_dfp","c2_sale_order_status_mapping_dyy","c2_sale_order_status_mapping_djd","c2_sale_order_status_mapping_dkc"])
        return result

