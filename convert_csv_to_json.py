import csv
import json


def csvToJson(csvFilePath, jsonFilePath):
    jsonArray = []

    # read csv file
    with open(csvFilePath, encoding='utf-8') as csvF:
        # load the csv file's data
        csvReader = csv.DictReader(csvF)

        # convert each csv row into python dict
        for row in csvReader:
            # add this python dict to json array
            jsonArray.append(row)

    # convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonF:
        jsonString = json.dumps(jsonArray, indent=4)
        jsonF.write(jsonString)
