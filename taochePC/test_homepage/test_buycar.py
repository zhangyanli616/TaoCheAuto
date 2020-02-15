# -*- coding:utf-8 -*-
from titan import tt_check
from taochePC import Base
from taochePC.config import config
from taochePC import HomePageLocator
from taochePC import HeaderLocator
from taochePC import BuyCarLocator
import requests
import re

home_url = config.home_url


class BuyCar(Base):

    def test_buycar_title(self):
        """测试我要买车区域我要买车title显示是否正确"""
        self.driver.get(home_url)
        buycar_title = self.driver.find_element(HomePageLocator.BUY_CAR_TITLE).text

        tt_check.assertEqual("我要买车", buycar_title, "我要买车区域的title，期望是我要买车，实际是%s" % buycar_title)

    def test_buycar_jump(self):
        """测试我要买车title跳转"""
        self.driver.get(home_url)
        self.driver.click(HomePageLocator.BUY_CAR_TITLE)
        nav_buycar_class = self.driver.find_element(HeaderLocator.NAV_BUYCAR).get_attribute('class')

        tt_check.assertEqual('current', nav_buycar_class, "测试点击我要买车，跳转后的页面导航买车是否为选中状态")

    def test_buycar_brand(self):
        """测试我要买车默认品牌名称"""
        # 品牌显示根据算法排序，对测试来讲具有不确定性，容易误报
        brand_expected = ['大众', '丰田', '本田', '奥迪', '宝马', '别克', '奔驰', '查看全部']
        self.driver.get(home_url)
        brand_li = self.driver.find_element(HomePageLocator.BUY_CAR_BRAND)
        brand_links = brand_li.find_elements_by_tag_name('a')

        brand_actual = []
        for brand_link in brand_links:
            brand_actual.append(brand_link.text)

        tt_check.assertEqual(sorted(brand_actual), sorted(brand_expected), "我要买车，品牌期望是%s，实际是%s(不计顺序)" % (brand_expected, brand_actual))

    def test_buycar_brand_img(self):
        """测试我要买车默认品牌的图片请求是否正常"""
        self.driver.get(home_url)
        brand_li = self.driver.find_element(HomePageLocator.BUY_CAR_BRAND)
        brand_links = brand_li.find_elements_by_tag_name('a')

        # 获取所有品牌名称和图片地址
        brand_set = {}
        for brand_link in brand_links:
            brand = brand_link.text
            if brand != '查看全部':
                img = brand_link.find_element_by_tag_name('img').get_attribute('src')
                brand_set[brand] = img

        # 循环所有图片地址，判断请求状态码是否为200
        result = []
        for brand, src in brand_set.items():
            try:
                img_status_code = requests.get(src).status_code
                tt_check.assertEqual(200, img_status_code, "品牌%s的图片请求状态，期望是200，实际是%s" % (brand, img_status_code))

            except AssertionError as msg:
                result.append(msg)

        if result:
            raise AssertionError(result)

    def test_buycar_brand_jump(self):
        """测试我要买车品牌筛选跳转是否正确"""
        self.driver.get(home_url)
        brand_li = self.driver.find_element(HomePageLocator.BUY_CAR_BRAND)
        brand_links = brand_li.find_elements_by_tag_name('a')

        # 遍历品牌筛选结果
        result = []
        for brand_link in brand_links:
            try:
                brand = brand_link.text
                brand_link.click()

                # 在新窗口判断筛选条件是否选中了点击的品牌
                self.driver.switch_to_window()

                # 如果点击查看全部，则判断面包屑长度
                if brand == '查看全部':
                    # 面包屑包含的所有链接
                    nav_links = self.driver.find_element(BuyCarLocator.NAV_STATUS).find_elements_by_tag_name('a')
                    tt_check.assertEqual(2, nav_links.__len__(), "点击了查看全部，跳转后未包含筛选条件")
                    continue
                else:
                    filter_content = self.driver.find_element(BuyCarLocator.FILTER_SELETED) \
                        .find_element_by_tag_name('a').text
                    tt_check.assertEqual(filter_content, brand,
                                         "所选品牌%s，跳转后已选择的第一个筛选条件是%s" % (brand, filter_content))

            except AssertionError as msg:
                result.append(msg)

            finally:
                # 重置driver
                self.driver.switch_to_window()
                self.driver.close_other_window()

        if result:
            raise AssertionError(result)

    def test_buycar_price_jump(self):
        """测试我要买车价格筛选跳转是否正确"""
        self.driver.get(home_url)
        price_li = self.driver.find_element(HomePageLocator.BUY_CAR_PRICE)
        price_links = price_li.find_elements_by_tag_name('a')

        # 遍历所有价格范围
        result = []
        for price_link in price_links:
            try:
                price = price_link.text
                price_range = re.findall(r'\d+', price)
                price_link.click()

                # 在新窗口判断筛选条件是否为选择的价格范围
                self.driver.switch_to_window()
                self.driver.wait()

                filter_content = self.driver.find_element(BuyCarLocator.FILTER_SELETED) \
                    .find_element_by_tag_name('a').text
                filter_price_range = re.findall(r'\d+', filter_content)
                tt_check.assertEqual(price_range, filter_price_range,
                                     "所选价格范围%s，跳转后已选择的筛选条件是%s" % (price, filter_content))

            except AssertionError as msg:
                result.append(msg)

            finally:
                # 重置driver
                self.driver.switch_to_window()
                self.driver.close_other_window()

        if result:
            raise AssertionError(result)

    def test_buycar_level_jump(self):
        """测试我要买车级别筛选跳转是否正确"""
        self.driver.get(home_url)
        level_li = self.driver.find_element(HomePageLocator.BUY_CAR_LEVEL)
        level_links = level_li.find_elements_by_tag_name('a')

        # 遍历所有级别
        result = []
        for level_link in level_links:
            try:
                level = level_link.text
                level_link.click()

                # 在新窗口判断筛选条件是否选中了点击的级别
                self.driver.switch_to_window()
                self.driver.wait()

                # 遍历已选择的筛选条件
                filters = []
                filter_elements = self.driver.find_element(BuyCarLocator.FILTER_SELETED) \
                    .find_elements_by_tag_name('a')
                for filter_element in  filter_elements:
                    filter_name = filter_element.get_attribute('title')
                    if filter_name:
                        filters.append(filter_name)

                if level == "准新车":
                    level_expected = ["2年内", "1万公里内"]

                elif level == "练手车":
                    level_expected = ["3-5万"]

                elif level == "SUV":
                    level_expected = ["小型SUV+紧凑型SUV+中型SUV+中大型SUV+大型SUV"]

                else:
                    level_expected = level.split()

                tt_check.assertEqual(level_expected, filters, "所选级别是%s，跳转后已选择的筛选条件是%s" % (level, filters))

            except AssertionError as msg:
                result.append(msg)

            finally:
                # 重置driver
                self.driver.switch_to_window()
                self.driver.close_other_window()

        if result:
            raise AssertionError(result)

