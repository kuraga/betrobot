var Nightmare = require('nightmare');
var path = require('path');
var fs = require('fs-extra');
var strftime = require('strftime');


function _parse_betcity_stage1() {
  var currentDate = new Date();
  var currentDateStr = strftime('%Y-%m-%d', currentDate);

  var nightmare = Nightmare({
    show: false,
    waitTimeout: 600000,
    pollInterval: 10000,
    switches: {
      'disable-http-cache': true,
      'ignore-certificate-errors': true
    }
  });


  nightmare
    .goto('https://www.betsbc.com/new/#!/line/line_ids=a:1')
    .wait(4000)

    .select('select[name=time]', '5')
    .wait(1000)

    .evaluate(function () {
      var selector = 'td.b1 input[type=checkbox][ng-click=changeOne]';
      var elements = document.querySelectorAll(selector);
      return elements.length;
    })

    .then(function (count) {
      console.log('Found ' + count + ' tournaments');

      var firsts = [];
      for (var first = 0; first < count; first += 10) {
        firsts.push(first);
      }

      firsts.reduce(function(accumulator, first) {
        return accumulator.then(function (results) {
          var last = Math.min(first + 10, count);

          console.log('Saving tournaments [' + first + ', ' + last + ')...');

          return nightmare
            .goto('https://www.betsbc.com/new/#!/line/line_ids=a:1')
            .wait(4000)

            .select('select[name=time]', '5')
            .wait(1000)

            .click('input#dop')
            .wait(1000)

            .evaluate(function (first, last) {
              var selector = 'td.b1 input[type=checkbox][ng-click=changeOne]';
              var elements = document.querySelectorAll(selector);
              for (var i = first; i < last; ++i) {
                var event = document.createEvent('MouseEvent');
                event.initEvent('click', true, true);
                elements[i].dispatchEvent(event);
              }
            }, first, last)
            .wait(5000)

            .click('a#btn_submit')
            .wait(1000)

            .wait(10000)

            .evaluate(function () {
              return document.documentElement.outerHTML;
            })
            .then(function (result) {
              var matchesHtmlDirPath = path.posix.join('tmp', 'update', 'betcity', 'datesHtml');
              fs.ensureDirSync(matchesHtmlDirPath);

              var matchesHtmlFilePath = path.posix.join('tmp', 'update', 'betcity', 'datesHtml', currentDateStr + '_' + first + '.html');
              fs.writeFileSync(matchesHtmlFilePath, result);
            })

            .catch(function (err) {
              console.error(err);
              process.exit(1);
            });
        });
      }, Promise.resolve([]))

      .then(function (results) {
          return nightmare.end();
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


_parse_betcity_stage1();
