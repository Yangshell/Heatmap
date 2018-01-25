#coding=utf-8
#
#  heatmap1.py
#
#  Created by Yangshell on 2018/1/25.
#  Copyright © 2018年 Yangshell. All rights reserved.
#
import ssl
from geopy.geocoders import Nominatim
import math
import pandas as pd
import os
import http.server
import socketserver
import webbrowser

script_path = os.path.realpath(__file__)
diradress = os.path.dirname(script_path)
dirname = 'test1.csv'
city = '北京'
df = pd.read_csv(diradress + '/' + dirname, header=None, sep=',', encoding='gb2312')
datastring = '            data: ['
unit = 10 ** math.floor(math.log10(min(df.iloc[:,1])))

for i in range(len(df)):
    ssl._create_default_https_context = ssl._create_unverified_context
    geolocator = Nominatim()
    print(city+df[0][i])
    try:
        (a, b) = (geolocator.geocode(city+df[0][i]).latitude, geolocator.geocode(city+df[0][i]).longitude)
    except:
        continue
    else:
        stringunit = '[' + str(b) + ',' + str(a) + ',' + str(unit) + ']' + ','
        datastring = datastring + stringunit * int(df[1][i] / unit)

datastring = datastring[:-1] + ']' + ',\n'

f = open(diradress + '/' + 'heatmap2.js')
lines = []
for line in f:
    lines.append(line)
f.close()
lines.insert(53, datastring)
s = ''.join(lines)
f = open(diradress + '/' + 'heatmap-bmap.html', 'w')
f.write(s)
f.close()
f = open(diradress + '/' + 'data.json','w')
f.write('')
f.close()

PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler
webbrowser.open_new('http://localhost:8000/heatmap-bmap.html')
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
