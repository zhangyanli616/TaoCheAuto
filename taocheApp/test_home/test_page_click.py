
from taocheApp import Base, HomeLoctor
from titan import tt_check


class HomePage(Base):


    def test_vendon_floor_show(self):
        """北京,首页精品店楼层是否展示，若展示则检查精品店名称，地址@author:fangyu"""
        vendor_floor_display = self.driver.find_element(HomeLoctor.HOME_VENDOR_FLOOR_KEY).get_attribute('displayed')
        vendor_name = self.driver.find_elements(HomeLoctor.HOME_VENDOR_NAME)[0].text
        vendor_address = self.driver.find_elements(HomeLoctor.HOME_VENDOR_ADDRESS)[0].text
        if vendor_floor_display:
            tt_check.assertTrue(True,"首页精品店名称:{vendor_name},精品店地址:{vendor_address}".format(vendor_name=vendor_name,
                                                                                        vendor_address=vendor_address))
        else:
            tt_check.assertFalse(False,"首页没有展示精品店楼层")


    def test_heart_favorite_show(self):
        """首页淘车心选楼层标题是否展示以及该楼层是否有数据@author:fangyu"""
        self.driver.sleep(4)
        self.driver.swipeUpDown(0.6, 0.1)
        heart_choose_text = self.driver.find_element(HomeLoctor.HEART_CHOOSE_KEY).text
        print("进入首页{heart_choose_text}楼层".format(heart_choose_text=heart_choose_text))

        tt_check.assertEqual(heart_choose_text, "淘车心选",
                             "首页淘车心选楼层,标题展示为:{heart_choose_text}".format(heart_choose_text=heart_choose_text))
        itemsList = self.driver.find_element(HomeLoctor.HEART_CHOOSE_LAY_ITEM).find_elements_by_id(
            "com.ucar.app:id/sdv_car")
        car_name_text = self.driver.find_elements(HomeLoctor.HEART_CHOOSE_TEXT_VIEW_KEY)[0].text
        if car_name_text:
            tt_check.assertTrue(True, "首页:{heart_choose_text}楼层,首条车源名称为:{car_name_text}".
                                format(heart_choose_text=heart_choose_text, car_name_text=car_name_text))
        else:
            tt_check.assertFalse(False, "首页:{heart_choose_text}楼层没有数据")


    def test_page_click(self):
        """app首页、列表页、详情页点击检查@author:fangyu"""
        brandText = self.driver.find_element(HomeLoctor.BRAND_KEY).text
        print(brandText)
        self.driver.find_element(HomeLoctor.BRAND_KEY).click()

        classList = self.driver.find_element(HomeLoctor.CAR_LIST_SCREEN_ID).find_elements_by_class_name('android.widget.TextView')
        if classList:
            classText = classList[0].text
            print(classText)
            tt_check.assertEqual(brandText,classText,'首页选中品牌:{brandText},列表页展示品牌:{classText}'.format(
                brandText=brandText,classText=classText
            ))
            carList = self.driver.find_elements(HomeLoctor.CAR_INFO_IDS)
            if carList:
                carNameText = carList[0].text
                print("取到车源列表页第一辆车:{carNameText}".format(carNameText=carNameText))
                carList[0].click()
                print("进入车源详情页")
                DetailCarNameText = self.driver.find_element(HomeLoctor.DETAIL_CAR_NAME).text
                print(DetailCarNameText)
                self.driver.swipeUpDown(0.9,0.1)
                qggText = self.driver.find_element(HomeLoctor.QGG_FLOOR_ID).text
                if qggText:
                    tt_check.assertTrue(True,"全国购店铺名称:{qggText}".format(qggText=qggText))
                else:
                    tt_check.assertFalse(False,"车源:{DetailCarNameText} 详情页没有全国购楼层".format(DetailCarNameText=DetailCarNameText))

            else:
                print('没有取到车源列表数据')
        else:
            print('首页没有取到品牌')



