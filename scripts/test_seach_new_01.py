from appium import webdriver
import pytest, time
from selenium.webdriver.common.by import By
from Page.searchPage import SearchPage
from Base.driver import Driver
from Base.get_date import Get_date

import allure
def gettt_date():
    date=Get_date.get_date('search_date.yaml')
    list = []
    for x in date:
        p = tuple(x.values())
        list.append(p)
    return list


date=gettt_date()
class Test_Search:

    def setup_class(self):
        # 实例化页面类
        self.sp_obj = SearchPage()

    def teardown_class(self):
        """退出driver"""
        Driver.quit_app_driver()

    # 因为只需要运行一次 并且是依赖方法，所以使用fixture工厂函数
    @pytest.fixture(scope="class", autouse=True)
    def click_search_btn(self):
        """点击搜索按钮 并且 点击一次"""
        self.sp_obj.click_search_btn()
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.step('总共分三步')
    @pytest.mark.parametrize("search_data, exp_data",date)
    def test_search_text_01(self, search_data, exp_data):
        """
        搜索测试方法
        :param search_data: 输入内容
        :param exp_data: 预期结果
        :return:
        """
        # 输入框输入内容
        self.sp_obj.search_text(search_data)
        allure.attach('测试输入框的','附件名字')
        # 断言
        assert exp_data in self.sp_obj.get_search_result()
    @allure.severity(allure.severity_level.CRITICAL)
    def test_02(self):
        print('哈哈哈')

    @allure.severity(allure.severity_level.NORMAL)
    def test_03(self):
        print('嘎嘎嘎嘎')

    @allure.severity(allure.severity_level.MINOR)
    def test_04(self):
        print('嘻嘻嘻嘻')

    @allure.severity(allure.severity_level.TRIVIAL)
    def test_05(self):
        prit('呵呵呵')
