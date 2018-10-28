var myChart =  echarts.init(document.getElementById('companyBar'));
var myChartLocation =  echarts.init(document.getElementById('companyBarLocation'));
var piaChart = echarts.init(document.getElementById('companyLocation'));
var popPiaChart = echarts.init(document.getElementById('compPopChart'));

(
    function () {
        $.get("/data/read?type=companyResult",function (data, status) {
            if(status=="success") {
                dataList = data.data;
                // console.log(dataList)
                createButton(dataList);
            }else{
                alert("Download data fail!")
            }
        });


    }()
);

function createButton(list) {
    companyList = document.getElementById('companyListButton');
    list.forEach(({content, name}) => {
        // console.log({});
        const item = document.createElement('button');
        item.innerText = name;
        item.type = 'button';
        item.id = name;

        if (name == "industry"){
            createCompanyBarChart(name,content)
        }
        onCompanyClick = enhancedOnCompanyClicked(item,name,content);
        item.onclick = onCompanyClick;
        companyList.appendChild(item)
    })
}

function enhancedOnCompanyClicked(item,name,list){

    return function () {
        // myChart.clear();
        // piaChart.clear();
        if ((name=="industry")||(name=="location")) {
            createCompanyBarChart(name, list);
        }else{
            createCompanyPiaChart(name, list)
        }

    }
}


function createCompanyPiaChart(company,data) {
    var list = [];
    var name = [];


    for (var i=0,l=8; i<l; i++){
        list.push({'value':data[i].value,'name':data[i].name});
        name[i] = data[i].name;
    }
    const bar = document.getElementById("companyBar");
    bar.style.display = "none";
    const bar2 = document.getElementById("companyBarLocation");
    bar2.style.display = "none";
    const pie = document.getElementById("companyLocation");
    pie.style.display = "block";

    piaChart = echarts.init(document.getElementById('companyLocation'));


        option = {
            title : {
                text: 'Location of '+company,
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
                data: name
            },
            textStyle:{
                fontSize: 15,
                fontWeight:'bolder',
            },
            // roseType: 'radius',
            series : [
                {
                    name: 'companies',
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

    var thedata = null;
    piaChart.on("mousemove",function(params){
        $.post("/data/read?type=compInfo_extract",
            {
                requiredFrom: company,
                required:params.name,
            },
            function (data, status) {
                if(status=="success") {
                    showCompanyList(data.data.resultList,company,params.name);
                    thedata = data.data;
                }else{
                    alert("Sorry, There are something wrong!");
                }
            });
    });
    piaChart.on("click",function(params){
        displayComanyPopChart(company,params.name,thedata);

    });
    myChart.dispose();

}

function createCompanyBarChart(company,data)  {

    const pie = document.getElementById("companyLocation");
    pie.style.display = "none";
    const bar = document.getElementById("companyBar");
    const bar2 = document.getElementById("companyBarLocation");

    var item = []
    var value = []
    for (var i=0,l=6; i<l; i++){
        item[i] = data[i].name;
        value[i] = data[i].value;
    }

    if (company =="industry"){
        myChart = echarts.init(document.getElementById('companyBar'));
        bar2.style.display = "none";
        bar.style.display = "block";
    }else if(company == "location"){
        console.log(company);
        myChart.dispose();
        myChartLocation.dispose();
        myChartLocation =  echarts.init(document.getElementById('companyBarLocation'));
        bar.style.display = "none";
        bar2.style.display = "block";
    }


    var option = {
        title: {
            text: 'Top 6 '+company,
            x:'center',
            textStyle:{
                fontSize: 25,
                fontWeight:'bolder',
            },
        },
        grid:{
            width:500,
            height:250,
            left:300
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
            data:['number of companies'],
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
            name: 'number of companies',
            type: 'bar',
            data: value,
        }],
        color:['#61a0a8']

    };




    piaChart.dispose();

    if (company =="industry"){
        myChart.setOption(option);
        var thedata = null;
        myChart.on("mousemove",function(params){
            $.post("/data/read?type=compInfo_extract",
                {
                    requiredFrom: company,
                    required:params.name,
                },
                function (data, status) {
                    if(status=="success") {
                        showCompanyList(data.data.resultList,company,params.name);
                        thedata = data.data;
                    }else{
                        alert("Sorry, There are something wrong!");
                    }
                });
        });
        myChart.on("click",function(params){
            displayComanyPopChart(company,params.name,thedata);

        });
        myChartLocation.dispose();

    }else if(company == "location"){
        myChartLocation.setOption(option);
        var thedata = null;
        myChartLocation.on("mousemove",function(params){
            $.post("/data/read?type=compInfo_extract",
                {
                    requiredFrom: company,
                    required:params.name,
                },
                function (data, status) {
                    if(status=="success") {
                        // console.log({"post":data})
                        showCompanyList(data.data.resultList,company,params.name);
                        thedata = data.data;
                    }else{
                        alert("Sorry, There are something wrong!");
                    }
                });
        });
        myChartLocation.on("click",function(params){
            displayComanyPopChart(company,params.name,thedata);

        });

        myChart.dispose();
    }

};

$(document).ready(function(){
    $(".closeIcon").click(function(){
        closePop()
    });
});



function showCompanyList(list,item,type) {
    // const list = totList.resultList;
    // displayComanyPopChart(item,type,totList);
    companyList = document.getElementById("companiesList");
    companyList.style.display="none";
    contentWrap = document.getElementById('contentWrap');
    $("#contentWrap").empty();
    $("#CompanyNameListH3").text(type);
    companyList.style.display="block";

    for (var a =0;a<list.length;a++){
        contemtTag = document.createElement("li");
        wrap = document.createElement("div");
        wrap.className = "listWrap";
        wrap.innerText = list[a];
        wrap.className = "companyListContent";
        contemtTag.appendChild(wrap);
        br = document.createElement('br');
        contemtTag.appendChild(br);
        contentWrap.appendChild(contemtTag)
    }



}

function displayComanyPopChart(item,type,totList) {

    companyPop = document.getElementById('companyPop');
    companyPop.style.display="block";
    companyPop.classList.add('open');
    const c = [{baseType:"location"},{baseType:"size"},{baseType:"industry"}];
    console.log(item);

    var companyPopButton = document.getElementById("pop"+item.toString());
    companyPopButton.style.display="none";
    c.forEach(({baseType}) => {
        if (baseType!=item){

            var companyPopButton2 = document.getElementById("pop"+baseType.toString());
            companyPopButton2.style.display="block";
            var theList = [];
            switch (baseType) {
                case "industry":
                    theList = totList.industry;
                    break;
                case "location":
                    theList = totList.location;
                    break;
                case "size":
                    theList = totList.size;
                    break;
            }
            $(document).ready(function(){
                 $("#pop"+baseType.toString()).click(function(){
                     enhancedOnCompanyPopClicked(baseType,type,theList)
                     });
            });
        }
    })

}



function enhancedOnCompanyPopClicked(item,type,theList){
    popPieChart(item,type,theList);
    
}

function popPieChart(field,type,data) {
    var list = [];
    var name = [];
    // var nameList = new Array();

    for (var i=0,l=data.length; i<l; i++){
        list.push({'value':data[i].value,'name':data[i].name});
        name[i] = data[i].name;
        // nameList.push(data[i].company);
    }

    popPiaChart = echarts.init(document.getElementById('compPopChart'));


    popoption = {
        title : {
            text: field+' of '+type,
            x:'center',
            y:70,
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
            data: name,
            textStyle: {
                fontSize: 11,
            },
        },
        textStyle:{
            fontSize: 15,
            fontWeight:'bolder',
            color:'black',
        },
        series : [
            {
                name: 'companies',
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
    popPiaChart.setOption(popoption);

    popPiaChart.on("mousemove",function(params){
        name = params.name;
        var namelist = [];
        for (var b = 0;b<data.length;b++){
            if(name == data[b].name){
                namelist = data[b].company;
            }
        }

        showCompanyList(namelist,field,name)
    });

}


function closePop() {

    popChart = document.getElementById('companyPop');
    if (popChart.classList.contains('open')){
        popChart.style.display='none';
        popChart.classList.remove('open');
        popPiaChart.dispose();
    }
}