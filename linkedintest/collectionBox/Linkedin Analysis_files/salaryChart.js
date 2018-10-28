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
        // value[i] = data[i].value
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
}

function createSalaryChart(data) {

    var item = [];
    var first = [];
    var second = [];
    var third = [];
    var industry = {};

    for (var i=0,l=data.length; i<l; i++){
        item[i] = data[i].position;
        first[i] = data[i].industry[0].baseSalary;
        second[i] = data[i].industry[1].baseSalary;
        third[i] = data[i].industry[2].baseSalary;
        industry[item[i]] = [];
        // arr = [];
        for (var a = 0; a<3;a++){
            industry[item[i]].push(data[i].industry[a].industry)
        }

        // value[i] = data[i].value
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
        console.log(params.name);
        showPopDetail(industry[params.name]);

    });

    $(document).ready(function(){

        $("#detailClose").click(function(){
                closesSalaryPop()
        }
            );
    });

}

function showPopDetail(list) {
    pop = document.getElementById('salaryPopChart');
    if (!pop.classList.contains('open')) {
        pop.style.display = 'block';
        pop.classList.add('open');
    }
}

function closesSalaryPop() {
    pop = document.getElementById('salaryPopChart');
    if (pop.classList.contains('open')){
        pop.style.display='none';
        pop.classList.remove('open');
    }
};