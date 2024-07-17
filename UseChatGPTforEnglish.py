import json
import time
import re
import openai
import pandas

openai.api_key=""

datas = pandas.read_excel('EnglishTestData.xlsx').values.tolist()


for num, data in enumerate(datas[:100]):
    if num >= 91:
        content = """
              There is an English grammar error correction task. You will be given two English sentences, one of which is a sentence with grammatical errors and the other is a corrected sentence. Please judge whether the corrected operation is correct and whether the corrected sentence still exists grammatical errors.
              The input format is (sentence with grammatical errors | corrected sentence)
              The output format is JSON, output example: {"Is the correction operation correct?": true, "Is there any error in the corrected sentence?": false}
              English sentence: ( %s | %s)
              JSON object:
            """
        content = content % (data[2],data[3])

        while True:
            response = openai.ChatCompletion.create(
              model="gpt-4",
              messages=[
                    # {"role": "system", "content": "You are an expert in English linguistics, proficient in correction and polishing of English texts."},
                    {"role": "system", "content": "You are an English grammatical error correction tool that can identify and correct grammatical errors in a text."},
                    {"role": "user", "content": content},

                ]
            )
            try:
                resp = json.loads(response["choices"][0]["message"]["content"])
                print(str(num), '\t', resp["Is the correction operation correct?"], '\t', resp["Is there any error in the corrected sentence?"])
                break
            except Exception as e:
                continue
