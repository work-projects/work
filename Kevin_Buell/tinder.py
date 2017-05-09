import requests
import urllib,sys

url = "https://api.gotinder.com/recs/core"

querystring = {"locale":"en"}

headers = {
    'platform': "android",
    'user-agent': "Tinder Android Version 6.11.0",
    'os-version': "23",
    'accept-language': "en",
    'app-version': "2082",
    'connection': "Keep-Alive",
    'accept-encoding': "gzip",
    'if-none-match': "W/\"-380394419\"",
    'x-auth-token': "87c79a7d-4ad9-4a25-bf83-4a987492d1cb",
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

recs = response.json()
#print recs
file_images = open('file_images.txt','a')
i=1
for profile in recs['results']:
    user_profile = profile['user']
    
    print 'Profile - {}'.format(str(i))
    
    try:
        print '\t\t Name : {}'.format(user_profile['name'].encode('ascii','ignore'))
    except:
        pass
    try:
        print '\t\t Id : {}'.format(user_profile['_id'])
    except:
        pass    
    try:
        print '\t\t Bio : {}'.format(user_profile['bio'].encode('ascii','ignore').replace('\n',''))
    except:
        pass    
    
    try:
        print '\t\t Distance from you : {} miles'.format(str(user_profile['distance_mi']).encode('ascii','ignore').replace('\n',''))
    except:
        pass    

    try:
        print '\t\t Photos : {}'.format(', '.join(photo['url'] for photo in user_profile['photos']))    
#         for photo1 in user_profile['photos']:
#             photo1 = photo1['url']
#             urllib.urlretrieve(photo1, 'Images/'+photo1.replace('http://images.gotinder.com/','').rsplit('/')[1])
    except Exception,e:
        print e
    try:
        print '\t\t Common Connections : {}'.format(user_profile['common_connections'])
    except:
        pass    
    
    try:
        print '\t\t Common Likes : {}'.format(user_profile['common_likes'])
    except:
        pass    
    
    try:
        print '\t\t Common Interests : {}'.format(', '.join(interest['name'] for interest in user_profile['common_interests']))
    except:
        pass    
    
    try:
        print '\t\t Common Friends : {}'.format(user_profile['common_friends'])
    except:
        pass    
    likes = requests.get('https://api.gotinder.com/like/{}?content_hash={}&s_number={}'.format(user_profile['_id'],user_profile['content_hash'],user_profile['s_number']),headers=headers).json()
    #print 'Like Profile - Done. Likes Remaining - {} '.format(likes['likes_remaining'])
    print 'Liked {}? - Successful'.format(user_profile['name'].encode('ascii','ignore'))
    print '\n\n' 
    #sys.exit()
    i+=1
    
    

#recs = requests.get('https://api.gotinder.com/pass/590f6bc1e4fab3033ce8760',headers=headers).json()
