
with open("2023\Day1\Day1-Input.txt") as file:
    fullText = file.read()

textSplit = fullText.split("\n");

answer = 0;

        
def firstIndex(text, checkText, number, numberPos):
    if text.count(checkText) > 0:

        if (text.index(checkText) <= numberPos[2]):
            pos = text.index(checkText);
            numberPos = [checkText, number, pos];
            
    return numberPos
    
def lastIndex(text, checkText, number, numberPos):
    if text.count(checkText) > 0:
        test = text.count(checkText);
        start = 0;
        truePos = 0;
        while test > 0:
            truePos = text.index(checkText, start)

            start = truePos + 1;
            test -= 1;
            
        if (truePos > numberPos[2]):
            numberPos = [checkText, number, truePos];
    return numberPos


for text in textSplit:

    print("--------");
    print(text);

    firstNumberPos = ["none", 0, 1000];
    lastNumberPos = ["none", 0, 0];

    firstNumberPos = firstIndex(text, "one", 1, firstNumberPos)
    firstNumberPos = firstIndex(text, "two", 2, firstNumberPos)
    firstNumberPos = firstIndex(text, "three", 3, firstNumberPos)
    firstNumberPos = firstIndex(text, "four", 4, firstNumberPos)
    firstNumberPos = firstIndex(text, "five", 5, firstNumberPos)
    firstNumberPos = firstIndex(text, "six", 6, firstNumberPos)
    firstNumberPos = firstIndex(text, "seven", 7, firstNumberPos)
    firstNumberPos = firstIndex(text, "eight", 8, firstNumberPos)
    firstNumberPos = firstIndex(text, "nine", 9, firstNumberPos)

    lastNumberPos = lastIndex(text, "one", 1, lastNumberPos)
    lastNumberPos = lastIndex(text, "two", 2, lastNumberPos)
    lastNumberPos = lastIndex(text, "three", 3, lastNumberPos)
    lastNumberPos = lastIndex(text, "four", 4, lastNumberPos)
    lastNumberPos = lastIndex(text, "five", 5, lastNumberPos)
    lastNumberPos = lastIndex(text, "six", 6, lastNumberPos)
    lastNumberPos = lastIndex(text, "seven", 7, lastNumberPos)
    lastNumberPos = lastIndex(text, "eight", 8, lastNumberPos)
    lastNumberPos = lastIndex(text, "nine", 9, lastNumberPos)
    
    textSize = len(text);
    pos = 0;
    firstNumber = 0;
    secondNumber = 0;

    for x in text:
        if text[pos].isdigit():
            firstNumber = text[pos]
            if pos > firstNumberPos[2]:
                firstNumber = firstNumberPos[1];
            break;
        pos = pos + 1;
    
    pos = textSize - 1;
    
    for x in text:
        if text[pos].isdigit():
            secondNumber = text[pos];
            if pos < lastNumberPos[2]:
                secondNumber = lastNumberPos[1];
            break;
        pos = pos - 1;

    fullNumber = str(firstNumber) + str(secondNumber);
    print(fullNumber);
    answer += int(fullNumber);

print(answer);