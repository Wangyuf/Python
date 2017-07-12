import requests
import re
import os
import time
local = time.strftime("%Y.%m.%d %H:%M")

picPathDir = 'bingPic'
if os.path.isdir(picPathDir) == False:
    os.makedirs(picPathDir)
monthPath = time.strftime("%Y.%m")
if os.path.isdir(picPathDir+'/'+monthPath) == False:
    os.makedirs(picPathDir+'/'+monthPath)

localDate = time.strftime("%Y.%m.%d")
datePicPath = picPathDir+'/'+monthPath+'/'+localDate + '.jpg';
if os.path.isfile(datePicPath) :
        print(localDate+': '+localDate+'.jpg'+' pic exists')
else:
    url = 'http://cn.bing.com/'
    con = requests.get(url)
    content = con.text
    p = re.compile(r"(/az/hprichbg/rb/.*?.jpg)")
    a = p.findall(content)
    if len(a) >0:
        read = requests.get(url+a[0])
        f = open(datePicPath, 'wb')
        f.write(read.content)
        f.close()
        print(local+': '+localDate+'.jpg'+' down pic success')
    else:
        print(local+': bing pic not find')
