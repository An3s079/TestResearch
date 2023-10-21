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

for filename in os.listdir("News Articles"):
    file = open("News Articles\\" + filename, "r+", encoding="utf8")
    Data = file.read()
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are analyzing news articles to determine if there is a difference in how harmful they portray a crime to be, "+
            "and how much malicious intent they attribute to the crime. Please rate their portrayed harmfullness and portrayed malicious intent from 1-10. Remember, please rate the articles based on "+
            "how harmful and malicious they portray the crime to be, not how harmful or malicious you believe the crime to be. Please Lay out your responses like so: "+
            "\"[<harmfullness rating>/10, <maliciousness rating>/10] <insert new line> <reason for harmfullness rating> (<harmfullness rating>/10),  <reason for maliciousness rating> (<maliciousness rating>/10)"},
            {"role": "user", "content": Data}
        ]
    )
    file.seek(0,0)
    file.write(str(response["choices"][0]["message"]["content"]) + "\n" + "\n" + Data)
    file.close()

    