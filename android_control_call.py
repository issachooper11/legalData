import uiautomator2 as u2
from method import delay
c = u2.connect_usb('e697a1a5')
# c = u2.connect_adb_wifi('192.168.0.100')
# c = u2.connect('192.168.0.100:5555')
c.app_start('com.tencent.mm')
delay(3)
c.click(0.93, 0.069)

# # 点击底部加号按钮
# c(resourceId="com.tencent.mm:id/aqe").click()
# # 点击添加朋友选项
# c(text="添加朋友").click()
# # 在搜索框中输入微信号或手机号码
# c(resourceId="com.tencent.mm:id/bhn").set_text("要添加的好友微信号或手机号码")
# # 点击搜索按钮
# c(resourceId="com.tencent.mm:id/kh").click()
delay(3)
c.app_stop('com.tencent.mm')