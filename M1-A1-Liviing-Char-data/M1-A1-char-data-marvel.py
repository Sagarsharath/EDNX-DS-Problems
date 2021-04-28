import csv

#complete file-path
inputFilePath = "dc-wikia-data.csv"

totalAppearances = {}
livingDict = {}

with open(inputFilePath) as csvFile:
    reader = csv.reader(csvFile)
    headers = next(reader)
    for row in reader:
        name = row[1].split("(")[0].rstrip()
        living = row[9]
        world = row[1][row[1].find("(") +1: row[1].find(")")]
        try:
            appear = int(row[10])
        except:
            continue
        if living == "Living Characters":
            if world not in livingDict:
                livingDict[world] = []
            if world not in totalAppearances:
                totalAppearances[world] = 0
                
            livingDict[world].append(name)
            totalAppearances[world] += int(appear)

print(livingDict)
print('-----------')
print(totalAppearances)