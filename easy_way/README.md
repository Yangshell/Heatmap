# 环境要求:  
- Python 3.
- pandas
- geopy
  
# 运行说明:  
将'heatmap1.js'、'heatmap1.py'和数据文件'*.csv'放在同一文件夹下,数据文件要求只包含两列，第一列为地址，第二列为数值：
  
![](https://github.com/Yangshell/Heatmap/blob/master/image/1.png)
  
在终端中运行'heatmap1.py'：
  
![](https://github.com/Yangshell/Heatmap/blob/master/image/2.png)
  
Windows系统在命令提示符中运行：
  
![](https://github.com/Yangshell/Heatmap/blob/master/image/6.png)
  
程序运行结束会自动调用浏览器打开一个页面：
  
![](https://github.com/Yangshell/Heatmap/blob/master/image/3.png)
  
此时文件夹下会生成一个与数据文件名相同的'.txt'文件：
  
![](https://github.com/Yangshell/Heatmap/blob/master/image/4.png)
  
将'.txt'中的内容复制到浏览器新打开的页面左侧，替换掉原来内容，点击运行，右侧就会出现热力地图：
  
![](https://github.com/Yangshell/Heatmap/blob/master/image/5.png)
  
# 参数设置:  
程序主要涉及三个参数(代码11-13行)的设定:   

`dirname 数据文件名`  
`center 地图中心(可以是城市名如'北京'、省份名如'辽宁'、国家名如'中国')`  
`size 地图尺度(根据要展示的地理范围大小在以下几项中选择：城区、市、省、中国)`  
  
![](https://github.com/Yangshell/Heatmap/blob/master/image/new7.png)
