import csv
import json

csvFile = open("News Articles\\MN-DS-news-classification.csv", 'r', encoding="utf-8") 
Reader = csv.DictReader(csvFile)
for row in Reader:
    jsonFile = json.dumps(row, indent=4, ensure_ascii=False)
    finalFile = open("News Articles\\" + json.loads(jsonFile)['data_id'] + ".json", 'w', encoding="utf-8")
    finalFile.write(jsonFile)
    finalFile.close()
csvFile.close()
 