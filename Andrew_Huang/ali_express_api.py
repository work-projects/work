'''
Created on Apr 28, 2017

@author: Mukadam
'''

import requests

url = "https://m.aliexpress.com/search/mainsearch/asy/GetMainSearchDataJson.do"
file_product_ids = open('file_product_ids.txt','w')
for i in range(1,100):
    querystring = {"keyword":"","start":str(i*20),"freeShipping":"false","ignoreSPU":"true","onePiece":"","pinProductIds":"","pop":"false","scene":"","secondSort":"","categoryId":"200000707","shipFromCity":"","shipFromCountry":"","shipFromProvince":"","shipToCity":"","shipToCountry":"","shipToProvince":"","attributes":"","maxPrice":"","minPrice":"","spuId":"","shoppingCoupon":"","firstSort":"","pageSize":"20","isBigSale":"false"}
    print 'Count : '+ str(i)
    response = requests.request("GET", url, params=querystring)
    
    #print(response.json())
    
    for item in response.json()['items']:
        try:
            file_product_ids.write(str(item['productId'])+'\n')
        except Exception, e:
            pass
    file_product_ids.flush()  
    response.close()
        