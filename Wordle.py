import re

FiveLetterArray = []
with open('Words.txt', 'r') as file:
    FiveLetterArray = [line.rstrip() for line in file]


gameGoing = True
print('')
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

alphabetCount = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0
]

firstLetter = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0
]

secondLetter = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0
]

thirdLetter = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0
]

forthLetter = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0
]

fifthLetter = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0
]


def hasDoubleLetter(word):
    double = False
    for i in range(len(word)):
        if (len(re.findall(word[i], word)) >= 2):
            double = True

    return double


def getLetterStats(Print, guessReveal):
    alphabet = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]

    alphabetCount = [
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0
    ]

    firstLetter = [
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0
    ]

    secondLetter = [
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0
    ]

    thirdLetter = [
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0
    ]

    forthLetter = [
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0
    ]

    fifthLetter = [
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0
    ]

    for i in range(len(FiveLetterArray)):
        for j in range(len(FiveLetterArray[i])):
            for k in range(len(alphabet)):
                if FiveLetterArray[i][j] == alphabet[k]:
                    alphabetCount[k] += 1
                    if j == 0:
                        firstLetter[k] += 1
                    elif j == 1:
                        secondLetter[k] += 1
                    elif j == 2:
                        thirdLetter[k] += 1
                    elif j == 3:
                        forthLetter[k] += 1
                    elif j == 4:
                        fifthLetter[k] += 1

    alphabetMax = []
    for i in range(len(alphabetCount)):
        alphabetMax.append(alphabetCount[i])
    #firstMax = firstLetter
    alphabetMax.sort(reverse=True)

    firstMax = []
    for i in range(len(firstLetter)):
        firstMax.append(firstLetter[i])
    #firstMax = firstLetter
    firstMax.sort(reverse=True)

    secondMax = []
    for i in range(len(secondLetter)):
        secondMax.append(secondLetter[i])
    #secondMax = secondLetter
    secondMax.sort(reverse=True)

    thirdMax = []
    for i in range(len(thirdLetter)):
        thirdMax.append(thirdLetter[i])
    #thirdMax = thirdLetter
    thirdMax.sort(reverse=True)

    forthMax = []
    for i in range(len(forthLetter)):
        forthMax.append(forthLetter[i])
    #forthMax = forthLetter
    forthMax.sort(reverse=True)

    fifthMax = []
    for i in range(len(fifthLetter)):
        fifthMax.append(fifthLetter[i])
    #fifthMax = fifthLetter
    fifthMax.sort(reverse=True)

    goodGuessesLetter = []
    goodGuessesAlphabet = []
    goodGuessesMixed = []

    if (guessReveal == 'y'):
        for first in range(4):
            for second in range(4):
                for third in range(4):
                    for forth in range(4):
                        for fifth in range(4):
                            wordSum = 0

                            if (firstMax[first] != 0):
                                letter1 = alphabet[firstLetter.index(
                                    firstMax[first])]
                                wordSum += firstMax[first]
                            elif (firstMax[first] == 0):
                                letter1 = alphabet[firstLetter.index(
                                    firstMax[0])]
                                wordSum += firstMax[0]

                            if (secondMax[second] != 0):
                                letter2 = alphabet[secondLetter.index(
                                    secondMax[second])]
                                wordSum += secondMax[second]
                            elif (secondMax[second] == 0):
                                letter2 = alphabet[secondLetter.index(
                                    secondMax[0])]
                                wordSum += secondMax[0]

                            if (thirdMax[third] != 0):
                                letter3 = alphabet[thirdLetter.index(
                                    thirdMax[third])]
                                wordSum += thirdMax[third]
                            elif (thirdMax[third] == 0):
                                letter3 = alphabet[thirdLetter.index(
                                    thirdMax[0])]
                                wordSum += thirdMax[0]

                            if (forthMax[forth] != 0):
                                letter4 = alphabet[forthLetter.index(
                                    forthMax[forth])]
                                wordSum += forthMax[forth]
                            elif (forthMax[forth] == 0):
                                letter4 = alphabet[forthLetter.index(
                                    forthMax[0])]
                                wordSum += forthMax[0]

                            if (fifthMax[fifth] != 0):
                                letter5 = alphabet[fifthLetter.index(
                                    fifthMax[fifth])]
                                wordSum += fifthMax[fifth]
                            elif (fifthMax[fifth] == 0):
                                letter5 = alphabet[fifthLetter.index(
                                    fifthMax[0])]
                                wordSum += fifthMax[0]

                            word = letter1 + letter2 + letter3 + letter4 + letter5

                            if (word in FiveLetterArray and [wordSum, word]
                                    not in goodGuessesLetter):
                                goodGuessesLetter.append([wordSum, word])

        for first in range(8):
            for second in range(8):
                for third in range(8):
                    for forth in range(8):
                        for fifth in range(8):
                            wordSum = 0

                            letter1 = alphabet[alphabetCount.index(
                                alphabetMax[first])]
                            wordSum += alphabetMax[first]

                            letter2 = alphabet[alphabetCount.index(
                                alphabetMax[second])]
                            wordSum += alphabetMax[second]

                            letter3 = alphabet[alphabetCount.index(
                                alphabetMax[third])]
                            wordSum += alphabetMax[third]

                            letter4 = alphabet[alphabetCount.index(
                                alphabetMax[forth])]
                            wordSum += alphabetMax[forth]

                            letter5 = alphabet[alphabetCount.index(
                                alphabetMax[fifth])]
                            wordSum += alphabetMax[fifth]

                            word = letter1 + letter2 + letter3 + letter4 + letter5

                            if (word in FiveLetterArray and [wordSum, word]
                                    not in goodGuessesAlphabet):
                                if (not hasDoubleLetter(word)):
                                    goodGuessesAlphabet.append([wordSum, word])

    for i in range(len(goodGuessesLetter)):
        for j in range(len(goodGuessesAlphabet)):
            if (goodGuessesAlphabet[j][1] == goodGuessesLetter[i][1]
                    and goodGuessesAlphabet[j] not in goodGuessesMixed):
                goodGuessesMixed.append(goodGuessesAlphabet[j])

    if (Print == 'y'):
      print("\n")
      print(alphabetCount)
      print("\n")
      print(firstLetter)
      print("\n")
      print(secondLetter)
      print("\n")
      print(thirdLetter)
      print("\n")
      print(forthLetter)
      print("\n")
      print(fifthLetter)
      print("\n")
      
    print("number of options left: " + str(len(FiveLetterArray)))
    if len(FiveLetterArray) == 12946:
        print('Use the word SOARE.')
    print("\n")

    if (len(FiveLetterArray) <= 50):
        print(FiveLetterArray)
        print("\n")

    if (guessReveal == 'y'):
        if (len(FiveLetterArray) == 1):
            print("The word is " + str(goodGuessesLetter))
        elif (len(goodGuessesMixed) > 0):
            goodGuessesMixed.sort(reverse=True)
            print("The best guesses are going to be " + str(goodGuessesMixed) +
                  "\n")
        elif (len(FiveLetterArray) >= 50 and len(goodGuessesAlphabet) > 0):
            goodGuessesAlphabet.sort(reverse=True)
            print("some good guesses might be " + str(goodGuessesAlphabet) +
                  "\n")

        elif (len(FiveLetterArray) < 50 and len(goodGuessesLetter) > 0):
            goodGuessesLetter.sort(reverse=True)
            print("some good guesses that might be right are " +
                  str(goodGuessesLetter) + "\n")
        else:
            print("some good guesses that might be right are " +
                  str(goodGuessesLetter) + "\n")
            print("some good guesses might be " + str(goodGuessesAlphabet) +
                  "\n")
            print("The best guesses are going to be " + str(goodGuessesMixed) +
                  "\n")

    goodGuessesLetter = []


getLetterStats('n', 'n')

while (gameGoing):
    word = input("What word did you put in?\n")
    print("\n")

    # green = input(
    #     "Which letters were in the correct spot? (Type each letter followed by a space  or type _ for nothing)\n"
    # )
    green = input(' Which letters were green? ')

    # yellow = input(
    #     "Which letters were correct but in the wrong spot? (type each letter followed by a space or type _ for nothing)a\n"
    # )
    yellow = input('Which letters were yellow? ')

    # red = input(
    #     "Which letters were not in the word(Type each separated by a space  or type _ for nothing)\n"
    # )

    red = input('Which letters were gray? ')

    word = word.lower()
    green = green.lower()
    yellow = yellow.lower()
    red = red.lower()

    yellowArray = re.split("\s", yellow)
    greenArray = re.split("\s", green)
    redArray = re.split("\s", red)

    keep = []
    if (len(greenArray) != 0 and '_' not in greenArray):
        for i in range(len(FiveLetterArray)):
            wordIn = True
            for j in range(len(greenArray)):
                greenIndex = word.find(greenArray[j])
                if (greenArray[j] != FiveLetterArray[i][greenIndex]):
                    wordIn = False

            if (wordIn):
                keep.append(FiveLetterArray[i])

        count = 0
        while (count < len(FiveLetterArray)):
            if (FiveLetterArray[count] not in keep):
                if (FiveLetterArray[count] in FiveLetterArray):
                    FiveLetterArray.remove(FiveLetterArray[count])
                    count -= 1
            count += 1

    keep = []
    if (len(yellowArray) != 0 and '_' not in yellowArray):
        for i in range(len(FiveLetterArray)):
            wordIn = True
            for j in range(len(yellowArray)):
                if (yellowArray[j] not in FiveLetterArray[i]):
                    wordIn = False
                yellowIndex = word.find(yellowArray[j])
                if (yellowArray[j] == FiveLetterArray[i][yellowIndex]):
                    wordIn = False

            if (wordIn):
                keep.append(FiveLetterArray[i])

        count = 0
        while (count < len(FiveLetterArray)):
            if (FiveLetterArray[count] not in keep):
                if (FiveLetterArray[count] in FiveLetterArray):
                    FiveLetterArray.remove(FiveLetterArray[count])
                    count -= 1
            count += 1

    keep = []
    if (len(redArray) != 0 and '_' not in redArray):
        for j in range(len(FiveLetterArray)):
            wordIn = True
            for i in range(len(redArray)):
                if (redArray[i] in FiveLetterArray[j]):
                    wordIn = False
            if (wordIn):
                keep.append(FiveLetterArray[j])

        count = 0
        while (count < len(FiveLetterArray)):
            if (FiveLetterArray[count] not in keep):
                if (FiveLetterArray[count] in FiveLetterArray):
                    FiveLetterArray.remove(FiveLetterArray[count])
                    count -= 1
            count += 1

    if (word in FiveLetterArray):
        FiveLetterArray.remove(word)

    getLetterStats('n', 'y')

    if (len(FiveLetterArray) <= 1):
        gameGoing = False
        