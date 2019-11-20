'''
clase que recibe un set de datos y genera la transformacion de los datos en escala logaritmica
'''

import pandas as pd
import numpy as np

class applyLogScale(object):

    def __init__(self, dataSet):

        self.dataSet = dataSet

        dicValues = {}
        for key in self.dataSet:
            row = self.transformLogScale(key)

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
    def transformLogScale(self, feature):

        dataValue = []

        if self.checkData(self.dataSet[feature]) == 0:

            for i in self.dataSet[feature]:
                if i >0:
                    dataValue.append(np.log2(i))
                else:
                    dataValue.append(0)
        else:
            for i in self.dataSet[feature]:
                dataValue.append(i)
        return dataValue
