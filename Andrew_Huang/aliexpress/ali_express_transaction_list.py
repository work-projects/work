import requests, json
from datetime import datetime



file_product_ids = open('file_product_ids.txt','r').read().split('\n')
file_transaction_list = open('file_transaction_list.txt','w')
for product in file_product_ids:
    print file_product_ids.index(product)
    for i in range(1,51):
        try:
            response = requests.get('https://feedback.aliexpress.com/display/evaluationProductDetailAjaxService.htm?productId={}&type=default&page={}'.format(str(product),str(i))).json()
            for item in response['records']:
                product_id = str(product)
                name = str(item['name'])
                country = str(item['countryName'])
                timestamp = str(item['date'])
                pieces = str(item['quantity'])
                customer_member_level = str(item['buyerAccountPointLeval'])
                time_scraped = str(datetime.now())
                
                file_transaction_list.write(product_id + '\t' + name + '\t' + country + '\t' + timestamp + '\t' + pieces + '\t' + customer_member_level + '\t' + time_scraped +'\n')
                    
        
        except Exception,e:
            print e
            break
    file_transaction_list.flush()