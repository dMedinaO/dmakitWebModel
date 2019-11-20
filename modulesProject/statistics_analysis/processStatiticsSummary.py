'''
clase con la responsabilidad de tomar los datos del tipo continuo y hacer los calculos asociados a las estadisticas
resumen de la informacion...
'''

from modulesProject.statistics_analysis import getFeatures
import numpy as np

class statisticsValues(object):

    def __init__(self, headerFeatures):

        self.headerFeatures = headerFeatures

    #metodo que permite obtener los datos continuos del set de datos
    def getValuesContinues(self):

        matrixResponse = []

        for feature in self.headerFeatures.listFeatures:
            if feature.kindData == "CONTINUA":
                matrixResponse.append(self.getStatistical(feature.data, feature.nameData))

        return matrixResponse

    #metodo que permite hacer los calculos asociados a las estadisticas de un atributo
    def getStatistical(self, data, nameData):

        mean = np.mean(data)
        std = np.std(data)
        variance = np.var(data)
        maxValue = max(data)
        minValue = min(data)

        row = [nameData, mean, std, variance, maxValue, minValue]

        return row
