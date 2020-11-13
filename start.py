from appium import webdriver
import time
import os

desired_caps_android_wechat = {
    "platformName": "Android",
    "platformVersion": os.getenv("APPIUM_DEVICE_VERSION", "10"),
    "automationName": os.getenv("APPIUM_AUTOMATION_NAME", "UiAutomator2"),
    "appActivity": os.getenv("APPIUM_APP_ACTIVITY", "com.tencent.mm.ui.LauncherUI"),
    "appPackage": os.getenv("APPIUM_APP_PACKAGE", "com.tencent.mm"),
    "deviceName": os.getenv("APPIUM_DEVICE_NAME", "AKC7N18907000186"),
    "newCommandTimeout": 7200,
    "noReset": True,
    "unicodeKeyboard": True,
    'resetKeyboard': True,
    'chromeOptions': {'androidProcess': 'com.tencent.mm:tools'}
}

driver = webdriver.Remote(os.getenv("APPIUM_URL", 'http://localhost:4723/wd/hub'), desired_caps_android_wechat)

print("Success to init driver")
time.sleep(15)
