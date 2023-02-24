from method import getFreshData, chooseUrl
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from controller import EdgeControl
if __name__ == '__main__':
    print('请选择任务啦')
    print('1------抓取威科全部的新数据')
    print('2------打开信息表查看数据是否符合要求')
    print('3------测试项目')
    print('4------根据12.xlsx与信息报对照获取新数据并保存')
    task_code = input('请选择任务啦-----------:')
    if task_code == '4':
        # 实例化edge开始按照步骤登录
        ser = Service(chooseUrl(2))
        op = webdriver.EdgeOptions()
        dr = webdriver.Edge(service=ser, options=op)
        lg = EdgeControl(dr)
        check_cpwsw = input('抓取裁判文书网数据(回车) or 打开信息表查看判决信息：')
        if check_cpwsw == '':
            lg.login_cpwsw()
        else:
            lg.login_cpws()
        a = input('是否开始筛选新数据:')
        if a == '':
            print('yes')
            getFreshData()
        else:
            print('no')

    else:
        # 实例化edge开始按照步骤登录
        ser = Service(chooseUrl(2))
        op = webdriver.EdgeOptions()
        dr = webdriver.Edge(service=ser, options=op)
        lg = EdgeControl(dr)
        lg.login()
        if task_code == '1':
            lg.collect_data()
        elif task_code == '2':
            lg.open_and_checkData()
        else:
            pass

