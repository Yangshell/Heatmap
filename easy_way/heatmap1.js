app.title = '热力图与百度地图扩展';

$.get('data/asset/data/hangzhou-tracks.json', function (data) {

    var points = [].concat.apply([], data.map(function (track) {
        return track.map(function (seg) {
            return seg.coord.concat([1]);
        });
    }));
    myChart.setOption(option = {
        animation: false,
        bmap: {


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
        var bmap = myChart.getModel().getComponent('bmap').getBMap();
        bmap.addControl(new BMap.MapTypeControl());
    }
});
