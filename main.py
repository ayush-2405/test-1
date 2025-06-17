# Updated main application
from utils import safe_divide

def calculate_values():
    return safe_divide(10, 0)  # This is safe now

if __name__ == "__main__":
    calculate_values()
