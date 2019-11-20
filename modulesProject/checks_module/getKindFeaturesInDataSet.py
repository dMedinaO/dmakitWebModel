'''
clase con la responsabilidad de revisar el set de datos y obtener el nombre de la feature y el tipo de set de dato que es
'''

import pandas as pd
from modulesProject.dataBase_module import ConnectDataBase
from modulesProject.dataBase_module import HandlerQuery

class checkDataSet(object):

    def __init__(self, dataSet, idDataSet):

        self.dataSet = pd.read_csv(dataSet)
        self.idDataSet = idDataSet
        self.connect = ConnectDataBase.ConnectDataBase()
        self.handler = HandlerQuery.HandlerQuery()

    #metodo que recorre toda la data e inserta los valores de las features de los set de datos...
    def insertFeaturesDB(self):

        self.getKeysInDS()#obtengo la lista de features

        for key in self.keys:#recorro la lista y obtengo el tipo por cada una
            response = self.checkKindFeature(key)
            #hacemos la insercion del feature en la bd...
            self.connect.initConnectionDB()
            query = "insert into feature values (null, '%s', '%s', %s)" % (key, response, self.idDataSet)
            self.handler.insertToTable(query, self.connect)
            self.connect.closeConnectionDB()

    #metodo que permite obtener todas las keys...
    def getKeysInDS(self):

        self.keys = []
        for element in self.dataSet:
            self.keys.append(element)


    #metodo que permite evaluar el tipo de set de datos...
    def checkKindFeature(self, feature):

        response ="CONTINUA"

        for i in range(len(self.dataSet)):

            try:
                data = float(self.dataSet[feature][i])
            except:
                response="DISCRETA"
                break

        return response
