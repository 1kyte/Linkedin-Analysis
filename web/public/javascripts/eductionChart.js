(
    function () {
        const option=[{type:'industry',fileName:'profile_location_v2'},{type:'education',fileName:'profile_school_v2'}];

        $.get("/data/read?type=profile_location_v2",function (data, status) {
            if(status=="success") {
                dataList = data.data;
                createLocationBarChart(dataList,'industry');
            }else{

            }
        });

        var buttonList = document.getElementById('profileListButton');
        option.forEach(({type, fileName})=> {
            console.log(type)
            const optionbutton = document.createElement('button')
            optionbutton.innerText=type
            optionbutton.id = type

            onOptionbuttonClick = enhancedOptionbuttonClicked(optionbutton,type,fileName);
            optionbutton.onclick = onOptionbuttonClick;
            buttonList.appendChild(optionbutton)
        })

    }()
);

function enhancedOptionbuttonClicked(optionbutton,type,fileName){
    return function () {
        $.get("/data/read?type="+fileName,function (data, status) {
            if(status=="success") {
                dataList = data.data;
                createLocationBarChart(dataList,type);
            }else{

            }
        });
        // createPiaChart(name,list)
    }
}
function createLocationBarChart(data,type) {

    var item = [];
    var value = [];
    for (var i=0,l=data.length; i<l; i++){
        item[i] = data[i].name
        value[i] = data[i].value
    }

    colorid  = parseInt(Math.random()*(11+1),10);
    c = ['#c23531','#2f4554', '#61a0a8', '#d48265', '#91c7ae','#749f83',  '#ca8622', '#bda29a','#6e7074', '#546570', '#c4ccd3'];


    var myChart = echarts.init(document.getElementById('profile_location'));

    var option = {
        title: {
            text: 'Top 6 '+type,
            x:'center',
            textStyle:{
                fontSize: 25,
                fontWeight:'bolder',
            },
        },
        grid:{
            width:500,
            height:300,
            left:250
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
            data:['amount of profile'],
            x:'right',
        },
        xAxis: {
        },
        yAxis: {
            inverse: true,
            data: item,
        },
        series: [{
            name: 'amount of profile',
            type: 'bar',
            data: value,
        }],
        color: [c[colorid]]
    };


    myChart.setOption(option);

};