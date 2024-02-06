import openai
import os
import json

openai.organization = ""
openai.api_key = ""

file_id_train = "アップロードしたファイルのID"
model = 'davinci'

FineTune = openai.FineTune.create(training_file = file_id_train,
                                  model = model,
                                  )

print(FineTune)
