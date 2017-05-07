'''
Created on Apr 29, 2017

@author: Mukadam
'''
import requests , re, json
from pyquery import PyQuery
from unicodedata import category
from datetime import datetime
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
file_product_list = open('file_product_list.txt','w')
file_store_list = open('file_store_list.txt','w')
url = "https://www.aliexpress.com/wholesale"

file_product_ids = open('file_product_ids.txt','r').read().split('\n')
headers = {
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    'accept-encoding': "gzip, deflate, sdch, br",
    'accept-language': "en-US,en;q=0.8",
    'cache-control': "no-cache",
    'cookie': "ali_apache_id=10.181.239.78.1493451988691.618488.7; xman_t=Eq7QY+EMFCUQ7beOxMIy5qCYUehuqb9CeKFgDzvLF/sjAXEjHBnLgHUsywMo7FMv; acs_usuc_t=acs_rt=04c36552a07749878b60970686f421fa; xman_f=9aScyedMkVWgiJliGyYcw5moakrD2bSmYFGX/RwJT4WnJEyLN8YRcxkUmY3Wr41uYAS3fPac0wVcqxx7wDRx3JBSB2sPWJDBT5dmaRFqOfY0d4rlwQwqWw==; ali_beacon_id=10.181.239.78.1493451988691.618488.7; cna=895bEevlzkACAWfPCpIulBPu; JSESSIONID=3510944EB7A0472631380B32E46C06CC; _mle_tmp0=eNrz4A12DQ729PeL9%2FV3cfUx8KvOTLFSMjY1NLA0MXF1Mnc0MDE3MjM2NLYwcDI2cjUxczYwc3ZW0kkusTI0sTQ2MTUyMjY3MbDQSUxGE8itsDKojQIAh2YXfw%3D%3D; aep_history=keywords%5E%0Akeywords%09%0A%0Aproduct_selloffer%5E%0Aproduct_selloffer%0932721349215; _ga=GA1.2.1306089451.1493451992; xman_us_f=x_l=1&x_locale=en_US; intl_locale=en_US; intl_common_forever=1v4pISpgwB8NhHVbjUkRTtaQqEg04wPE3BAijibAD+EVEV9YNQiRiA==; _gat=1; aep_usuc_f=site=glo&region=US&b_locale=en_US&c_tp=USD; l=AhMTT8iyUxEZ6nvwM2SG5hynI509yKeK; isg=AqurfvhpdvZs16tx63l5rGHlOs_-tb9CGUoF8h0oh-pBvMsepZBPkkkeMEso; ali_apache_track=; ali_apache_tracktmp=",
    'referer': "https://www.aliexpress.com/item/12-Constellations-Bracelet-2016-New-Fashion-Jewelry-Leather-Bracelet-Men-Casual-Personality-Alloy-Vintage-Punk-Bracelet/32721349215.html",
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"
    }
current_count = 1
for product in file_product_ids:
    print 'Count : '+str(current_count)
    try:
    
        current_count+=1
        querystring = {"SearchText":str(product)}
        try:
            response = requests.request("GET", url,params=querystring)
            response_shipping = requests.request("GET", "https://freight.aliexpress.com/ajaxFreightCalculateService.htm?f=d&productid={}&count=1&currencyCode=USD&sendGoodsCountry=&country=IN&province=&city=&abVersion=1".format(str(product))).text[1:-1]
            response_last_6_months = requests.request('GET', 'https://feedback.aliexpress.com/display/evaluationProductDetailAjaxService.htm?productId={}&type=default&page=1'.format(product)).json()
        
        except Exception, e:
            print 'skipped'
            continue
        #print(response.text)
        
        product_id = ''
        store_id = ''
        product_title = ''
        product_image_urls = []
        price = ''
        currency = ''
        unit = ''
        discount_price = ''
        discount_currency = ''
        discount_unit = ''
        rating = ''
        votes = ''
        rating_5 = ''
        rating_4 = ''
        rating_3 = ''
        rating_2 = ''
        rating_1 = ''
        category = []
        shipping = ''
        estimated_delivery_time = ''
        pieces_available = ''
        orders = ''
        transaction_last_6_months = ''
        shipping_options = []
        product_handle = ''
        time_scraped = ''
    
        
        
        
        
        
        
        
        
        
        
        
    
        
        
        
        
        
        
        
        
        
        pq = PyQuery(response.text)
        
        
        product_id =                str(product).strip()
        store_id =                  pq('.store-number').text().strip()
        product_title =             pq('.product-name').text()
        product_image_urls = []
        for image in pq('.img-thumb-item img'):
            product_image_urls.append(image.attrib['src'].replace('jpg_50x50.jpg','jpg_640x640.jpg'))
        price =                     pq('#j-sku-price').text()
        currency =                  pq('.p-del-price-detail .p-symbol').text()
        unit =                      pq('.p-del-price-detail .p-unit').text()
        discount_price =            pq('#j-sku-discount-price').text()
        discount_currency =         pq('.p-current-price [itemprop="priceCurrency"]').text()
        discount_unit =             pq('.p-current-price .p-unit').text()
        rating =                    pq('.product-customer-reviews [itemprop="ratingValue"]').text()
        votes =                     pq('.product-customer-reviews [itemprop="reviewCount"]').text()
        rating_5 =                  pq('.detail .rate-list [data="5 Stars"]').text()
        rating_4 =                  pq('.detail .rate-list [data="4 Stars"]').text()
        rating_3 =                  pq('.detail .rate-list [data="3 Stars"]').text()
        rating_2 =                  pq('.detail .rate-list [data="2 Stars"]').text()
        rating_1 =                  pq('.detail .rate-list [data="1 Stars"]').text()
        category = []
        for cat in pq('.ui-breadcrumb a'):
            category.append(re.sub("\D", "", cat.attrib['href']))
        
        
        response_shipping = json.loads(response_shipping)
        if response_shipping['freight']:
            if response_shipping['freight'][0]['status']:
                shipping = "Free Shipping to United States via Seller's Shipping Method"
            else:
                shipping = "{} to United States via {}".format(response_shipping['freight'][0]['totalFreightFormatStr'],response_shipping['freight'][0]['companyDisplayName'])
            
            #response_shipping.close()
            estimated_delivery_time = response_shipping['freight'][0]['time']
        pieces_available = str(re.search('window.runParams.totalAvailQuantity=(.*?);',response.text).group(1))
        orders = pq('#j-order-num').text()
        transaction_last_6_months = response_last_6_months['range']['transactions']
        shipping_options = []
        for info in response_shipping['freight']:
            info_obj = {}
            info_obj['Shipping Company'] = info['companyDisplayName']
            info_obj['Estimated Delivery Time'] = info['time']
            info_obj['Shipping Cost'] = info['totalFreightFormatStr']
            if info['isTracked']:
                info_obj['Tracking Information'] = 'Available'
            else:
                info_obj['Tracking Information'] = 'Not Available'
            shipping_options.append(info_obj)
        shipping_options = json.dumps(shipping_options)
        product_handle = response.url.replace('https://www.aliexpress.com/item/','').replace('/{}.html'.format(str(product)),'')
        time_scraped = str(datetime.now())
        
        
        output_data = str(product_id)+'\t'+str(store_id)+'\t'+str(product_title)+'\t'+str(product_image_urls)+'\t'+str(price)+'\t'+str(currency)+'\t'+str(unit)+'\t'+str(discount_price)+'\t'+str(discount_currency)+'\t'+str(discount_unit)+'\t'+str(rating)+'\t'+str(votes)+'\t'+str(rating_5)+'\t'+str(rating_4)+'\t'+str(rating_3)+'\t'+str(rating_2)+'\t'+str(rating_1)+'\t'+str(category)+'\t'+str(shipping)+'\t'+str(estimated_delivery_time)+'\t'+str(pieces_available)+'\t'+str(orders)+'\t'+str(transaction_last_6_months)+'\t'+str(shipping_options)+'\t'+str(product_handle)+'\t'+str(time_scraped)+'\n'
        file_product_list.write(output_data) 
        file_product_list.flush()
        
        
        response_store_feedback = requests.get('https://m.aliexpress.com/store/sellerInfo.htm?sellerAdminSeq={}'.format(str(pq('.s-mail .send-mail-btn').attr('data-id1'))))
        pq_store = PyQuery(response_store_feedback.text)
        
        
        store_name = pq('.shop-name a').text()
        try:
            positive_feedback = str(re.search('sellerScore":(.*?),', response_store_feedback.text).group(1))
            feeback_score = str(re.search('feedbackRating":"(.*?)"', response_store_feedback.text).group(1))
            
            date_opened = str(re.search('"since":"(.*?)"', response_store_feedback.text).group(1))
            item_as_described = str(re.search('"proDescEval":"(.*?)"', response_store_feedback.text).group(1))
            
            communication =     str(re.search('"sellerServiceEval":"(.*?)"', response_store_feedback.text).group(1))
            shipping_speed =    str(re.search('"shippingServiceEval":"(.*?)"', response_store_feedback.text).group(1))
        except Exception,e:
            continue
        time_scraped = str(datetime.now())
    
        file_store_list.write(store_id + '\t' + store_name + '\t' +  positive_feedback + '\t' +  feeback_score + '\t' +  date_opened + '\t' +   item_as_described + '\t' +  communication + '\t' +  shipping_speed + '\t' +  time_scraped + '\n')
        
        response_store_feedback.close()
        response.close()
        file_store_list.flush()
    except Exception,e :
        print ' Skipping '
    