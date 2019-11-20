'''
clase que permite transforma la data discreta en su frecuencia de aparicion...
'''

import pandas as pd

class frequenceData(object):

    def __init__(self, dataSet):

        self.dataSet = dataSet

        dicValues = {}
        for key in self.dataSet:
            row = self.processFrequence(key)

            #create a data frame
            dicValues.update({key:row})
                    
        self.dataTransform = pd.DataFrame(dicValues)

    #metodo que transforma la clase en valores continuos desde el 0 hasta el n...
    def transformClassData(self, array):

        #preguntamos si la clase es letras o numeros
        if self.checkData(array) == 1:
            valueClass = list(set(array))

            dictResponse = {}
            index=0
            for value in valueClass:
                dictResponse.update({value:index})
                index+=1

            dataResponse = []

            for i in array:
                dataResponse.append(dictResponse[i])
            return dataResponse
        else:
            dataResponse = array
            return dataResponse

    #metodo que permite definir el tipo de data...
    def checkData(self, array):
        response = 0

        try:
            for i in array:
                data = float(i)
        except:
            response = 1
        return response

    def processFrequence(self, feature):

        dataValue = []
        if self.checkData(self.dataSet[feature]) == 1:

            dictFrequence = self.getFrequence(self.dataSet[feature], feature)
            print dictFrequence

            #ahora hacemos la transformacion de los elementos
            for i in self.dataSet[feature]:
                dataValue.append(dictFrequence[i])
        else:
            dataValue = self.dataSet[feature]

        return dataValue

    #metodo que permite formar las frecuencias
    def getFrequence(self, arrayData, nameFeature):

        #hacemos el conteo...
        data = list(set(arrayData))

        dictResponse = {}

        for element in data:
            cont=0

            for value in arrayData:
                if element == value:
                    cont+=1
            freq = float(cont)/float(len(arrayData))

            dictResponse.update({element:freq})

        return dictResponse
