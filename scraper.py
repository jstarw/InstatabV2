import urllib2
import csv
import json

key = '8c78771934d3245c13a7ca25966549fa'
secret = '17e2425c2d5ec462'
baseUrl = 'https://api.flickr.com/services/rest/?'
pageNumber = '4'
url = baseUrl+'&method=flickr.interestingness.getList'+'&api_key='+key+'&page='+pageNumber+'&format=json'

def getRequest(url):
	response = urllib2.urlopen(url)
	JSONP = response.read()
	JSONP = JSONP[ JSONP.index("(") + 1 : JSONP.rindex(")") ]
	data = json.loads(JSONP)
	return data

# MAIN SECTION
photoSet = getRequest(url)

csvfile =  open('data.csv', 'a')
writer = csv.writer(csvfile, delimiter=",")

index=1

for photo in photoSet['photos']['photo']:
	photoInfo = getRequest(baseUrl+'&method=flickr.photos.getInfo'+'&api_key='+key+'&photo_id='+photo['id']+'&format=json')
	tags = photoInfo['photo']['tags']['tag']
	tagArray = []
	for tag in tags:
		tagName = tag['_content']
		csvfile.write(tagName.encode("utf-8"))
		csvfile.write(",")
	csvfile.write("\n")
	print index
	index+=1
	

csvfile.close()