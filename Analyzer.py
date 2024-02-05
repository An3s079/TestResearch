#
# IF YALL ARE SEEING THIS IN THE STEM LAB
# PLEASE DONT RUN IT
# THIS COSTS ME REAL MONEY EVERY TIME ITS RUN 😭
#

import openai
import os
 
apiFile = open("API_Key.txt", "r")
openai.api_key = apiFile.read()
apiFile.close()

crime_type = ["Harmful White Collar", "Harmful Street", "Financial White Collar", "Financial Street"]
for type in crime_type:
    for filename in os.listdir("News Articles\\"+type):
        file = open("News Articles\\"+type+"\\" + filename, "r+", encoding="utf8")
        Data = file.read()
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are analyzing news articles to determine if there is a difference in how harmful they portray a crime to be, "+
                "and how much malicious intent they attribute to the crime.Please rate the following article out of ten based on how harmful they describe the crime "+ 
                "to be, and how much malicious intent they prescribe to the perpetrator. An article is considered to be portraying more harmfulness when it focuses "+
                "more on the impact of the crime on the victims and uses adjectives, adverbs, etc., to emphasize it. An article is considered to be portraying more "+
                "malicious intent when it showcases that the perpetrator intended or knew they would cause harm, and showcases selfish motives from the perpetrator "+
                "such as to gain wealth, revenge, etc. Remember, please rate the articles based on how harmful and malicious they portray the crime to be, not how " +
                "harmful or malicious you believe the crime to be. Please rate them to the best of your ability and understanding from the above definitions. " +
                "Please Lay out your responses like so: "+
                "<harmfullness rating><insert comma><maliciousness rating><insert comma>" + "<insert new line> <reason for harmfullness rating> (<harmfullness rating>/10),  <reason for maliciousness rating> (<maliciousness rating>/10)"},
                {"role": "user", "content": Data}
            ]
        )
        file.seek(0,0)
        file.write(str(response["choices"][0]["message"]["content"]) + "\n" + "\n" + Data)
        data_file_malice = open(type+"_m.txt", "a")
        data_file_harm = open(type+"_h.txt", "a")
        data_file_harm.write(str(response["choices"][0]["message"]["content"]).split(",")[0]+",")
        data_file_malice.write(str(response["choices"][0]["message"]["content"]).split(",")[1]+",")
        data_file_harm.close()
        data_file_malice.close()
        print("Completed " + filename)
        file.close()


