# Take a JSON file as input and generate a CSV file as output

import csv
import json

# Read JSON file - load data to variable
with open("input.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Write CSV file
with open("output.csv", "w", newline="", encoding="utf-8") as csv_file:
    # Get Header Values
    fieldnames = list(dict.fromkeys(key for row in data for key in row.keys()))
    # Create a CSV writer agent
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)