
from selenium.webdriver.common.by import By
import time
import project_parameters

def test_main(driver):
    time.sleep(12)

    driver.execute_script("window.scrollBy(0,100)")

    update_location_selectors = ['/html/body/div[1]/main/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[6]/form/div[2]/fieldset/div[2]/div[1]/div/label/strong/span/button/span',
                                '/html/body/div[1]/main/div/div/div[1]/div/div[2]/div/div[1]/div/div[2]/form/ul/li[2]/div[1]/div/span[2]/span/span/button']


    count = 0
    is_find_updateLocation = False
    while not is_find_updateLocation:
        if count <= len(update_location_selectors):
            for selector_sku in update_location_selectors:
                try:
                    count+=1
                    driver.find_element_by_xpath(selector_sku).click()
                    is_find_updateLocation = True
                    break
                except:
                    if count == len(update_location_selectors):
                        is_find_updateLocation = True
                        print("Limit of attempts reached UPDATE LOCATION")

                        driver.quit()
                        break
                    print('It was not the selector for the SKU')

    # 10. Click 'location2'
    location2 = driver.find_element(By.CSS_SELECTOR,
                                    "#location")
    location2.click()

    # 11. Type '19713' in 'location2'
    location2 = driver.find_element(By.CSS_SELECTOR,
                                    "#location")
    location2.send_keys(f'{project_parameters.zipCode}')

    # 12. Click 'Update1'
    update1 = driver.find_element(By.XPATH,
                                  "//button[. = 'Update']")
    update1.click()

