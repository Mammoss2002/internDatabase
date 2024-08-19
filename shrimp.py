import csv
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['myDatabase']
collection = db['internDatabase']

csv_filename = 'output.csv'
start_parsing = False
header = None

with open(csv_filename, mode='r') as file:
    csv_reader = csv.reader(file)
    
    for index, row in enumerate(csv_reader):
        if not start_parsing:
            if len(row) >= 9 and row[0] == 'Process Step' and row[1] == 'Data Name' and row[2] == 'Data Value' and row[3] == 'Unit of Measure' and row[4] == 'Device ID' and row[5] == 'Is Parametric' and row[6] == 'Lower Limit' and row[7] == 'Upper Limit' and row[8] == 'Status':
                header = row
                start_parsing = True
                print("Start Process Plan")
            continue
        
        if start_parsing:
            if len(row) != len(header):
                print(f"Not Match {index + 1}: {row}")
                continue

            data = {header[i]: row[i] if i < len(row) and row[i].strip() else "null" for i in range(len(header))}
            
            try:
                collection.insert_one(data)
                print(f"Put Data in ManogoDB: {data}")
            except Exception as e:
                print(f"Fail To Put Data in MongoDB: {e}")

print("Success All Process")