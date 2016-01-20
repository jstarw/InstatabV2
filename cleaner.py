import json

#make a unique bag of tags

with open('data.json', 'w') as tags:
	tagMatrix = []
	for line in open('data.csv'):
		if (line == '\n'): continue
		line = line.rstrip()
		tagList = line[0:len(line)-1].split(',')
		tagMatrix.append(tagList)

	json.dump(tagMatrix, tags)

def removeDuplicates(tags):
	return list(set(tags))