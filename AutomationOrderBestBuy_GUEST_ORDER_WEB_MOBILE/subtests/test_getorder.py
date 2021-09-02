
import project_parameters
import requests
import time

def test_main():
    getOrder()
    
    order = False
    while not order:
        if project_parameters.order['status'] == True:
            time.sleep(4)
            print('Orders in queue')
            project_parameters.profile_id = project_parameters.order['profile_id']
            project_parameters.firstName = project_parameters.order['billing_address']['first_name']
            project_parameters.urlProduct = project_parameters.order['products'][0]['url']
            project_parameters.product_quantity = project_parameters.order['products'][0]['quantity']
            project_parameters.unit_price = project_parameters.order['products'][0]['forced_price']
            project_parameters.product_sku = project_parameters.order['products'][0]['forced_sku']
            project_parameters.lastName = project_parameters.order['billing_address']['last_name']
            project_parameters.addressLineOne = project_parameters.order['billing_address']['address_line1']
            project_parameters.addressLineTwo = project_parameters.order['billing_address']['address_line2']
            project_parameters.city = project_parameters.order['billing_address']['city']
            project_parameters.zipCode = project_parameters.order['billing_address']['zip_code']
            project_parameters.email = project_parameters.order['retailer_credentials']['email']
            project_parameters.phoneNumber = project_parameters.order['shipping_address']['phone_number']
            project_parameters.password = project_parameters.order['retailer_credentials']['password']
            project_parameters.warehouse_id = project_parameters.order['warehouse_id']
            project_parameters.subwarehouse_id = project_parameters.order['subwarehouse_id']
            project_parameters.gift_card_vendor_id = project_parameters.order['gift_card_vendor_id']
            project_parameters.create_account_retailer = project_parameters.order['retailer_credentials']['create_account_retailer']
            project_parameters.proxy = project_parameters.order['proxy']
            project_parameters.amount = project_parameters.order['amount']
            project_parameters.isFake = project_parameters.order['advance_settings']['fake_order']
            project_parameters.state = project_parameters.order['billing_address']['state']
            print(project_parameters.isFake)
            order = True
        elif project_parameters.order['status'] == False:
            time.sleep(4)
            print('No orders')
            getOrder()
         
def getOrder():
    headers = {'x-api-key': 'Mz6ZZig4M62MWvTCoANjLcXIQQLMhWf9g8WQQaYh'}
    url_bestbuy = 'https://hrnta21voa.execute-api.sa-east-1.amazonaws.com/Prod/orders/orderZoneOregon'
    project_parameters.order = requests.get(url_bestbuy, headers=headers).json()
