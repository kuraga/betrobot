printjson({
    'totalCount': db.proposed.count(),
    'totalAvg': db.proposed.aggregate({ '$match': { 'ground_truth': { '$in': [true, false] } } }, { '$group': { '_id': null, 'avg': { '$avg': '$bet_value' } } }).next().avg,
    'positiveRatio': db.proposed.find({ 'ground_truth': true }).count() / db.proposed.find({ 'ground_truth': { '$in': [true, false] } }).count(),
    'positiveAvg': db.proposed.aggregate({ '$match': { 'ground_truth': true } }, { '$group': { '_id': null, 'avg': { '$avg': '$bet_value' } } }).next().avg,
    'ROI': db.proposed.aggregate({ '$match': { 'ground_truth': true } }, { '$group': { '_id': null, 'sum': { '$sum': '$bet_value' } } }).next().sum / db.proposed.find({ 'ground_truth': { '$in': [true, false] } }).count() - 1
});
