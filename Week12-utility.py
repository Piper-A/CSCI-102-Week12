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
