(
    function () {

        $.get("/data/read?type=job_industry",function (data, status) {
            if(status=="success") {
                dataList = data.data;
                createprofile_industryChart(dataList);
                console.log("STATUS: " + status);

            }else{
                alert("Download data fail!")
            }
        });

        var jobHomeBar = document.getElementById('jobindustryBar');
        var jobBar = document.getElementById('profile_industry_Chart')
        var jobLevelChart = document.getElementById('job_level_piaChart');
        jobHomeBar.focus();

        $(document).ready(function(){
            $("#jobLevel").click(function(){
                $.get("/data/read?type=jobLevel",function (data, status) {
                    if(status=="success") {
                        dataList = data.data;
                        jobLevelChart.style.display='block';
                        jobBar.style.display='none';
                        // console.log()
                        createJobLevelChart(dataList);
                        console.log("STATUS: " + status);

                    }else{
                        alert("Download data fail!")
                    }
                });
            });
        });

        $(document).ready(function(){
            $("#jobindustryBar").click(function(){
                $.get("/data/read?type=job_industry",function (data, status) {
                    if(status=="success") {
                        dataList = data.data;
                        jobLevelChart.style.display='none';
                        jobBar.style.display='block';
                        createprofile_industryChart(dataList);
                        console.log("STATUS: " + status);

                    }else{
                        alert("Download data fail!")
                    }
                });
            });
        });
    }()
);



function createprofile_industryChart(data) {

    var item = []
    var value = []
    for (var i=0,l=data.length; i<l; i++){
        item[i] = data[i].name
        value[i] = data[i].value
    }
    console.log(item);

    var myChart = echarts.init(document.getElementById('profile_industry_Chart'));

    var option = {
        title: {
            text: 'Top 6 industries of Recuritments',
            x:'center',
            textStyle:{
                fontSize: 25,
                fontWeight:'bolder',
            },
        },
        grid:{
            width:500,
            height:250,
            right:50,
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
            data:['number of recuritment'],
            x:'middle',
            y:'bottom',
        },
        xAxis: {

        },
        yAxis: {
            inverse: true,
            data: item,
            axisLabel: {
                show: true,
                textStyle: {
                    color: 'black',
                    fontSize:'14'
                }
            },

        },
        series: [{
            name: 'number of recuritment',
            type: 'bar',
            data: value,
        }],
        color:['#61a0a8']

    };


    myChart.setOption(option);

    myChart.on("click",function(params){
        showData(params.name);
        // console.log(params.name)
    });

    $(document).ready(function(){
        $(".closeIcon").click(function(){
            close()
        });
    });
};

function showData(name) {
    // console.log(name);
    popChart = document.getElementById('popChart');
    if (!popChart.classList.contains('open')) {
        popChart.style.display = 'block';
        popChart.classList.add('open');
        getTheDetailChart(name)
    }

};

function getTheDetailChart(name) {
    n = name.replace(' ','');
    console.log({'n':n});
    const item = name+"_industry";
    console.log(item);

    industryBarButton = document.getElementById("industryBar");
    locationBarButton = document.getElementById("locationBar");
    industryBarButton.focus();

    $.get("/data/read?type="+item,function (data, status) {
        if(status=="success") {
            console.log({"data":data});
            dataList = data.data;
            createPopChart(dataList);
            // createprofile_industryChart(dataList);
            console.log("STATUS: " + status);

        }else{
            alert("Download data fail!")
        }
    });

    $(document).ready(function(){
        $("#locationBar").click(function(){
            const locationItem = name+"_location"
            $.get("/data/read?type="+locationItem,function (data, status) {
                if(status=="success") {
                    dataList = data.data;
                    createPopChart(dataList);
                    console.log("STATUS: " + status);

                }else{
                    alert("Download data fail!")
                }
            });
        });
    });

    $(document).ready(function(){
        $("#industryBar").click(function(){
            $.get("/data/read?type="+item,function (data, status) {
                if(status=="success") {
                    dataList = data.data;
                    createPopChart(dataList);
                    console.log("STATUS: " + status);

                }else{
                    alert("Download data fail!")
                }
            });
        });
    });

};

function createPopChart(dataList) {
    var item = [];
    var value = [];
    for (var i = 0, l = dataList.length; i < l; i++) {
        item[i] = dataList[i].name;
        value[i] = dataList[i].value;
    }

    colorid  = parseInt(Math.random()*(11+1),10);
    console.log(colorid);
    c = ['#c23531','#2f4554', '#61a0a8', '#d48265', '#91c7ae','#749f83',  '#ca8622', '#bda29a','#6e7074', '#546570', '#c4ccd3'];

    var myChart = echarts.init(document.getElementById('popChartContent'));

    var option = {
        backgroundColor: 'white',
        title: {
            text: 'The Top 6 Industries of Corresponding Companies',
            // x: 'center',
            right: 50,
            textStyle: {
                fontSize: 25,
                fontWeight: 'bolder',
            },
        },
        grid: {
            width: 500,
            height: 250,
            right: 60,
        },
        tooltip: {
            trigger: 'axis',
        },
        textStyle: {
            fontSize: 15,
            fontWeight: 'bolder',
        },
        animationType: 'scale',
        tooltip: {},
        legend: {
            data: ['number of Companies'],
            x: 'right',
            y:'bottom',
        },
        xAxis: {},
        yAxis: {
            inverse: true,
            data: item,
            axisLabel: {
                show: true,
                textStyle: {
                    color: 'black',
                    fontSize:'16'
                }
            },
        },
        series: [{
            name: 'number of Companies',
            type: 'bar',
            data: value,
        }],
        color: [c[colorid]]
    };
    myChart.setOption(option);
};

function close() {

    popChart = document.getElementById('popChart');
    if (popChart.classList.contains('open')){
        popChart.style.display='none';
        popChart.classList.remove('open');
    }
};

function createJobLevelChart(data) {
    var item = [];
    for (var i = 0, l = data.length; i < l; i++) {
        item[i] = data[i].name
        console.log({'item':data[i].name});
    }
    // console.log({'item':item});
    var piaChart = echarts.init(document.getElementById('job_level_piaChart'));

    option1 = {
        title : {
            text: 'Level of jobs',
            x:'center',
            textStyle:{
                fontSize: 25,
                fontWeight:'bolder',
            },
        },
        tooltip : {
            trigger: 'item',
            formatter: "{a} <br/>{b} : {c} ({d}%)"
        },
        legend: {
            orient: 'vertical',
            left: 'left',
            data: item
        },
        textStyle:{
            fontSize: 16,
            fontWeight:'bolder',
        },
        grid: {
            width: 600,
            height: 600,
        },
        // roseType: 'radius',
        series : [
            {
                name: 'Types of jobs',
                type: 'pie',
                radius : '55%',
                center: ['50%', '60%'],
                data:data,
                itemStyle: {
                    emphasis: {
                        shadowBlur: 10,
                        shadowOffsetX: 0,
                        shadowColor: 'rgba(0, 0, 0, 0.5)'
                    }
                }
            }
        ]
    };
    piaChart.setOption(option1);

    // piaChart.on('click',function(params){
    //     console.log(params.data.name)
    //
    // });
}