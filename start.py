from appium import webdriver
import time
import os

desired_caps_ios_wechat = {
    "platformName": "iOS",
    "PlatformVersion": os.getenv('APP_DEVICE_VERSION', "12.2"),
    "deviceName": os.getenv('APP_DEVICE_NAME', "iPhone"),
    "automationName": "XCUITest",
    "udid": os.getenv("APP_UDID", "029d553ea04ba899509dc0630fda19bdac61231a"),
    "bundleId": os.getenv("APP_BUNDLEIDENTIFIER", "com.tencent.xin"),
    "newCommandTimeout": 7200,
    "startIWDP": True,
    "webDriverAgentUrl": os.getenv("WEBDRIVERAGENT_URL", "http://localhost:8100")
}

driver = webdriver.Remote(os.getenv("APPIUM_URL", 'http://localhost:4723/wd/hub'), desired_caps_ios_wechat)

print("Success to init driver")
time.sleep(15)
