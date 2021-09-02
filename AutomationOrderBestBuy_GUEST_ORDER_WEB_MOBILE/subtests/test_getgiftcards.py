

from selenium.webdriver.common.by import By
import requests
import project_parameters

    
headers = {
        "accept": "application/json",
        "accept-language": "en-US,en;q=0.9",
        'authorization': 'Basic QkVTVEJVWU9SREVSUzo3RnNkJXNsb0ZBODIxJCVWOSlN',
        "cache-control": "no-cache",
        "content-type": "application/json",
        "pragma": "no-cache",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "none"
    }


def test_main(driver):
    
    total_price = get_total_price(driver)
    
    project_parameters.total_price = total_price
    print(project_parameters.total_price)
    
    # if total_price == project_parameters.amount:
    apiGCS = 'https://cloud.thecornercloud.com/index.php/api/gcs/request'
    body = {"vendor_id":project_parameters.gift_card_vendor_id,"amount":total_price,"max_gc":10,"ignore_gcs":[],"is_automatic_order":1,"limit":10,"profile_id":project_parameters.profile_id}
    reply_giftcards = requests.post(apiGCS, headers=headers, json=body)
    is_Validated = False    
    while not is_Validated:
        if  reply_giftcards.json()['status'] == True:
            print("Valid GiftCart")
            print(reply_giftcards.json())
            is_Validated = True
        else:
            print("Invalid Giftcart")
            print(reply_giftcards.json())
            reply_giftcards = requests.post(apiGCS, headers=headers, json=body)

    project_parameters.gift_cards = reply_giftcards.json()



def get_total_price(driver):
    step_output = ''
    is_find = False
    while not is_find:
        try: 
            total_price = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/header/div/div/button/span/span[2]").text
            step_output = float(total_price.replace('$','').replace(',',''))
            is_find = True
        except:
            print("No Total Price field has been entered.")
            
    return step_output

