import numpy as np
from scipy import stats
import pandas as pd
from sklearn.decomposition import KernelPCA

#metodos de la libreria utils...
from modulesProject.utils import transformDataClass
from modulesProject.utils import transformFrequence
from modulesProject.utils import ScaleNormalScore
from modulesProject.utils import ScaleMinMax
from modulesProject.utils import ScaleDataSetLog
from modulesProject.utils import ScaleLogNormalScore

class kpca(object):

	def __init__(self, user, job, dataSet, pathResponse, optionNormalize):

		self.user = user
		self.job = job
		self.pathResponse = pathResponse
		self.dataSet = dataSet
		self.optionNormalize = optionNormalize
	#metodo que permite normalizar el set de datos con respecto a la opcion entregada
	def normalizeDataSet(self):
		#ahora transformamos el set de datos por si existen elementos discretos...
		transformDataSet = transformFrequence.frequenceData(self.dataSet)
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

	def doKPCA(self):
		#Mykernel puede ser:
		#linear
		#poly
		#rbf
		#sigmoid
		#cosine
		#precomputed
		okiedoki=""
		try:

			X_or = self.normalizeDataSet()

			high, width = X_or.shape

			transformer = KernelPCA(n_components=width, kernel='linear')
			Y = transformer.fit_transform(X_or)

				#CSV
			file = "%s%s/%s/KernelPCA_%s.csv" % (self.pathResponse, self.user, self.job, self.job)

			df = pd.DataFrame(Y)
			df.to_csv(file)

			okiedoki = "OK"

		except Exception as e:
			#raise e
			okiedoki = "ERROR"
			pass
		return okiedoki
