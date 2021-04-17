first = open("first.txt", 'r', encoding='utf-8')
second = open("second.txt", 'r', encoding='utf-8')

firstList = first.readlines()
secondList = second.readlines()

if(len(firstList) == len(secondList)):
    first.close()
    second.close()
    output = open("result.txt", 'w', encoding='utf-8')
    for i in range(0, len(firstList)):
        output.write(firstList[i])
        output.write(secondList[i] + "\n\n")
    output.close()
