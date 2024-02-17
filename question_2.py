#You are given a CSV file named "data.csv" that contains two columns: "height" and "weight". 
#Write a Python function called "calculate_bmi" that takes the filename as an input and calculates the BMI (Body Mass Index) for each person in the file. 
# The BMI is calculated using the formula: BMI = weight / (height ** 2). 
# The function should return a list of tuples, where each tuple contains the height, weight, and BMI for a person.


import csv

data = [
    {'height': 1.70, 'weight': 65},
    {'height': 1.65, 'weight': 75},
    {'height': 1.80, 'weight': 80}
]

def create_dataset(filename, data):
    fieldnames = ['height', 'weight']
    with open(filename, 'w') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

# Example usage:
create_dataset('data.csv', data)
print("Dataset created successfully!")

def calculate_bmi(filename):
    results = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            height = float(row['height'])
            weight = float(row['weight'])
            bmi = weight / (height ** 2)
            results.append((height, weight, round(bmi, 2)))
    return results

# Example usage:
data = calculate_bmi('data.csv')
print(data)