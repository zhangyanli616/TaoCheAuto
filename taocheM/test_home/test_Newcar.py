# -*- coding:utf-8 -*-
#@author:xulanzhong

from titan import tt_check
from taocheM.base_m import Base
from taocheM.locator_m import Locator_Home
from taocheM.config_m import config

url = config.home_url

class Newcar(Base):

    # def test_New(self):
    #
    #     """测试首页淘车新车楼层是否展示,@author:xulanzhong"""
    #     self.driver.get(url)
    #
    #     self.driver.pause(2)
    #
    #     self.driver.execute_script("window.scrollTo(0, 120)")
    #
    #     self.driver.pause(2)
    #
    #     Newcar_is_dispayed = self.driver.is_display(Locator_Home.Newcar)
    #
    #     self.driver.pause(2)
    #
    #     tt_check.assertTrue(Newcar_is_dispayed, "首页淘车心选是否显示：%s" % Newcar_is_dispayed)

    def test_ncar(self):

        """测试点击首页新车推荐，跳转新车是否包含新车签,@author:xulanzhong"""

        self.driver.get(url)

        self.driver.pause(2)

        #self.driver.execute_script("window.scrollTo(0, 1300)")

        # js = "var q=document.body.scrollTop=0"
        # self.driver.execute_script(js)

        self.driver.pause(2)

        self.driver.click(Locator_Home.ncar)

        self.driver.pause(2)

        test_ncar = self.driver.is_display(Locator_Home.ncar_label)

        tt_check.assertTrue(test_ncar, "新车签是否显示， %s" % test_ncar)


    def test_Newcar(self):

        """测试默认品牌名称,@author:xulanzhong"""

        Newcar_expect = ['新车推荐', '开走吧', '分期购车']

        self.driver.get(url)

        self.driver.execute_script("window.scrollTo(0, 900)")

        self.driver.pause(2)

        Newcar_li = self.driver.find_element(Locator_Home.Newcar_list)
        Newcar_links = Newcar_li.find_elements_by_tag_name('a')

        Newcar_actual = []

        for Newcar_link in Newcar_links:
            Newcar_actual.append(Newcar_link.text)

        tt_check.assertEqual(sorted(Newcar_actual), sorted(Newcar_expect), "淘车新车楼层，期望是%s，实际是%s" % (Newcar_expect, Newcar_actual))