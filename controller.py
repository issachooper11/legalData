# 开发者:小白菜
# 开发时间: 2022/3/24 12:27
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from base import BaseControl
from method import getUnEditCodes, getPlaintiff
from util import showInfo, docs, delay, provinces, filterHtmlData, wk_url, handleByInfo, manual_confirm, changeData, \
    transToExcel


class EdgeControl(BaseControl):
    def __init__(self, driver):
        super().__init__(driver)

    def login_test(self):
        showInfo('开始登录')
        self.setWinPosition(0, 0)
        self.setWinSize(1024, 1024)
        self.driver.get('https://www.bjcourt.gov.cn/')
        delay(15)
        self.driver.find_element(By.LINK_TEXT, '公告公示').click()
        delay(20)
        self.driver.quit()

    # 登陆程序简化出来可以复用
    def login(self):
        showInfo('开始登录')
        # self.driver.maximize_window()
        self.setWinPosition(0, 0)
        self.setWinSize(1024, 1024)
        self.driver.get(wk_url)
        self.controlByXpath(docs['账号']).send_keys('jianyu_a_wang2022')
        self.controlByXpath(docs['密码']).send_keys('caiyuan2022')
        self.controlByXpath(docs['登录']).click()
        # 点击法律数据库
        self.waitLoading(docs['法律数据库']).click()
        # 点击(6)  威科先行
        self.waitLoading(docs['(6)  威科先行']).click()
        # 选择入口
        enter_code = input('选择入口,(enter)默认是0--1--2--3:')
        if enter_code == '1':
            # 只点进去即可
            self.waitLoading(docs['入口1']).click()
        elif enter_code == '2':
            self.waitLoading(docs['入口2']).click()
        elif enter_code == '3':
            self.waitLoading(docs['入口3']).click()
        elif enter_code == '':
            self.waitLoading(docs['入口0']).click()
        # 切换到新窗口
        if len(self.driver.window_handles) > 1:
            self.driver.switch_to.window(self.driver.window_handles[1])
        # 点击法律数据库
        # if enter_code == '':
        #     self.waitLoading(docs['点击进入威科FF入口']).click()
        # 切换到新窗口
        # if len(self.driver.window_handles) > 2:
        #     self.driver.switch_to.window(self.driver.window_handles[2])
        #     # 进入页面如空白刷新下
        #     self.driver.refresh()
        handleByInfo('进入主页面')
        # 切换到最终窗口
        self.waitLoading(docs['案例'])
        # 对定位到的元素执行鼠标悬停操作
        ActionChains(self.driver).move_to_element(self.controlByXpath(docs['案例'])).perform()
        # 点击裁判文书
        self.waitLoading(docs['裁判文书']).click()
        handleByInfo('按回车继续')

    # 登录指定网站并抓取新数据
    def login_and_collectAllNewData(self, sec, pageNum):
        showInfo('进入主页面')
        self.waitLoading(docs['输入框']).send_keys('二审')
        delay(2)
        self.waitLoading(docs['搜索']).click()
        # self.waitLoading(docs['下拉菜单'])
        # showInfo('点击下拉菜单100')
        # Select(self.controlByXpath(docs['下拉菜单'])).select_by_value('100')
        finalArr = []
        # 手动点击条件
        a = input('手动点击条件')
        # 不符合要求的关闭窗口打开下一个
        if a == '':
            showInfo('开始点击:查看更多')
            self.driver.execute_script('window.scrollTo(0,220);')
            self.controlByText('查看更多').click()
        # 点击加号
        # for k in docsItem:
        #     showInfo('开始点击:' + k)
        #     self.controlByXpath(docsItem[k]).click()
        #     delay(sec)
        for v in provinces:
            # if '陕西省' == v:
            #     # 手动点击条件
            #     a = input('省份需要手动点击了')
            #     # 不符合要求的关闭窗口打开下一个
            #     if a == '':
            #         pass
            showInfo('开始点击:' + v)
            self.controlByXpath(provinces[v]).click()
            delay(sec)
            showInfo('开始采集数据')
            # 积累数据
            finalData = []
            for i in range(pageNum):
                list_text = []
                for li in self.controlByXpath(docs['列表']).find_elements(By.TAG_NAME, 'li'):
                    list_text.append(li.text)
                finalData.extend(list_text)
                self.controlByText('下一页').click()
                delay(20)
            finalArr.extend(finalData)
            # filterHtmlData(finalData)
            # self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
        filterHtmlData(finalArr)
        showInfo('打印最终抓取的数据')
        showInfo('任务完成，全部退出')
        self.driver.quit()

    # 打开收集的数据根据案号查看判决内容识别是否符合电话对象
    def open_and_checkData(self):
        court_codes = getUnEditCodes()
        showInfo('进入主页面')
        showInfo('开始打开案件详情页')
        self.waitLoading(docs['输入框'])
        for num, i in enumerate(court_codes):
            self.controlByXpath(docs['输入框']).send_keys(i)
            delay(2)
            if num == 0:
                self.waitLoading(docs['搜索'])
                self.controlByXpath(docs['搜索']).click()
            else:
                self.waitLoading(docs['新搜索'])
                self.controlByXpath(docs['新搜索']).click()
            delay(3)
            self.controlByXpath(docs['点击案件']).click()
            delay(10)
            # 跳转到案件详情页并滑到底部看判决内容
            self.driver.switch_to.window(self.driver.window_handles[-1])
            self.waitLoading(docs['二审判决内容'])
            for content in self.controlByXpath(docs['二审判决内容']).find_elements(By.TAG_NAME, 'p'):
                print(content.text)
            delay(3)
            self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            a = input('请确认本判决是否符合要求（enter，不符合）:')
            # 不符合要求的关闭窗口打开下一个
            if a == '':
                self.driver.close()
            elif a == '0000':
                self.driver.quit()
            else:
                pass
            # delay(2)
            # 再转移回搜索页面 删除输入的内容 入口2的时候开随便开一个网页占位
            if len(self.driver.window_handles) > 2:
                self.driver.switch_to.window(self.driver.window_handles[2])
            else:
                self.driver.switch_to.window(self.driver.window_handles[1])
            delay(2)
            self.controlByXpath(docs['删除']).click()
            delay(2)

    # 执行逻辑：
    # 登陆指定网站
    # 手动点击条件节约时间
    # 每页获取100条数据后循环判断抓取信息，
    # 如果符合公司名称则点击链接转入详情页查询是否为合格数据，并手动复制判决内容输入到方法中保存
    # 否则倒计时3s自动跳过进入下一条信息的判断，不预设翻页参数，添加方法手动跳出
    def collect_data(self):
        self.waitLoading(docs['输入框']).send_keys('二审')
        delay(2)
        self.waitLoading(docs['搜索']).click()
        finalArr = []
        total_num = 0
        manual_confirm('手动点击条件，完成后按回车继续工作')
        while True:
            data_input = input('程序是否继续运行:')
            if data_input == '':
                list_text = []
                for li in self.controlByXpath(docs['列表']).find_elements(By.TAG_NAME, 'li'):
                    list_text.append(li.text)
                showInfo('未处理的数据展示如下')
                new_list_text = getPlaintiff(changeData(list_text))
                # print(changeData(list_text))
                # new_filter_list_text = changeData(list_text)
                # filter_list_text = []
                # if len(new_list_text) > 0:
                #     for i in new_list_text:
                #         check_data = input(i[0] + '---是否符合要求:')
                #         if check_data == '':
                #             showInfo('打开进入详情页')
                #             self.driver.find_element(By.PARTIAL_LINK_TEXT, i[0]).click()
                #             self.driver.switch_to.window(self.driver.window_handles[-1])
                #             detail_data = input('案件是否符合要求：')
                #             if detail_data == '':
                #                 filter_list_text.extend(i)
                #                 showInfo('已添加')
                #                 self.driver.close()
                #             else:
                #                 showInfo('不符合')
                #                 self.driver.close()
                #         else:
                #             showInfo('过滤')
                #         if len(self.driver.window_handles) > 2:
                #             self.driver.switch_to.window(self.driver.window_handles[2])
                #         else:
                #             self.driver.switch_to.window(self.driver.window_handles[1])
                showInfo('本页收集' + str(len(new_list_text)) + '条有效数据')
                finalArr.extend(new_list_text)
                total_num = total_num + len(new_list_text)
                self.controlByText('下一页').click()
                showInfo('等待页面加载完')
                delay(10)
            elif data_input == '2023':
                manual_confirm('手动切换地区，按回车继续采集')
            else:
                showInfo('最终数据' + str(total_num) + '条数据')
                print(finalArr)
                print(len(finalArr))
                transToExcel(finalArr)
                break
