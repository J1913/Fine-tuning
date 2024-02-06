import json
import openai
import os

filepath_train = "./finetuning2.jsonl"
openai.api_key = "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"

upload_file_train = openai.File.create(
        file=open(filepath_train, "rb"),
        purpose='fine-tune',
        )

print(upload_file_train)
