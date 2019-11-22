'''
Orden option algorithm

1. Bayesian
2. Elastic Net
3. Lars Lasso
4. Lasso
5. Linear Regression
6. Logistic
7. Multi-task-elastic
8. Multi-task-lasso
9. Ridge Regression
'''

from modulesProject.linear_regression import bayesianRegression
from modulesProject.linear_regression import elasticNet
from modulesProject.linear_regression import larsLasso
from modulesProject.linear_regression import lassoModel
from modulesProject.linear_regression import linearRegression
from modulesProject.linear_regression import logisticRegression
from modulesProject.linear_regression import multiTaskElastic
from modulesProject.linear_regression import multiTaskLasso
from modulesProject.linear_regression import ridgeRegression
from modulesProject.linear_regression import performanceData

#metodos de la libreria utils...
from modulesProject.utils import transformDataClass
from modulesProject.utils import transformFrequence
from modulesProject.utils import ScaleNormalScore
from modulesProject.utils import ScaleMinMax
from modulesProject.utils import ScaleDataSetLog
from modulesProject.utils import ScaleLogNormalScore

import pandas as pd
import json

class execProcess(object):

    def __init__(self, dataSet, user, job, pathResponse, algorithm, featureClass, optionNormalize):

        self.dataSet = dataSet
        self.user = user
        self.job = job
        self.pathResponse = pathResponse
        self.algorithm = algorithm
        self.featureClass = featureClass
        self.optionNormalize = optionNormalize
        self.createDataSet()

        self.responseExec = {}#diccionario con la respuesta para formar el json

    #metodo que permite formar el set de datos y el target con la informacion...
    def createDataSet(self):

        targetResponse = self.dataSet[self.featureClass]
        dictData = {}

        for key in self.dataSet:
            if key != self.featureClass:
                arrayFeature = []
                for i in self.dataSet[key]:
                    arrayFeature.append(i)
                dictData.update({key:arrayFeature})

        #formamos el nuevo set de datos...
        dataSetNew = pd.DataFrame(dictData)

        #ahora evaluamos si la clase tiene valores discretos o continuos y los modificamos en caso de que sean discretos
        transformData = transformDataClass.transformClass(targetResponse)
        self.response = transformData.transformData
        self.dictTransform = transformData.dictTransform

        #ahora transformamos el set de datos por si existen elementos discretos...
        transformDataSet = transformFrequence.frequenceData(dataSetNew)
        dataSetNewFreq = transformDataSet.dataTransform

        #ahora aplicamos el procesamiento segun lo expuesto
        if self.optionNormalize == 1:#normal scale
            applyNormal = ScaleNormalScore.applyNormalScale(dataSetNewFreq)
            self.data = applyNormal.dataTransform

        if self.optionNormalize == 2:#min max scaler
            applyMinMax = ScaleMinMax.applyMinMaxScaler(dataSetNewFreq)
            self.data = applyMinMax.dataTransform

        if self.optionNormalize == 3:#log scale
            applyLog = ScaleDataSetLog.applyLogScale(dataSetNewFreq)
            self.data = applyLog.dataTransform

        if self.optionNormalize == 4:#log normal scale
            applyLogNormal = ScaleLogNormalScore.applyLogNormalScale(dataSetNewFreq)
            self.data = applyLogNormal.dataTransform

        if self.optionNormalize == 0:#no normalizar
            self.data = dataSetNewFreq
        
