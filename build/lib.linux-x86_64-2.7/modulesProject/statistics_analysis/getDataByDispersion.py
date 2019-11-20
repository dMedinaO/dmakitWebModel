'''
clase con la responsabilidad de obtener los datos del tipo continuo y formar el json que se requiere para la carga de
datos en la vista...
tiene diferentes metodos con respecto al tipo escala que debe aplicarse
'''

from modulesProject.statistics_analysis import getFeatures
from modulesProject.statistics_analysis import getOutliers

import json

class dataByDispersion(object):

    def __init__(self, headerFeatures):

        self.headerFeatures = headerFeatures

    #metodo que permite obtener los datos continuos del set de datos
    def getValuesContinues(self):

        keys = []
        features = []
        outliers = []

        for feature in self.headerFeatures.listFeatures:
            if feature.kindData == "CONTINUA":
                keys.append(feature.nameData)
                features.append(feature.data)
                #obtenemos los outliers para el atributo
                outlierObject = getOutliers.getOutliers(feature.data)
                outliers.append(outlierObject.getOutliersNormalValues())

        dictResponse = {}
        dictResponse.update({"keys": keys})
        dictResponse.update({"data": features})
        dictResponse.update({"outliers": outliers})
        
        return dictResponse
