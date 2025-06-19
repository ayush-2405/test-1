from utils import *

def calculate_values():
    result1 = safe_divide(10, 2)
    result2 = risky_divide(10, 0)  # This will cause ZeroDivisionError
    return result1 + result2

if __name__ == "__main__":
    calculate_values()
