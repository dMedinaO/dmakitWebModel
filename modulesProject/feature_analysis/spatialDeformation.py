'''
clase con la responsabilidad de generar la deformacion espacial de los elementos y generar un ranking de la importancia
de los atributos mediante la aplicacion de random forest default. Si el set de datos no tiene clases, se obtienen
mediante la aplicacion de clustering y se selecciona el con mejor calinski y mejor siluetas (en ese orden)
'''

from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
import pandas as pd
import numpy as np

#metodos de la libreria utils...
from modulesProject.utils import transformDataClass
from modulesProject.utils import transformFrequence
from modulesProject.utils import ScaleNormalScore
from modulesProject.utils import ScaleMinMax
from modulesProject.utils import ScaleDataSetLog
from modulesProject.utils import ScaleLogNormalScore

class spatialDeformation(object):

    def __init__(self, user, job, dataSet, pathResponse, optionNormalize):

        self.user = user
        self.job = job
        self.dataSet = dataSet
        self.pathResponse = pathResponse
        self.optionNormalize = optionNormalize

    #metodo que permite normalizar el set de datos con respecto a la opcion entregada
    def normalizeDataSet(self, dataSetOri):

        #ahora transformamos el set de datos por si existen elementos discretos...
        transformDataSet = transformFrequence.frequenceData(dataSetOri)
        dataSetNewFreq = transformDataSet.dataTransform

        dataSetNorm = ""
        #ahora aplicamos el procesamiento segun lo expuesto
        if self.optionNormalize == 1:#normal scale
            applyNormal = ScaleNormalScore.applyNormalScale(dataSetNewFreq)
            dataSetNorm = applyNormal.dataTransform

        if self.optionNormalize == 2:#min max scaler
            applyMinMax = ScaleMinMax.applyMinMaxScaler(dataSetNewFreq)
            dataSetNorm = applyMinMax.dataTransform

        if self.optionNormalize == 3:#log scale
            applyLog = ScaleDataSetLog.applyLogScale(dataSetNewFreq)
            dataSetNorm = applyLog.dataTransform

        if self.optionNormalize == 4:#log normal scale
            applyLogNormal = ScaleLogNormalScore.applyLogNormalScale(dataSetNewFreq)
            dataSetNorm = applyLogNormal.dataTransform

        return dataSetNorm

    #metodo que permite aplicar random Forest para obtener las importancias...
    def applyRandomForestClassifier(self, data, target):

        response = ""

        try:
        #instancia a random forest y aplicacion del mismo
            random_forest = RandomForestClassifier(max_depth=2, random_state=0, n_estimators=10, n_jobs=-1, criterion='gini')
            random_forest = random_forest.fit(data, target)

            #obtenemos las importancias
            importances = pd.DataFrame({'feature':data.columns.tolist(),'importance':np.round(random_forest.feature_importances_,3)})
            importances = importances.sort('importance',ascending=False).set_index('feature')

            #exportamos el resultado
            nameCSV = "%s%s/%s/rankingImportance_%s.csv" % (self.pathResponse, self.user, self.job, self.job)
            importances.to_csv(nameCSV)
            response = "OK"
        except:
            response = "ERROR"
            pass
        return response

    #metodo que permite aplicar random Forest para obtener las importancias...
    def applyRandomForestPrediction(self, data, target):

        response = ""
        try:
            #instancia a random forest y aplicacion del mismo
            random_forest = RandomForestRegressor(max_depth=2, random_state=0, n_estimators=10, n_jobs=-1, criterion='mse')
            random_forest = random_forest.fit(data, target)

                #obtenemos las importancias
            importances = pd.DataFrame({'feature':data.columns.tolist(),'importance':np.round(random_forest.feature_importances_,3)})
            importances = importances.sort('importance',ascending=False).set_index('feature')

                #exportamos el resultado
            nameCSV = "%s%s/%s/rankingImportance_%s.csv" % (self.pathResponse, self.user, self.job, self.job)
            importances.to_csv(nameCSV)
            response = "OK"
        except:
            response = "ERROR"
            pass

        return response
    #metodo que permite obtener las clases y los atributos desde un set de datos
    def getClass_Attribute(self, dataSet, featureResponse):

        targetResponse = self.dataSet[featureResponse]
        dictData = {}

        for key in self.dataSet:
            if key != featureResponse:
                arrayFeature = []
                for i in self.dataSet[key]:
                    arrayFeature.append(i)
                dictData.update({key:arrayFeature})

        #formamos el nuevo set de datos...
        dataSetNew = pd.DataFrame(dictData)

        return dataSetNew, targetResponse

    #metodo que permite aplicar la deformacion de espacio...
    def applySpatialDeformation(self, feature, kindDataSet):

        if kindDataSet == 'CLASS':
            data, target = self.getClass_Attribute(self.dataSet, feature)

            #normalizo el set de datos...
            dataNorm = self.normalizeDataSet(data)

            #transformamos las clases en variables numericas si es necesario...
            transformData = transformDataClass.transformClass(target)
            targetTransform = transformData.transformData

            response = self.applyRandomForestClassifier(dataNorm, targetTransform)

        elif kindDataSet == 'PREDICTION':
            data, response = self.getClass_Attribute(self.dataSet, feature)

            #normalizamos el set de datos...
            dataNorm = self.normalizeDataSet(data)
            response = self.applyRandomForestPrediction(dataNorm, response)

        else:
            response = "Option not available for this type of data set"

        return response
