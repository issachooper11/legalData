import uiautomator2 as u2
from method import delay, getDailyPhoneCallInfo
import os


# 本文件实现excel表当日待呼叫数据的获取，根据手机号查询微信名称并呼叫
def open_wechat():
    c = u2.connect_usb('e697a1a5')
    c.app_start('com.tencent.mm')
    x = input('微信是否已经打开输入框(回车是已经打开了)：')
    if x != '':
        print('没打开')
        c.click(0.926, 0.072)  # 点击+号
        c(text='添加朋友').click(offset=(0.5, 0.5))  # 点击添加朋友
        c.click(0.384, 0.127)  # 点击空白行
    else:
        pass
    data = getDailyPhoneCallInfo(3061.0)
    for i in data:
        print(i[2])
        for j in i[2]:
            delay(3)
            c(focused=True).set_text(j)  # 输入电话号
            delay(3)
            c.click(0.411, 0.138)  # 点击搜索
            delay(5)
            c.click(0.053, 0.072)  # 返回
            delay(2)
            c.click(0.811, 0.074)  # 清除
            delay(1)


def call_wechat():
    data = getDailyPhoneCallInfo(3061.0)
    for i in data:
        print(i)
        for j in i[2]:
            # 使用ADB命令拨打电话
            a = input('是否呼叫：')
            if a == '':
                os.system(f'adb shell am start -a android.intent.action.CALL -d tel:{j}')
            else:
                print('结束')


call_wechat()
