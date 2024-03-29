from range import Range
from convertA_to_D import convertAmpsListToDigital, convertAmpsToDigital

rangeRecords = []


def isConsecutive(number1, number2):
    difference = number2 - number1
    return (difference == 0 or difference == 1)


def getRangeDetails(rangeArray):
    global rangeRecords
    rangeRecords = []
    numberOfConsecutiveNumbers = 1

    rangeArray.sort()

    rangeFirstNumber = rangeArray[0]
    rangeEndNumber = rangeArray[0]

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
    numberOfRanges = getRangeDetails(rangeArray)
    print("Range", "Details")
    for rangeItem in rangeRecords:
        print(rangeItem.firstNumber, "-", rangeItem.endNumber,
              ", ", rangeItem.noOfReadings)
    return numberOfRanges


def getRangesForAmpsLists(AmpsArray):
    digitalValuesList = convertAmpsListToDigital(AmpsArray)
    return getRangeDetails(digitalValuesList)
