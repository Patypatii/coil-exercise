import numpy as np

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

# Exercise 9: Import iris dataset keeping text intact
def ex9():
    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
    # Use local file if available
    try:
        data = np.genfromtxt('files/iris.csv', delimiter=',', dtype=object, encoding=None, skip_header=1)
    except:
        data = np.genfromtxt(url, delimiter=',', dtype=object, encoding=None)
    return data[:3]

# Exercise 10: Missing values check
def ex10():
    # Load first 4 columns
    try:
        iris_numbers = np.genfromtxt('files/iris.csv', delimiter=',', dtype=float, encoding=None, skip_header=1, usecols=[0,1,2,3])
    except:
        url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
        iris_numbers = np.genfromtxt(url, delimiter=',', dtype=float, encoding=None, usecols=[0,1,2,3])
    
    # Introduce missing values for testing
    iris_numbers[1, 2] = np.nan
    iris_numbers[2, 2] = np.nan
    
    missing_count = np.isnan(iris_numbers[:, 0]).sum()
    missing_positions = np.where(np.isnan(iris_numbers[:, 0]))
    return missing_count, missing_positions

# Exercise 11: Mean, median, std dev of sepallength
def ex11():
    try:
        sepallength = np.genfromtxt('files/iris.csv', delimiter=',', dtype=float, encoding=None, skip_header=1, usecols=[0])
    except:
        url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
        sepallength = np.genfromtxt(url, delimiter=',', dtype=float, encoding=None, usecols=[0])
    
    return np.mean(sepallength), np.median(sepallength), np.std(sepallength)

# Exercise 12: 5th and 95th percentile
def ex12():
    try:
        sepallength = np.genfromtxt('files/iris.csv', delimiter=',', dtype=float, encoding=None, skip_header=1, usecols=[0])
    except:
        url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
        sepallength = np.genfromtxt(url, delimiter=',', dtype=float, encoding=None, usecols=[0])
    
    return np.percentile(sepallength, [5, 95])

# Exercise 13: Filter iris data
def ex13():
    try:
        data = np.genfromtxt('files/iris.csv', delimiter=',', dtype=float, encoding=None, skip_header=1, usecols=[0,1,2,3])
    except:
        url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
        data = np.genfromtxt(url, delimiter=',', dtype=float, encoding=None, usecols=[0,1,2,3])
    
    # sepallength (1st col) < 5.0 and petallength (3rd col) > 1.5
    condition = (data[:, 0] < 5.0) & (data[:, 2] > 1.5)
    return data[condition]

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
