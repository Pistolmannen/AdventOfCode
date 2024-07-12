
with open("2023\Day1\Day1-Input.txt") as file:
    fullText = file.read()

textSplit = fullText.split("\n");

answer = 0;

for text in textSplit:
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
        pos -= 1;

    fullNumber = firstNumber + secondNumber;
    print(fullNumber);
    answer += int(fullNumber);

print(answer);






