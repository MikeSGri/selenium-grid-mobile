


from selenium.webdriver.common.by import By
import project_parameters
import time
import requests
import json

def test_main(driver):

    # get_value_tax(driver)

    gift_card_field = ["/html/body/div[1]/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/div[3]/section/div[1]/a",
                       "/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[3]/div/section/a"]

    is_find = False
    while not is_find:
        for selector in gift_card_field:
            try:
                use_a_best_buy_gift_card_discount_co_ = driver.find_element(By.XPATH,selector)
                use_a_best_buy_gift_card_discount_co_.click()
                is_find = True
                for gift_cards in project_parameters.gift_cards['gcs']:
                    print(gift_cards['gc_code'],' ',gift_cards['pin'])
                    apply_gift_cards(driver,gift_cards['gc_code'],gift_cards['pin'],gift_cards['amount'])
                break
            except Exception as e:
                print(str(e))
                print('No Use a Best Buy Gift Card field found')


def apply_gift_cards(driver,code,pin,amount):
    time.sleep(3)

    selector_textGiftCard = ['/html/body/div[1]/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/div[3]/section/div[1]/div[3]/div[2]/div[2]/div[1]/div/div/input',
                                '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[3]/div/section/div[1]/div[3]/div[2]/div[2]/div[1]/div/div/input']

    for selector in selector_textGiftCard:
        try:
            payment_promotioncode = driver.find_element(By.XPATH,selector)
            for characters in code:
                payment_promotioncode.send_keys(characters)
                time.sleep(0.2)
            break
        except Exception as e:
            print(str(e))
            print('No selector textGiftCard field found')

    selector_pinGiftCard = ['/html/body/div[1]/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/div[3]/section/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]/div/div/input',
                            '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[3]/div/section/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]/div/div/input']

    for selector in selector_pinGiftCard:
        try:
            payment_giftcard_pin = driver.find_element(By.XPATH,selector)
            for characters in pin:
                payment_giftcard_pin.send_keys(characters)
                time.sleep(0.2)
            break
        except Exception as e:
            print(str(e))
            print('No selector textGiftCard field found')

    selector_buttonApply = ['/html/body/div[1]/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/div[3]/section/div[1]/div[3]/div[2]/div[2]/div[2]/div[2]/button',
                            '//*[@id="checkoutApp"]/div[2]/div[1]/div[1]/main/div[2]/div[3]/div/section/div[3]/div[2]/div[2]/div[2]/div[2]/button']

    for selector in selector_buttonApply:
        try:

            applyButtom = driver.find_element(By.XPATH,selector)
            applyButtom.click()
            break
        except Exception as e:
            print(str(e))
            print('No selector textGiftCard field found')

    # verification_giftcard(driver,code,pin,amount)
    time.sleep(4)


# def verification_giftcard(driver,code,pin,amount):
#     try:
#         time.sleep(3)
#         message = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[3]/div/section/div[3]/div[2]/div[3]/div/div/span[2]').text
#         invalidate_gift_card(message,code,amount)
#         time.sleep(0.5)
#         payment_promotioncode = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[3]/div/section/div[3]/div[2]/div[2]/div[1]/div/div/input')
#         payment_promotioncode.send_keys('')
#         time.sleep(0.2)
#         payment_giftcard_pin = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[3]/div/section/div[3]/div[2]/div[2]/div[2]/div[1]/div/div/input')
#         payment_giftcard_pin.send_keys('')
#         time.sleep(0.2)
#     except Exception as e:
#         print(str(e))
#         print("There was no error")


def invalidate_gift_card(reason,code,amount):

    url = "https://thecornercloud.com/developers/index.php/api/gcs/invalid-suspected"

    payload = json.dumps({"giftcard_id": code,"user_id": 213,"amount":amount,"reason": reason})

    headers = {'Content-Type': 'application/json'}

    response = requests.request("POST", url, headers=headers, data=payload)


# def get_value_tax(driver):
#     time.sleep(4)
#     is_find = False
#     while not is_find:
#         try:
#             tax_value = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[4]/section[1]/div[2]/section/div/div[3]/div[2]/span").text
#             step_output = float(tax_value.replace('$','').replace(',',''))
#             project_parameters.taxes = step_output
#             print('Taxes',project_parameters.taxes)
#             is_find = True
#         except Exception as e:
#             print(str(e))
#             print('No Use a Tax field found')

