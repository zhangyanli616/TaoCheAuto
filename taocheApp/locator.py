class InitLocator:

    #手机权限确认
    MOBILE_LIMIT = ("xpath", "//*[@text='始终允许']")
    #app评价提示
    GRADE_REJECT = ("id", "com.umetrip.android.msky.app:id/tv_reject")
    #appMenu
    MENU_BAR = ("id", "com.umetrip.android.msky.app:id/tv_text")


class MineLocator:
    # 登录
    HEAD_LOGIN = ("xpath", "//*[@text='点击登录']")
    TEST123 = ("id", "com.umetrip.android.msky.app:id/regist_name_edit")
    TEST234 = ("id", "com.umetrip.android.msky.app:id/regist_name_edit")
    TEST1111 = ("id", "com.umetrip.android.msky.app:id/regist_pass_edit")


class HomeLoctor:

    HEART_CHOOSE_KEY = ("id","com.ucar.app:id/tv_tab_title")
    HEART_CHOOSE_LAY_ITEM=("id","com.ucar.app:id/re_lay_item")
    HEART_CHOOSE_TEXT_VIEW_KEY=("id","com.ucar.app:id/tv_car_name")
    SEARCH_MORE = ("id","com.ucar.app:id/home ._filter_more")
    SEARCH_CLICK = ("id","com.ucar.app:id/tv_search")
    SEARCH_KEY = ("id", "com.ucar.app:id/actv_search")
    HOME_VENDOR_FLOOR_KEY=("id","com.ucar.app:id/store_view_pager")
    HOME_VENDOR_NAME=("id","com.ucar.app:id/store_pager_item_tv_name")
    HOME_VENDOR_ADDRESS=("id","com.ucar.app:id/store_pager_item_tv_address")

    BRAND_KEY = ('id','com.ucar.app:id/home_page_brand_text')
    CAR_LIST_SCREEN_ID = ('id','com.ucar.app:id/v_has_screen')
    CAR_INFO_ID = ('id','com.ucar.app:id/view_bottom_line')
    CAR_INFO_IDS = ('id','com.ucar.app:id/tv_car_name')
    DETAIL_CAR_NAME = ('id','com.ucar.app:id/tv_car_name')
    QGG_FLOOR_ID = ('id','com.ucar.app:id/tv_car_store_name')

    #首页广告楼层
    #焦点图广告
    JDAD_ID = ('id','com.ucar.app:id/sdv_item')
    JD_Index_ID = ('id','com.ucar.app:id/ll_indicator')
    #首页品牌专区广告楼层
    PPAD_ID = ('id','com.ucar.app:id/fl_dake_brand')
    PPAD1_ID = ('id','com.ucar.app:id/sdv_brand_1')
    PPAD2_ID = ('id', 'com.ucar.app:id/sdv_brand_2')
    PPAD3_ID = ('id', 'com.ucar.app:id/sdv_brand_3')


    # 五个吸底tab id
    SHOUYE_ID = ('id','com.ucar.app:id/rlTabHome')

    # 新车楼层
    XINCHETUIJIAN_ID = ('id','com.ucar.app:id/new_car_left_layout')
    XINCHEH5_TEXT_ID = ('id','com.ucar.app:id/base_tv_center')
    XINCHEH5_BACK_ID = ('id','com.ucar.app:id/base_iv_left')
    KAIZOUBA_ID = ('id','com.ucar.app:id/new_car_top_layout')
    FENQIGOUCHE_ID = ('id','com.ucar.app:id/new_car_bottom_layout')

    #首页推荐区楼层
    JINRISHANGXIN_IDS = ('id','com.ucar.app:id/ll_big_left')
    JINRISHANGXIN_TEXT_IDS = ('id','com.ucar.app:id/tv_big_left_title')
    JINRISHANGXIN_SUBTITLE_IDS = ('id','com.ucar.app:id/tv_big_left_subtitle')
    ZHUNXINCHE_IDS = ('id','com.ucar.app:id/ll_small_left')


    #二手车推荐楼层
    USEDCARREC_ID = ('id','com.ucar.app:id/fl_recommend_used_car')
    USEDCARTESE_IDS = ('id','com.ucar.app:id/ll_tap')
    USEDCARTESE_TITLE_ID = ('id','com.ucar.app:id/tv_tab_title')
    USEDCAR_CONTENT_ID = ('id','com.ucar.app:id/recommend_used_car_content')
    USEDCARLIST_IDS = ('id','com.ucar.app:id/item_used_car_cv_parent')
    USEDCARPRICE_ID = ('id','com.ucar.app:id/item_used_car_txt_price')
    USEDCARMORE_ID = ('id','com.ucar.app:id/item_recycler_txt_more')


    # 首页糖豆区
    TANGDOU_ALL_IDS = ('id', 'com.ucar.app:id/sugar_peas')
    TANGDOU_TEXT_IDS = ('id', 'com.ucar.app:id/sugar_peas_name')
    TANGDOU_IDS = ('id','com.ucar.app:id/sugar_peas_root')

    # 首页品牌推荐楼层
    PINPAI_ALL_ID = ('id', 'com.ucar.app:id/common_tab_layout_brand_container')
    PINPAI_TEXT_IDS = ('id','com.ucar.app:id/home_page_brand_text')
    PINPAI_IMAGE_IDS = ('id','com.ucar.app:id/home_page_brand_image')

    #品牌页
    PINPAI_TITLE_ID = ('id','com.ucar.app:id/action_bar_center_title_txtview')
    PINPAI_BACK_ID = ('id','com.ucar.app:id/bar_left')

    # 首页价格推荐楼层
    JIAGE_ID = ('id','com.ucar.app:id/home_page_filter_text')

    # 首页足迹楼层
    ZUJI_PRINT_ID = ('id','com.ucar.app:id/fl_footer_print')
    ZUJI_ITEM_IDS = ('id','com.ucar.app:id/tv_footer_print_item')

    #首页红色查看全部车源按钮
    HOME_ALL_ID = ('id','com.ucar.app:id/home_filter_more')
    HOME_ALL_TEXT_ID = ('id','com.ucar.app:id/home_filter_more_text')

class CarDetails:
    #车源售价
    CARPRICE_SALES = ('id', "com.ucar.app:id/tv_sales")




class  BuyCarLocator:
    TAB = ("id", "com.ucar.app:id/imgTabBuy")#买车TAB
    SEARCH=("id","com.ucar.app:id/ll_search")#列表页搜索输入框
    SEARCH_INPUT=("id","com.ucar.app: id / actv_search")#搜索页输入框
    CITY=("id","com.ucar.app:id/base_tv_left")#城市选择
    SHAIXUAN=("id","com.ucar.app:id/tv_car_list_screen")#筛选
    GV_FEATURESCREEN_ID=("id","com.ucar.app:id/gv_featurescreen")#车源特色标签
    QUEDING=("id","com.ucar.app:id/btn_sure_screen")
    JINRISHANGXIN=("xpath","/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[2]/android.widget.RelativeLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.TextView")

    # 沈阳
    SY=("xpath","/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[4]/android.widget.GridView/android.widget.TextView[7]")
    #关闭城市选择框
    CITY_CLOSE=("xpath","/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.ImageView")
   #保真车
    BZC=("ID",)
    #淘车直营
    TCZY = ("ID","com.ucar.app:id/xlistview_header_progressbar")
    #全国购
    QGG=("ID","com.ucar.app:id/xlistview_header_hint_textview")
    #排序
    PX=("id","com.ucar.app:id/btnSort")
    #价格最低
    JGZD=("xpath","/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.TextView")
    #价格筛选框“
    JG=("id","com.ucar.app:id/btnPrice")
    #价格100万以上
    JG1=("xpath","/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.GridView/android.widget.LinearLayout[11]/android.widget.TextView")

    #价格最低车源价格

    JGFIRST=("xpath","/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[4]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.TextView[1]")

    JDFIRST=("xpath","self.driver.find_element(BuyCarLocator.JG1).click()")
    #筛选菜单
    SHAIXUANMENU = ('id','com.ucar.app:id/menu')
    BUYCARTABKEY=("id","com.ucar.app:id/imgTabBuy")
    BUYCARBRANDTEXTKEY=("id","com.ucar.app:id/btnBrand")
    BUYCARRECOMMONDBRAND=("id","com.ucar.app:id/gird_recommend_serial_data")
    BUYCARSCREENKEY=("id","com.ucar.app:id/v_has_screen")
    BUYCARBRANDLISTKEY=("id","com.ucar.app:id/txt_item_brand_content_name")
    BUYCARNOLIMITKEY=("id","com.ucar.app:id/list_serial_data")
    BUYCARHOTSERIALLISTKEY=("id","com.ucar.app:id/ll_rec_brand_car_serials")
    BUYCARBRANDDATAKEY = ("id","com.ucar.app:id/list_brand_data")
    BUYCARRECYLERLISTKEY=("id","com.ucar.app:id/lv_car_list")
    BUYCARHELPKEY=("id","com.ucar.app:id/lv_car_list")
    BUYCARLISTVENDOR=("id","com.ucar.app:id/store_view_pager")
    BUYCARSEARCHFLOOR=("id","com.ucar.app:id/base_relay_title_bg")
    BUYCARHOTSEARCHKEY=("id","com.ucar.app:id/ll_search_hot")
    BUYCARFILTERBAOZHENKEY=("id","com.ucar.app:id/menu")
    BUYCARSEARCHTEXTKEY=("id","android:id/content")
    #品牌回显
    PPHX=("xpath","/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[2]/android.widget.RelativeLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.TextView")
    LL_SEARCH=('id','com.ucar.app:id/ll_search')
    ACTV_SEARCH=('id','com.ucar.app:id/actv_search')
    SEARCH_CAR_AUTOTEXT_NAME=('id','com.ucar.app:id/search_car_autotext_name')
    FOOTTEXT=('id','com.ucar.app:id/has_screen_parent')


class  SellCarLocator:
    TAB=("id","com.ucar.app:id/imgTabSell")#卖车TAB
    TITLE=("id","com.ucar.app:id/base_tv_center")#卖车页面标题

class  WoDeLoator:
    TAB=("id","com.ucar.app:id/imgTabMine")#我的TAB
    DENGLU=("id","com.ucar.app:id/tv_login")#登录入口
    PWDL=("id","com.ucar.app:id/password")#密码登录切换口
    UN=("id","com.ucar.app:id/password_tel")#用户名输入框
    PW=("id","com.ucar.app:id/new_password")#密码输入框
    DL=("id","com.ucar.app:id/ok")#登录按钮
    COLLECT=('id','com.ucar.app:id/ll_collect')#我收藏的入口
    CONTACT=('id','com.ucar.app:id/ll_contact_history')#我咨询的入口
    BROWSE =('id', 'com.ucar.app:id/ll_browse_history')  # 我看过的入口
    PK=('id', 'com.ucar.app:id/ll_pk')  # 我对比的入口
    COLLECTNAME=('id','com.ucar.app:id/base_tv_center')#收藏页面标题
    CONTACTNAME=('id','com.ucar.app:id/base_tv_center')#我咨询的页面标题
    BROWSENAME = ('id', 'com.ucar.app:id/base_tv_center')  # 我看过的页面标题
    PKNAME = ('id', 'com.ucar.app:id/base_tv_center')  # 对比页面标题
    SETTING=('id','com.ucar.app:id/rl_setting')#设置入口
    LOGOUT=('id','com.ucar.app:id/tv_logout')#退出登录入口
    YES=('id','com.ucar.app:id/md_buttonDefaultNegative')#确认退出选项




