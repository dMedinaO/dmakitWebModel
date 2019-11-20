'''
script que permite hacer la prueba de shapiro sobre un set de datos
'''

import pandas as pd
import sys
import json
from scipy import stats

dataSet = pd.read_csv(sys.argv[1])
feature = sys.argv[2]

dataValues = dataSet[feature]

#evaluamos shapiro
response = stats.shapiro(dataValues)
dictResponse = {'statistic':response[0], 'pvalue':response[1]}

print json.dumps(dictResponse)
