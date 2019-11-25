from NeuralNetUtil import buildExamplesFromCarData, buildExamplesFromPenData
from NeuralNet import buildNeuralNet
import cPickle
from math import pow, sqrt


def average(argList):
    return sum(argList)/float(len(argList))


def stDeviation(argList):
    mean = average(argList)
    diffSq = [pow((val-mean), 2) for val in argList]
    return sqrt(sum(diffSq)/len(argList))


penData = buildExamplesFromPenData()


def testPenData(hiddenLayers=[24]):
    return buildNeuralNet(penData, maxItr=200, hiddenLayerList=hiddenLayers)


carData = buildExamplesFromCarData()


def testCarData(hiddenLayers=[16]):
    return buildNeuralNet(carData, maxItr=200, hiddenLayerList=hiddenLayers)


accuracyListPen = []
# for i in range(0,5):
# 	nnet, accuracy = testPenData()
# 	accuracyListPen.append(accuracy)

accuracyListCar = []
# for j in range(0, 5):
# 	nnet, accuracy = testCarData()
# 	accuracyListCar.append(accuracy)

# print "-------------Pen--------------"
# print "Max: %.5f | Average: %.5f | StDev: %.5f" % (max(accuracyListPen), average(accuracyListPen), stDeviation(accuracyListPen))
# print "-------------Car--------------"
# print "Max: %.5f | Average: %.5f | StDev: %.5f" % (max(accuracyListCar), average(accuracyListCar), stDeviation(accuracyListCar))


print "=============VARYING THE NUMBER OF HIDDEN LAYERS============="
penParams = [[0 for x in range(9)] for y in range(3)]
carParams = [[0 for x in range(9)] for y in range(3)]
for i in range(0, 41, 5):
    print "*Number of hidden layers: %d*" % (i)

    for j in range(0, 5):
        nnet, accuracy = testPenData([i])
        accuracyListPen.append(accuracy)

    # Pen Data: [[max, avg, stDev]]
    penParams[0][int(i / 5)] = max(accuracyListPen)
    penParams[1][int(i / 5)] = average(accuracyListPen)
    penParams[2][int(i / 5)] = stDeviation(accuracyListPen)

    accuracyListCar = []
    for k in range(0, 5):
        nnet, accuracy = testCarData([i])
        accuracyListCar.append(accuracy)

    # Car Data: [[max, avg, stDev]]
    carParams[0][int(i / 5)] = max(accuracyListCar)
    carParams[1][int(i / 5)] = average(accuracyListCar)
    carParams[2][int(i / 5)] = stDeviation(accuracyListCar)
print "=============TEST RESULTS============="
for i in range(0, 9):
    print "Test #%d: %d hidden layers" % (i, i*5)
    for j in range(0, 3):
        if j == 0:
            print "Max:   Pen = %.6f, Car = %.6f" % (penParams[j][i], carParams[j][i])
        elif j == 1:
            print "Mean:  Pen = %.6f, Car = %.6f" % (penParams[j][i], carParams[j][i])
        else:
            print "StDev: Pen = %.6f, Car = %.6f" % (penParams[j][i], carParams[j][i])
