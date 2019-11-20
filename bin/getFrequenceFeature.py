'''
script que permite leer un csv y retorna la frecuencia de valores
'''

import pandas as pd
import sys
import json

dataSet = pd.read_csv(sys.argv[1])
feature = sys.argv[2]

valueList = list(set(dataSet[feature]))

dictValues = {}

for value in valueList:
    cont=0
    for i in dataSet[feature]:
        if value == i:
            cont+=1
    dictValues.update({value:cont})

print json.dumps(dictValues)
