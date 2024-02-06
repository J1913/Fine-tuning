import openai
import os
import json

openai.organization = "org-UBSwr4XNUOZVv4PQ3owv7lGS"
openai.api_key = "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"

file_id_train = "file-wJNVeGu5UlMd7BROafSapo4t"
model = 'davinci'

FineTune = openai.FineTune.create(training_file = file_id_train,
                                  model = model,
                                  )

print(FineTune)
