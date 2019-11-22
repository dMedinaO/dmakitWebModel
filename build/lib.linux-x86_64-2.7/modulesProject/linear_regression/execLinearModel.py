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

        self.dataSet.dropna(how='any',axis=0)#remove row with dummy values
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

    def execAlgorithmByOptions(self):

        if self.algorithm == 1:#Bayesian

            errorData = {}
            self.responseExec.update({"algorithm": "Bayesian"})
            self.responseExec.update({"Params": "Default"})

            try:
                #instancia al objeto...
                bayesianObject = bayesianRegression.bayessionRegression(self.data, self.response)
                bayesianObject.trainingMethod()

                performance = {}
                performance.update({"r_score":bayesianObject.r_score})
                performance.update({"predict_values": bayesianObject.predicctions.tolist()})
                performance.update({"real_values": bayesianObject.target.tolist()})

                #calculamos las medidas asociadas a la data de interes...
                performanceValues = performanceData.performancePrediction(self.response, bayesianObject.predicctions.tolist())
                pearsonValue = performanceValues.calculatedPearson()
                spearmanValue = performanceValues.calculatedSpearman()
                kendalltauValue = performanceValues.calculatekendalltau()

                #los agregamos al diccionario
                performance.update({"pearson":pearsonValue})
                performance.update({"spearman":spearmanValue})
                performance.update({"kendalltau":kendalltauValue})

                self.responseExec.update({"Performance": performance})
                errorData.update({"Process" : "OK"})
            except:
                errorData.update({"Process" : "ERROR"})
                pass

            self.responseExec.update({"errorExec": errorData})

            #exportamos tambien el resultado del json
            nameFile =self.pathResponse+self.user+"/"+self.job+"/responseTraining"+str(self.job)+".json"
            with open(self.pathResponse+self.user+"/"+self.job+"/responseTraining"+str(self.job)+".json", 'w') as fp:
                json.dump(self.responseExec, fp)

        if self.algorithm == 2:#Elastic Net

            errorData = {}
            self.responseExec.update({"algorithm": "Elastic Net"})
            self.responseExec.update({"Params": "Default"})

            try:
                #instancia al objeto...
                elasticNetObject = elasticNet.elasticNet(self.data, self.response)
                elasticNetObject.trainingMethod()

                performance = {}
                performance.update({"r_score":elasticNetObject.r_score})
                performance.update({"predict_values": elasticNetObject.predicctions.tolist()})
                performance.update({"real_values": elasticNetObject.target.tolist()})

                #calculamos las medidas asociadas a la data de interes...
                performanceValues = performanceData.performancePrediction(self.response, elasticNetObject.predicctions.tolist())
                pearsonValue = performanceValues.calculatedPearson()
                spearmanValue = performanceValues.calculatedSpearman()
                kendalltauValue = performanceValues.calculatekendalltau()

                #los agregamos al diccionario
                performance.update({"pearson":pearsonValue})
                performance.update({"spearman":spearmanValue})
                performance.update({"kendalltau":kendalltauValue})

                self.responseExec.update({"Performance": performance})
                errorData.update({"Process" : "OK"})
            except:
                errorData.update({"Process" : "ERROR"})
                pass

            self.responseExec.update({"errorExec": errorData})

            #exportamos tambien el resultado del json
            nameFile =self.pathResponse+self.user+"/"+self.job+"/responseTraining"+str(self.job)+".json"
            with open(self.pathResponse+self.user+"/"+self.job+"/responseTraining"+str(self.job)+".json", 'w') as fp:
                json.dump(self.responseExec, fp)

        if self.algorithm == 3:#larsLasso

            errorData = {}
            self.responseExec.update({"algorithm": "Lars Lasso"})
            self.responseExec.update({"Params": "Default"})

            try:
                #instancia al objeto...
                larsLassoObject = larsLasso.larsLasso(self.data, self.response)
                larsLassoObject.trainingMethod()

                performance = {}
                performance.update({"r_score":larsLassoObject.r_score})
                performance.update({"predict_values": larsLassoObject.predicctions.tolist()})
                performance.update({"real_values": larsLassoObject.target.tolist()})

                #calculamos las medidas asociadas a la data de interes...
                performanceValues = performanceData.performancePrediction(self.response, larsLassoObject.predicctions.tolist())
                pearsonValue = performanceValues.calculatedPearson()
                spearmanValue = performanceValues.calculatedSpearman()
                kendalltauValue = performanceValues.calculatekendalltau()

                #los agregamos al diccionario
                performance.update({"pearson":pearsonValue})
                performance.update({"spearman":spearmanValue})
                performance.update({"kendalltau":kendalltauValue})

                self.responseExec.update({"Performance": performance})
                errorData.update({"Process" : "OK"})
            except:
                errorData.update({"Process" : "ERROR"})
                pass

            self.responseExec.update({"errorExec": errorData})

            #exportamos tambien el resultado del json
            nameFile =self.pathResponse+self.user+"/"+self.job+"/responseTraining"+str(self.job)+".json"
            with open(self.pathResponse+self.user+"/"+self.job+"/responseTraining"+str(self.job)+".json", 'w') as fp:
                json.dump(self.responseExec, fp)

        if self.algorithm == 4:#Lasso

            errorData = {}
            self.responseExec.update({"algorithm": "Lasso"})
            self.responseExec.update({"Params": "Default"})

            try:
                #instancia al objeto...
                lassoObject = lassoModel.lassoModel(self.data, self.response)
                lassoObject.trainingMethod()

                performance = {}
                performance.update({"r_score":lassoObject.r_score})
                performance.update({"predict_values": lassoObject.predicctions.tolist()})
                performance.update({"real_values": lassoObject.target.tolist()})

                #calculamos las medidas asociadas a la data de interes...
                performanceValues = performanceData.performancePrediction(self.response, lassoObject.predicctions.tolist())
                pearsonValue = performanceValues.calculatedPearson()
                spearmanValue = performanceValues.calculatedSpearman()
                kendalltauValue = performanceValues.calculatekendalltau()

                #los agregamos al diccionario
                performance.update({"pearson":pearsonValue})
                performance.update({"spearman":spearmanValue})
                performance.update({"kendalltau":kendalltauValue})

                self.responseExec.update({"Performance": performance})
                errorData.update({"Process" : "OK"})
            except:
                errorData.update({"Process" : "ERROR"})
                pass

            self.responseExec.update({"errorExec": errorData})

            #exportamos tambien el resultado del json
            nameFile =self.pathResponse+self.user+"/"+self.job+"/responseTraining"+str(self.job)+".json"
            with open(self.pathResponse+self.user+"/"+self.job+"/responseTraining"+str(self.job)+".json", 'w') as fp:
                json.dump(self.responseExec, fp)

        if self.algorithm == 5:#linearRegression

            errorData = {}
            self.responseExec.update({"algorithm": "Linear Regression"})
            self.responseExec.update({"Params": "Default"})

            try:
                #instancia al objeto...
                linearRegressionObject = linearRegression.linearRegression(self.data, self.response)
                linearRegressionObject.trainingMethod()

                performance = {}
                performance.update({"r_score":linearRegressionObject.r_score})
                performance.update({"predict_values": linearRegressionObject.predicctions.tolist()})
                performance.update({"real_values": linearRegressionObject.target.tolist()})

                #calculamos las medidas asociadas a la data de interes...
                performanceValues = performanceData.performancePrediction(self.response, linearRegressionObject.predicctions.tolist())
                pearsonValue = performanceValues.calculatedPearson()
                spearmanValue = performanceValues.calculatedSpearman()
                kendalltauValue = performanceValues.calculatekendalltau()

                #los agregamos al diccionario
                performance.update({"pearson":pearsonValue})
                performance.update({"spearman":spearmanValue})
                performance.update({"kendalltau":kendalltauValue})

                self.responseExec.update({"Performance": performance})
                errorData.update({"Process" : "OK"})
            except:
                errorData.update({"Process" : "ERROR"})
                pass

            self.responseExec.update({"errorExec": errorData})

            #exportamos tambien el resultado del json
            nameFile =self.pathResponse+self.user+"/"+self.job+"/responseTraining"+str(self.job)+".json"
            with open(self.pathResponse+self.user+"/"+self.job+"/responseTraining"+str(self.job)+".json", 'w') as fp:
                json.dump(self.responseExec, fp)

        if self.algorithm == 6:#Ridge Regression

            errorData = {}
            self.responseExec.update({"algorithm": "Ridge Regression"})
            self.responseExec.update({"Params": "Default"})

            #try:
                #instancia al objeto...
            ridgeObject = ridgeRegression.ridgeRegression(self.data, self.response)
            ridgeObject.trainingMethod()

            performance = {}
            performance.update({"r_score":ridgeObject.r_score})
            performance.update({"predict_values": ridgeObject.predicctions.tolist()})
            performance.update({"real_values": ridgeObject.target.tolist()})

            #calculamos las medidas asociadas a la data de interes...
            performanceValues = performanceData.performancePrediction(self.response, ridgeObject.predicctions.tolist())
            pearsonValue = performanceValues.calculatedPearson()
            spearmanValue = performanceValues.calculatedSpearman()
            kendalltauValue = performanceValues.calculatekendalltau()

            #los agregamos al diccionario
            performance.update({"pearson":pearsonValue})
            performance.update({"spearman":spearmanValue})
            performance.update({"kendalltau":kendalltauValue})

            self.responseExec.update({"Performance": performance})
            errorData.update({"Process" : "OK"})
            #except:
            #    errorData.update({"Process" : "ERROR"})
            #    pass

            self.responseExec.update({"errorExec": errorData})

            #exportamos tambien el resultado del json
            nameFile =self.pathResponse+self.user+"/"+self.job+"/responseTraining"+str(self.job)+".json"
            with open(self.pathResponse+self.user+"/"+self.job+"/responseTraining"+str(self.job)+".json", 'w') as fp:
                json.dump(self.responseExec, fp)
