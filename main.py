# Updated main application
from utils import risky_divide

def calculate_values():
    return risky_divide(10, 0)  # This will cause division by zero

if __name__ == "__main__":
    calculate_values()
