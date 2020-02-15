import time
from typing import List
from selenium.webdriver.remote.webelement import WebElement
from taochePC import config, Search
from taochePC import Base
from titan import tt_check

home_url = config.config.home_url

class CarSearchResult(Base):
    def test_searchResult(self):
        """首页搜索框输入“奥迪”后，点击搜索查看结果是否是“奥迪”@author:dingdongdong"""
        self.driver.get(home_url)
        self.driver.find_element(Search.Search_Box).click()
        search_expected = "奥迪"
        self.driver.find_element(Search.Search_Box).send_keys("奥迪")
        print("输入的搜索条件为：",search_expected)
        time.sleep(2)
        self.driver.find_element(Search.Search_Button).click()
        self.driver.switch_to_window()
        result_actual = self.driver.find_element(Search.Result_aodi).get_attribute('title')
        print("获取到已选择的为：",result_actual)
        time.sleep(1)
        aodi_reault = tt_check.assertEqual(search_expected,result_actual,
                                           '搜索期望为%s, 实际为%s' % (search_expected, result_actual))

    def test_dropDown_Box(self):
        """点击输入框后，检查下拉框的热卖车型是够正确@author:dingdongdong"""
        dropDown_expected = ["保真车", "全国购", "宝马5系", "本田 雅阁", "奥迪A4L", "奥迪A6L", "丰田 凯美瑞", "宝马3系", "本田 思域", "丰田 汉兰达"
            , "丰田 卡罗拉", "大众 高尔夫"]
        self.driver.get(home_url)
        self.driver.find_element(Search.Search_Box).click()
        time.sleep(1)
        #获取页面实际下拉框显示的热卖车型
        list = self.driver.find_element(Search.SEARCH_DROP_LIST_ID).find_element_by_tag_name('li')

#        dropDown_actual = []
#        for hotRecords in hotRecordLi :
#            dropDown_actual.append(hotRecordLi.text)

#        tt_check.assertEqual()

    def test_home_search(self):
        """点击首页搜索框检查输入搜索条件，点击第三个下拉框查看是够正确@author:dingdongdong"""
        self.driver.get(home_url)
        time.sleep(1)
        self.driver.find_element(Search.SEARCH_TEXT).click()
        time.sleep(1)
        liList = self.driver.find_element(Search.SEARCH_DROP_LIST_ID).find_elements_by_tag_name('li')
        ThirdBrandText = liList[4].find_element_by_tag_name('a').find_element_by_tag_name('i').text
        print("点击下拉框实际的车型为：",ThirdBrandText)
        liList[4].find_element_by_tag_name('a').find_element_by_tag_name('i').click()
        self.driver.switch_to_window()
        time.sleep(3)
        title = self.driver.find_element(Search.SEARCH_BRAND_NAME).get_attribute('title')
        text = self.driver.find_element(Search.SEARCH_BRAND_NAME).text
        print("页面实际回显出的车型为：",text)
        tt_check.assertEqual(ThirdBrandText, text,'首页选中品牌:{ThirdBrandText},'
                                '列表页展示品牌:{text}'.format(ThirdBrandText=ThirdBrandText,text=text))