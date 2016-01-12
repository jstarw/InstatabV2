import urllib2
import csv
import json

key = '8c78771934d3245c13a7ca25966549fa'
secret = '17e2425c2d5ec462'
baseUrl = 'https://api.flickr.com/services/rest/?'
url = baseUrl+'&method=flickr.interestingness.getList'+'&api_key='+key+'&page=3&format=json'

def getRequest(url):
	response = urllib2.urlopen(url)
	JSONP = response.read()
	JSONP = JSONP[ JSONP.index("(") + 1 : JSONP.rindex(")") ]
	data = json.loads(JSONP)
	return data

photoSet = getRequest(baseUrl+'&method=flickr.interestingness.getList'+'&api_key='+key+'&page=3&format=json')
# print len(photoSet['photos']['photo'])
with open('data.csv', 'wb') as csvfile:
	writer = csv.writer(csvfile, delimiter=" ")

	for photo in photoSet['photos']['photo']:
		photoInfo = getRequest(baseUrl+'&method=flickr.photos.getInfo'+'&api_key='+key+'&photo_id='+photo['id']+'&format=json')
		tags = photoInfo['photo']['tags']['tag']
		tagArray = []
		for tag in tags:
			tagName = tag['_content']
			tagArray.append(tagName)
		print tagArray
		writer.writerow(tagArray)

