excel_url = "/Users/alex/Desktop/12.xlsx"
excel_url1 = 'C:/Users/money/Desktop/12.xlsx'
login_url = 'http://www.mxstsg.com/account/login'
aiqicha_url = 'https://aiqicha.baidu.com/'
wk_url = 'http://www.mxstsg.com/account/login'
originalUrl = '/Users/alex/Desktop/2023客户数据.xlsx'
originalUrl1 = 'C:/Users/money/Desktop/2023客户数据.xlsx'
driver_url = '/Users/alex/Downloads/edgedriver_mac64/msedgedriver'
driver_url1 = 'E:\software\msedgedriver.exe'

docs = {
    '账号': '//*[@id="login_username"]',
    '密码': '//*[@id="loginform"]/div[3]/div/div/input',
    '登录': '//*[@id="loginform"]/div[6]/div/div[4]/button',
    '法律数据库': '//*[@id="sidebar"]/ul/li[3]/ul/li[3]/a',
    '(6)  威科先行': '//*[@id="content"]/div[2]/div/ul/li[5]/a',
    '入口0': '//*[@id="content"]/div[2]/div/ul/li[1]/a',
    '入口1': '//*[@id="content"]/div[2]/div/ul/li[2]/a',
    '入口2': '//*[@id="content"]/div[2]/div/ul/li[3]/a',
    '入口3': '//*[@id="content"]/div[2]/div/ul/li[4]/a',
    '点击这里登陆——法律信息库': '/html/body/font/b/h3/form/input',
    'entry': '//*[@id="information1"]/table/tbody[1]/tr/td[2]/a/button',
    '案例': '//*[@id="dropdownMenu3"]',
    '裁判文书': '//*[@id="navbar"]/ul/li[3]/ul/li[1]/a',
    '输入框': '//*[@id="queryString"]',
    '点击案件': '//*[@id="column-list"]/li[1]/b-list-item/div/div[1]/b-lock/a/span',
    '搜索': '//*[@id="search_button"]',
    '删除': '/html/body/bold-app/b-judgment/div[1]/div/div/div/div[1]/div[1]/div/div/a',
    '新搜索': '//*[@id="new_common_search_button"]',
    '内容': '//*[@id="main_detail"]',
    '下拉菜单': '/html/body/bold-app/b-judgment/div[2]/b-no-data/div[1]/div/div[2]/div/div[2]/select[2]',
    '列表': '//*[@id="column-list"]',
    '下一页': '/html/body/bold-app/b-judgment/div[2]/b-no-data/div[1]/div/div[2]/div/div[3]/pagination/ul/li[9]',
    '查看更多': '//*[@id="court_more_a"]',
    '二审判决内容': '//*[@id="main_detail"]/span/div/div[3]/div[1]/div[2]',
    '点击进入威科FF入口': '/html/body/div/p[1]/strong/span/a'
}
docsItem = {
    '加号': '//*[@id="causeOfActionǁ01000000000000民事ǁǂ"]/i',
    '合同': '//*[@id="causeOfActionǁ01000000000000民事/01040000000000合同、准合同纠纷ǁǂ_anchor"]',
    '二审': '//*[@id="instanceǁ002ǁǂ_anchor"]',
    '判决书': '//*[@id="typeOfDecisionǁ001ǁǂ_anchor"]',
}

provinces = {
    '浙江省': '//*[@id="courtǁ032000000浙江省ǁǂ_anchor"]',
    '安徽省': '//*[@id="courtǁ002000000安徽省ǁǂ_anchor"]',
    '山东省': '//*[@id="courtǁ023000000山东省ǁǂ_anchor"]',
    '河北省': '//*[@id="courtǁ011000000河北省ǁǂ_anchor"]',
    '江苏省': '//*[@id="courtǁ017000000江苏省ǁǂ_anchor"]',
    '河南省': '//*[@id="courtǁ013000000河南省ǁǂ_anchor"]',
    '北京市': '//*[@id="courtǁ003000000北京市ǁǂ_anchor"]',
    '江西省': '//*[@id="courtǁ018000000江西省ǁǂ_anchor"]',
    '陕西省': '//*[@id="courtǁ026000000陕西省ǁǂ_anchor"]',
    '山西省': '//*[@id="courtǁ025000000山西省ǁǂ_anchor"]',
    '湖北省': '//*[@id="courtǁ014000000湖北省ǁǂ_anchor"]',
    '湖南省': '//*[@id="courtǁ015000000湖南省ǁǂ_anchor"]'
}



