(
    function () {
        var piaChart = echarts.init(document.getElementById('piaChart'));

        option1 = {
            title : {
                text: 'Types of jobs',
                x:'center'
            },
            tooltip : {
                trigger: 'item',
                formatter: "{a} <br/>{b} : {c} ({d}%)"
            },
            legend: {
                orient: 'vertical',
                left: 'left',
                data: ["Internship", "Volunteer", "Temporary", "Part-time", "Contract", "Full-time","Other"]
            },
            // roseType: 'radius',
            series : [
                {
                    name: 'Types of jobs',
                    type: 'pie',
                    radius : '55%',
                    center: ['50%', '60%'],
                    data:[
                        {value:6, name:'Internship'},
                        {value:8, name:'Volunteer'},
                        {value:82, name:'Temporary'},
                        {value:150, name:'Part-time'},
                        {value:323, name:'Contract'},
                        {value:3103, name:'Full-time'},
                        {value:21, name:'Other'}
                    ],
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

        piaChart.on('click',function(params){
            console.log(params.data.name)

        });


        var piaChart2 = echarts.init(document.getElementById('piaChart2'));

        option2 = {
            title : {
                text: 'Levels of jobs',
                x:'center'
            },
            tooltip : {
                trigger: 'item',
                formatter: "{a} <br/>{b} : {c} ({d}%)"
            },
            legend: {
                orient: 'vertical',
                left: 'left',
                data: ["Internship", "Executive", "Director", "Entry level", "Associate","Mid-Senior level"]
            },
            series : [
                {
                    name: 'Levels of jobs',
                    type: 'pie',
                    radius : '55%',
                    center: ['50%', '60%'],
                    data:[
                        {value:22, name:'Internship'},
                        {value:60, name:'Executive'},
                        {value:111, name:'Director'},
                        {value:571, name:'Entry level'},
                        {value:874, name:'Associate'},
                        {value:1470, name:'Mid-Senior level'}
                    ],
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
        piaChart2.setOption(option2);

        piaChart2.on('click',function(params){
            console.log(params.data.name)

        })
    }()

)
