#coding=utf-8
import ssl
from geopy.geocoders import Nominatim
import math
import pandas as pd
import webbrowser
import sys
import os
#import platform

dirname = 'test1.csv'
center = '北京'
size = '城区'

script_path = os.path.realpath(__file__)
diradress = os.path.dirname(script_path)
#diradress = '/Users/yangshell/Desktop'
df = pd.read_csv(diradress + '/' + dirname, header=None, sep=',', encoding='gb2312')
'''
if(platform.system()[0]=='D'):
    df = pd.read_csv(diradress + '/' + dirname, header=None, sep=',', encoding='gb2312')
else:
    if(platform.system()[0]=='W'):
        diradress = diradress.replace('\\', '\\\\')
        df = pd.read_csv(diradress + '\\' + dirname, header=None, sep=',', encoding='gbk')
'''
datastring = '            data: ['
unit = 10 ** math.floor(math.log10(min(df.iloc[:, 1])))

total = len(df)
for i in range(total):
    ssl._create_default_https_context = ssl._create_unverified_context
    geolocator = Nominatim()
    #print(center+df[0][i])
    print("\r",'进度：', int((i+1)/total*100), '%', end="")
    sys.stdout.flush()
    try:
        (a, b) = (geolocator.geocode(center+df[0][i]).latitude, geolocator.geocode(center+df[0][i]).longitude)
    except:
        continue
    else:
        stringunit = '[' + str(b) + ',' + str(a) + ',' + str(unit) + ']' + ','
        datastring = datastring + stringunit * int(df[1][i] / unit)

datastring = datastring[:-1] + ']' + ','

f = open(diradress + '/' + 'heatmap1.js', encoding='utf-8')
lines = []
for line in f:
    lines.append(line)
f.close()

ssl._create_default_https_context = ssl._create_unverified_context
geolocator = Nominatim()
(centera, centerb) = (geolocator.geocode(center).latitude, geolocator.geocode(center).longitude)
lines.insert(12, '            center: [' + str(centerb) + ',' + str(centera) + '],\n')
zoom = {'城区': '12', '市': '9', '省': '8', '中国': '5'}

lines.insert(13, '            zoom: ' + zoom[size] + ',')
lines.insert(30, datastring)
s = ''.join(lines)
fp = open(diradress + '/' + dirname.split('.')[0] +'.txt', 'w', encoding='utf-8')
fp.write(s)
fp.close()

print('Finish')
webbrowser.open_new('http://echarts.baidu.com/examples/editor.html?c=heatmap-bmap')
