import os

# 输入电话号码
phone_number = '13644120346'
os.system(f'adb shell am start -a android.intent.action.CALL -d tel:{phone_number}')

