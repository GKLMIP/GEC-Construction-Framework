import json
import time
import re
import openai
import pandas

openai.api_key=""

new_datas = pandas.read_excel('IndonesianData.xlsx').values.tolist()


for num, data in enumerate(new_datas):
    if num >= 100:
        content = """
               Berikut ini adalah tugas koreksi kesalahan tata bahasa Indonesia. Anda akan diberikan dua kalimat dalam bahasa Indonesia, salah satu adalah kalimat dengan kesalahan tata bahasa dan yang lain adalah kalimat yang sudah diperbaiki/dikoreksi. Diharapkan menilai apakah koreksi tersebut yang benar dan apakah kalimat yang sudah diperbaiki/dikoreksi itu masih ada kesalahan tata bahasa.
               Format inputnya adalah (kalimat dengan kesalahan tata bahasa | kalimat yang sudah diperbaiki/dikoreksi)
               Format outputnya adalah JSON, contoh output {"Apakah koreksi itu benar?": benar, "Apakah ada kesalahan dalam kalimat yang dikoreksi?": salah}
               Kalimat bahasa Indonesia : ( %s | %s)
               objek JSON:
            """
        content = content % (data[2],data[3])

        while True:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    # {"role": "system", "content": "You are an expert in English linguistics, proficient in correction and polishing of English texts."},
                    {"role": "system", "content": "Anda adalah alat koreksi kesalahan tata bahasa Indonesia yang dapat mengidentifikasi dan memperbaiki kesalahan tata bahasa dalam sebuah teks."},
                    {"role": "user", "content": content},

                ]
            )
            try:
                resp = json.loads(response["choices"][0]["message"]["content"])
                print(str(num), '\t', resp["Apakah koreksi itu benar?"], '\t',
                      resp["Apakah ada kesalahan dalam kalimat yang dikoreksi?"])
                break
            except Exception as e:
                print(e)
                continue
