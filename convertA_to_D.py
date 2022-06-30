def convertAmpsToDigital(reading):
    ampere_value = 10*(float(reading/4094))
    return round(ampere_value)


def convertAmpsListToDigital(array):
    digitalValuesList = []

    for reading in array:
        ampere_value = convertAmpsToDigital(reading)
        if(ampere_value > 1 and ampere_value < 4095):
            digitalValuesList.append(ampere_value)

    return digitalValuesList
