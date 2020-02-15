#添加邀约记录case
from xmdAPI.base import Base
from xmdAPI.test_yd_api.common_fuc import helpReserve
from xmdAPI.test_yd_api.process_fuc import getOrderNumber


class TestRESERVECase(Base):

    '''
    {
    	"carCode": "001553305",
    	"followRecordPhotos": ["https:\/\/images-qa.kanche.com\/merchant\/basic_inf\/d6082bc38577c4b6a5b7acaaf8d61b5b.jpg"],
    	"starLevel": "5",
    	"taskNo": "TX156974125643811",
    	"followRecord": "安那般那呐喊给您寄了跟进记录",
    	"carFullName": "奥迪 RS 3 2017款 2.5T Limousine",
    	"carStype": "9",
    	"reservePlace": "哈哈哈我是地址",
    	"saleOrderNo": "GD156974124870815",
    	"token": "29a0cd5d0c704e4e9c72911b4e567873",
    	"reserveTime": "2019-10-13 14:30:38",
    	"invitationType": "1"
    }
    '''
    #成功添加邀约记录
    #跟进记录，预约地点，预约时间，销售工单单号，token,通话记录ID，
    # 任务编号，流程类型(4:云店流程 1:门店流程) 不传默认是云店流程，1：上门；2：到店


    #添加邀约记录成功，carcode为空，不校验
    def test_ReserveSuccess_emptyCarcode(self):
        ordNo = getOrderNumber(self)
        result = helpReserve("",
                             ["https://images-qa.kanche.com/merchant/basic_inf/d6082bc38577c4b6a5b7acaaf8d61b5b.jpg"],
                             "5",
                             "TX156974125643811",
                             "安那般那呐喊给您寄了跟进记录"
                             "奥迪 RS 3 2017款 2.5T Limousine",
                             "9",
                             "哈哈哈我是地址",
                             ordNo,
                             "2019-10-13 14:30:38"
                              )
        self.assertEqual(result['code'], 200)


    #添加邀约记录成功，starLevel为空，不校验
    def test_ReserveSuccess_emptyStarLevel(self):
        ordNo = getOrderNumber(self)
        result = helpReserve("001553305",
                             ["https://images-qa.kanche.com/merchant/basic_inf/d6082bc38577c4b6a5b7acaaf8d61b5b.jpg"],
                             "",
                             "TX156974125643811",
                             "安那般那呐喊给您寄了跟进记录"
                             "奥迪 RS 3 2017款 2.5T Limousine",
                             "9",
                             "哈哈哈我是地址",
                             ordNo,
                             "2019-10-13 14:30:38"
                              )
        self.assertEqual(result['code'], 200)

    #添加邀约记录成功，taskNo为空，不校验
    def test_ReserveSuccess_emptytaskNo(self):
        ordNo = getOrderNumber(self)
        result = helpReserve("001553305",
                             ["https://images-qa.kanche.com/merchant/basic_inf/d6082bc38577c4b6a5b7acaaf8d61b5b.jpg"],
                             "5",
                             "",
                             "安那般那呐喊给您寄了跟进记录"
                             "奥迪 RS 3 2017款 2.5T Limousine",
                             "9",
                             "哈哈哈我是地址",
                             ordNo,
                             "2019-10-13 14:30:38"
                              )
        self.assertEqual(result['code'],200)

    #添加邀约记录成功，followRecord为空，不校验
    def test_ReserveSuccess_emptyfollowRecord(self):
        ordNo = getOrderNumber(self)
        result = helpReserve("001553305",
                             ["https://images-qa.kanche.com/merchant/basic_inf/d6082bc38577c4b6a5b7acaaf8d61b5b.jpg"],
                             "5",
                             "TX156974125643811",
                             ""
                             "奥迪 RS 3 2017款 2.5T Limousine",
                             "9",
                             "哈哈哈我是地址",
                             ordNo,
                             "2019-10-13 14:30:38"
                              )
        self.assertEqual(result['code'],200)

    #添加邀约记录成功，carFullName为空，不校验
    def test_ReserveSuccess_emptycarFullName(self):
        ordNo = getOrderNumber(self)
        result = helpReserve("001553305",
                             ["https://images-qa.kanche.com/merchant/basic_inf/d6082bc38577c4b6a5b7acaaf8d61b5b.jpg"],
                             "5",
                             "TX156974125643811",
                             "安那般那呐喊给您寄了跟进记录"
                             "",
                             "9",
                             "哈哈哈我是地址",
                             ordNo,
                             "2019-10-13 14:30:38"
                              )
        self.assertEqual(result['code'],200)

    #添加邀约记录成功，carStype为空，不校验
    def test_ReserveSuccess_emptycarStype(self):
        ordNo = getOrderNumber(self)
        result = helpReserve("001553305",
                             ["https://images-qa.kanche.com/merchant/basic_inf/d6082bc38577c4b6a5b7acaaf8d61b5b.jpg"],
                             "5",
                             "TX156974125643811",
                             "安那般那呐喊给您寄了跟进记录"
                             "奥迪 RS 3 2017款 2.5T Limousine",
                             "",
                             "哈哈哈我是地址",
                             ordNo,
                             "2019-10-13 14:30:38"
                              )
        self.assertEqual(result['code'], 200)


    #添加邀约记录成功，reservePlace为空，不校验
    def test_ReserveSuccess_emptyreservePlace(self):
        ordNo = getOrderNumber(self)
        result = helpReserve("001553305",
                             ["https://images-qa.kanche.com/merchant/basic_inf/d6082bc38577c4b6a5b7acaaf8d61b5b.jpg"],
                             "5",
                             "TX156974125643811",
                             "安那般那呐喊给您寄了跟进记录"
                             "奥迪 RS 3 2017款 2.5T Limousine",
                             "9",
                             "",
                             ordNo,
                             "2019-10-13 14:30:38"
                              )
        self.assertEqual(result['code'], 200)


    def test_ReserveSuccess(self):
        ordNo = getOrderNumber(self)
        result = helpReserve("001553305",
                             ["https://images-qa.kanche.com/merchant/basic_inf/d6082bc38577c4b6a5b7acaaf8d61b5b.jpg"],
                             "5",
                             "TX156974125643811",
                             "安那般那呐喊给您寄了跟进记录"
                             "奥迪 RS 3 2017款 2.5T Limousine",
                             "9",
                             "哈哈哈我是地址",
                             ordNo,
                             "2019-10-13 14:30:38"
                              )
        print(result)


    # 添加邀约记录失败，followRecordPhotos为空
    def test_ReserveFail_emptyPhoto(self):
        ordNo = getOrderNumber(self)
        result = helpReserve("001553305",
                             "",
                             "5",
                             "TX156974125643811",
                             "安那般那呐喊给您寄了跟进记录"
                             "奥迪 RS 3 2017款 2.5T Limousine",
                             "9",
                             "哈哈哈我是地址",
                             ordNo,
                             "2019-10-13 14:30:38"
                             )
        self.assertEqual(result['error'], "Bad Request")

    # 添加邀约记录失败，followRecordPhotos异常
    def test_ReserveFail_unusualPhoto(self):
        ordNo = getOrderNumber(self)
        result = helpReserve("001553305",
                             "33kjjj333jjj33",
                             "5",
                             "TX156974125643811",
                             "安那般那呐喊给您寄了跟进记录"
                             "奥迪 RS 3 2017款 2.5T Limousine",
                             "9",
                             "哈哈哈我是地址",
                             ordNo,
                             "2019-10-13 14:30:38"
                             )
        self.assertEqual(result['error'], "Bad Request")

    #添加邀约记录失败，saleOrderNo为空
    def test_ReserveFail_emptysaleOrderNo(self):
        result = helpReserve("001553305",
                             ["https://images-qa.kanche.com/merchant/basic_inf/d6082bc38577c4b6a5b7acaaf8d61b5b.jpg"],
                             "5",
                             "TX156974125643811",
                             "安那般那呐喊给您寄了跟进记录"
                             "奥迪 RS 3 2017款 2.5T Limousine",
                             "9",
                             "哈哈哈我是地址",
                             "",
                             "2019-10-13 14:30:38"
                             )
        self.assertIn("销售工单单号信息不能为空",result['message'] )

    #添加邀约记录失败，saleOrderNo异常
    def test_ReserveFail_unusualsaleOrderNo(self):
        result = helpReserve("001553305",
                             ["https://images-qa.kanche.com/merchant/basic_inf/d6082bc38577c4b6a5b7acaaf8d61b5b.jpg"],
                             "5",
                             "TX156974125643811",
                             "安那般那呐喊给您寄了跟进记录"
                             "奥迪 RS 3 2017款 2.5T Limousine",
                             "9",
                             "哈哈哈我是地址",
                             "dddffdfff",
                             "2019-10-13 14:30:38"
                             )
        print(result)
        self.assertIn("无此工单号",result['message'] )

    #添加邀约记录失败，reserveTime为空
    def test_ReserveFail_emptyreserveTime(self):
        ordNo = getOrderNumber(self)
        result = helpReserve("001553305",
                             ["https://images-qa.kanche.com/merchant/basic_inf/d6082bc38577c4b6a5b7acaaf8d61b5b.jpg"],
                             "5",
                             "TX156974125643811",
                             "安那般那呐喊给您寄了跟进记录"
                             "奥迪 RS 3 2017款 2.5T Limousine",
                             "9",
                             "哈哈哈我是地址",
                             ordNo,
                             ""
                             )
        print(result)
        self.assertEqual(result['message'], "添加预约记录异常")


    #添加邀约记录失败，reserveTime异常
    def test_ReserveFail_unusualreserveTime(self):
        ordNo = getOrderNumber(self)
        result = helpReserve("001553305",
                             ["https://images-qa.kanche.com/merchant/basic_inf/d6082bc38577c4b6a5b7acaaf8d61b5b.jpg"],
                             "5",
                             "TX156974125643811",
                             "安那般那呐喊给您寄了跟进记录"
                             "奥迪 RS 3 2017款 2.5T Limousine",
                             "9",
                             "哈哈哈我是地址",
                             ordNo,
                             "dddeee"
                             )
        print(result)
        self.assertEqual(result['message'], "添加预约记录异常")
