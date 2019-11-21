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

