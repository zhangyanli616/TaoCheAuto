#线下签约case
from xmdAPI.base import Base
from xmdAPI.test_yd_api.common_fuc import helpSignoffline



class TestSIGNOFFLINECase(Base):
# {
# 	"orderId": "20190711145009",
# 	"images": [{
# 		"make": "",
# 		"model": "",
# 		"latitude": 39.936656951904297,
# 		"cdn": "np\/dealer\/5e2ade12-973b-49b3-ab26-38b93818f174.png",
# 		"source": "np\/dealer\/5e2ade12-973b-49b3-ab26-38b93818f174.png",
# 		"longitude": 116.32012176513672
# 	}],
# 	"type": 3
# }
# 旧订单数据
    def test_signoff_success(self):
    #
        result = helpSignoffline("20190803995967", "122121", "1222", "39.99",
                             "np\/dealer\/5e2ade12-973b-49b3-ab26-38b93818f174.png",
                             "np\/dealer\/5e2ade12-973b-49b3-ab26-38b93818f174.png",
                             "116.7", "3")
        self.assertEqual(result['message'], "根据订单ID查询不存在数据")
        print(result)

    #旧订单数据
    def test_signoff_success(self):
        #
        result = helpSignoffline("20190711145009","122121","1222","39.99",
                                  "np\/dealer\/5e2ade12-973b-49b3-ab26-38b93818f174.png",
                                  "np\/dealer\/5e2ade12-973b-49b3-ab26-38b93818f174.png",
                                  "116.7","3")
        self.assertEqual(result['message'],"根据订单ID查询不存在数据")
        print(result)



    def test_signoff_empty(self):
        #
        result = helpSignoffline("","","","",
                                  "",
                                  "",
                                  "","3")
        self.assertEqual(result['message'],"订单编号不能为空")
        print(result)