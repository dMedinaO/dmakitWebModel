'''
scrip que permite ejecutar un algoritmo de clustering, recibe los parametros y estima los valores que son necesarios,
recibe el archivo csv y genera los archivos asociados a los resultados para la generacion de graficos y creacion del csv
con las etiquetas generadas por el algoritmo de clustering.

# NOTE: El archivo con los resultados se encontrara en formato json y contendra el error si es que existe o los valores de
los resultados obtenidos....

# NOTE: Explicacion del atributo param

Param es una lista de parametros dependiente de cada algoritmo, toma los siguientes valores posibles

Algoritmo   Valor param
K_means     k
Birch       k
Aglomerativo [linkage, affinity, numberK]
Otros       Void
'''

from modulesProject.clustering_analysis import processClustering
from modulesProject.clustering_analysis import evaluationClustering

from modulesProject.utils import transformFrequence
from modulesProject.utils import ScaleNormalScore
from modulesProject.utils import ScaleMinMax
from modulesProject.utils import ScaleDataSetLog
from modulesProject.utils import ScaleLogNormalScore

import pandas as pd
import json

class execAlgorithm(object):

    #constructor de la clase
    def __init__(self, dataSet, user, job, pathResponse, algorithm, params, optionNormalize, optionEncoded):

        self.optionNormalize = optionNormalize
        self.optionEncoded = optionEncoded
        self.processDataSet(dataSet)#hacemos el preprocesamiento a los datos

        self.user = user
        self.job = job
        self.pathResponse = pathResponse
        self.algorithm = algorithm
        self.params = params#params es una lista de parametros asociados al algoritmo
        self.applyClustering = processClustering.aplicateClustering(self.dataSet)
        self.response = {}#diccionario con la respuesta para formar el json

    #metodo que permite procesar el set de datos segun la opcion del usuario a normalizar
    def processDataSet(self, dataSetInput):

        
        #ahora transformamos el set de datos por si existen elementos discretos...
        transformDataSet = transformFrequence.frequenceData(dataSetInput)
        dataSetNewFreq = transformDataSet.dataTransform

        #ahora aplicamos el procesamiento segun lo expuesto
        if self.optionNormalize == 1:#normal scale
            applyNormal = ScaleNormalScore.applyNormalScale(dataSetNewFreq)
            self.dataSet = applyNormal.dataTransform

        if self.optionNormalize == 2:#min max scaler
            applyMinMax = ScaleMinMax.applyMinMaxScaler(dataSetNewFreq)
            self.dataSet = applyMinMax.dataTransform

        if self.optionNormalize == 3:#log scale
            applyLog = ScaleDataSetLog.applyLogScale(dataSetNewFreq)
            self.dataSet = applyLog.dataTransform

        if self.optionNormalize == 4:#log normal scale
            applyLogNormal = ScaleLogNormalScore.applyLogNormalScale(dataSetNewFreq)
            self.dataSet = applyLogNormal.dataTransform

    #metodo que permite evaluar la ejecucion del algoritmo con respecto a los parametros de entrada
    def execAlgorithmByOptions(self):

        nameDoc = ""
        if self.algorithm == 1:#kmeans

            responseExec = self.applyClustering.aplicateKMeans(int(self.params[0]))

            self.response.update({"algorithm": "K Means"})
            paramsData = {}
            paramsData.update({"Number K": self.params[0]})
            self.response.update({"Params": paramsData})

            if responseExec == 0:
                self.response.update({"responseExec":"OK"})
            else:
                self.response.update({"responseExec":"ERROR"})

        elif self.algorithm == 2:#Birch

            responseExec = self.applyClustering.aplicateBirch(int(self.params[0]))
            self.response.update({"algorithm": "Birch"})
            paramsData = {}
            paramsData.update({"Number K": self.params[0]})
            self.response.update({"Params": paramsData})

            if responseExec == 0:
                self.response.update({"responseExec":"OK"})
            else:
                self.response.update({"responseExec":"ERROR"})

        elif self.algorithm == 3:#Agglomerative

            responseExec = self.applyClustering.aplicateAlgomerativeClustering(self.params[0], self.params[1], int(self.params[2]))
            self.response.update({"algorithm": "Agglomerative Clustering"})
            paramsData = {}
            paramsData.update({"Linkage": self.params[0]})
            paramsData.update({"Affinity": self.params[1]})
            paramsData.update({"Number K": self.params[2]})
            self.response.update({"Params": paramsData})

            if responseExec == 0:
                self.response.update({"responseExec":"OK"})
            else:
                self.response.update({"responseExec":"ERROR"})

        elif self.algorithm == 4:#DBSCAN

            responseExec = self.applyClustering.aplicateDBSCAN()
            self.response.update({"algorithm": "DBSCAN"})
            paramsData = {}
            paramsData.update({"Default": "Default"})
            self.response.update({"Params": paramsData})

            if responseExec == 0:
                self.response.update({"responseExec":"OK"})
            else:
                self.response.update({"responseExec":"ERROR"})

        elif self.algorithm == 5:#MeanShift

            responseExec = self.applyClustering.aplicateMeanShift()
            self.response.update({"algorithm": "Mean Shift"})
            paramsData = {}
            paramsData.update({"Default": "Default"})
            self.response.update({"Params": paramsData})
            if responseExec == 0:
                self.response.update({"responseExec":"OK"})
            else:
                self.response.update({"responseExec":"ERROR"})

        else:
            responseExec = self.applyClustering.aplicateAffinityPropagation()
            self.response.update({"algorithm": "Affinity Propagation"})
            paramsData = {}
            paramsData.update({"Default": "Default"})
            self.response.update({"Params": paramsData})
            if responseExec == 0:
                self.response.update({"responseExec":"OK"})
            else:
                self.response.update({"responseExec":"ERROR"})

        #solo si la ejecucion fue correcta!
        if self.response['responseExec'] == "OK":
            #evaluamos el clustering y obtenemos los resultados...
            result = evaluationClustering.evaluationClustering(self.dataSet, self.applyClustering.labels)#evaluamos...
            self.response.update({"calinski_harabaz_score": result.calinski})
            self.response.update({"silhouette_score": result.siluetas})

            #finalmente, agregamos los labels al set de datos y generamos el resultado en el path entregado...
            self.dataSet["Labels"] = pd.Series(self.applyClustering.labels, index=self.dataSet.index)
            self.dataSet.to_csv(self.pathResponse+self.user+"/"+self.job+"/responseClustering.csv")

            #hacemos el conteo de los elementos por grupo para la generacion del grafico de torta asociada a la cantidad de grupos...
            self.response.update({"membersGroup":self.countMemberGroup()})

        #exportamos tambien el resultado del json
        with open(self.pathResponse+self.user+"/"+self.job+"/responseClustering.json", 'w') as fp:
            json.dump(self.response, fp)

    #metodo que recibe una lista y genera un diccionario asociado a los grupos y su cantidad...
    def countMemberGroup(self):

        groups = list(set(self.applyClustering.labels))

        countGroup = {}

        for element in groups:
            cont =0

            for label in self.applyClustering.labels:
                if element == label:
                    cont+=1
            key = "Group"+str(element)
            countGroup.update({key: cont})
        return countGroup
