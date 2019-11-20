'''
script que recibe un data set y una key y genera el json asociado a la respuesta para cargar un grafico de torta
'''

import json

class pieChart(object):

    #definimos los atributos para la clase
    def __init__(self, dataSet, key):

        self.dataSet = dataSet
        self.key = key

    #creamos la respuesta para el manejo del set de datos...
    def createExport(self):

        dataInformation = self.dataSet[self.key]

        #obtenemos las key y generamos los contadores
        keys = list(set(dataInformation))
        counts = []

        for element in keys:
            cont=0
            for data in dataInformation:
                if data == element:
                    cont+=1
            counts.append(cont)

        dicResponse = {}
        dicResponse.update({"keys":keys})
        dicResponse.update({"values":counts})
        print json.dumps(dicResponse)
