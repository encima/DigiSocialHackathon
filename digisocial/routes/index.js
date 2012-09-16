var sqlite3 = require('sqlite3').verbose();
var db = new sqlite3.Database('public/files/wales_health_data.sqlite');
/*
 * GET home page.
 */

exports.index = function(req, res){
  res.render('index', { title: 'Hospitales' });
};	  

exports.get = function(req, res) {
      console.log(req.params.value);
      var value = req.params.value;
      var result = new Array();
	    var i = 0;
      var query = "";
      switch(value) {
        case("avg_stay"):
          query = "SELECT lhb, total FROM avg_len_stay;";
          break;
        case("wait_time_4"):
          query = "SELECT lhb, all_lt_4_hrs_pc AS total FROM A_and_E_times_10_11;";
          break;
        case("wait_time_8"):
          query = "SELECT lhb, all_lt_8_hrs_pc AS total FROM A_and_E_times_10_11;";
          break;
        case("bed_avail"):
          query = "Select lhb, total from bed_avail;";
          break;
        case("bed_occ"):
          query = "SELECT lhb, total from bed_occ;";
          break;
        default:
          query = "";
          break;
      }
      if(query) {
        db.serialize(function() {
          db.each(query, function(err, row) {
            if(!err) {
              result[i] = row;
              i++;
            }else
              console.log(err);
          }, function() {
            var results = "{ \"lhbs\": " + JSON.stringify(result) + "}";
            res.writeHead(200, {'content-type': 'text/json' });
            res.write(results);
            res.end('\n');  
          });
        });
      }
}