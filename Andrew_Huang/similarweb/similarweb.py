import requests,urllib
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
    #print site
    try:
        j = json.loads(response.text)
       
        #print len(j.keys())
        f_andrew_output.write(url_id + '\t' +site+'\t'+
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
        f_andrew_output.write('"')
        for a in j['TopCategoriesAndFills']:
            f_andrew_output.write(a['Category'] + ', ')
        f_andrew_output.write('"\t')
        f_andrew_output.write('"')
        for a in j['TopAlsoVisited']:
            f_andrew_output.write(a + ', ')
        f_andrew_output.write('"\t')
        f_andrew_output.write('"')
        for a in j['TopReferring']:
            f_andrew_output.write(a['Site'] + ' ' + str(a['Value'] * 100) + ',')
        f_andrew_output.write('"\t')


        f_andrew_output.write(str(j['EstimatedMonthlyVisits']['2016-11-01']) + '\t')
        f_andrew_output.write(str(j['EstimatedMonthlyVisits']['2016-12-01']) + '\t')
        f_andrew_output.write(str(j['EstimatedMonthlyVisits']['2017-01-01']) + '\t')
        f_andrew_output.write(str(j['EstimatedMonthlyVisits']['2017-02-01']) + '\t')
        f_andrew_output.write(str(j['EstimatedMonthlyVisits']['2017-03-01']) + '\t')
        f_andrew_output.write(str(j['EstimatedMonthlyVisits']['2017-04-01']) + '\t')
        f_andrew_output.write(str(datetime.now()))





    except Exception, e:
        print e
        f_andrew_output.write(url_id+'\t'+site)
    finally:
        response.close()
    f_andrew_output.write('\n')
    f_andrew_output.flush()













j=1
for i in f_urls:  
    #quoted = urllib.quote('{"api_key": "5qtwIL4abHItxy3qOFNQ3Q","units":"imperial","height":"'+height+'","belly":"'+belly+'","ethnicity":"'+race+'","age":"AG40","eyes":"EYR","nose":"NOS","lips":"LPB","beard_style":"BS04","beard_color":"BC06","hair_color":"'+hair_color+'","hair_style":"'+hair_style+'","background":"blank","view":"'+angle+'","delta":{"current":{"weight":"'+weight+'","shape":"'+shape+'","outfit":"undergarment"},"goal":{"weight":"190","shape":"muscular","outfit":"undergarment"}}}')
    future = session.get("https://api.similarweb.com/SimilarWebAddon/"+i.split('\t')[1].replace('\n','').strip()+"/all#"+i.split('\t')[0],background_callback=bg_cb)
    print j
    if j%10 == 0:
        response = future.result()
    j+=1
    
    
    
    