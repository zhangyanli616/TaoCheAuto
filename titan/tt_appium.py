#!/usr/bin/env python
# coding:utf-8
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from titan.tt_log import LOG
from titan import tt_config
import os
import time

report_path = tt_config.REPORT_PATH
log_dir = os.path.join(report_path, 'testScreen')
os.makedirs(log_dir, exist_ok=True)


class AppiumDriver(object):
    def __init__(self, appium_service, desired_caps):
        """
        Run class initialization method, the default is proper
        to drive the Firefox browser,. Of course, you can also
        pass parameter for other browser, such as Chrome browser for the "Chrome",
        the Internet Explorer browser for "internet explorer" or "ie".
        """

        try:
            self.driver = webdriver.Remote(appium_service, desired_caps)
            self.driver.implicitly_wait(30)
            LOG.info("【打开】手机：%s，App：%s" % (desired_caps['deviceName'], desired_caps['appPackage']))
        except Exception as msg:
            raise NameError("链接手机App失败！" + msg)

    @staticmethod
    def sleep(sec):
        """
        强制休眠
        :param sec: 秒
        :return:
        """
        time.sleep(sec)
        LOG.info("【等待】强制等待%s s" % sec)

    def touchaction_press(self, x: int, y: int):
        """
        按坐标点击
        :param x:横坐标，屏幕从左至右
        :param y:纵坐标，屏幕从上至下
        :return:
        """
        TouchAction(self.driver).press(x=x, y=y).release().perform()
        LOG.info("【点击】坐标（%d，%d)" % (x, y))

    def wait(self, seconds=5):
        self.driver.implicitly_wait(seconds)

    def find_element(self, locator):
        try:
            self.is_locator_checked(locator)
            by = locator[0]
            value = locator[1]

            if by == "id":
                return self.driver.find_element(by=By.ID, value=value)
            elif by == "name":
                return self.driver.find_element(by=By.NAME, value=value)
            elif by == "class":
                return self.driver.find_element(by=By.CLASS_NAME, value=value)
            elif by == "text":
                return self.driver.find_element(by=By.LINK_TEXT, value=value)
            elif by == "text_part":
                return self.driver.find_element(by=By.PARTIAL_LINK_TEXT, value=value)
            elif by == "xpath":
                return self.driver.find_element(by=By.XPATH, value=value)
            elif by == "css":
                return self.driver.find_element(by=By.CSS_SELECTOR, value=value)

        except NoSuchElementException:
            raise NoSuchElementException("未定位到元素,特征{0} = {1}".format(*locator))

    @staticmethod
    def is_locator_checked(locator):
        by = ['id', 'name', 'class', 'text', 'text_part', 'xpath', 'css']
        if len(locator) != 2 or locator[0] not in by:
            raise NameError("元素定位器错误'%s'，正确格式如['id', '123']。" % locator)

    def find_elements(self, locator):
        try:
            self.is_locator_checked(locator)
            by = locator[0]
            value = locator[1]

            if by == "id":
                return self.driver.find_elements(by=By.ID, value=value)
            elif by == "name":
                return self.driver.find_elements(by=By.NAME, value=value)
            elif by == "class":
                return self.driver.find_elements(by=By.CLASS_NAME, value=value)
            elif by == "text":
                return self.driver.find_elements(by=By.LINK_TEXT, value=value)
            elif by == "text_part":
                return self.driver.find_elements(by=By.PARTIAL_LINK_TEXT, value=value)
            elif by == "xpath":
                return self.driver.find_elements(by=By.XPATH, value=value)
            elif by == "css":
                return self.driver.find_elements(by=By.CSS_SELECTOR, value=value)

        except NoSuchElementException:
            raise NoSuchElementException("未定位到元素,特征{0} = {1}".format(*locator))

    def wait_element(self, locator, seconds=5):

        self.is_locator_checked(locator)
        by = locator[0]
        value = locator[1]

        try:
            if by == "id":
                WebDriverWait(self.driver, seconds).until(EC.presence_of_element_located((By.ID, value)))
            elif by == "name":
                WebDriverWait(self.driver, seconds).until(EC.presence_of_element_located((By.NAME, value)))
            elif by == "class":
                WebDriverWait(self.driver, seconds).until(EC.presence_of_element_located((By.CLASS_NAME, value)))
            elif by == "text":
                WebDriverWait(self.driver, seconds).until(EC.presence_of_element_located((By.LINK_TEXT, value)))
            elif by == "xpath":
                WebDriverWait(self.driver, seconds).until(EC.presence_of_element_located((By.XPATH, value)))
            elif by == "css":
                WebDriverWait(self.driver, seconds).until(EC.presence_of_element_located((By.CSS_SELECTOR, value)))

        except NoSuchElementException:
            raise NoSuchElementException("未定位到元素,特征{0} = {1}".format(*locator))

    def selector(self, locator):
        """
        定位选择控件
        :param locator:
        :return:
        """
        selector = self.find_element(locator)
        return Select(selector)

    def select_by_index(self, locator, index):
        """
        通过index选择控件的选项
        :param locator:
        :param index:
        :return:
        """
        self.selector(locator).select_by_index(index)
        LOG.info("【选择】特征为{0}={1}的下拉框".format(*locator) + "，选择第%d个选项" % (index + 1))

    def select_by_text(self, locator, text):
        """
        通过text选择下拉控件的选项
        :param locator:
        :param text:
        :return:
        """
        self.selector(locator).select_by_visible_text(text)
        LOG.info("【选择】特征为{0}={1}的下拉框".format(*locator) + "，选择%s" % text)

    def select_by_value(self, locator, value):
        """
        通过value选择控件的选项
        :param locator:
        :param value:
        :return:
        """
        self.selector(locator).select_by_value(value)
        LOG.info("【选择】特征为{0}={1}的下拉框".format(*locator) + "，选择value为'%s'的选项" % value)

    def select_first_option(self, locator):
        """
        选择控件的第一个选项
        :param locator:
        :return:
        """
        return self.selector(locator).first_selected_option

    def select_options(self, locator):
        """
        返回选择控件的所有选项
        :param locator:
        :return:
        """
        return self.selector(locator).options

    def element_is_selected(self, locator):
        """
        返回选择控件的已选项
        :param locator:
        :return:
        """
        return self.find_element(locator).is_selected()

    def element_is_enabled(self, locator):
        """
        返回元素是否可用
        :param locator:
        :return:
        """
        return self.find_element(locator).is_enabled()

    def send_keys(self, locator, keywords):
        try:
            self.find_element(locator).send_keys(keywords)
            LOG.info("【输入】特征为{0}={1}的元素中".format(*locator) + "，输入选择%s" % keywords)
        except Exception as msg:
            raise Exception("【输入】%s" % msg)

    def clear(self, locator):
        try:
            self.find_element(locator).clear()
            LOG.info("【清除】特征为{0}={1}元素的内容".format(*locator))
        except Exception as msg:
            raise Exception("【输入】%s" % msg)

    def click(self, locator):
        try:
            self.find_element(locator).click()
            LOG.info("【点击】点击特征为{0}={1}的元素".format(*locator))
        except Exception as msg:
            raise Exception("【点击】%s" % msg)

    def press_keycode(self, keycode):
        """
        通过按键码进行操作
        :param keycode:
        :return:
        """
        self.driver.press_keycode(keycode)

    def back(self):
        """
        Driver后退
        :return:
        """
        self.driver.back()
        LOG.info("【后退】App后退")

    def forward(self):
        """
        Driver前进
        :return:
        """
        self.driver.forward()
        LOG.info("【前进】App前进")

    def get_size(self):
        """
        返回屏幕尺寸
        :return:
        """
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y

    # 上下滑动
    def swipeUpDown(self, start, end):
        """
        上下滑动，start、end为比例，范围0到1，如0.9代表屏幕高度x0.9的位置，高度是从上到下计算
        :param start: 滑动的起始位置
        :param end: 滑动的终止位置
        :return:
        """
        screen_size = self.get_size()
        x1 = int(screen_size[0] * 0.5)
        y1 = int(screen_size[1] * start)
        y2 = int(screen_size[1] * end)
        self.driver.swipe(x1, y1, x1, y2, 300)

    # 左右滑动
    def swipeLeftRight(self, start, end):
        """
        左右滑动，start、end为比例，范围0到1，如0.9代表屏幕宽度x0.9的位置，从左至右
        :param start: 滑动的起始位置
        :param end: 滑动的终止位置
        :return:
        """
        screen_size = self.get_size()
        y1 = int(screen_size[0] * 0.5)
        x1 = int(screen_size[1] * start)
        x2 = int(screen_size[1] * end)
        self.driver.swipe(x1, y1, x2, y1, 300)

    #自定义滑动
    def swipe(self,start,start1,end,end1):
        screen_size = self.get_size()
        x1 = int(screen_size[1] * start)
        x2 = int(screen_size[1] * end)
        y1 = int(screen_size[1] * start1)
        y2 = int(screen_size[1] * end1)
        self.driver.swipe(x1,y1,x2,y2,500)


    def get_attribute(self, locator, attribute):
        """
        获取某个元素的某个属性值
        :param locator:
        :param attribute:
        :return:
        """
        return self.find_element(locator).get_attribute(attribute)

    def get_text(self, locator):
        """
        获取某个元素的文本
        :param locator:
        :return:
        """
        return self.find_element(locator).text

    def is_display(self, locator):
        """
        返回某个元素是否显示，true 显示，false 隐藏
        :param locator:
        :return:
        """
        return self.find_element(locator).is_displayed()

    def get_title(self):
        """
        获取页面Title
        :return:
        """
        return self.driver.title

    def get_url(self):
        """ 获取当前的Url"""
        return self.driver.current_url

    def get_screenshot(self, file_path):
        try:
            self.driver.get_screenshot_as_file(file_path)
            LOG.info("【截图】%s" % file_path)
        except Exception as msg:
            LOG.error("【截图】%s" % msg)

    def submit(self, locator):
        """
        提交某个元素表单
        :param locator:
        :return:
        """
        try:
            self.find_element(locator).submit()
            LOG.info("【提交】提交特征{0}={1}的表单".format(locator))
        except Exception as msg:
            raise Exception("【提交】%s" % msg)

    def refresh(self):
        """
        刷新页面
        :return:
        """
        self.driver.refresh()
        LOG.info("【刷新】")

    def close(self):
        """
        关闭当前窗口
        :return:
        """
        try:
            self.driver.close()
            LOG.info("【关闭】App")
        except ReferenceError:
            raise ReferenceError("未发现可关闭的App")

    # 此部分需要考虑app相关的操作，如切换app，唤醒app，来电打断，隐藏app等
    # def current_window_handle(self):
    #     return self.driver.current_window_handle
    #
    # def window_handles(self):
    #     return self.driver.window_handles
    #
    # def open_new_window(self, locator):
    #     current_windows = self.driver.current_window_handle
    #     self.click(locator)
    #     all_handles = self.driver.window_handles
    #     for handle in all_handles:
    #         if handle != current_windows:
    #             self.driver.switch_to.window(handle)
    #
    # def switch_to_window(self):
    #     current_windows = self.driver.current_window_handle
    #     all_handles = self.driver.window_handles
    #     for handle in all_handles:
    #         if handle != current_windows:
    #             self.driver.switch_to.window(handle)
    #
    # def close_other_window(self):
    #     current_window = self.driver.current_window_handle
    #     all_handles = self.driver.window_handles
    #     for handle in all_handles:
    #         if handle != current_window:
    #             self.driver.switch_to.window(handle)
    #             self.driver.close()
    #     self.driver.switch_to.window(current_window)

    def screen_shot(self, caseName):
        screen_shot_time = time.strftime('%H%M%S', time.localtime())
        screen_shot_name = caseName + "_" + screen_shot_time + ".png"
        screen_shot_fullname = os.path.join(log_dir, screen_shot_name)
        self.driver.get_screenshot_as_file(screen_shot_fullname)
        LOG.error("【异常】<a href='%s'>截图</a>" % screen_shot_fullname)

    def quit(self):
        """
        退出驱动
        :return:
        """
        self.driver.quit()



