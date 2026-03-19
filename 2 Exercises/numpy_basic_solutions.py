import numpy as np
import matplotlib.pyplot as plt
import os

# Ensure reports directory exists
if not os.path.exists('reports'):
    os.makedirs('reports')

# Exercise 1: 3x3 matrix with values ranging from 2 to 10
def ex1():
    return np.arange(2, 11).reshape(3, 3)

# Exercise 2: 3x5 array filled with 2
def ex2():
    return np.full((3, 5), 2)

# Exercise 3: 5x5 matrix with row values ranging from 0 to 4
def ex3():
    return np.tile(np.arange(0, 5, dtype=float), (5, 1))

# Exercise 4: Reverse an array
def ex4():
    arr = np.arange(12, 38)
    return arr[::-1]

# Exercise 5: 20 random integers between 1 and 6, filter odd
def ex5():
    arr = np.random.randint(1, 7, 20)
    odd = arr[arr % 2 != 0]
    return arr, odd

# Exercise 6: Positions where elements of a and b match
def ex6():
    a = np.array([1,2,3,2,3,4,3,4,5,6])
    b = np.array([7,2,10,2,7,4,9,4,9,8])
    return np.where(a == b)

# Exercise 7: 8x8 checkerboard pattern
def ex7():
    matrix = np.zeros((8, 8), dtype=int)
    matrix[1::2, ::2] = 1
    matrix[::2, 1::2] = 1
    return matrix

# Exercise 8: 4x4 matrix and extractions
def ex8():
    matrix = np.arange(16).reshape(4, 4)
    rows_1_4 = matrix[[0, 3], :]
    cols_1_4 = matrix[:, [0, 3]]
    inner = matrix[1:3, 1:3]
    return matrix, rows_1_4, cols_1_4, inner

# Helper function to load iris data (shared by multiple exercises)
def _load_iris(dtype=float, usecols=None, skip_header=0):
    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
    try:
        # Try local file first
        data = np.genfromtxt('files/iris.csv', delimiter=',', dtype=dtype, encoding=None, skip_header=1 if skip_header == 0 and 'iris.csv' in 'files/iris.csv' else skip_header, usecols=usecols)
    except:
        # Fallback to URL
        data = np.genfromtxt(url, delimiter=',', dtype=dtype, encoding=None, usecols=usecols)
    return data

# --- DRY: Load data once for all exercises ---
# iris_object: used for Exercise 9 (keeping text intact)
# iris_numeric: used for Exercises 10-14 (calculations and plotting)

_iris_object = _load_iris(dtype=object)
_iris_numeric = _load_iris(dtype=float, usecols=[0,1,2,3])

# Exercise 9: Import iris dataset keeping text intact
def ex9():
    return _iris_object[:3]

# Exercise 10: Missing values check
def ex10():
    # Work on a copy if we're going to modify it for testing
    data = _iris_numeric.copy()
    
    # Introduce missing values for testing
    data[1, 2] = np.nan
    data[2, 2] = np.nan
    
    missing_count = np.isnan(data[:, 0]).sum()
    missing_positions = np.where(np.isnan(data[:, 0]))
    return missing_count, missing_positions

# Exercise 11: Mean, median, std dev of sepallength
def ex11():
    sepallength = _iris_numeric[:, 0]
    return np.mean(sepallength), np.median(sepallength), np.std(sepallength)

# Exercise 12: 5th and 95th percentile
def ex12():
    sepallength = _iris_numeric[:, 0]
    return np.percentile(sepallength, [5, 95])

# Exercise 13: Filter iris data
def ex13():
    # sepallength (1st col) < 5.0 and petallength (3rd col) > 1.5
    condition = (_iris_numeric[:, 0] < 5.0) & (_iris_numeric[:, 2] > 1.5)
    return _iris_numeric[condition]

# Exercise 14: Data Visualization (Added based on feedback)
def ex14():
    plt.figure(figsize=(10, 6))
    plt.scatter(_iris_numeric[:, 0], _iris_numeric[:, 1], c='blue', alpha=0.5)
    plt.title('Iris Sepal Length vs Width')
    plt.xlabel('Sepal Length')
    plt.ylabel('Sepal Width')
    plt.grid(True)
    plt.savefig('reports/sepal_scatter.png')
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.hist(_iris_numeric[:, 2], bins=20, color='green', alpha=0.7)
    plt.title('Distribution of Petal Length')
    plt.xlabel('Petal Length')
    plt.ylabel('Frequency')
    plt.savefig('reports/petal_distribution.png')
    plt.show()
    return "Plots saved to reports/ directory."

if __name__ == "__main__":
    print("Testing NumPy Basic Exercises...")
    print(f"Ex 1:\n{ex1()}")
    print(f"Ex 2:\n{ex2()}")
    print(f"Ex 3:\n{ex3()}")
    print(f"Ex 4:\n{ex4()}")
    a, o = ex5(); print(f"Ex 5: {a[:5]}... -> {o[:5]}...")
    print(f"Ex 6: {ex6()}")
    print(f"Ex 7:\n{ex7()}")
    m, r14, c14, inn = ex8(); print(f"Ex 8 Rows 1&4:\n{r14}")
    print(f"Ex 9:\n{ex9()}")
    print(f"Ex 10: {ex10()}")
    print(f"Ex 11: {ex11()}")
    print(f"Ex 12: {ex12()}")
    print(f"Ex 13:\n{ex13()}")
    print(f"Ex 14: {ex14()}")
