const express = require('express');
const router = express.Router();
const fs = require('fs');
const PATH = './public/data/';
// const getData = require('getData');




router.get('/read', function(req, res, next) {

    var type = req.param('type') || '';//获取url传递的参数，如果用户没有传默认为空
    fs.readFile(PATH + type + '.json', function(err, data){
        if(err){
            return res.send({
                status:0,
                info:'Read file Error.'
            });
        }
        var COUNT = 6
        if (type=='companyResult'){
            COUNT = 50
        }
        ;//返回最多50行数据
        var obj = [];
        try{
            obj = JSON.parse(data.toString());
        }catch(e){
            obj =[];
        }

        if(obj.length > COUNT){
            obj = obj.slice(0,COUNT);

        }
        return res.send({
            status:1,
            data:obj
        });
    });
});

router.post('/read',function (req, res, next) {

    var type = req.param('type') || '';
    var item = req.body;
    fs.readFile(PATH + type + '.json', function(err, data){
        if(err){
            return res.send({
                status:0,
                info:'Read file Error.'
            });
        }
        var COUNT = 220;

        var obj = [];
        try{
            obj = JSON.parse(data.toString());
        }catch(e){
            obj =[];
        }

        if(obj.length > COUNT) {
            obj = obj.slice(0, COUNT);

        }
        var companyNameList = getCompany(item.requiredFrom,item.required,obj);

        return res.send({
            status:1,
            data:companyNameList
        });
    });
});

function getCompany(requiredFrom,item,obj){
    var resultList = [];
    var finalList = {};
    switch (requiredFrom) {
        case "industry":
            var l = [];
            var locationRecording = [];
            var sizeRecording = [];
            var s = [];
            obj.forEach(({industry,name,location,size})=> {
                if (industry == item){
                    if (locationRecording.indexOf(location)<0){
                        if (location!=undefined){
                            arr = new Array();
                            arr.push(name);
                            l.push({name:location,value:1,company:arr});
                            locationRecording.push(location)
                        }
                    }else{
                        for (var a = 0;a<l.length;a++){
                            if (l[a].name==location){
                                l[a].value +=1
                                l[a].company.push(name);
                            }
                        }
                    }
                    if (sizeRecording.indexOf(size)<0){
                        if (size !=undefined){
                            s.push({name:size,value:1,company:[name]});
                            sizeRecording.push(size)
                        }

                    }else {
                        for (var b = 0;b<s.length;b++){
                            if (s[b].name==size){
                                s[b].value +=1;
                                s[b].company.push(name);
                            }
                        }
                    }

                    resultList.push(name);
                }
            });
            finalList.size = s;
            finalList.location = l;
            finalList['resultList'] = resultList;
            break;

        case "location":
            var i = [];
            var industryRecording = [];
            var sizeRecording = [];
            var s = [];
            obj.forEach(({industry,name,location,size})=> {
                if (location == item){
                    if (industryRecording.indexOf(industry)<0){
                        if (industry!=undefined){
                            i.push({name:industry,value:1,company:[name]});
                            industryRecording.push(industry)
                        }
                    }else{
                        for (var a = 0;a<i.length;a++){
                            if (i[a].name==industry){
                                i[a].value +=1;
                                i[a].company.push(name)
                            }
                        }
                    }
                    if (sizeRecording.indexOf(size)<0){
                        if (size !=undefined){
                            s.push({name:size,value:1,company:[name]});
                            sizeRecording.push(size)
                        }
                    }else {
                        for (var b = 0;b<s.length;b++){
                            if (s[b].name==size){
                                s[b].value +=1;
                                s[b].company.push(name)
                            }
                        }
                    }
                    resultList.push(name);
                }
            });
            finalList.size = s;
            finalList.industry = i;
            finalList['resultList'] = resultList;
            break;

        case "size":
            var l = [];
            var locationRecording = [];
            var industryRecording = [];
            var i = [];
            obj.forEach(({industry,name,location,size})=> {
                if (size == item){
                    if (locationRecording.indexOf(location)<0){
                        if (location!=undefined){
                            l.push({name:location,value:1,company:[name]});
                            locationRecording.push(location)
                        }
                    }else{
                        for (var a = 0;a<l.length;a++){
                            if (l[a].name==location){
                                l[a].value +=1;
                                l[a].company.push(name)
                            }
                        }
                    }
                    if (industryRecording.indexOf(industry)<0){
                        if (industry!=undefined){
                            i.push({name:industry,value:1,company:[name]});
                            industryRecording.push(industry)
                        }

                    }else {
                        for (var b = 0;b<i.length;b++){
                            if (i[b].name==industry){
                                i[b].value +=1
                                i[b].company.push(name)
                            }
                        }
                    }

                    resultList.push(name);
                }
            });
            finalList.industry = i;
            finalList.location = l;
            finalList['resultList'] = resultList;
            break;
    }

    return finalList
};


module.exports = router;