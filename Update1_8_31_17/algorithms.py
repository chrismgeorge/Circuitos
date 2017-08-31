def parAdd(numbers):
    total = 0
    for i in numbers:
        total += 1/i
    return total**-1 if total != 0 else 0

def totalResistanceSolver(infiniteList, series = True): #calculates resis. of circuit
    currentAddition = []
    for elements in infiniteList:
        if not isinstance(elements, list):
            currentAddition.append(elements)
        else:
            series = not series
            currentAddition.append(totalResistanceSolver(elements, series))
            series = not series
    if series:
        return sum(currentAddition)
    else:
        return parAdd(currentAddition)


def solveResistorCircuit(infiniteList, PD, current, series = True):
    for elements in infiniteList:
        if series:
            if isinstance(elements, list): #series to parallel
                totalResistance = totalResistanceSolver(elements, False) #find total resistance of list, false means parallel
                newPD = current * totalResistance #V = IR, current doesnt change
                solveResistorCircuit(elements, newPD, current, False)
            else:
                PDAcrossResistor = elements * current #using current and resistor find pd #do i need to change this then?
                resistorsPDandCurrents.append([elements, current, PDAcrossResistor])
        else: #if parallel
            if isinstance(elements, list): #parrallel to series
                totalResistance = totalResistanceSolver(elements, True) #true means series
                newCurrent = PD / totalResistance
                solveResistorCircuit(elements, PD, newCurrent, True)
            else:
                currentAcrossResistor = PD / elements
                resistorsPDandCurrents.append([elements, currentAcrossResistor, PD])
    return 42 #unneccesary yet completely practicle

resistorsPDandCurrents = []
totalPD = 16
circuit = [6, [4,[2,2]]]
totalR = totalResistanceSolver(circuit)
totalCurrent = totalPD / totalR
solveResistorCircuit(circuit, totalPD, totalCurrent, True)

for index, things in enumerate(resistorsPDandCurrents):
    resistor = things[0]
    current = things[1]
    pd = things[2]
    print(resistor, current, pd)

