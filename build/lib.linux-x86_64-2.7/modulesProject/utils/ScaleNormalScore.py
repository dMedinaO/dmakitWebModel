'''
clase que recibe un set de datos y genera la transformacion de los datos en escala logaritmica
'''

import pandas as pd
import numpy as np

class applyNormalScale(object):

    def __init__(self, dataSet):

        self.dataSet = dataSet
        dicValues = {}
        for key in self.dataSet:
            row = self.transformNormalScale(key)

            #create a data frame
            dicValues.update({key:row})

        self.dataTransform = pd.DataFrame(dicValues)

    #metodo que permite definir el tipo de data...
    def checkData(self, array):
        response = 0

        try:
            for i in array:
                data = float(i)
        except:
            response = 1
        return response

    #metodo que toma una columna del set de datos y aplica la transformacion logaritmica de los datos...
    def transformNormalScale(self, feature):

        dataValue = []

        if self.checkData(self.dataSet[feature]) == 0:

            meanValue = np.mean(self.dataSet[feature])
            stdValue = np.std(self.dataSet[feature])

            for i in self.dataSet[feature]:

                valueData = float(i)
                value = (valueData-meanValue)/stdValue
                dataValue.append(value)
        else:
            for i in self.dataSet[feature]:
                dataValue.append(i)
        return dataValue
