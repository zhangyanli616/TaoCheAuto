class OnLineConfig:
    appium_service = 'http://localhost:4723/wd/hub'

    desired_caps = {
        'platformName': 'Android',
        'platformVersion': '8.0.0',
        'deviceid': '98899a305842545358',
        'deviceName': 'Galaxy S8+',
        'appPackage': 'com.ucar.app',
        'appActivity': 'com.ucar.app.activity.home.AppstartActivity',
        'noReset': True,  # true:不重新安装APP，false:重新安装app
        'noSign': True,
        'unicodeKeyboard': True,
        'recreateChromeDriverSessions': True,
        'resetKeyboard': True
    }

   # desired_caps = {

        # 'platformName': 'Android',
        # 'deviceName': 'huawei mate9',
        # 'platformVersion': '9',
        # 'appPackage': 'com.ucar.app',
        # 'appActivity': 'com.ucar.app.activity.home.AppstartActivity',
        # 'deviceid': 'GWY0217408004575',
        # 'noReset': True,
        # 'noSign': True,
        # 'recreateChromeDriverSessions': True,
        # 'appWaitPackage': 'com.ucar.app',
        # 'appWaitActivity': 'com.ucar.app.activity.home.AppstartActivity',
        # 'appWaitDuration': '30000'


    #}



     # 企业微信通知名单,个人 域账号，所有人 @all
    to_user = ['@all']


class TestConfig:
    appium_service = 'http://localhost:4723/wd/hub'
    desired_caps = {
        "platformName": "Android",
        "platformVersion": "8.0.0",
        "deviceid": "98899a305842545358",
        "appActivity": "com.ucar.app.activity.home.AppstartActivity",
         "noReset": True,
         "noSign": True,
        "deviceName": "Galaxy S8+",
        "appPackage": "com.ucar.app",
        #"unicodeKeyboard": True,
        #"resetKeyboard": True
    }
    # 企业微信通知名单
    to_user = ['@all']


config = OnLineConfig()


