#
#Piper Arnold
#CSCI 102- A
#Week 12

def PrintOutput(text):
    print("OUTPUT", text)
    return

def LoadFile(file_name):
    file = open(file_name, 'r')
    lines = file.readlines()
    contents = []
    for line in lines:
        contents.append(line.strip())
    return PrintOutput(contents)

def UpdateString(str_one, str_two, index):
    list_one = []
    for i in str_one:
        list_one.append(i)
    list_one[index] = str_two
    output = ''
    for j in list_one:
        output += j
    return PrintOutput(output)

def FinalWordCount(list_thing, string):
    occur = 0
    for i in list_thing:
        if i.find(string) > -1:
            occur += 1
    return PrintOutput(occur)

def ScoreFinder(list_names, list_scores, player):
    low_names = []
    for i in list_names:
        low_names.append(i.lower())
    player = player.lower()
    index = -1
    for j in range(len(low_names)):
        if low_names[j] == player:
            index = j
    if index > -1:
        outputname = list_names[index]
        outputscore = list_scores[index]
        out = outputname + ' ' + "got a score of" + ' ' + str(outputscore)
    else:
        out = "player not found"
    return PrintOutput(out)

def Union(list_one, list_two):
    union = list_one
    for i in list_two:
        if i not in union:
            union.append(i)
    return PrintOutput(union)
