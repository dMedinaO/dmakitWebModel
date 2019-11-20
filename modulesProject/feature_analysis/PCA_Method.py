# coding=utf-8
'''
Clase qye construye un pca simple, su funcion reside en calcular un pca para un set de
datos entregado.
Recibe un set de datos en formato (carac, dato) sin tomar en consideracion la clase
que clasifica.
La clase automaticamente calculara el tamaño del set de datos asi como tambien estandarizara
los datos en base a un zscore.

'''

import numpy as np
from scipy import stats
import pandas as pd
from sklearn.decomposition import IncrementalPCA

#metodos de la libreria utils...
from modulesProject.utils import transformDataClass
from modulesProject.utils import transformFrequence
from modulesProject.utils import ScaleNormalScore
from modulesProject.utils import ScaleMinMax
from modulesProject.utils import ScaleDataSetLog
from modulesProject.utils import ScaleLogNormalScore

class pca(object):
	"""docstring for pca"""

	def __init__(self, user, job, dataset, pathResponse, optionNormalize):
		self.user = user
		self.job = job
		self.pathResponse = pathResponse
		self.dataset = dataset
		self.optionNormalize = optionNormalize

	#metodo que permite normalizar el set de datos con respecto a la opcion entregada
	def normalizeDataSet(self):
		#ahora transformamos el set de datos por si existen elementos discretos...
		transformDataSet = transformFrequence.frequenceData(self.dataset)
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

	def doPCA(self):

		okidokie = ""
		try:
			X_or = self.normalizeDataSet()

				#PCA
			X = stats.zscore(X_or, axis=0)
			high, width = X.shape
			V = np.cov(X.T)
			values, vectors = np.linalg.eig(V)

			eig_pairs = [(abs(values[i]), vectors[:,i]) for i in range(len(values))]
			eig_pairs.sort()				#ordena menor a mayor
			eig_pairs.reverse()				#idem

			suma = sum(values)			#suma los valores eigen
			pct = [(i*100)/suma for i in sorted(values, reverse=True)]			#saca los pct de  peso de cada caracteristica

			aux= 0
			W = np.empty((width,0))				# se crea 1 matriz vacia
			P = np.empty((0,2))
			for i in (pct):
				W = np.hstack((W, eig_pairs[aux][1].reshape(width,1)))
				P = np.vstack((P,[aux+1, i]))
				aux+=1

			Y = X.dot(W)
				#############################
				#Archivos y cosas
			file = "%s%s/%s/TransformedPCA_%s.csv" % (self.pathResponse, self.user, self.job, self.job)
			filePCT = "%s%s/%s/PCTPCA_%s.csv" % (self.pathResponse, self.user, self.job, self.job)

			df = pd.DataFrame(Y)
			df.to_csv(file)

			dfPct= pd.DataFrame(P, columns=["Component", "Relevance"])
			dfPct.to_csv(filePCT, index=False)

			okidokie = "OK"
		except Exception as e:
			#raise e
			okidokie = "ERROR"
			pass
		return okidokie

	def incrementalPCA(self):

		okidokie = ""
		try:
			X_or = self.normalizeDataSet()

			high, width = X_or.shape
			trans = IncrementalPCA(n_components=width)
			Y = trans.fit_transform(X_or)

			#CSV
			file = "%s%s/%s/IncrementalPCA_%s.csv" % (self.pathResponse, self.user, self.job, self.job)
			df = pd.DataFrame(Y)
			df.to_csv(file)

			#varianza explicada
			explaindVariance = trans.explained_variance_ratio_

			matrix = []
			index=1
			for element in explaindVariance:
				component = "PCA "+str(index)
				row = [component, element*100]
				matrix.append(row)
				index+=1

			fileExport = "%s%s/%s/varianzaExplained_%s.csv" % (self.pathResponse, self.user, self.job, self.job)
			dfVar = pd.DataFrame(matrix, columns=["Component", "Variance"])
			dfVar.to_csv(fileExport, index=False)

			okidokie = "OK"

		except Exception as e:
			#raise e
			okidokie = "ERROR"
			pass

		return okidokie
