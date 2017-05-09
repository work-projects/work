import json
import requests.packages.urllib3
from datetime import datetime
requests.packages.urllib3.disable_warnings()
from requests_futures.sessions import FuturesSession
requests.packages.urllib3.disable_warnings()
session = FuturesSession()

f_urls = open('urls.txt', 'r').read().split('\n')
f_andrew_output = open('f_andrew_output.txt', 'w')



def bg_cb(sess, response):
    #print f_urls.index(i)
    #if f_urls.index(i) > 4383:
        #response = requests.request("GET", "https://api.similarweb.com/SimilarWebAddon/{}/all".format(i.split('\t')[1].replace('\n','')))

        #print str(f_urls.index(i)) + '\t',
    url_id = response.url.rsplit('#')[1]
    site = response.url.rsplit('/',3)[2]
    
    website_details =''
    try:
        j = json.loads(response.text)
        
       
        #print len(j.keys())
        website_details = (url_id + '\t' +site+'\t'+
        str(int(j['Engagments']['Visits'])) + '\t' +
        str(j['Engagments']['PagePerVisit']) + '\t' +
        str(j['Engagments']['BounceRate'] * 100) + '\t' +
        str(j['TrafficSources']['Direct'] * 100) + '\t' +
        str(j['TrafficSources']['Referrals'] * 100) + '\t' +
        str(j['TrafficSources']['Search'] * 100) + '\t' +
        str(j['TrafficSources']['Social'] * 100) + '\t' +
        str(j['TrafficSources']['Paid Referrals'] * 100) + '\t' +
        str(j['TrafficSources']['Mail'] * 100) + '\t' +
        str(j['PaidSearchShare'] * 100) + '\t')
        
        
        #f_andrew_output.write()
        website_details+=('"')
        for a in j['TopCategoriesAndFills']:
            website_details+=(a['Category'] + ', ')
        website_details+=('"\t')
        website_details+=('"')
        for a in j['TopAlsoVisited']:
            website_details+=(a + ', ')
        website_details+=('"\t')
        website_details+=('"')
        for a in j['TopReferring']:
            website_details+=(a['Site'] + ' ' + str(a['Value'] * 100) + ',')
        website_details+=('"\t')


        website_details+=(str(j['EstimatedMonthlyVisits']['2016-11-01']) + '\t')
        website_details+=(str(j['EstimatedMonthlyVisits']['2016-12-01']) + '\t')
        website_details+=(str(j['EstimatedMonthlyVisits']['2017-01-01']) + '\t')
        website_details+=(str(j['EstimatedMonthlyVisits']['2017-02-01']) + '\t')
        website_details+=(str(j['EstimatedMonthlyVisits']['2017-03-01']) + '\t')
        website_details+=(str(j['EstimatedMonthlyVisits']['2017-04-01']) + '\t')
        website_details+=(str(datetime.now())+'\n')

        print 'Count :'+ url_id+'\t'+site +'\t\t : Successful'



    except Exception, e:
        print 'Count :'+ url_id+'\t'+site +'\t\t : No info found'
        website_details = (url_id+'\t'+site+'\n')
    finally:
        response.close()
    f_andrew_output.write(website_details)
    f_andrew_output.flush()


j=1
for i in f_urls:  
    #quoted = urllib.quote('{"api_key": "5qtwIL4abHItxy3qOFNQ3Q","units":"imperial","height":"'+height+'","belly":"'+belly+'","ethnicity":"'+race+'","age":"AG40","eyes":"EYR","nose":"NOS","lips":"LPB","beard_style":"BS04","beard_color":"BC06","hair_color":"'+hair_color+'","hair_style":"'+hair_style+'","background":"blank","view":"'+angle+'","delta":{"current":{"weight":"'+weight+'","shape":"'+shape+'","outfit":"undergarment"},"goal":{"weight":"190","shape":"muscular","outfit":"undergarment"}}}')
    future = session.get("https://api.similarweb.com/SimilarWebAddon/"+i.split('\t')[1].replace('\n','').strip()+"/all#"+i.split('\t')[0],background_callback=bg_cb)
    #print j
    if j%5 == 0:
        response = future.result()
    j+=1
    
    
    
    