# 开发者:小白菜
# 开发时间: 2022/3/24 12:11
# 威科更新 需要在输入框输入二审，再按照流程获取数据
import traceback

from method import getFreshData, getNewWkData
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from controller import EdgeControl
from util import chooseUrl, showInfo

if __name__ == '__main__':
    print('请选择任务啦')
    print('1------抓取威科全部的新数据')
    print('2------打开信息表查看数据是否符合要求')
    print('3------测试项目')
    print('4------根据12.xlsx与信息报对照获取新数据并保存')
    task_code = input('亲, 请选择任务啦-----------:')
    if task_code == '4':
        # 运行完方法获得新数据后 去重 再爱企查批量查询导出 不然报错
        # getFreshData()
        getNewWkData()
    else:
        ser = Service(chooseUrl(2))
        op = webdriver.EdgeOptions()
        dr = webdriver.Edge(service=ser, options=op)
        # 实例化edge开始按照步骤登录
        lg = EdgeControl(dr)
        lg.login()
        if task_code == '1':
            seconds = 35
            pageNum = 10
            try:
                lg.login_and_collectAllNewData(seconds, pageNum)
            except:
                traceback.print_exc()
                showInfo('出错啦!!!')
                lg.closePage()
            finally:
                showInfo('完事啦！！')
        elif task_code == '2':
            try:
                lg.open_and_checkData()
            except:
                traceback.print_exc()
                showInfo('出错啦!!!')
                lg.closePage()
            finally:
                showInfo('结束')
        else:
            pass
