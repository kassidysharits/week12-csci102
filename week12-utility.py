# Kassidy Sharits
# CSCI 102 - Section B
# Week 12

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

