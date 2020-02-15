class OnLineConfig:
    home_url = 'https://www.taoche.com/'
    news_url = 'https://news.taoche.com/home/'
    pinggu_url = 'https://www.taoche.com/pinggu/'
    bugcar_url = 'https://zhengzhou.taoche.com/all/'
    beijing_buycar_url ='https://beijing.taoche.com/all'
    buycar_collect_url='https://www.taoche.com/buycar/b-dealerydg222015747t.html?source=2808'
    brand_name = '宝马'
    # 是否开启静默，True 开启，False 关闭
    is_headless = False
    # 企业微信通知名单,个人 域账号，所有人 @all
    to_user = ['@all']


class TestConfig:
    home_url = 'https://www.taoche.com'
    news_url = 'https://news.taoche.com/home/'
    pinggu_url = 'https://www.taoche.com/pinggu/'
    bugcar_url = 'https://zhengzhou.taoche.com/all/'
    brand_name = '宝马'
    # 是否开启静默，True 开启，False 关闭
    is_headless = False
    # 企业微信通知名单
    to_user = ['@all']


config = OnLineConfig()
