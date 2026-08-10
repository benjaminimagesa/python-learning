# Operating system
import os
import json

current_directory = os.getcwd()
print(current_directory)


data = {"name": "Benjac", "age": 21}
json_string = json.dumps(data)
