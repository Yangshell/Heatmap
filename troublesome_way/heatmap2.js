<!DOCTYPE html>
<html style="height: 100%">
   <head>
       <meta charset="utf-8">
   </head>
   <body style="height: 100%; margin: 0">
       <div id="container" style="height: 100%"></div>

       
       <script type="text/javascript" src="http://apps.bdimg.com/libs/jquery/2.1.4/jquery.min.js"></script>
       

       <script type="text/javascript" src="http://echarts.baidu.com/gallery/vendors/echarts/echarts-all-3.js"></script>
       <script type="text/javascript" src="http://echarts.baidu.com/gallery/vendors/echarts/extension/dataTool.min.js"></script>
       <script type="text/javascript" src="http://echarts.baidu.com/gallery/vendors/echarts/map/js/china.js"></script>
       <script type="text/javascript" src="http://echarts.baidu.com/gallery/vendors/echarts/map/js/world.js"></script>
       <script type="text/javascript" src="http://api.map.baidu.com/api?v=2.0&ak=ZUONbpqGBsYGXNIYHicvbAbM"></script>
       <script type="text/javascript" src="http://echarts.baidu.com/gallery/vendors/echarts/extension/bmap.min.js"></script>
       <script type="text/javascript">
          var dom = document.getElementById("container");
          var myChart = echarts.init(dom);
          var app = {};
          option = null;
          app.title = '热力图与百度地图扩展';

          $.get('data.json', function (data) {
              var data = eval("("+data+")");
              var points = [].concat.apply([], data.map(function (track) {
              return track.map(function (seg) {
                  return seg.coord.concat([1]);
              });
          }));
          myChart.setOption(option = {
              animation: false,
              bmap: {
                  center: [116.40066322374, 39.940018034923],
                  zoom: 12,
                  roam: true
              },
              visualMap: {
                  show: false,
                  top: 'top',
                  min: 0,
                  max: 5,
                  seriesIndex: 0,
                  calculable: true,
                  inRange: {
                      color: ['blue', 'blue', 'green', 'yellow', 'red']
                  }
              },
              series: [{
                  type: 'heatmap',
                  coordinateSystem: 'bmap',
                  pointSize: 3,
                  blurSize: 20
              }]
          });
              if (!app.inNode) {
                  // 添加百度地图插件
                  var bmap = myChart.getModel().getComponent('bmap').getBMap();
                  bmap.addControl(new BMap.MapTypeControl());
              }
          },"text");
          if (option && typeof option === "object") {
              myChart.setOption(option, true);
          }
       </script>
   </body>
</html>
