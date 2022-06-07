from range import Range

rangeRecords = []


def getRangeDetails(rangeArray):
    numberOfRanges = 0
    numberOfConsecutiveNumbers = 1
    rangeFirstNumber = rangeArray[0]
    rangeEndNumber = rangeArray[0]

    for index in range(0, len(rangeArray)-1):
        if(rangeArray[index+1]-rangeArray[index] == 0 or rangeArray[index+1]-rangeArray[index] == 1):
            numberOfConsecutiveNumbers += 1
            rangeEndNumber = rangeArray[index+1]
        else:
            newRangeRecord = Range(
                rangeFirstNumber, rangeEndNumber, numberOfConsecutiveNumbers)
            rangeRecords.append(newRangeRecord)
            numberOfRanges += 1
            numberOfConsecutiveNumbers = 1
            rangeFirstNumber = rangeArray[index+1]
            rangeEndNumber = rangeArray[index+1]

    newRangeRecord = Range(
        rangeFirstNumber, rangeEndNumber, numberOfConsecutiveNumbers)
    rangeRecords.append(newRangeRecord)
    return len(rangeRecords)
