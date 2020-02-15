class OnLineConfig:
    env = 'ONLINE'  # 环境标识
    to_user = ['@all']  # 企业微信通知名单,个人 域账号，所有人 @all

    home_url = 'https://www.taoche.com/'
    news_url = 'https://news.taoche.com/home/'
    pinggu_url = 'https://www.taoche.com/pinggu/'
    app_sugar_bean_url = 'https://appapi.taoche.com/'
    m_sugar_bean_url = 'https://proconsumer.taoche.com/'

class TestConfig:
    env = 'TEST'  # 环境标识
    to_user = ['@all']  # 企业微信通知名单,个人 域账号，所有人 @all

    home_url = 'https://www.taoche.com'
    news_url = 'https://news.taoche.com/home/'
    m_sugar_bean_url = 'https://proconsumer.taoche.com/'
    app_sugar_bean_url = 'https://appapi.taoche.com/'


config = OnLineConfig()

