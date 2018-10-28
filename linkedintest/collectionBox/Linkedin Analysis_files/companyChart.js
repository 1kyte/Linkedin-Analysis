(
    function () {
        $.get("/data/read?type=company_inAU",function (data, status) {
            if(status=="success") {
                dataList = data.data;
                console.log({'company':data});
                createButton(dataList);
                // createPiaChart(data)
            }else{
                alert("Download data fail!")
            }
        });
    }()
);

function createButton(list) {
    companyList = document.getElementById('companyListButton');
    list.forEach(({location, name}) => {
        // console.log(location)
        const company = document.createElement('button');
        company.innerText = name
        company.type = 'button';
        company.id = name;

        onCompanyClick = enhancedOnCompanyClicked(company,name,location);
        company.onclick = onCompanyClick;
        companyList.appendChild(company)
    })
}

function enhancedOnCompanyClicked(company,name,list){

    return function () {
        createPiaChart(name,list)
    }
}


function createPiaChart(company,data) {
    var list = [];
    var name = [];
    for (var i=0,l=data.length; i<l; i++){
        list.push({'value':data[i].number,'name':data[i].title})
        name[i] = data[i].title;
    }

    // console.log(name)

    var piaChart = echarts.init(document.getElementById('companyLocation'));

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

}
