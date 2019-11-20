'''
script que permite leer un csv y retorna el valor de la columna
'''

import pandas as pd
import sys
import json

dataSet = pd.read_csv(sys.argv[1])
feature = sys.argv[2]

response = []
for i in dataSet[feature]:
    response.append(i)

dataResponse = {"feature":response}

print json.dumps(dataResponse)
