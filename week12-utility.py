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

