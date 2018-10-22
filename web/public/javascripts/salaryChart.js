(
    function () {
        var dataList;
        $.get("/data/read?type=salary_extract",function (data, status) {
            if(status=="success") {
                dataList = data.data;
                createSalaryChart(dataList);
                console.log({'salary':data});
                console.log("STATUS: " + status);

            }else{
                alert("Download data fail!")
            }
        });

        var salary_jobBar = document.getElementById('salary_industry');
        var salaryBar = document.getElementById('salary');
        var salary_location_Chart = document.getElementById('salary_location_Chart');
        salary_jobBar.focus();

        $(document).ready(function(){
            $("#salary_location").click(function(){
                salary_location_Chart.style.display='block';
                salaryBar.style.display='none';
                createLocationBar(dataList)
            });
        });

        $(document).ready(function(){
            $("#salary_industry").click(function(){
                salary_location_Chart.style.display='none';
                salaryBar.style.display='block';
                createSalaryChart(dataList);
            });
        });


    }()
);

function createLocationBar(data) {
    console.log(data);
    var item = [];
    var first = [];
    var second = [];
    var third = [];

    for (var i=0,l=data.length; i<l; i++){
        item[i] = data[i].position;
        first[i] = data[i].location[0].basesalary;
        second[i] = data[i].location[1].basesalary;
        third[i] = data[i].location[2].basesalary;
        location[item[i]] = [];
        for (var a = 0,le = data[i].location.length; a<le;a++){
            location[item[i]].push({"baseSalary":data[i].location[a].basesalary,"industry":data[i].location[a].location})
        }data[i].location[a]

        console.log(location)
    }


    var multiBar = echarts.init(document.getElementById('salary_location_Chart'));

    option = {
        title: {
            text: 'Base Salary of several positions',
            x:'center',
        },
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'shadow'
            }
        },
        legend: {
            data: ['First', 'Second','Third'],
            y:'bottom',
        },
        grid: {
            left: '3%',
            right: '4%',
            bottom: '10%',
            containLabel: true
        },
        xAxis: {
            type: 'value',
            boundaryGap: [0, 0.01]
        },
        yAxis: {
            type: 'category',
            data: item,
        },
        series: [
            {
                name: 'First',
                type: 'bar',
                data: first,
            },
            {
                name: 'Second',
                type: 'bar',
                data: second,
            },
            {
                name: 'Third',
                type: 'bar',
                data: third
            }
        ]
    };
    multiBar.setOption(option);

    multiBar.on('click',function(params){
        console.log(location[params.name])
        showPopDetail(location[params.name],params.name);

    });

    $(document).ready(function(){

        $("#detailClose").click(function(){
                closesSalaryPop()
            }
        );
    });
}



function createSalaryChart(data) {

    var item = [];
    var first = [];
    var second = [];
    var third = [];
    var industry = {};
    console.log({'data':data})
    for (var i=0,l=data.length; i<l; i++){
        item[i] = data[i].position;
        first[i] = data[i].industry[0].baseSalary;
        second[i] = data[i].industry[1].baseSalary;
        third[i] = data[i].industry[2].baseSalary;
        industry[item[i]] = [];
        for (var a = 0,le = data[i].industry.length; a<le;a++){
            industry[item[i]].push(data[i].industry[a])
        }

    }


    var multiBar = echarts.init(document.getElementById('salary'));

    option = {
        title: {
            text: 'Base Salary of several positions',
            x:'center',
        },
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'shadow'
            }
        },
        legend: {
            data: ['First', 'Second','Third'],
            y:'bottom',
        },
        grid: {
            left: '3%',
            right: '4%',
            bottom: '10%',
            containLabel: true
        },
        xAxis: {
            type: 'value',
            boundaryGap: [0, 0.01]
        },
        yAxis: {
            type: 'category',
            data: item,
        },
        series: [
            {
                name: 'First',
                type: 'bar',
                data: first,
            },
            {
                name: 'Second',
                type: 'bar',
                data: second,
            },
            {
                name: 'Third',
                type: 'bar',
                data: third
            }
        ]
    };
    multiBar.setOption(option);

    multiBar.on('click',function(params){
        showPopDetail(industry[params.name],params.name);

    });

    $(document).ready(function(){

        $("#detailClose").click(function(){
                closesSalaryPop()
        }
            );
    });

}

function showPopDetail(list,name) {
    pop = document.getElementById('salaryPopChart');
    if (!pop.classList.contains('open')) {
        pop.style.display = 'block';
        pop.classList.add('open');
        createPiaChart(name,list)
    }
};

function closesSalaryPop() {
    pop = document.getElementById('salaryPopChart');
    if (pop.classList.contains('open')){
        pop.style.display='none';
        pop.classList.remove('open');
    }
};

function createPiaChart(position,data) {
    var list = [];
    var name = [];
    for (var i=0,l=data.length; i<l; i++){
        list.push({'value':data[i].baseSalary,'name':data[i].industry})
        name[i] = data[i].industry;
    }
    // console.log(name)
    var piaChart = echarts.init(document.getElementById('popDetailChart'));

    option = {
        title : {
            text: 'Salary of '+position,
            x:'center',
            textStyle:{
                fontSize: 25,
                fontWeight:'bolder',
            },
        },
        backgroundColor: 'white',
        tooltip : {
            trigger: 'item',
            formatter: "{a} <br/>{b} : {c} ({d}%)"
        },
        legend: {
            orient: 'vertical',
            left: 'left',
            data: name
        },
        textStyle:{
            fontSize: 15,
            fontWeight:'bolder',
        },
        series : [
            {
                name: 'Types of jobs',
                type: 'pie',
                radius : '55%',
                center: ['50%', '60%'],
                data:list,
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
    piaChart.setOption(option);

};
