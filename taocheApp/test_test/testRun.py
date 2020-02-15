# -*- encoding:utf-8 -*-
from taocheApp import Base, HomeLoctor


class Login(Base):
    def test_home_page(self):
        self.driver.find_element(HomeLoctor.SEARCH_MORE).click()
        self.driver.sleep(1)
