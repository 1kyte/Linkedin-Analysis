// (
//     function () {
//
//
//         //============================================= PieChart1 =============================================
//
//         var piaChart = echarts.init(document.getElementById('piaChart4'));
//
//         option1 = {
//             title : {
//                 text: 'Types of jobs',
//                 x:'center',
//                 textStyle:{
//                     fontSize: 25,
//                     fontWeight:'bolder',
//                 },
//             },
//             tooltip : {
//                 trigger: 'item',
//                 formatter: "{a} <br/>{b} : {c} ({d}%)"
//             },
//             legend: {
//                 orient: 'vertical',
//                 left: 'left',
//                 data: ["Internship", "Volunteer", "Temporary", "Part-time", "Contract", "Full-time","Other"]
//             },
//             textStyle:{
//                 fontSize: 15,
//                 fontWeight:'bolder',
//             },
//             // roseType: 'radius',
//             series : [
//                 {
//                     name: 'Types of jobs',
//                     type: 'pie',
//                     radius : '55%',
//                     center: ['50%', '60%'],
//                     data:[
//                         {value:6, name:'Internship'},
//                         {value:8, name:'Volunteer'},
//                         {value:82, name:'Temporary'},
//                         {value:150, name:'Part-time'},
//                         {value:323, name:'Contract'},
//                         {value:3103, name:'Full-time'},
//                         {value:21, name:'Other'}
//                     ],
//                     itemStyle: {
//                         emphasis: {
//                             shadowBlur: 10,
//                             shadowOffsetX: 0,
//                             shadowColor: 'rgba(0, 0, 0, 0.5)'
//                         }
//                     }
//                 }
//             ]
//         };
//         piaChart.setOption(option1);
//
//         piaChart.on('click',function(params){
//             console.log(params.data.name)
//
//         });
//
//         //============================================= PieChart2 =============================================
//
//         var piaChart2 = echarts.init(document.getElementById('levels_of_Job'));
//
//         option2 = {
//             title : {
//                 text: 'Levels of jobs',
//                 x:'center',
//                 textStyle:{
//                     fontSize: 25,
//                     fontWeight:'bolder',
//                 },
//
//             },
//             tooltip : {
//                 trigger: 'item',
//                 formatter: "{a} <br/>{b} : {c} ({d}%)"
//             },
//             legend: {
//                 orient: 'vertical',
//                 left: 'left',
//                 data: ["Internship", "Executive", "Director", "Entry level", "Associate","Mid-Senior level"]
//             },
//             textStyle:{
//                 fontSize: 15,
//                 fontWeight:'bolder',
//             },
//             series : [
//                 {
//                     name: 'Levels of jobs',
//                     type: 'pie',
//                     radius : '55%',
//                     center: ['50%', '60%'],
//                     data:[
//                         {value:22, name:'Internship'},
//                         {value:60, name:'Executive'},
//                         {value:111, name:'Director'},
//                         {value:571, name:'Entry level'},
//                         {value:874, name:'Associate'},
//                         {value:1470, name:'Mid-Senior level'}
//                     ],
//                     itemStyle: {
//                         emphasis: {
//                             shadowBlur: 10,
//                             shadowOffsetX: 0,
//                             shadowColor: 'rgba(0, 0, 0, 0.5)'
//                         }
//                     }
//                 }
//             ]
//         };
//         piaChart2.setOption(option2);
//
//         piaChart2.on('click',function(params){
//
//             showData(params.data.name);
//
//
//         });
//         $(document).ready(function(){
//             $(".closeIcon").click(function(){
//                 close()
//             });
//         });
//
//     }()
//
// );
//
// function showData(name) {
//     console.log(name);
//     popChart = document.getElementById('popChart');
//     popChart.style.display='block';
//     popChart.classList.add('open');
//
// }
//
// function close() {
//     popChart = document.getElementById('popChart');
//     if (popChart.classList.contains('open')){
//         popChart.style.display='none';
//         popChart.classList.remove('open');
//     }
// }
//
//
//
