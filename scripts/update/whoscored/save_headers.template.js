var Nightmare = require('nightmare');
require('nightmare-webrequest-addon');
var path = require('path');
var fs = require('fs');
var cookie = require('cookie');


function _save_headers() {

  var nightmare = Nightmare({
    show: true,
    waitTimeout: 30000,
    pollInterval: 1000,
    switches: {
      'disable-http-cache': true,
      'ignore-certificate-errors': true
    }
  });

  var headersFilePath = path.posix.join('tmp', 'update', 'headers', 'www.whoscored.com.json');
  var requestHeaders = undefined;

  if (fs.existsSync(headersFilePath)) {
    var requestHeadersString = fs.readFileSync(headersFilePath, 'utf8');
    requestHeaders = JSON.parse(requestHeadersString);
  }

  nightmare
    .onBeforeSendHeaders(function f(details, callback) {
      var r = HEADERS_JSON_HERE;
      callback( { cancel: false, requestHeaders: r });
    })
    .onSendHeaders({ urls: ['*://www.whoscored.com/tournamentsfeed/13796/Fixtures*'] })
    .on('onSendHeaders', function (details) {
      requestHeaders = details.requestHeaders;
      var requestHeadersJsonString = JSON.stringify(requestHeaders);

      fs.writeFileSync(headersFilePath, requestHeadersJsonString);
    })
    .goto('https://www.whoscored.com/Regions/252/Tournaments/2/England-Premier-League')
    .wait(2000)
    .click('#date-config-toggle-button')
    .wait(1000)
    .click('.days .selectable')
    .wait(1000)
    .then(function (result) {
      nightmare
        .goto('https://www.whoscored.com/')
        .wait(2000)
        .click('#popular-tournaments-list a')
        .wait(5000)
        .evaluate(function () {
          return document.documentElement.outerHTML;
        })
        .end()
        .then(function (result) {
          var matchesHtmlFilePath = path.posix.join('tmp', 'update', 'whoscoredPage.html');
          fs.writeFileSync(matchesHtmlFilePath, result);
        })
        .catch(function (err) {
          console.error(err);
          process.exit(1);
        });
    })
    .catch(function (err) {
      console.error(err);
      process.exit(1);
    });

}


_save_headers();
