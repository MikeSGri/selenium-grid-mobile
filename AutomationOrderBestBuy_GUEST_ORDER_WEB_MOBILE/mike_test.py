import os
import time
import project_parameters
from selenium import webdriver
import time
from subtests import test_applygiftcards
from subtests import test_getgiftcards
from subtests import test_getorder
from subtests import test_product_mobile_web
from subtests import test_reportstepfinish
from subtests import test_sendordercornercloud
from subtests import test_shipping_mobile_web
import pytest


def drivercall():
    # project_parameters.zone = os.getenv('Zone', 'orderZoneOhio')
    #test_getorder.test_main()
    print("starting grid")
    capabilities = {"platformName": "Android", "browserName": "chrome"}
    driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=capabilities)
    time.sleep(5)

    print("grid has been achieved")
    driver.implicitly_wait(20)
    #chrome_cmd_off = 'docker exec -it '+ deviceId[device] + ' adb shell pm clear com.android.chrome'
    #os.popen(chrome_cmd_off)
    #deviceId = {"ce031713e05ad8300d": "4bafbd2b3de4"}

    #device = driver.capabilities["deviceName"]

    #chrome_cmd_off = 'docker exec -it '+ deviceId[device] + ' adb shell svc data disable'
    #chrome_cmd_on = 'docker exec -it '+ deviceId[device] + ' adb shell svc data enable'
    #device_ip = 'docker exec -it ' + deviceId[device] + 'adb shell ifconfig "| grep Mask"'

    return driver
    
def test_main():
    try:
        driver = drivercall()
        print("changing ip")
        driver.get("https://www.whatismyip.com/")
        time.sleep(3)
        #chrome_cmd_off = ' docker exec -it '+ devicedID[device] + ' 
        # 13. Run reportStepFinish

        driver.quit()
    except Exception as e:
        print(str(e))
     #   chrome_cmd_off = 'docker exec -it '+ deviceId[device] + ' adb shell pm clear com.android.chrome'
        os.popen(chrome_cmd_off)
        driver.quit()

