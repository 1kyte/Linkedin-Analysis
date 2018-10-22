var express = require('express');
var router = express.Router();
var fs = require('fs');
var PATH = './public/data/';

//data/read?type=it
//data/read?type=it.json
router.get('/read', function(req, res, next) {
    var type = req.param('type') || '';//获取url传递的参数，如果用户没有传默认为空
    fs.readFile(PATH + type + '.json', function(err, data){
        if(err){
            return res.send({
                status:0,
                info:'Read file Error.'
            });
        }
        var COUNT = 6;//返回最多50行数据
        var obj = [];
        try{
            obj = JSON.parse(data.toString());//这里做异常处理，如果文件中存储的不是json格式的字符串（比如空文件）这里会抛出异常
        }catch(e){
            obj =[];
        }

        if(obj.length > COUNT){
            obj = obj.slice(0,COUNT);//返回前50行数据

        }
        return res.send({
            status:1,
            data:obj
        });
    });
});

module.exports = router;