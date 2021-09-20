import csv, json

csvData = "superheroes_nlp_dataset.csv"
jsonOut = "superheroes.json"

data = {}
with open(csvData) as csvFile:
    csvRead = csv.DictReader(csvFile)
    for rows in csvRead:
        id = rows['id']
        data[id] = rows

with open(jsonOut, 'w') as jsonFile:
    jsonFile.write(json.dumps(data, indent=4))
