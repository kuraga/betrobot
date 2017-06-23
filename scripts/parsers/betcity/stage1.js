var Nightmare = require('nightmare');
var fs = require('fs');
var path = require('path');


var nightmare = Nightmare({
  show: true,
  waitTimeout: 1800000,
  pollInterval: 60000,
  switches: {
    'proxy-server': 'socks5://127.0.0.1:9050',
    'disable-http-cache': true
  }
});


nightmare
  .goto('https://www.betsbc.com/new/#/line/line_ids=a:1')
  .wait(5000)
  .wait('input[name=simple]')
  .wait(1000)
  .click('input#dop')
  .wait(1000)
  .click('input[name=simple]')
  .wait(1000)
  .click('a#btn_submit')
  .wait(60000)
  .wait(function () {
    var n = document.getElementsByClassName('loadingExt').length;
    if (window.lastN === n) {
      return true;
    } else {
      window.lastN = n;
      return false;
    }
  })
  .wait(10000)
  .evaluate(function () {
    return document.documentElement.outerHTML;
  })
  .end()
  .then(function (result) {
    var matchesHtmlPath = path.posix.join('tmp', 'update', 'betcity', 'current.html');
    fs.writeFileSync(matchesHtmlPath, result);
  })
  .catch(function (err) {
    console.error(err);
    process.exit(1);
  });
