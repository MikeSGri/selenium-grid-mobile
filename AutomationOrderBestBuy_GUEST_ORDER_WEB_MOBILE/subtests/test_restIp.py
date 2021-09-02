import os
import test_guest_order_web_mobile
import time



def test_main(driver):
    deviceId = {"KPS7N18419007886": "d8b842424a8d", "AGT4C19425000061":"5b91bb5cb9da", "5200ca115ba01547":"b31ac489b390"}
    
 

    device = driver.capabilities["deviceName"]
    print("DEVICE NANE --",driver.capabilities["deviceName"])

    print(deviceId[device])
    chrome_cmd_off = 'docker exec -it '+ deviceId[device] + ' adb shell svc data disable'
    os.popen(chrome_cmd_off)
    time.sleep(3)
    chrome_cmd_on = 'docker exec -it '+ deviceId[device] + ' adb shell svc data enable'
    os.popen(chrome_cmd_on)