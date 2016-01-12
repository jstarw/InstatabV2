var initialset = 20;

var tumblr = {
	key: '8c78771934d3245c13a7ca25966549fa',
	secret: '17e2425c2d5ec462',
	baseUrl: 'https://api.flickr.com/services/rest/?',

	init: function() {
		var method = 'flickr.interestingness.getList';

		$.get(this.baseUrl, 
			{
				method: method,
				api_key:this.key,
				per_page:initialset,
				format: 'json'	
			}
		).always(function(o) {
			console.log(o.responseText);
			tumblr.parseResponse(o.responseText);
		});
	},

	parseResponse: function(data) {
		var jsonData = data.substring(14, data.length-1);
	 	var obj = JSON.parse(jsonData);
		console.log(obj);
		this.createNode(obj);
	},

	createNode: function(obj) {
		var url = obj.photos.photo.map(this.createURL);
		var targ = $('.content');
		console.log(url);
		url.forEach(function(elem) {
			$(targ).append("<img src='" + elem + "'>");
		});
	},

	createURL: function(elem) {
		var url = 'https://farm' + elem.farm + '.staticflickr.com/'
				+ elem.server + '/' + elem.id + '_' + elem.secret
				+ '.jpg';
		return url;
	}
};



$(document).ready(function() {
	tumblr.init();
});

