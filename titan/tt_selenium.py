#!/usr/bin/env python
# coding:utf-8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from titan.tt_log import LOG
from titan import tt_config
import os
import time

report_path = tt_config.REPORT_PATH
log_dir = os.path.join(report_path, 'testScreen')
os.makedirs(log_dir, exist_ok=True)


class SeleniumDriver(object):
    def __init__(self, browser='chrome', btype='pc', is_headless=False, mobile_options=None):
        """
        Run class initialization method, the default is proper
        to drive the Firefox browser,. Of course, you can also
        pass parameter for other browser, such as Chrome browser for the "Chrome",
        the Internet Explorer browser for "internet explorer" or "ie".
        """
        if browser == "firefox":
            driver = webdriver.Firefox()

        elif browser == "ie":
            driver = webdriver.Ie()

        elif browser == "chrome":
            options = webdriver.ChromeOptions()
            # 是否开启静默
            if is_headless:
                options.add_argument('--headless')
                options.add_argument('--disable-gpu')

            if btype == "pc":
                driver = webdriver.Chrome(chrome_options=options)

            elif btype == "m":
                options.add_argument(mobile_options)
                driver = webdriver.Chrome(chrome_options=options)
            else:
                raise NameError("选择Chrome时，默认为pc，测试M站需要指定type='m'。")

        try:
            self.driver = driver
            LOG.info("【打开】%s" % browser)
        except Exception as msg:
            raise NameError("泰坦仅支持Firefox、IE和Chrome浏览器！" + msg)

    def get(self, url):
        self.driver.get(url)
        LOG.info("【访问】%s" % url)

    def max_window(self):
        self.driver.maximize_window()
        LOG.info("最大化浏览器")

    def set_window_size(self, wide, high):
        """
        Set browser window wide and high.

        Usage:
        driver.set_window_size(wide,high)
        """
        self.driver.set_window_size(wide, high)
        LOG.info("设置浏览器宽%s,高s%" % (wide, high))

    @staticmethod
    def pause(seconds):
        time.sleep(seconds)

    def wait(self, seconds=5):
        self.driver.implicitly_wait(seconds)

    def execute_script(self,  script, *args):
        self.driver.execute_script(script, args)

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
        selector = self.find_element(locator)
        return Select(selector)

    def select_by_index(self, locator, index):
        self.selector(locator).select_by_index(index)
        LOG.info("【选择】特征为{0}={1}的下拉框".format(*locator) + "，选择第%d个选项" % (index + 1))

    def select_by_text(self, locator, text):
        self.selector(locator).select_by_visible_text(text)
        LOG.info("【选择】特征为{0}={1}的下拉框".format(*locator) + "，选择%s" % text)

    def select_by_value(self, locator, value):
        self.selector(locator).select_by_value(value)
        LOG.info("【选择】特征为{0}={1}的下拉框".format(*locator) + "，选择value为'%s'的选项" % value)

    def select_first_option(self, locator):
        return self.selector(locator).first_selected_option

    def select_options(self, locator):
        return self.selector(locator).options

    def element_is_selected(self, locator):
        return self.find_element(locator).is_selected()

    def element_is_enabled(self, locator):
        return self.find_element(locator).is_enabled()

    def send_keys(self, locator, keywords):
        try:
            self.find_element(locator).send_keys(keywords)
            LOG.info("【输入】特征为{0}={1}的元素中".format(*locator) + "，输入选择%s" % keywords)
        except Exception as msg:
            raise Exception("【输入】%s" % msg)

    def click(self, locator):
        try:
            self.find_element(locator).click()
            LOG.info("【点击】点击特征为{0}={1}的元素".format(*locator))
        except Exception as msg:
            raise Exception("【点击】%s" % msg)

    # def right_click(self, element):
    #     """
    #     Right click element.
    #
    #     Usage:
    #     driver.right_click("class=right")
    #     """
    #     LOG.info("右击元素！")
    #
    #     try:
    #         ActionChains(self.driver).context_click(self.find_element(element)).perform()
    #     except NoSuchElementException as message:
    #         LOG.error(message)
    #
    # def move_to_element(self, element):
    #     '''
    #     Mouse over the element.
    #
    #     Usage:
    #     driver.move_to_element("css=choose")
    #     '''
    #     LOG.info("移动到该元素")
    #     try:
    #         ActionChains(self.driver).move_to_element(self.find_element(element)).perform()
    #     except NoSuchElementException as message:
    #         LOG.error(message)
    #
    # def double_click(self, element):
    #     """
    #     Double click element.
    #
    #     Usage:
    #     driver.double_click("name=baidu")
    #     """
    #     LOG.info("双击该元素！")
    #     try:
    #         ActionChains(self.driver).double_click(self.find_element(element)).perform()
    #     except NoSuchElementException as message:
    #         LOG.error(message)
    #
    # def drag_and_drop(self, source_element, target_element):
    #     """
    #     Drags an element a certain distance and then drops it.
    #
    #     Usage:
    #     driver.drag_and_drop("id=s","id=t")
    #     """
    #     LOG.info("拖拽页面")
    #
    #     try:
    #         ActionChains(self.driver).drag_and_drop(self.find_element(source_element),
    #                                                 self.find_element(target_element)).perform()
    #     except NoSuchElementException as message:
    #         LOG.error(message)
    #
    def back(self):
        self.driver.back()
        LOG.info("浏览器返回")

    def forward(self):
        self.driver.forward()
        LOG.info("浏览器前进")

    def get_attribute(self, locator, attribute):
        return self.find_element(locator).get_attribute(attribute)

    def get_text(self, locator):
        return self.find_element(locator).text

    def is_display(self, locator):
        return self.find_element(locator).is_displayed()

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def get_screenshot(self, file_path):
        try:
            self.driver.get_screenshot_as_file(file_path)
            LOG.info("【截图】%s" % file_path)
        except Exception as msg:
            LOG.error("【截图】%s" % msg)

    def submit(self, locator):
        try:
            self.find_element(locator).submit()
            LOG.info("【提交】提交特征{0}={1}的表单".format(locator))
        except Exception as msg:
            raise Exception("【提交】%s" % msg)


    def F5(self):
        self.driver.refresh()
        LOG.info("【刷新】")

    # def scrollto_element(self, element):
    #     '''
    #
    #     :param element: 移动至元素
    #     :return:
    #     '''
    #     LOG.info("滑动页面至元素")
    #     try:
    #         self.driver.execute_script("arguments[0].scrollIntoView();", element)
    #     except NoSuchElementException as message:
    #         LOG.error(message)
    #
    # def js(self, script):
    #     """
    #     Execute JavaScript scripts.
    #
    #     Usage:
    #     driver.js("window.scrollTo(200,1000);")
    #     """
    #     LOG.info("输入js：%s" % script)
    #     try:
    #         self.driver.execute_script(script)
    #     except NoSuchElementException as message:
    #         LOG.error(message)
    #
    # def exjstoElement(self, script, element):
    #     """
    #     Execute JavaScript scripts.
    #
    #     Usage:
    #     driver.js("window.scrollTo(200,1000);")
    #     """
    #     LOG.info("输入js：%s" % script)
    #     try:
    #         self.driver.execute_script(script, element)
    #     except NoSuchElementException as message:
    #         LOG.error(message)
    #
    def alert_accept(self):
        try:
            self.driver.switch_to.alert.accept()
            LOG.info("【确认提示框】")
        except AttributeError:
            raise AttributeError("未发现alert框")

    def alert_dismiss(self):
        try:
            self.driver.switch_to.alert.dismiss()
            LOG.info("【关闭提示框】")
        except AttributeError:
            raise AttributeError("未发现alert框")

    def alert_text(self):
        try:
            self.driver.switch_to.alert.text()
        except AttributeError:
            raise AttributeError("未发现alert框")

    def close(self):
        try:
            self.driver.close()
            LOG.info("【关闭】浏览器")
        except ReferenceError:
            raise ReferenceError("未发现可关闭的浏览器")

    def current_window_handle(self):
        return self.driver.current_window_handle

    def window_handles(self):
        return self.driver.window_handles

    def open_new_window(self, locator):
        current_windows = self.driver.current_window_handle
        self.click(locator)
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != current_windows:
                self.driver.switch_to.window(handle)

    def switch_to_window(self):
        current_windows = self.driver.current_window_handle
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != current_windows:
                self.driver.switch_to.window(handle)

    def close_other_window(self):
        current_window = self.driver.current_window_handle
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != current_window:
                self.driver.switch_to.window(handle)
                self.driver.close()
        self.driver.switch_to.window(current_window)

    def screen_shot(self, caseName):
        screen_shot_time = time.strftime('%H%M%S', time.localtime())
        screen_shot_name = caseName + "_" + screen_shot_time + ".png"
        screen_shot_fullname = os.path.join(log_dir, screen_shot_name)
        self.driver.get_screenshot_as_file(screen_shot_fullname)
        LOG.error("【异常】<a href='%s'>截图</a>" % screen_shot_fullname)

    def quit(self):
        self.driver.quit()

