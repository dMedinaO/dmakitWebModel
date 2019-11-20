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
from modulesProject.utils import encodingFeatures

import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import matplotlib.cm as cm
from sklearn.metrics import silhouette_samples, silhouette_score

import pandas as pd
import json
import numpy as np

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

        dataSetInput.dropna(how='any',axis=0)#remove row with dummy values
        #evaluamos el tipo de codificacion a realizar
        encodingData = encodingFeatures.encodingFeatures(dataSetInput, self.optionEncoded)
        encodingData.evaluEncoderKind()

        dataSetNewFreq = encodingData.dataSet

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
        else:#no se realiza ninguna opcion
            self.dataSet = dataSetNewFreq

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
            dataPrev = self.dataSet
            self.dataSet["Labels"] = pd.Series(self.applyClustering.labels, index=self.dataSet.index)
            self.dataSet.to_csv(self.pathResponse+self.user+"/"+self.job+"/responseClustering.csv", index=False)

            #hacemos el conteo de los elementos por grupo para la generacion del grafico de torta asociada a la cantidad de grupos...
            self.response.update({"membersGroup":self.countMemberGroup()})

            #hacemos las figuras
            n_clusters = len(list(set(self.applyClustering.labels)))
            cluster_labels = self.applyClustering.labels
            clusterer = self.applyClustering.model
            #transformamos el conjunto de datos en matriz
            matrixData = []
            for i in range(len(dataPrev)):
                row = []
                for element in dataPrev:
                    row.append(dataPrev[element][i])
                matrixData.append(row)

            try:
                self.createPicturesForPerformance(n_clusters, matrixData, cluster_labels, clusterer, result.siluetas)
                nameFig = self.pathResponse+self.user+"/"+self.job+"/plotClusters.png"
                plt.savefig(nameFig)
                self.response.update({"figureClusters":"OK"})
            except:
                self.response.update({"figureClusters":"ERROR"})
                pass

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

    #metodo que permite hacer los graficos asociados a las siluetas y proyeccion
    def createPicturesForPerformance(self, n_clusters, X, cluster_labels, clusterer,silhouette_avg):

        # Create a subplot with 1 row and 2 columns
        fig, (ax1, ax2) = plt.subplots(1, 2)
        fig.set_size_inches(18, 7)

        # The 1st subplot is the silhouette plot
        # The silhouette coefficient can range from -1, 1 but in this example all
        # lie within [-0.1, 1]
        ax1.set_xlim([-0.1, 1])
        # The (n_clusters+1)*10 is for inserting blank space between silhouette
        # plots of individual clusters, to demarcate them clearly.
        ax1.set_ylim([0, len(X) + (n_clusters + 1) * 10])

        # Compute the silhouette scores for each sample
        sample_silhouette_values = silhouette_samples(X, cluster_labels)

        y_lower = 10
        for i in range(n_clusters):
            # Aggregate the silhouette scores for samples belonging to
            # cluster i, and sort them
            ith_cluster_silhouette_values = \
                sample_silhouette_values[cluster_labels == i]

            ith_cluster_silhouette_values.sort()

            size_cluster_i = ith_cluster_silhouette_values.shape[0]
            y_upper = y_lower + size_cluster_i

            color = cm.nipy_spectral(float(i) / n_clusters)
            ax1.fill_betweenx(np.arange(y_lower, y_upper),
                              0, ith_cluster_silhouette_values,
                              facecolor=color, edgecolor=color, alpha=0.7)

            # Label the silhouette plots with their cluster numbers at the middle
            ax1.text(-0.05, y_lower + 0.5 * size_cluster_i, str(i))

            # Compute the new y_lower for next plot
            y_lower = y_upper + 10  # 10 for the 0 samples

        ax1.set_title("The silhouette plot for the various clusters.")
        ax1.set_xlabel("The silhouette coefficient values")
        ax1.set_ylabel("Cluster label")

        # The vertical line for average silhouette score of all the values
        ax1.axvline(x=silhouette_avg, color="red", linestyle="--")

        ax1.set_yticks([])  # Clear the yaxis labels / ticks
        ax1.set_xticks([-0.1, 0, 0.2, 0.4, 0.6, 0.8, 1])

        # 2nd Plot showing the actual clusters formed
        #obtenemos los array
        x1 = []
        x2 = []
        for i in range(len(X)):
            x1.append(X[i][0])
            x2.append(X[i][1])
        colors = cm.nipy_spectral(cluster_labels.astype(float) / n_clusters)
        ax2.scatter(x1, x2, marker='.', s=30, lw=0, alpha=0.7,
                    c=colors, edgecolor='k')

        # Labeling the clusters
        centers = clusterer.cluster_centers_
        # Draw white circles at cluster centers
        ax2.scatter(centers[:, 0], centers[:, 1], marker='o',
                    c="white", alpha=1, s=200, edgecolor='k')

        for i, c in enumerate(centers):
            ax2.scatter(c[0], c[1], marker='$%d$' % i, alpha=1,
                        s=50, edgecolor='k')

        ax2.set_title("The visualization of the clustered data.")
        ax2.set_xlabel("Feature space for the 1st feature")
        ax2.set_ylabel("Feature space for the 2nd feature")

        plt.suptitle(("Silhouette analysis for clustering on sample data "
                      "with n_clusters = %d" % n_clusters),
                     fontsize=14, fontweight='bold')
