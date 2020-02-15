# -*- coding:utf-8 -*-
import time
import requests

from taochePC.config import config
from taochePC import Base, BuyCarLocator, BuyCarTag
from titan import tt_check
import json

bugcar_url = config.bugcar_url
brand_name = config.brand_name
beijing_buycar_url = config.beijing_buycar_url


class CarList(Base):

    def search_car(self):
        """买车列表页搜索功能@author:fangyu"""
        self.driver.get(bugcar_url)
        self.driver.find_element(BuyCarLocator.SEARCH_KEY_WORD).send_keys(brand_name)
        self.driver.find_element(BuyCarLocator.SEARCH_ACTION).click()
        title = self.driver.find_element(BuyCarLocator.SEARCH_RESULT).get_attribute('title')
        time.sleep(1)
        tt_check.assertEqual(title, brand_name, '搜索车:{brand_name},检索结果:{title}'.format(brand_name=brand_name,
                                                                                       title=title))

    # def test_city_submenu_tab(self):
    #     """非直营城市检查淘车直营tab是否展示，非直营城市检查默认值@author:fangyu"""
    #     citys = ['beijing', 'zhengzhou', 'shenyang']
    #     for city in citys:
    #         url = 'https://{city}.taoche.com/all/'.format(city=city)
    #         self.driver.get(url)
    #         if city == 'zhengzhou' or city == 'shenyang':
    #             submenu_tab_zy = self.driver.find_element(BuyCarLocator.SUBMENU_TAB_ZY)
    #             text = submenu_tab_zy.find_element_by_tag_name('a').text
    #             tt_check.assertEqual(text, '淘车直营', '当前城市为:%s,应该包含淘车直营tab，实际上展示了%stab' % (city, text))
    #         else:
    #             submenu_tab_fzy = self.driver.find_element(BuyCarLocator.SUBMENU_TAB_FZY).get_attribute('class')
    #             tt_check.assertEqual(submenu_tab_fzy, 'active', '当前城市为:%s, tab展示了:%s二手车' % (city, city))

    def test_common_tool(self):
        """测试买车列表页 常用工具的展示以及跳转请求是否正常@author:fangyu"""
        resultList = {}
        self.driver.get(bugcar_url)
        ulList = self.driver.find_element(BuyCarLocator.COMMON_TOOLS).find_elements_by_tag_name('li')
        if ulList:
            for li in ulList:
                text = li.find_element_by_tag_name('a').text
                url = li.find_element_by_tag_name('a').get_attribute('href')
                resultList[text] = url

            for url in resultList:
                r = requests.get(resultList[url])
                status = r.status_code
                if status != 200:
                    tt_check.assertFalse(False, '%s对应的地址:%s,请求ERROR,状态码:%s' % (url, resultList[url], status))
                else:
                    tt_check.assertTrue(True, '%s对应的地址:%s,请求OK,状态码:%s' % (url, resultList[url], status))
        else:
            tt_check.assertFalse(False, '列表页常用工具未展示')

    def test_hot_serial(self):
        """买车列表页热门车系，热门品牌@author:fangyu"""
        serialNameMap = {}
        serialNameList = []

        brandNameMap = {}
        brandNameList = []

        resultList = []
        self.driver.get(bugcar_url)

        hot_serial = self.driver.find_element(BuyCarLocator.HOT_SERIAL).find_elements_by_tag_name('li')
        if hot_serial:
            for hs_tab in hot_serial:
                hs = hs_tab.find_element_by_tag_name('a').text
                if hs == '热门车系':
                    serial_name = self.driver.find_element(BuyCarLocator.HOT_SERIAL_NAME).find_elements_by_tag_name(
                        'li')
                    for sn in serial_name:
                        snn = sn.find_element_by_tag_name('a').text
                        serialNameList.append(snn)
                        serialNameMap[hs] = serialNameList
                    resultList.append(serialNameMap)

                elif hs == '热门品牌':
                    brand_name = self.driver.find_element(BuyCarLocator.HOT_BRAND_NAME).find_elements_by_tag_name(
                        'li')
                    for bn in brand_name:
                        bnn = bn.find_element_by_tag_name('a').get_attribute('title')
                        brandNameList.append(bnn)
                        brandNameMap[hs] = brandNameList
                    resultList.append(brandNameMap)
                else:
                    pass

            result_str = json.dumps(resultList, ensure_ascii=False)

            if resultList and len(resultList) > 0:
                tt_check.assertTrue(True, '列表页热门品牌或者热门车系展示正常,展示为{result_str}'.format(result_str=result_str))
            else:
                tt_check.assertFalse(False, '列表页热门品牌或者热门车系数据为空')
        else:
            tt_check.assertFalse(False, '列表页热门品牌或者热门车系有数据为空')

    def test_buycar_Screening(self):
        """点击第一个品牌+车系，查看列表中第一个车是否是自己选择的 @author:dingdongdong"""
        self.driver.get(beijing_buycar_url)
        time.sleep(1)
        #获取品牌字母A
        codeList = self.driver.find_element(BuyCarTag.BUY_CAR_BRAND_CODE).find_elements_by_tag_name('li')
        brand_codeChoose = codeList[1].find_element_by_tag_name('a').text
        codeList[1].find_element_by_tag_name('a').click()
        print("选择的品牌字母为：",brand_codeChoose)
        #获取品牌字母A下的第一个品牌且点击
        brand_name_choose = self.driver.find_element(BuyCarTag.BUY_CAR_BRAND_CODE_A).find_elements_by_tag_name('li')
        BN = brand_name_choose[0].find_element_by_tag_name('a').text
        print("选择的品牌为：",BN)
        time.sleep(1)
        brand_name_choose[0].find_element_by_tag_name('a').click()
        #获取奥迪下第一个车系
        cx_name_choose = self.driver.find_element(BuyCarTag.CX_LIST).find_elements_by_tag_name('li')
        CX = cx_name_choose[1].find_element_by_tag_name('a').text
        print("你选择的车系为：",CX)
        cx_name_choose[1].find_element_by_tag_name('a').click()
        #实际筛选结果展示的品牌和车系是否和选择的一致
        actual_brand = self.driver.find_element(BuyCarTag.Result_brand_list).get_attribute('title')
        print("页面实际展示的品牌为：",actual_brand)
        actual_cx = self.driver.find_element(BuyCarTag.Result_CX_list).get_attribute('title')
        tt_check.assertTrue(actual_cx,"实际展示的车系是 %s" % actual_cx )
        print("页面实际展示的车系为：", actual_cx)
        aa = self.driver.find_element(BuyCarTag.Result_CX_list).is_displayed()
        time.sleep(2)
        tt_check.assertEqual(BN, actual_brand,
                             '搜索的品牌期望为%s, 页面实际展示的品牌为%s' % (BN, actual_brand))
        #获取第一个车源title
        show_carOne_name_list = self.driver.find_element(BuyCarTag.show_carlist).find_element_by_tag_name('ul').find_elements_by_tag_name('li')
        show_carone_titleName = show_carOne_name_list[0].find_elements_by_tag_name('div')
        title_text_name = show_carone_titleName[0].find_element_by_tag_name('div').find_element_by_tag_name('a').get_attribute('title')
        print("第一个车源title名字为：",title_text_name)
        tt_check.assertTrue(title_text_name,"展示的名称如果有奥迪A6L，则检索的结果是正确的，实际展示的结果为：%s" % title_text_name)

    def test_clean_select(self):
        """test选择筛选后，点击后面的清除全部按钮 @author:dingdongdong """
        self.driver.get(beijing_buycar_url)
        time.sleep(1)
        # 获取品牌字母A
        codeList = self.driver.find_element(BuyCarTag.BUY_CAR_BRAND_CODE).find_elements_by_tag_name('li')
        brand_codeChoose = codeList[1].find_element_by_tag_name('a').text
        codeList[1].find_element_by_tag_name('a').click()
        print("选择的品牌字母为：", brand_codeChoose)
        # 获取品牌字母A下的第一个品牌且点击
        brand_name_choose = self.driver.find_element(BuyCarTag.BUY_CAR_BRAND_CODE_A).find_elements_by_tag_name('li')
        BN = brand_name_choose[0].find_element_by_tag_name('a').text
        print("选择的品牌为：", BN)
        time.sleep(1)
        brand_name_choose[0].find_element_by_tag_name('a').click()
        # 获取奥迪下第一个车系
        cx_name_choose = self.driver.find_element(BuyCarTag.CX_LIST).find_elements_by_tag_name('li')
        CX = cx_name_choose[1].find_element_by_tag_name('a').text
        cx_name_choose[1].find_element_by_tag_name('a').click()
        #检查面包屑展示的是否有北京二手车奥迪A6L
        show_carlist_top = self.driver.find_element(BuyCarTag.show_carlist_top).find_element_by_tag_name('div').find_elements_by_tag_name('a')
        list_top_text = show_carlist_top[3].text
        tt_check.assertTrue(list_top_text,"面包屑展示的名称是否为：%s" % list_top_text)
        #清除全部，检测面包屑应该展示为：北京二手车
        Obtain_clear_btn = self.driver.find_element(BuyCarTag.chexing_choose).find_element_by_tag_name('ul').find_elements_by_tag_name('li')
        print("测试数据",Obtain_clear_btn)
        clear_btn = Obtain_clear_btn[2].find_element_by_tag_name('a').click()
        show_carlist_top = self.driver.find_element(BuyCarTag.show_carlist_top).find_element_by_tag_name('div').find_elements_by_tag_name('a')
        clear_list_top = show_carlist_top[1].text
        tt_check.assertTrue(clear_list_top,"清除后的面包屑展示的名称为：%s" % clear_list_top)

    def Custom_Price_choose_car(self):
        """取第一个自定义价格筛选的结果的价格是否小于等于设定自定义价格的最大值 @author:dingdongdong"""
        self.driver.get(beijing_buycar_url)
        time.sleep(2)

        self.driver.find_element(BuyCarTag.customer_price_btn).click()
        self.driver.find_element(BuyCarTag.price_inputMin_box).click()
        self.driver.find_element(BuyCarTag.price_inputMin_box).send_keys(0)
        self.driver.find_element(BuyCarTag.price_inputMax_box).click()
        self.driver.find_element(BuyCarTag.price_inputMax_box).send_keys(8)

        self.driver.find_element(BuyCarTag.price_Determine_btn).click()
        #获取第一个车源信息的价格
        show_carOne_name_list = self.driver.find_element(BuyCarTag.show_carlist).find_element_by_tag_name('ul').find_elements_by_tag_name('li')
        show_carone_titleName = show_carOne_name_list[0].find_elements_by_tag_name('div')
        price_text = show_carOne_name_list[0].find_element_by_xpath('//*[@id="container_base"]/ul/li[1]/div[2]/div[1]/i[2]').text
 #      price_Actual = show_carOne_name_list[0].find_element_by_xpath(BuyCarTag.shs).text
        tt = price_text.split("万")
        JRTH_price = tt[0]

        price_int = float(JRTH_price)

        if price_int >0 and price_int<8 :
            print("检索出来的车符合你的输入规则")
        else:
            print("检测出来的结果不符合你的查询")





























