import pandas as pd
import numpy as np
import sys


def validate_data(input_file, weights, impacts):
    """
    Validate the input data.

    Parameters:
        input_file (str): The input file path.
        weights (list): The weight vector for the criteria.
        impact (list): The impact vector for the criteria.

    Returns:
        np.ndarray: The decision matrix.
    """

    # Read the input file
    try:
        matrix = pd.read_csv(input_file)
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


def topsis(matrix, weights, impact):
    """
    Implement the TOPSIS method for multi-criteria decision making.

    Parameters:
        matrix (np.ndarray): The decision matrix.
        weights (np.ndarray): The weight vector for the criteria.
        impact (np.ndarray): The impact vector for the criteria.

    Returns:
        np.ndarray: The result vector.
    """

    raw_matrix = matrix.drop(matrix.columns[0], axis=1)

    # Convert impact to 1 or -1
    impact = np.where(impact == "+", 1, -1)

    # Normalize the decision matrix
    raw_matrix = raw_matrix / np.sqrt(np.sum(raw_matrix**2, axis=0))

    # Calculate the weighted decision matrix
    weighted_matrix = raw_matrix * weights

    # Calculate the ideal and negative-ideal solutions after multiplying with the impact vector
    ideal_best = np.amax(weighted_matrix * impact, axis=0).abs()
    ideal_worst = np.amin(weighted_matrix * impact, axis=0).abs()

    # Calculate euclidean distance from ideal best and ideal worst
    Si_best = np.sqrt(np.sum((weighted_matrix - ideal_best) ** 2, axis=1))
    Si_worst = np.sqrt(np.sum((weighted_matrix - ideal_worst) ** 2, axis=1))

    # Calculate performance score
    performance_score = Si_worst / (Si_best + Si_worst)

    # Calculate rank in descending order
    rank = performance_score.rank(ascending=False).astype(int)

    # Add performance score and rank to the decision matrix
    matrix["Performance Score"] = performance_score
    matrix["Rank"] = rank

    return matrix

def start():
    """
    Main function.
    """
    if len(sys.argv) != 5:
        print("Error: Invalid number of arguments")
        sys.exit(1)

    # Get the input file path, weights and impacts from the command line
    input_file = sys.argv[1]
    weights = sys.argv[2].split(",")
    impacts = sys.argv[3].split(",")
    output_file = sys.argv[4]

    # Validate the input data
    matrix, weights, impacts = validate_data(input_file, weights, impacts)

    # Implement the TOPSIS method
    result = topsis(matrix, weights, impacts)

    # Save the result to the output file
    result.to_csv(output_file, index=False)

    print("Output saved to", output_file)

if __name__ == "__main__":
    start()
