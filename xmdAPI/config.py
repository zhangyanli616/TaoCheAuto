class OnLineConfig:
    env = 'ONLINE'  # 环境标识
    to_user = ['@all']  # 企业微信通知名单,个人 域账号，所有人 @all

    HOME_URL = 'http://p-api.kanche.com'
    # 登录接口
    TEST_LOGIN_URL = "/v1/crmpassport/login"
    # 自建工单接口
    TEST_ZJ_URL = "/v1/c2-xmd/xmd/saleOrder/buildByOneself"
    # 工单详情页
    TEST_ORDERDETAIL_URL = "/v1/c2-xmd/bss/getOrderDetail?isEncrypt=1&orderNo=GD156930926107803"
    # 工单列表
    TEST_ORDERLIST_URL = "/v1/c2-xmd/bss/getBssOrders"
    # 添加预约记录
    TEST_REVERSE_URL = "/v1/c2-xmd/xmd/saleOrder/reserve"
    # 订单电子签（车辆交接函）
    TEST_HANDOVERCONFIRM_URL = "/v1/cloudorder/contract/generateHandoverConfirm"
    # 订单电子签（保真协议）
    TEST_ENSUREREAL_URL = "/v1/cloudorder/contract/generateEnsureReal"
    # 订单线下签
    TEST_PAPERSIGN_URL = "/v1/cloudorder/contract/paperSign"

class TestConfig:
    env = 'TEST'  # 环境标识
    to_user = ['@all']  # 企业微信通知名单,个人 域账号，所有人 @all

    HOME_URL = 'http://p-api-test.kanche.com'
    # 登录接口
    TEST_LOGIN_URL = "/v1/crmpassport/login"
    # 自建工单接口
    TEST_ZJ_URL = "/v1/c2-xmd/xmd/saleOrder/buildByOneself"
    # 工单详情页
    TEST_ORDERDETAIL_URL = "/v1/c2-xmd/bss/getOrderDetail?isEncrypt=1&orderNo=GD156930926107803"
    # 工单列表
    TEST_ORDERLIST_URL = "/v1/c2-xmd/bss/getBssOrders"
    # 添加预约记录
    TEST_REVERSE_URL = "/v1/c2-xmd/xmd/saleOrder/reserve"
    # 订单电子签（车辆交接函）
    TEST_HANDOVERCONFIRM_URL = "/v1/cloudorder/contract/generateHandoverConfirm"
    # 订单电子签（保真协议）
    TEST_ENSUREREAL_URL = "/v1/cloudorder/contract/generateEnsureReal"
    # 订单线下签
    TEST_PAPERSIGN_URL = "/v1/cloudorder/contract/paperSign"


config = TestConfig()




#手机号
PHONENUMBER = 10000000000

#CRM测试报告接收人
RECEIVERS = ["liusai@taoche.com"]

#测试报告存储地址
TEST_RESULT_ADDR = "D:\\autoTestResult\\"

#CRM测试报告存储位置
CRM_REPORT_ADDR = TEST_RESULT_ADDR + "CRM\\"


#测试接口
START_URL = "http://p-api-test.kanche.com"
#线上接口
START_URL_PRO = "http://p-api.kanche.com"


#登录接口
TEST_LOGIN_URL = "/v1/crmpassport/login"
#自建工单接口
TEST_ZJ_URL = "/v1/c2-xmd/xmd/saleOrder/buildByOneself"
#工单详情页
TEST_ORDERDETAIL_URL = "/v1/c2-xmd/bss/getOrderDetail?isEncrypt=1&orderNo=GD156930926107803"
#工单列表
TEST_ORDERLIST_URL = "/v1/c2-xmd/bss/getBssOrders"
#添加预约记录
TEST_REVERSE_URL = "/v1/c2-xmd/xmd/saleOrder/reserve"
#订单电子签（车辆交接函）
TEST_HANDOVERCONFIRM_URL="/v1/cloudorder/contract/generateHandoverConfirm"
#订单电子签（保真协议）
TEST_ENSUREREAL_URL = "/v1/cloudorder/contract/generateEnsureReal"
#订单线下签
TEST_PAPERSIGN_URL = "/v1/cloudorder/contract/paperSign"


#车源-车源列表
TEST_CARLIST_URL = "/v1/search/cloud_store_vehicles?page=0&saleStatus=on_sale&size=20&tag=system%2Cmigratory"

#车源-详情页-
TEST_CARNUM_URL = "/v1/search/cloud_store_vehicles/020802221"
#车源-
TEST_CAR_URL = "/v1/vehicles/valuation?cityCode=540400&unifiedNumber=020802221"