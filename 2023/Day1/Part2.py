
fullText = """two1nine"""

textSplit = fullText.split("\n");

answer = 0;


def changeTextToNumber(checkText, number, text):
    if text.count(checkText) > 0:
        text = text.replace(checkText, str(number))

    return text

def checkPos(text):
    firstNumberPos = ["none", 0];
    firstNumberPos = firstIndex(text, "one", firstNumberPos)
    firstNumberPos = firstIndex(text, "two", firstNumberPos)
    firstNumberPos = firstIndex(text, "three", firstNumberPos)
    firstNumberPos = firstIndex(text, "four", firstNumberPos)
    firstNumberPos = firstIndex(text, "five", firstNumberPos)
    firstNumberPos = firstIndex(text, "six", firstNumberPos)
    firstNumberPos = firstIndex(text, "seven", firstNumberPos)
    firstNumberPos = firstIndex(text, "eight", firstNumberPos)
    firstNumberPos = firstIndex(text, "nine", firstNumberPos)
        
def firstIndex(text, number, numberPos):
    if text.count(number) > 0:
        if (text.index(number) < numberPos[1]):
            pos = text.index(number);
            numberPos = [number, pos]
    return numberPos
    
def lastIndex(text, number, numberPos):
    if text.count(number) > 0:
        if (text.index(number) > numberPos[1]):
            pos = text.index(number);
            numberPos = [number, pos]
    return numberPos


for text in textSplit:
    print(text);

    firstNumberPos = ["none", 0];
    lastNumberPos = ["none", 0];

    firstNumberPos = firstIndex(text, "one", firstNumberPos)
    firstNumberPos = firstIndex(text, "two", firstNumberPos)
    firstNumberPos = firstIndex(text, "three", firstNumberPos)
    firstNumberPos = firstIndex(text, "four", firstNumberPos)
    firstNumberPos = firstIndex(text, "five", firstNumberPos)
    firstNumberPos = firstIndex(text, "six", firstNumberPos)
    firstNumberPos = firstIndex(text, "seven", firstNumberPos)
    firstNumberPos = firstIndex(text, "eight", firstNumberPos)
    firstNumberPos = firstIndex(text, "nine", firstNumberPos)

    lastNumberPos = lastIndex(text, "one", lastNumberPos)
    lastNumberPos = lastIndex(text, "two", lastNumberPos)
    lastNumberPos = lastIndex(text, "three", lastNumberPos)
    lastNumberPos = lastIndex(text, "four", lastNumberPos)
    lastNumberPos = lastIndex(text, "five", lastNumberPos)
    lastNumberPos = lastIndex(text, "six", lastNumberPos)
    lastNumberPos = lastIndex(text, "seven", lastNumberPos)
    lastNumberPos = lastIndex(text, "eight", lastNumberPos)
    lastNumberPos = lastIndex(text, "nine", lastNumberPos)

    text = changeTextToNumber(firstNumberPos[0], firstNumberPos[1], text);
    text = changeTextToNumber(lastNumberPos[0], lastNumberPos[1], text);

    print("--------");
    print(text);
    
    textSize = len(text);
    pos = textSize - 1;

    firstNumber = 0;
    secondNumber = 0;

    for x in text:
        if x.isdigit():
            firstNumber = x
            break;

    for x in text:
        if text[pos].isdigit():
            secondNumber = text[pos];
            break;
        pos = pos - 1;

    fullNumber = firstNumber + secondNumber;
    print(fullNumber);
    answer += int(fullNumber);

print(answer);