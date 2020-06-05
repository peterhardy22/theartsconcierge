import csv
import json
import yaml


def csv_importer():
    with open('app/static/data/csv/bayareatracker.csv') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        first_line = True
        exhibits = []
        for row in csv_data:
            if not first_line:
                exhibits.append({
                    "institution": row[0],
                    "title": row[1],
                    "dates": row[2],
                    "image": row[3],
                    "link": row[4]
                })
            else:
                first_line = False

    exhibits_json = json.dumps(exhibits)

    return yaml.safe_load(exhibits_json)
