'''
Created on May 5, 2017

@author: Mukadam
'''
import urllib
images_file = open('Input_files/after_men.txt','r').read().split('\n')
for image in images_file:
    print images_file.index(image)
    urllib.urlretrieve(image.replace('http://sandbox-compositor.modelmydiet.com/i/','http://images.modelmydiet.com/i/'), 'Images/After_men/'+image.replace('http://sandbox-compositor.modelmydiet.com/i/',''))