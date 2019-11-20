'''
Clase que permite evaluar el resultado de un algoritmo de clustering con sus parametros de ejecucion
Recibe como entrada el set de datos y los labes asociados a la respuesta del clustering...
dentro de sus atributos presenta dos elementos asociados a los indices de evaluacion...
'''

from sklearn import metrics

class evaluationClustering(object):

    def __init__(self, dataSet, labelsResponse):

        self.dataSet = dataSet
        self.labelsResponse = labelsResponse
        try:
            self.calinski = metrics.calinski_harabaz_score(self.dataSet, self.labelsResponse)
            self.siluetas = metrics.silhouette_score(self.dataSet, self.labelsResponse, metric='euclidean')
        except:
            self.calinski = "ERROR"
            self.siluetas = "ERROR"
            pass
