var page;
var pageCount = 0;

scanPage(pageCount);

function scanPage(pageIndex) {
 // dispose of page before moving on
 if (typeof page !== 'undefined')
{
  page.release();
}
 // dispose of phantomjs if we're done
if (pageIndex > 0) {
  phantom.exit();
  return;
 }
 pageIndex++;
 
 // start crawling...
 page = require('webpage').create();
 var currentPage = 'http://localhost:8888/index.html';
 page.viewportSize = { width: 1920, height: 500};
 page.open(currentPage, function(status) {
  if (status === 'success') {
	    
	  var title =new Date();
     var day=title.getDate();
    var hour=title.getHours();
	var min=title.getMinutes();
	var yr=title.getFullYear();
	var mn=title.getMonth();
	 page.clipRect = { left:500, top: 0, width: 1200, height: 1000 };
	page.zoomFactor = 1.0;
	console.log("DATE="+day+"-"+mn+"-"+yr+" TIME="+hour+"-"+min+'.jpeg');
   window.setTimeout(function() {
  page.render("DATE="+day+"-"+mn+"-"+yr+" TIME="+hour+"-"+min+'.jpeg', {format: 'jpeg', quality: '100'});
      phantom.exit();
   },1000);

  


  }
  else {
   console.log('error crawling page ' + pageIndex);
   page.release();
  }
 });
}

// checks for interesting keywords in the book title,
// and saves the link for us if necessary

