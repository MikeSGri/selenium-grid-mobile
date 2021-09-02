
from selenium.webdriver.common.by import By
import project_parameters
import time



def test_main(driver):
    time.sleep(7)
    # get_name(driver)
            
def get_name(driver):
    selectors_name = ['/html/body/div[3]/main/div[2]/div/div[1]/div[3]/div[1]/div[1]/div/div/div[1]/h1',
                    '/html/body/div[3]/main/div[2]/div[3]/div[1]/div[1]/div/div/div[1]/h1']
    
    countName = 0
    is_find = False  
    while not is_find:
        if countName <= len(selectors_name):                                   
            for selector in selectors_name:
                try:
                    countName+=1
                    name = driver.find_element_by_xpath(selector).text
                    project_parameters.product_name = name
                    is_find = True
                    break
                except:
                    if countName == len(selectors_name):
                        is_find = True
                        print("Limit of attempts reached name")
                     
                        driver.quit()
                        break
                    print ("It was not the selector for the product name")
    
    
    
   

