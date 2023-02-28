import uiautomator2 as u2
from method import delay
import os


def check_phone_and_call(info_number):
    c = u2.connect_usb('e697a1a5')
    c.app_start('com.tencent.mm')
    delay(3)
    x = input('微信是否已经打开输入框(回车是已经打开了)：')
    if x != '':
        print('没打开')
        c.click(0.926, 0.072)  # 点击+号
        c(text='添加朋友').click(offset=(0.5, 0.5))  # 点击添加朋友
        c.click(0.384, 0.127)  # 点击空白行
    else:
        pass
    c.send_keys(info_number, clear=True)  # 输入电话号
    delay(3)
    c.click(0.411, 0.138)  # 点击搜索
    delay(5)
    c.click(0.053, 0.072)  # 返回
    delay(2)
    c.click(0.811, 0.074)  # 清除
    delay(1)
    c.press("home")
    # 使用ADB命令拨打电话
    a = input('是否呼叫：')
    if a == '':
        os.system(f'adb shell am start -a android.intent.action.CALL -d tel:{info_number}')
    else:
        print('结束')


phone = '13644120346'
check_phone_and_call(phone)
