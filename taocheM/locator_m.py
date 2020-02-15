# class locator_sugar_bean:
#     MORE_CAR = ('xpath', '//*[@id="app"]/div[2]/div/div[2]')
#     SUGAR_BEAN=('xpath', '//*[@id="app"]/ul')
#     DIV_CLASS=('xpath','//*[@id="app"]/span/div[2]')
#     CLOSE_DIV_GATE=('xpath','//*[@id="app"]/span/div[2]/dl/dd')

"""
Locator_Logo       #首页-淘车logo
Locator_Topic      #首页-专题广告
Locator_SugarBean  #首页-糖豆
Locator_Hotsearch  #首页-搜索
Locator_CarBrand   #首页-品牌糖豆
Locator_CarPrice   #首页-价格糖豆
Locator_CarVehicle #首页-车型糖豆
Locator_CarMore    #首页-查看更多
Locator_CarShop    #首页-店铺楼层（郑州）
Locator_Recommend  #首页-推荐楼层：今日上新。。。
Locator_Taps       #首页-全国购、4S店直卖。。
Locator_Newcar     #首页-淘车新车
Locator_Newchoice  #首页-淘车心选

===================================

Locator_SearchBZ       #买车-保真车查询
Locator_SearchNewsale  #买车-今日上新
Locator_SearchQGG      #买车-全国购

"""


class Locator_Home:

    #首页-淘车logo  @author:xulanzhong

    LOGO = ('class', 'logo')

    #首页-专题广告  @author:xulanzhong
    pass

    #首页-糖豆   @author:xulanzhong

    sugar_list = ('class','nav-wrap')
    flush_click =('xpath','//*[@id="app"]/ul/li[2]')
    sugar_test = ('xpath','//*[@id="app"]/ul/li/text()')
    sugar_qgg = ('xpath','//*[@id="app"]/ul/li[2]')
    test_qgg = ('class','trackul')
    test_footstep = ('class','footstep')

    #首页-搜索  @author:xulanzhong
    search = ('xpath','//*[@id="app"]/span/header/div[1]')
    bzcar = ('xpath','//*[@id="oldSearchHot"]/div[2]/div[1]/a')
    bzcar_foot = ('xpath','/html/body/div[1]/div[1]/div[3]/div[1]/ul/li/a')

    #首页-品牌  @author:xulanzhong

    CarBrand_list = ('class','lb-carlist')

    # 首页-车型  @author:xulanzhong
    #CarVehicle_list = ('class','lb-carlist-wz')
    CarVehicle_list = ('xpath','//*[@id="app"]/div[2]/div/div[1]/div[2]')

    #首页-价格糖豆  @author:xulanzhong
    carprive_list = ('class','lb-carlist-wz')
    carprive_click = ('text',"5万以下")
    carprive_foot = ('class','trackul')

    #首页-车型糖豆  @author:xulanzhong
    pass

    #首页-查看更多  @author:xulanzhong
    pass

    #首页-店铺楼层（郑州）   @author:xulanzhong
    carshop_click = ('xpath','//*[@id="app"]/div[3]/div/div/div[2]/div[1]')
    carshop_name = ('xpath','//*[@id="yxWrapper"]/div/div[1]/div')
    #首页-推荐楼层：今日上新。。。 @author:xulanzhong
    Recommend = ('xpath','//*[@id="app"]/div[4]/div/a[1]')
    today_new = ('xpath','/html/body/div[1]/div[1]/div[3]/div[1]/ul/li/a/b')
    #首页-全国购、4S店直卖。。@author:xulanzhong
    pass

    #首页-淘车新车楼层  @author:xulanzhong
    #Newcar_list = ('xpath','//*[@id="app"]/div[7]')
    Newcar_list = ('class','newcar-section')
    Newcar = ('xpath','//*[@id="app"]/div[6]/div[1]')
    ncar = ('xpath','//*[@id="app"]/div[6]/div[2]/a[1]')
    ncar_label = ('xpath','//*[@id="header-bar"]/h1/span[2]')

    #首页-淘车心选   @author:xulanzhong
    Newchoice =('xpath','//*[@id="app"]/div[8]/div[2]/div')



    #买车-保真车查询  @author:xulanzhong
    pass

    #首页-顶通广告  @author:xulanzhong
    topic = ('xpath','//*[@id="app"]/div[1]/span/div/div[1]/div[1]/div/img[1]')



class Locator_BuyCar:
    #列表页，点击宝马  @author:xulanzhong
    price_click = ('xpath','/html/body/div[1]/div[1]/div[3]/ul[1]/li[5]/a')
    price_list = ('xpath','/html/body/div[1]/div[1]/div[3]/div[1]/ul/li/a/b')
    newsale = ('xpath','/html/body/div[1]/div[1]/div[2]/a[3]')
    newsale_foot = ('xpath','/html/body/div[1]/div[1]/div[3]/div[1]/ul/li/a/b')
    newsale_label = ('xpath','/html/body/div[1]/ul/li[1]/a/div[1]/span')
    SearchQgg = ('xpath','/html/body/div[1]/div[1]/div[2]/a[2]')
    SearchQgg_label = ('xpath','/html/body/div[1]/ul/li[1]/a/div[2]/div[1]/span/span')


class SellCar_Locator:
    #卖车 @author:zhagnyanli
    SELL_CAR_TITLE = ('xpath','//*[@id="header-bar"]/h1/span[2]')
    SELL_CAR_CITY = ('id', 'city-iscroll')
    SELL_CAR_MOBILE = ('class','verify-mobile')
    SELL_CAR_VERIFYCODE = ('class','verify-code')
    SELL_CAR_BUTTON = ('xpath','//*[@id="zmWrapper"]/div[1]/div[1]/div[2]/div[4]/span')
    SELL_CAR_CHOOSE_CITY = ('text','成都')
    SELL_CAR_TAB = ('text','卖车')

class PingGu_Locator:
    #评估 @author:zhagnyanli
    PINGGU_TITLE = ('xpath','//*[@id="header-bar"]/h1/span[2]')
    PINGGU_CAR = ('xpath','//*[@id="aCar"]/span')
    PINGGU_LICENSED_DATE = ('xpath','//*[@id="time-select"]')
    PINGGU_MILE = ('id','txtMileage')
    PINGGU_CITY = ('id','area-select')
    PINGGU_MOBILE = ('id','sellcar-mobile')
    PINGGU_INTENTION = ('id', 'gjyx-trigger')
    PINGGU_ESTIMATE_BUTTON = ('id','sellcar-btn')
    PINGGU_CAR_BRAND = ('xpath', ' //*[@id="popBrand"]/div/div[3]/div[2]/ul/li[1]')
    PINGGU_CAR_LIST = ('class','choose-car-list')
    PINGGU_CAR_MODLE = ('id','popCar')
    PINGGU_YEAR = ('id','year-container')
    PINGGU_MONTH = ('id','month-container')
    PINGGU_PROVINCE = ('id','province-container')
    PINGGU_CITY_CHOOSE = ('id','city-container')
    PINGGU_INTENTION_CHOOSE = ('id','gjyxSelect')
    PINGGU_CLOSE = ('class','close')
    PINGGU_VALUE_RESULT = ('class','valueResult')
    PINGGU_RELEVANT_CAR = ('xpath','//*[@id="yxWrapper"]/div/div[3]/div[1]')
    PINGGU_CHART = ('xpath','//*[@id="yxWrapper"]/div/div[2]/p')

class Login_Locator:
    #登录 @author:zhagnyanli
    LOGIN_PASSWORD_LOGIN = ('class','toggle-bar')
    LOGIN_MOBILE = ('xpath','//*[@id="yxWrapper"]/div[2]/div[2]/ul/li[1]/input')
    LOGIN_PASSWORD = ('xpath','//*[@id="yxWrapper"]/div[2]/div[2]/ul/li[2]/input')
    LOGIN_SUBMITE = ('xpath','//*[@id="yxWrapper"]/div[2]/div[2]/div/a')
    LOGIN_TITLE = ('class','font-nav')
    LOGIN_USERCENTER = ('text','我的')
    LOGIN_USERNAME = ('xpath','//*[@id="a_login"]')
    LOGIN_ADLAYER = ('class','flush-layer-con')
    LOGIN_ADLAYER_CLOSE = ('class','close-btn')


class CarDetail_Locator:
    #详情页 @author:zhagnyanli
    DETAIL_TITLE = ('xpath','//*[@id="app"]/div[1]/div[2]/header/div[1]/span[2]/a/i')
    DETAIL_ACTIVITY_DOMAIN = ('class','huodong dl')
    DETAIL_ACTIVITY = ('xpath','//*[@id="carInfo"]/div/div[4]/div[1]')
    DETAIL_COUPON = ('xpath','//*[@id="carInfo"]/div/div[4]/div[2]')
    DETAIL_STORE_INFO = ('xpath','//*[@id="carInfo"]/div/div[5]/div[2]')
    DETAIL_FINANCE = ('xpath','//*[@id="carInfo"]/div/div[4]/div[2]/div[2]/span[2]')
    DETAIL_SERVICE = ('xpath','//*[@id="carInfo"]/div/div[4]/div[2]/div[3]/span[2]')
    DETAIL_ZHIYINGINFO = ('xpath','//*[@id="carInfo"]/div/div[5]/div[2]')
    DETAIL_BAOZHANG = ('xpath','//*[@id="carInfo"]/div/div[6]/div[2]')
    DETAIL_SCORE = ('xpath','//*[@id="carArchive"]/div/div/div[2]')
    #p配置文件
    CONFIG_TITLE = ('xpath','//*[@id="headerBar"]/div[1]/span[2]/a/i')
    CONFIG_BOX = ('class','config-box')
    CONFIG_SIZE = ('id','configItem35')
    #检测报告
    REPORT_TITLE = ( 'xpath','//*[@id="carReport"]/div/div/h2')
    REPORT_TYPE = ('xpath','//*[@id="carReport"]/div/div')
    #服务保障
    SEVICE_TITLE = ('xpath','//*[@id="header-bar"]/h1/span[2]')








