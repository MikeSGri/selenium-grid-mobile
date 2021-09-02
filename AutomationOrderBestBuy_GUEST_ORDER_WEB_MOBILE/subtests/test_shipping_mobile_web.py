from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import time
import project_parameters


"""
This pytest test was automatically generated by TestProject
    Project: AutomationOrderBestBuy
    Package: TestProject.Generated.Tests.AutomationOrderBestBuy
    Test: shipping_mobile_web
    Generated by: Nicolas Duran (nicolas.duran@atlanticsoft.us)
    Generated on 07/29/2021, 20:22:27
"""



def test_main(driver):
    # Test Parameters
    # Auto generated application URL parameter
    ApplicationURL = "https://bestbuy.com/?intl=nosplash"

    # 1. Pause for '3000'ms
    time.sleep(5)

    # 2. Click 'consolidatedAddresses.ui_address_2.fi...1'
    consolidatedaddresses_ui_address_2_fi_1 = driver.find_element(By.XPATH,
                                                                  "//section/div[1]/label//input")
    consolidatedaddresses_ui_address_2_fi_1.click()

    # 3. Pause for '3000'ms
    time.sleep(5)

    # 4. Type '{project_parameters.firstName}' in 'consolidatedAddresses.ui_address_2.fi...1'
    consolidatedaddresses_ui_address_2_fi_1 = driver.find_element(By.XPATH,
                                                                  "//section/div[1]/label//input")
    consolidatedaddresses_ui_address_2_fi_1.send_keys(
        f'{project_parameters.firstName}')

    # 5. Pause for '3000'ms
    time.sleep(5)

    # 6. Click 'consolidatedAddresses.ui_address_2.la...1'
    consolidatedaddresses_ui_address_2_la_1 = driver.find_element(By.XPATH,
                                                                  "//section/section/div[2]//input")
    consolidatedaddresses_ui_address_2_la_1.click()

    # 7. Pause for '3000'ms
    time.sleep(5)

    # 8. Type '{project_parameters.lastName}' in 'consolidatedAddresses.ui_address_2.la...1'
    consolidatedaddresses_ui_address_2_la_1 = driver.find_element(By.XPATH,
                                                                  "//section/section/div[2]//input")
    consolidatedaddresses_ui_address_2_la_1.send_keys(
        f'{project_parameters.lastName}')

    # 9. Pause for '3000'ms
    time.sleep(5)

    # 10. Click 'consolidatedAddresses.ui_address_2.st...1'
    consolidatedaddresses_ui_address_2_st_1 = driver.find_element(By.XPATH,
                                                                  "//div/div[2]/div/div/input")
    consolidatedaddresses_ui_address_2_st_1.click()

    # 11. Pause for '3000'ms
    time.sleep(5)

    # 12. Type '{project_parameters.addressLineOne}' in 'consolidatedAddresses.ui_address_2.st...1'
    consolidatedaddresses_ui_address_2_st_1 = driver.find_element(By.XPATH,
                                                                  "//div/div[2]/div/div/input")
    consolidatedaddresses_ui_address_2_st_1.send_keys(
        f'{project_parameters.addressLineOne}')

    # 13. Pause for '3000'ms
    time.sleep(5)

    # 14. Click 'Hide Suggestions1'
    hide_suggestions1 = driver.find_element(By.XPATH,
                                            "//button[. = 'Hide Suggestions']")
    hide_suggestions1.click()

    # 15. Pause for '3000'ms
    time.sleep(5)

    # 16. Click 'add_apt_suite_floor_optional_1'
    add_apt_suite_floor_optional_1 = driver.find_element(By.XPATH,
                                                         "//span[. = 'Add Apt #, Suite, Floor (optional)']")
    add_apt_suite_floor_optional_1.click()

    # 17. Pause for '3000'ms
    time.sleep(5)

    # 18. Type '{project_parameters.addressLineTwo}' in 'Address_line_two'
    address_line_two = driver.find_element(By.XPATH,
                                           "//input[@placeholder = 'Apt #, Suite, Floor (optional)']")
    address_line_two.send_keys(f'{project_parameters.addressLineTwo}')

    # 19. Pause for '3000'ms
    time.sleep(5)

    # 20. Click 'consolidatedAddresses.ui_address_2.ci...1'
    consolidatedaddresses_ui_address_2_ci_1 = driver.find_element(By.XPATH,
                                                                  "//div[5]//input")
    consolidatedaddresses_ui_address_2_ci_1.click()

    # 21. Pause for '3000'ms
    time.sleep(5)

    # 22. Scroll window by ('0','350')
    driver.execute_script("window.scrollBy(0,350)")

    # 23. Pause for '3000'ms
    time.sleep(5)

    # 24. Type '{project_parameters.city}' in 'consolidatedAddresses.ui_address_2.ci...1'
    consolidatedaddresses_ui_address_2_ci_1 = driver.find_element(By.XPATH,
                                                                  "//div[5]//input")
    consolidatedaddresses_ui_address_2_ci_1.send_keys(
        f'{project_parameters.city}')

    # 25. Pause for '3000'ms
    time.sleep(5)

    # 26. Click 'state4'
    state4 = driver.find_element(By.XPATH,
                                 "//select")
    state4.click()

    # 27. Pause for '3000'ms
    time.sleep(5)

    # 28. Select the '{project_parameters.state}' option in 'state4'
    state4 = driver.find_element(By.XPATH,
                                 "//select")
    Select(state4).select_by_value(f'{project_parameters.state}')

    # 29. Pause for '3000'ms
    time.sleep(5)

    # 30. Click 'consolidatedAddresses.ui_address_2.zi...1'
    consolidatedaddresses_ui_address_2_zi_1 = driver.find_element(By.XPATH,
                                                                  "//div[6]//input")
    consolidatedaddresses_ui_address_2_zi_1.click()

    # 31. Pause for '3000'ms
    time.sleep(5)

    # 32. Scroll window by ('0','550')
    driver.execute_script("window.scrollBy(0,550)")

    # 33. Pause for '3000'ms
    time.sleep(5)

    # 34. Type '{project_parameters.zipCode}' in 'consolidatedAddresses.ui_address_2.zi...1'
    consolidatedaddresses_ui_address_2_zi_1 = driver.find_element(By.XPATH,
                                                                  "//div[6]//input")
    consolidatedaddresses_ui_address_2_zi_1.send_keys(
        f'{project_parameters.zipCode}')

    # 35. Pause for '3000'ms
    time.sleep(5)

    # 36. Click 'user.emailAddress2'
    user_emailaddress2 = driver.find_element(By.XPATH,
                                             "//div/section/div[2]/label//input")
    user_emailaddress2.click()

    # 37. Pause for '3000'ms
    time.sleep(5)

    # 38. Type '{project_parameters.email}' in 'user.emailAddress2'
    user_emailaddress2 = driver.find_element(By.XPATH,
                                             "//div/section/div[2]/label//input")
    user_emailaddress2.send_keys(f'{project_parameters.email}')

    # 39. Pause for '3000'ms
    time.sleep(5)

    # 40. Click 'user.phone1'
    user_phone1 = driver.find_element(By.XPATH,
                                      "//div[3]/label//input")
    user_phone1.click()

    # 41. Pause for '3000'ms
    time.sleep(5)

    # 42. Type '{project_parameters.phoneNumber}' in 'user.phone1'
    user_phone1 = driver.find_element(By.XPATH,
                                      "//div[3]/label//input")
    user_phone1.send_keys(f'{project_parameters.phoneNumber}')

    # 43. Pause for '3000'ms
    time.sleep(5)

    # 44. Click 'Continue to Payment Information2'
    continue_to_payment_information2 = driver.find_element(By.XPATH,
                                                           "//button[. = 'Continue to Payment Information']")
    continue_to_payment_information2.click()

    # 45. Scroll window by ('0','-533')
    driver.execute_script("window.scrollBy(0,-533)")

    # 46. Click 'Keep Address as Entered1'
    keep_address_as_entered1 = driver.find_element(By.XPATH,
                                                   "//button[. = 'Keep Address as Entered']")
    keep_address_as_entered1.click()
