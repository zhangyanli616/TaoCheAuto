class OnLineConfig:
    home_url = 'https://www.taoche.com/'
    news_url = 'https://news.taoche.com/home/'
    pinggu_url = 'https://www.taoche.com/pinggu/'
    app_sugar_bean_url = 'https://appapi.taoche.com/'
    m_sugar_bean_url = 'https://proconsumer.taoche.com/'
    # 企业微信通知名单,个人 域账号，所有人 @all
    to_user = ['@all']


class TestConfig:
    home_url = 'https://www.taoche.com'
    news_url = 'https://news.taoche.com/home/'
    app_sugar_bean_url = 'https://appapi.taoche.com/'
    m_sugar_bean_url = 'https://proconsumer.taoche.com/'
    # 企业微信通知名单
    to_user = ['@all']


config = OnLineConfig()


class Test_M:
    #M登录
    login_url ='https://passport.m.taoche.com/Login/Login'

