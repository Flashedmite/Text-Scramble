import random

inputText = open("py.txt", 'r', encoding='utf-8')
outputText = open("outputtext.txt", 'w',encoding='utf-8')

linesList = inputText.readlines()

for line in linesList:
    result = line.split()
    random.shuffle(result)
    result = " / ".join(result)
    print(result)
    outputText.write(result + "\n")

inputText.close()
outputText.close()
