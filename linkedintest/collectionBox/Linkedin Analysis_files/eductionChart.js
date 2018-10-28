(
    function () {
        $.get("/data/read?type=profile_school_v2",function (data, status) {
            if(status=="success") {
                // console.log(data);
                dataList = data.data;
                createBarChart(dataList);
                // console.log("STATUS: " + status);

            }else{

            }
        });
    }()
);
function createLocationBarChart(data) {

    var item = []
    var value = []
    for (var i=0,l=data.length; i<l; i++){
        item[i] = data[i].name
        value[i] = data[i].value
    }
    console.log(item);

    var myChart = echarts.init(document.getElementById('main'));

    var option = {
        title: {
            text: 'Top 6 location using Linkedin',
            x:'center',
            textStyle:{
                fontSize: 25,
                fontWeight:'bolder',
            },
        },
        grid:{
            width:500,
            height:300,
            x:'center'
        },
        tooltip: {
            trigger: 'axis',
        },
        textStyle:{
            fontSize: 15,
            fontWeight:'bolder',
        },
        animationType: 'scale',
        tooltip: {},
        legend: {
            data:['Quantity'],
            x:'right',
        },
        xAxis: {
        },
        yAxis: {
            inverse: true,
            data: item,
        },
        series: [{
            name: 'Quantity',
            type: 'bar',
            data: value,
        }]
    };


    myChart.setOption(option);

    myChart.on("click",function(params){
        console.log(params)

    })
};