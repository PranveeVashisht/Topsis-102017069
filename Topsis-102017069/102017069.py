import pandas as pd
import numpy as np
import sys
import os


def error_handling(data, weights, impacts):
    # Read the input file
    try:
        matrix = pd.read_csv(data)
    except:
        print("Error: Invalid input file")
        sys.exit(1)

    # Input file must have at least 3 columns
    if matrix.shape[1] < 3:
        print("Error: Invalid input file, must have at least 3 columns")
        sys.exit(1)

    # Check if weights and impacts are valid
    try:
        weights = np.array(weights, dtype=float)
        impacts = np.array(impacts)
    except Exception as e:
        print(e)
        print("Error: Invalid weights or impacts")
        sys.exit(1)

    # Check for correct number of weights and impacts and if they're separated by commas
    try:
        if len(weights) != matrix.shape[1] - 1 or len(impacts) != matrix.shape[1] - 1:
            print("Error: Invalid number of weights or impacts")
            sys.exit(1)
    except:
        print("Error: Invalid weights or impacts, must be separated by commas")
        sys.exit(1)

    # from 2nd column onwards, all columns must be numeric
    for col in matrix.columns[1:]:
        if not pd.api.types.is_numeric_dtype(matrix[col]):
            print("Error: Invalid input file, all columns must be numeric")
            sys.exit(1)

    # Impacts must be either + or -
    if not all([impact in ["+", "-"] for impact in impacts]):
        print("Error: Invalid impacts, must be either + or -")
        sys.exit(1)

    # Weights must be positive
    if not all([weight > 0 for weight in weights]):
        print("Error: Invalid weights, must be positive")
        sys.exit(1)

    return matrix, weights, impacts

#Function to find topsis score and rank
def topsis(matrix, weights, impact):

    raw_matrix = matrix.drop(matrix.columns[0], axis=1)

    # Convert impacts to 1 or -1
    impact = np.where(impact == "+", 1, -1)

    # Vector Normalization
    raw_matrix = raw_matrix / np.sqrt(np.sum(raw_matrix**2, axis=0))

    # Calculate the weighted decision matrix
    weighted_matrix = raw_matrix * weights

    # Calculating ideal best and ideal worst values
    ideal_best = np.amax(weighted_matrix * impact, axis=0).abs()
    ideal_worst = np.amin(weighted_matrix * impact, axis=0).abs()

    # Calculating euclidean distance from ideal best and ideal worst
    Si_best = np.sqrt(np.sum((weighted_matrix - ideal_best) ** 2, axis=1))
    Si_worst = np.sqrt(np.sum((weighted_matrix - ideal_worst) ** 2, axis=1))

    # Calculating performance score
    performance_score = Si_worst / (Si_best + Si_worst)

    # Calculating rank in descending order
    rank = performance_score.rank(ascending=False).astype(int)


    matrix["Performance Score"] = performance_score
    matrix["Rank"] = rank

    return matrix

def start():
    if len(sys.argv) != 5:
        print("Error: Invalid number of arguments")
        sys.exit(1)

    # Get the input file path, weights and impacts from the command line
    data= sys.argv[1]
    weights= sys.argv[2]
    impacts= sys.argv[3]
    result= sys.argv[4]

   #Error handling
    matrix, weights, impacts = error_handling(data, weights, impacts)

    # Implement the TOPSIS method
    result = topsis(matrix, weights, impacts)

    # Save the result to the output file
    result.to_csv(result, index=False)

    print("Output saved to", result)

if __name__ == "__main__":
    start()
