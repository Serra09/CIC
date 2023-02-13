import json
import os

f = open(os.getcwd() + '/Documents/CIC/prueba.json')

data = json.load(f)

print(data)



