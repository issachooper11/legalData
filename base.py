# 开发者:小白菜
# 开发时间: 2022/3/24 12:11
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseControl(object):
    def __init__(self, driver):
        self.driver = driver

    # 通过xpath名称找到元素
    def controlByXpath(self, info):
        return self.driver.find_element(By.XPATH, info)

    # 通过xpath名称找到元素
    def controlByXpaths(self, info):
        return self.driver.find_elements(By.XPATH, info)

    # 通过名称找到元素
    def controlByText(self, info):
        return self.driver.find_element(By.PARTIAL_LINK_TEXT, info)

    # 退出
    def closePage(self):
        return self.driver.quit()

    # 刷新页面
    def refreshPage(self):
        return self.driver.refresh()

    # 显示加载等待元素
    def waitLoading(self, path):
        wait = WebDriverWait(self.driver, 60, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
        return wait.until(EC.element_to_be_clickable((By.XPATH, path)))

    # 显示加载等待元素
    def waitLoadingByLocated(self, path):
        wait = WebDriverWait(self.driver, 60, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
        return wait.until(EC.presence_of_element_located((By.XPATH, path)))

    # 前进
    def pageForward(self):
        return self.driver.forward()

    # 倒退
    def pageBack(self):
        return self.driver.back()

    # 设置窗口大小
    def setWinSize(self, x, y):
        return self.driver.set_window_size(x, y)

    # 设置窗口位置
    def setWinPosition(self, x, y):
        return self.driver.set_window_position(x, y)

    # 设置窗口全屏
    def setMaxScreen(self):
        return self.driver.maximize_window()
