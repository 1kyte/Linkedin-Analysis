const express = require('express');
const router = express.Router();
// const data = require('data.js');

/* GET home page. */
router.get('/', function(req, res, next) {
    // res.send('ok')
    res.render('index', { title: 'Express' });

});

module.exports = router;