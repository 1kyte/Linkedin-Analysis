
// function getresponse(){
//     $.get("/data",function (data, status) {
//         if(status=="success") {
//             console.log("DATA: " + data + "\nSTATUS: " + status);
//             // result = JSON.parse(data);
//         }else{
//             // showTheResult("Sorry, There are something wrong!");
//         }
//     });
// }
(
    function () {

        $.get("/data",function (data, status) {
            if(status=="success") {
                console.log("DATA: " + data + "\nSTATUS: " + status);
                // result = JSON.parse(data);
            }else{
                // showTheResult("Sorry, There are something wrong!");
            }
        });

        var myChart = echarts.init(document.getElementById('main'));

        var option = {
            title: {
                text: 'ECharts 入门示例'
            },
            tooltip: {},
            legend: {
                data:['销量']
            },
            xAxis: {
                data: ["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"]
            },
            yAxis: {},
            series: [{
                name: '销量',
                type: 'bar',
                data: [5, 20, 36, 10, 10, 20]
            }]
        };


        myChart.setOption(option);

        myChart.on("click",function(params){
            console.log(params)

        })
    }()
)