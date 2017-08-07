var Nightmare = require('nightmare');
var fs = require('fs');
var path = require('path');
var fs = require('fs-extra');
var strftime = require('strftime');


function _parse_betcity_stage1() {
  var currentDate = new Date();
  var currentDateStr = strftime('%Y-%m-%d', currentDate);

  var nightmare = Nightmare({
    show: true,
    waitTimeout: 1800000,
    pollInterval: 60000,
    switches: {
      'disable-http-cache': true,
      'ignore-certificate-errors': true
    }
  });

  nightmare
    .goto('https://www.betsbc.com/new/#/line/line_ids=a:1')
    .wait(5000)
    .wait('input[name=simple]')
    .wait(1000)
    .select('select[name=time]', '5')
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
      var matchesHtmlDirPath = path.posix.join('tmp', 'update', 'betcity');
      fs.ensureDirSync(matchesHtmlDirPath);

      var matchesHtmlFilePath = path.posix.join('tmp', 'update', 'betcity', 'datesHtml', currentDateStr + '.html');
      fs.writeFileSync(matchesHtmlFilePath, result);
    })
    .catch(function (err) {
      console.error(err);
      process.exit(1);
    });
}


_parse_betcity_stage1();
