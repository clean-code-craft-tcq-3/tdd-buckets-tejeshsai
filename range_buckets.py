from range import Range


def isConsecutive(number1, number2):
    difference = number2 - number1
    return (difference == 0 or difference == 1)


def getRangeDetails(rangeArray):
    rangeRecords = []
    numberOfConsecutiveNumbers = 1
    rangeFirstNumber = rangeArray[0]
    rangeEndNumber = rangeArray[0]

    rangeArray.sort()

    for index in range(0, len(rangeArray)-1):
        if(isConsecutive(rangeArray[index], rangeArray[index+1])):
            numberOfConsecutiveNumbers += 1
            rangeEndNumber = rangeArray[index+1]
        else:
            newRangeRecord = Range(
                rangeFirstNumber, rangeEndNumber, numberOfConsecutiveNumbers)
            rangeRecords.append(newRangeRecord)
            numberOfConsecutiveNumbers = 1
            rangeFirstNumber = rangeArray[index+1]
            rangeEndNumber = rangeArray[index+1]

    newRangeRecord = Range(
        rangeFirstNumber, rangeEndNumber, numberOfConsecutiveNumbers)
    rangeRecords.append(newRangeRecord)
    return len(rangeRecords)


def printRangeDetails(rangeArray):
    pass
