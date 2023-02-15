# 开发者:小白菜
# 开发时间: 2022/3/24 12:11
from openpyxl import load_workbook

from util import chooseUrl


# 获取信息表所有的公司名称和新抓取的数据进行对比
def getCoureCode():
    wb = load_workbook(chooseUrl(3))
    ws = wb['2023信息']
    list = []
    for num, j in enumerate(ws.rows):
        if num > 0:
            for index, n in enumerate(j):
                if 2 == index:
                    list.append(n.value)
    return list


# 获取没有验证的所有案号
def getUnEditCodes():
    wb = load_workbook(chooseUrl(3))
    ws = wb['2022信息']
    arr = []
    for num, j in enumerate(ws.rows):
        if num > 0:
            for index, n in enumerate(j):
                if 0 == index:
                    if n.value is not None:
                        break
                if 1 == index:
                    arr.append(n.value)
                if 3 == index:
                    if len(str(n.value)) != 11:
                        arr.pop()
                        break
    return arr


# 获取案号和公司名称
def getCodeAndNames():
    wb = load_workbook(chooseUrl(3))
    ws = wb['2022信息']
    lists = []
    for num, j in enumerate(ws.rows):
        arr = []
        if num > 0:
            for index, n in enumerate(j):
                if 1 == index:
                    arr.append(n.value)
                if 2 == index:
                    arr.append(n.value)
            lists.append(arr)
    return lists


# 对新表循环获取处理过的公司数据
def getFreshData():
    url = chooseUrl(1)
    wb = load_workbook(url)
    ws = wb['Sheet']
    arr = getCoureCode()
    news = wb.create_sheet()
    news.append(['公司名称', '案号', '法院', '日期'])
    for num, j in enumerate(ws.rows):
        if num > 0:
            new_list = []
            for index, n in enumerate(j):
                # 判断顺序 是0则为公司字符串 否则为案号等其他信息
                if 0 == index:
                    if n.value in arr:
                        print('第' + str(num) + '行原表里已经有了...........' + n.value)
                        break
                    else:
                        print('第' + str(num) + '行添到新的数据了...........' + n.value)
                        new_list.append(n.value)
                else:
                    new_list.append(n.value)
            if len(new_list) != 0:
                news.append(new_list)
    wb.save(url)
    print('成功筛选')


# 对抓取完的初始数据进行筛查和处理 找出公司客户
def getNewWkData():
    url = chooseUrl(1)
    wb = load_workbook(url)
    ws = wb['Sheet']
    news = wb.create_sheet()
    news.append(['公司名称', '案号', '法院', '日期'])
    for num, j in enumerate(ws.rows):
        if num > 0:
            list = []
            for index, n in enumerate(j):
                # 判断顺序 是0则为公司字符串 否则为案号等其他信息
                if 0 == index:
                    name = n.value
                    if name.find('、') != -1:
                        name = name.split('、')[0]
                    elif name.find('与') != -1:
                        name = name.split('与')[0]
                        if name.find('等') != -1:
                            name = name.split('等')[0]
                    elif name.find('等') != -1:
                        name = name.split('等')[0]
                    elif name.find('二审') != -1:
                        name = name.split('二审')[0]
                    else:
                        pass
                    if len(name) > 5:
                        if checkValue(name):
                            list.append(name)
                    else:
                        break
                else:
                    list.append(n.value)
            if len(list) == 4:
                news.append(list)
    wb.save(url)
    print('成功筛选')
    a = input('手动剔除重复项目，是否再启动对比程序并添加新数据:')
    # 不符合要求的关闭窗口打开下一个
    if a == '':
        getFreshData()
    else:
        pass


def checkValue(data):
    if '银行' in data:
        return False
    elif '委员会' in data:
        return False
    elif '解放军' in data:
        return False
    elif '律师' in data:
        return False
    elif '学校' in data:
        return False
    elif '医院' in data:
        return False
    elif '政府' in data:
        return False
    elif '学院' in data:
        return False
    elif '大学' in data:
        return False
    elif '中学' in data:
        return False
    elif '小学' in data:
        return False
    elif '合作社' in data:
        return False
    elif '纠纷' in data:
        return False
    else:
        return True


# 处理数组内容中含'等 、 二审等字样的内容只截取到原告信息进行判断
# 去重复项目 去空项目 去个人项目
def getPlaintiff(arr):
    new_arr = arr
    separators = ['与', '等', '二审', '、', ';', '*', '·']
    for i in arr:
        for sep in separators:
            i[0] = i[0].split(sep)[0]
    unique_dict = {}
    for array in new_arr:
        key = array[0]
        if key != '':
            if len(key) > 4:
                if checkValue(key):
                    if key not in unique_dict:
                        unique_dict[key] = array
    return list(unique_dict.values())
