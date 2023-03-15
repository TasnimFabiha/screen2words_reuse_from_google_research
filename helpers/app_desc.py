import csv
import json

OUTPUT_DIC = '../tmp/'
with open('id_to_desc.csv', encoding='utf8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        screenId = row['screenId']
        description = row['Description']
        json_data = {'screenId': screenId, 'appDesc': description}
        filename = f'{screenId}_APPDESC.json'
        with open(OUTPUT_DIC + filename, 'w') as jsonfile:
            json.dump(json_data, jsonfile)