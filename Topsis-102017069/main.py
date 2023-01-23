from os import path
import pandas as pd
import math
import sys


def topsis(filename, weights, impacts, resultFileName):
    # READING INPUT FILE
    dataset = pd.read_csv(filename)

    # ONLY TAKING NUMERICAL VALUES
    d = dataset.iloc[0:, 1:].values

    # CONVERTING INPUT FILE INTO A MATRIX
    mat = pd.DataFrame(d)

    if len(mat.columns) != len(weights) and len(mat.columns) != len(impacts):
        print("Error")
        exit()
    # CALCULATING ROOT OF SUM OF SQUARES
    sumOfSquares = []
    for col in range(0, len(mat.columns)):
        X = mat.iloc[0:, [col]].values
        sum = 0
        for value in X:
            sum = sum + math.pow(value, 2)
        sumOfSquares.append(math.sqrt(sum))
    # print(sumOfSquares)

    # FINDING NORMALIZED DECISION MATRIX
    j = 0
    while (j < len(mat.columns)):
        for i in range(0, len(mat)):
            mat[j][i] = mat[j][i]/sumOfSquares[j]
        j = j+1

    # FINDING WEIGHTED NORMALIZED DECISION MATRIX
    k = 0
    while (k < len(mat.columns)):
        for i in range(0, len(mat)):
            mat[k][i] = mat[k][i]*weights[k]
        k = k+1

    # CALCULATING IDEAL BEST AND IDEAL WORST
    best = []
    worst = []

    for col in range(0, len(mat.columns)):
        Y = mat.iloc[0:, [col]].values

        if impacts[col] == "+":
            maxi = max(Y)
            mini = min(Y)
            best.append(maxi[0])
            worst.append(mini[0])

        if impacts[col] == "-":
            maxi = max(Y)
            mini = min(Y)
            best.append(mini[0])
            worst.append(maxi[0])

    # CALCULATING EUCLIDEAN DISTANCE FROM IDEAL BEST AND WORST (Si+ and Si-)
    separatePlus = []
    SiMinus = []

    for row in range(0, len(mat)):
        temp = 0
        temp2 = 0
        wholeRow = mat.iloc[row, 0:].values
        for value in range(0, len(wholeRow)):
            temp = temp + (math.pow(wholeRow[value] - best[value], 2))
            temp2 = temp2 + (math.pow(wholeRow[value] - worst[value], 2))
        separatePlus.append(math.sqrt(temp))
        SiMinus.append(math.sqrt(temp2))

    # CALCULATING PERFORMANCE SCORE
    Pi = []

    for row in range(0, len(mat)):
        Pi.append(SiMinus[row]/(separatePlus[row] + SiMinus[row]))

    # FINAL RESULT
    Rank = []
    sortedPi = sorted(Pi, reverse=True)

    for row in range(0, len(mat)):
        for i in range(0, len(sortedPi)):
            if Pi[row] == sortedPi[i]:
                Rank.append(i+1)

    col1 = dataset.iloc[:, [0]].values
    mat.insert(0, dataset.columns[0], col1)
    mat['Topsis Score'] = Pi
    mat['Rank'] = Rank
    newColNames = []
    for name in dataset.columns:
        newColNames.append(name)
    newColNames.append('Topsis Score')
    newColNames.append('Rank')
    mat.columns = newColNames

    # SAVING THE MATRIX INTO A CSV FILE
    mat.to_csv(resultFileName)


def errorhandling():
    if len(sys.argv) == 5:
        # filename
        filename = sys.argv[1].lower()
        # weights
        weights = sys.argv[2].split(",")
        for i in range(0, len(weights)):
            weights[i] = int(weights[i])
        # impacts
        impacts = sys.argv[3].split(",")
        # resultFileName
        resultFileName = sys.argv[-1].lower()
        #Checking if result filename ends with .csv
        if ".csv" not in resultFileName:
            print("ERROR: Result filename should end with a  '.csv'")
            return
        #Weights and impacts
        if path.exists(filename):
            if len(weights) == len(impacts):
                topsis(filename, weights, impacts, resultFileName)
            else:
                print("ERROR: Number of weights and impacts should be equal.")
                return
        else:
            print("ERROR: Input file does not exist.")
            return
    else:
        print("ERROR: Enter the required number of arguments.")
        print("SAMPLE INPUT : python <script_name> <input_data_file_name> <weights> <impacts> <result_file_name>")
        return


# MAIN FUNCTION
errorhandling()
