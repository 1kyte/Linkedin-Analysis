const express = require('express');
const router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
    // res.send('ok')
    res.render('index', { title: 'Express' });

});

router.get('/data',function (req,res,next) {
    res.send({'app':'ok'});
});

module.exports = router;