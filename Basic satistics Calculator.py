# Basic Statistics Calcultor

import math

def calculate_mean(data):
    return sum(data) / len(data)

def calculate_median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    middle = n // 2
    if n % 2 == 0: # even numbers of data elements
        return (sorted_data[middle - 1] + sorted_data[middle]) / 2
    else: # odd numbers of data elements
        return sorted-data[middle]
    
def calculate_mode(data):
    frequency = {}
    for item in data:
        frequency[item] = frequency.get(item, 0) + 1
    max_freq = max(frequency.values())
    modes = [key for key, value in frequency.items() if value == max_freq]
    if len(modes) == len(data):
        return None
    return modes

def calculate_variance(data):
    mean = sum(data) / len(data)
    squared_diffs = [(x - mean) ** 2 for x in data]
    return sum(squared_diffs) / len(data)

def calculate_standard_deviation(data):
    mean = sum(data) / len(data)
    sum_squared_diff = 0
    for x in data:
        sum_squared_diff += (x - mean ) ** 2
    avg_squared_diff = sum_squared_diff / len(data)
    return math.sqrt(avg_squared_diff)

# # Sample data
# data = [2, 4, 4, 4, 5, 5, 7, 9]

# print("Data:", data)
# print("Mean:", calculate_mean(data))
# print("Median:", calculate_median(data))
# print("Mode:", calculate_mode(data))
# print("Variance:", calculate_variance(data))
# print("Standard Deviation:", calculate_standard_deviation(data))
def get_user_data():
    print("Enter your numbers separated by spaces:")
    user_input = input()
    # Split input by spaces and convert each to float
    data = list(map(float, user_input.strip().split()))
    return data

def main():
    data = get_user_data()
    print("\nYour data:", data)
    print("Mean:", calculate_mean(data))
    print("Median:", calculate_median(data))
    mode = calculate_mode(data)
    if mode is None:
        print("Mode: No mode (all values unique)")
    else:
        print("Mode:", mode)
    print("Standard Deviation:", calculate_standard_deviation(data))

if __name__ == "__main__":
    main()