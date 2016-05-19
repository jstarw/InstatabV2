import json
from collections import defaultdict

FILENAME = "data.json"

#make a unique bag of tags
def addToJson(): 
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

def makeBag(bag):
    bag_of_tags = []

    for row in bag: 
        for word in row:
            bag_of_tags.append(word)

    bag_of_tags = list(set(bag_of_tags))
    return bag_of_tags


if __name__ == "__main__":
    bag = []

    with open (FILENAME, 'r') as f:
        for row in f:
            bag.append(json.loads(row))

    bag = bag[0] #some reason bag is a list(list())
    bag_of_tags = makeBag(bag)
    
    # for each image, create array with length of bag_of_tags
    bagLength = len(bag_of_tags)
    feature_matrix = [[]]
    for img_tags in bag: 
        arr = [None] * bagLength;
        word_count = defaultdict(int)
        for tag in img_tags:
            word_count[tag] += 1
        for i, word in enumerate(bag_of_tags):
            print i
            if word_count[word] > 0:
                arr[i] =  word_count[word]

        feature_matrix.append(arr)

    #feature_matrix = feature_matrix[1:]
    print feature_matrix

