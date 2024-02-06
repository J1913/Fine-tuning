import json
import openai
import os

filepath_train = "アップロードしたいファイルのパス"
openai.api_key = ""

upload_file_train = openai.File.create(
        file=open(filepath_train, "rb"),
        purpose='fine-tune',
        )

print(upload_file_train)
