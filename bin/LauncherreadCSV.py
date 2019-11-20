'''
script que recibe un csv y lo lee retornando en formajo JSON la data de la matriz y la data de los header...
'''
import pandas as pd
import sys
import json

dataSet = pd.read_csv(sys.argv[1])

#obtenemos las key
keys = []
for element in dataSet:
    keys.append(element)

keys = keys[1:]

#ahora obtenemos los elementos para formar la matriz...
matrixResponse = []

for i in range(len(dataSet)):
    row = []
    for key in keys:
        row.append(dataSet[key][i])
    matrixResponse.append(row)

dictResponse = {}

dictResponse.update({"keys": keys})
dictResponse.update({"data": matrixResponse})

print json.dumps(dictResponse)
