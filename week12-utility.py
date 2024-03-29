# Kassidy Sharits
# CSCI 102 - Section B
# Week 12
# https://github.com/kassidysharits/week12-csci102

def PrintOutput(output):
    print('OUTPUT ' + output)

def LoadFile(filename):
    file = open(filename, 'r+')
    contents = file.read()
    lines = contents.splitlines()
    return lines

def UpdateString(string1, string2, index):
    string3 = ''
    for x in range (len(string1)):
        if x == index:
            string3 += string2
        else:
            string3 += string1[x]
    return string3

def FindWordCount(lists,word):
    string1 = ""
    count = 0
    for x in range(len(lists)):
        string1 += lists[x]
        string1 += ' '
    lists = string1.split()
    for x in range(len(lists)):
        if lists[x] == word:
            count += 1
    return count

def ScoreFinder(players, scores, name):
    for x in range(len(players)):
        if players[x] == name:
            return (players[x] + ' got a score of ' + str(scores[x]))
    return "player not found"

def Union(list1, list2):
    for x in range(len(list2)):
        list1.append(list2[x])
    lenlist = len(list1)
    x = 0
    while(lenlist != x+1):
        if list1.count(list1[x]) > 1:
            list1.pop(x)
            lenlist -= 1
            x -= 1
        x +=1
    return list1

def Intersection(list1, list2):
    list3 = []
    for x in range(len(list1)):
        for y in range(len(list2)):
            if list1[x] == list2[y]:
                list3.append(list1[x])
    return list3

def NotIn(list1, list2):
    list3 = []
    count = 0
    for x in range(len(list1)):
        count = 0
        for y in range(len(list2)):
            if list1[x] == list2[y]:
                break
            count += 1
            if count == len(list1):
                list3.append(list1[x])
            
            
    return list3



