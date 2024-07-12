
Text = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet""";

TextSplit = Text.split("\n");

for x in TextSplit:
    print(x);

    print("-------");
    print(x[0]);
    print(x[-1]);

    print("-------");
    print(x[0] + x[-1]);






