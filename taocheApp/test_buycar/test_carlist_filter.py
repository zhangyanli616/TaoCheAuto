import time

from taocheApp import Base, BuyCarLocator
from titan import tt_check
import json


class CarListAPP(Base):

    def test_car_brand_screen(self):
        """验证列表页筛选品牌与回显是否一致@author:fangyu"""
        time.sleep(1)
        self.driver.find_element(BuyCarLocator.BUYCARTABKEY).click()
        time.sleep(1)
        self.driver.find_element(BuyCarLocator.BUYCARBRANDTEXTKEY).click()
        recommon_host_brand_text = self.driver.find_element(BuyCarLocator.BUYCARRECOMMONDBRAND). \
            find_elements_by_id("com.ucar.app:id/txt_item_hot_brand_name")[0].text
        self.driver.find_element(BuyCarLocator.BUYCARRECOMMONDBRAND). \
            find_elements_by_id("com.ucar.app:id/txt_item_hot_brand_name")[0].click()
        choose_brand_screen = \
        self.driver.find_element(BuyCarLocator.BUYCARSCREENKEY).find_elements_by_class_name("android.widget.TextView")[
            1].text
        tt_check.assertEqual(recommon_host_brand_text, choose_brand_screen,
                             "您选择了:{recommon_host_brand_text},页面回显:{choose_brand_screen}".format(
                                 recommon_host_brand_text=recommon_host_brand_text,
                                 choose_brand_screen=choose_brand_screen))

    def test_car_hot_serial_show(self):
        """验证列表页品牌下是否有热门车系，如果有则读取出来,如果@author:fangyu"""
        time.sleep(1)
        self.driver.find_element(BuyCarLocator.BUYCARTABKEY).click()
        self.driver.find_element(BuyCarLocator.BUYCARBRANDTEXTKEY).click()

        time.sleep(1)
        choose_car_brand_name = self.driver.find_element(BuyCarLocator.BUYCARBRANDDATAKEY).find_elements_by_id(
            "com.ucar.app:id/txt_item_brand_content_name")[1].text
        self.driver.find_element(BuyCarLocator.BUYCARBRANDDATAKEY).find_elements_by_id(
            "com.ucar.app:id/txt_item_brand_content_name")[1].click()
        print(choose_car_brand_name)

        self.driver.find_element(BuyCarLocator.BUYCARNOLIMITKEY).find_element_by_id(
            "com.ucar.app:id/txt_item_brand_content_name").click()
        host_serial_list = self.driver.find_element(BuyCarLocator.BUYCARHOTSERIALLISTKEY).find_elements_by_id(
            "com.ucar.app:id/brand_serial_item_parent")

        hotserialListNew = {}

        if host_serial_list:
            for serial in host_serial_list:
                hot_car_text = serial.find_element_by_id("com.ucar.app:id/tv_brand_serial_name").text
                hot_car_price = serial.find_element_by_id("com.ucar.app:id/tv_brand_serial_price").text
                hotserialListNew[hot_car_text] = hot_car_price
            hotserialListNewStr = json.dumps(hotserialListNew, ensure_ascii=False)
            tt_check.assertTrue(True, "该品牌:{choose_car_brand_name} 有热门车系，热门车系为:{hotserialListNewStr}".
                                format(choose_car_brand_name=choose_car_brand_name,
                                       hotserialListNewStr=hotserialListNewStr))
        else:
            tt_check.assertFalse(False, "该品牌:{choose_car_brand_name} 无热门车系".format(
                choose_car_brand_name=choose_car_brand_name))

    def test_car_model_list_show(self):
        """验证列表页选中车源是否有车款列表，如果有则读取出来@author:fangyu"""
        hotModelList = {}
        time.sleep(1)
        self.driver.find_element(BuyCarLocator.BUYCARTABKEY).click()
        time.sleep(1)
        self.driver.find_element(BuyCarLocator.BUYCARBRANDTEXTKEY).click()
        recommon_host_brand_text = self.driver.find_element(BuyCarLocator.BUYCARRECOMMONDBRAND). \
            find_elements_by_id("com.ucar.app:id/txt_item_hot_brand_name")[0].text

        self.driver.find_element(BuyCarLocator.BUYCARRECOMMONDBRAND). \
            find_elements_by_id("com.ucar.app:id/txt_item_hot_brand_name")[0].click()

        print(recommon_host_brand_text)

        time.sleep(1)

        car_list_model_list = self.driver.find_element(BuyCarLocator.BUYCARRECYLERLISTKEY). \
            find_element_by_id("com.ucar.app:id/car_series_recycler")


        if car_list_model_list:
            for model in car_list_model_list:
                seials_text = model.find_element_by_id("com.ucar.app:id/car_serials_year_and_num").text
                price_text = model.find_element_by_id("com.ucar.app:id/car_serials_price_range").text
                hotModelList[seials_text] = price_text

            hotModelStr = json.dumps(hotModelList, ensure_ascii=False)
            tt_check.assertTrue(True, "该车源:{recommon_host_brand_text} 有车款列表，车款列表为:{hotModelStr}".format(
                recommon_host_brand_text=recommon_host_brand_text, hotModelStr=hotModelStr
            ))
        else:
            tt_check.assertFalse(False, "该车源:{recommon_host_brand_text} 无车款列表".format(
                recommon_host_brand_text=recommon_host_brand_text))


    def test_help_find_car(self):
        """检查车源列表页帮我找车楼层是否展示@author:fangyu"""
        time.sleep(1)
        self.driver.find_element(BuyCarLocator.BUYCARTABKEY).click()
        time.sleep(1)
        self.driver.swipeUpDown(0.6,0.1)
        help_buy_car_show = self.driver.find_element(BuyCarLocator.BUYCARHELPKEY).find_element_by_id("com.ucar.app:id/car_list_help_find_bg").\
            get_attribute("displayed")
        print(help_buy_car_show)
        if help_buy_car_show:
            tt_check.assertTrue(True, "车源列表页帮我找车楼层正常展示")
        else:
            tt_check.assertFalse(False,"车源列表页帮我找车楼层未展示")

    def test_car_list_vendor(self):
        """检查车源列表页精品店楼层是否展示@author:fangyu"""
        time.sleep(1)
        self.driver.find_element(BuyCarLocator.BUYCARTABKEY).click()
        time.sleep(1)
        self.driver.swipeUpDown(0.9, 0.1)
        car_list_vendor = self.driver.find_element(BuyCarLocator.BUYCARLISTVENDOR).get_attribute("displayed")
        if car_list_vendor:
            vendor_text = self.driver.find_element(BuyCarLocator.BUYCARLISTVENDOR).find_element_by_id("com.ucar.app:id/store_pager_item_tv_name").text
            tt_check.assertTrue(True,"车源列表页精品店展示：{vendor_text}".format(vendor_text=vendor_text))
        else:
            tt_check.assertFalse(False,"车源列表页精品店未正常展示")

    def test_car_list_hot_search(self):
        """列表页检查热门是否展示且是否有数据@author:fangyu"""
        hostSearchTextList = []
        time.sleep(1)
        self.driver.find_element(BuyCarLocator.BUYCARTABKEY).click()
        self.driver.find_element(BuyCarLocator.BUYCARSEARCHFLOOR).find_element_by_id("com.ucar.app:id/base_tv_center_search").click()
        time.sleep(1)
        host_search_displayed = self.driver.find_element(BuyCarLocator.BUYCARHOTSEARCHKEY).get_attribute("displayed")
        if host_search_displayed:
            hot_search_class = self.driver.find_element(BuyCarLocator.BUYCARHOTSEARCHKEY).find_elements_by_class_name("android.widget.TextView")
            for hotSearch in hot_search_class:
                text = hotSearch.text
                hostSearchTextList.append(text)
            hostSearchTextListStr = json.dumps(hostSearchTextList, ensure_ascii=False)
            tt_check.assertTrue(True,"列表页热门搜索:{hostSearchTextListStr}".format(hostSearchTextListStr=hostSearchTextListStr))
        else:
            tt_check.assertFalse(False,"列表页热门搜索无数据")



    def test_car_host_search_right(self):
        """买车列表页搜索功能验证@author:fangyu"""
        self.driver.find_element(BuyCarLocator.LL_SEARCH).click()
        time.sleep(1)
        self.driver.find_element(BuyCarLocator.ACTV_SEARCH).send_keys("帕萨特")
        time.sleep(1)
        self.driver.find_element(BuyCarLocator.SEARCH_CAR_AUTOTEXT_NAME).click()
        search_text = self.driver.find_element(BuyCarLocator.FOOTTEXT).find_element_by_id('com.ucar.app:id/v_has_screen').\
            find_elements_by_class_name('android.widget.TextView')[1].text
        tt_check.assertIn('帕萨特',search_text,"搜索的车源:帕萨特,列表页展示{search_text}".format(search_text=search_text))






















