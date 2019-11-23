#metodos de la libreria utils...
from modulesProject.utils import transformDataClass
from modulesProject.utils import transformFrequence
from modulesProject.utils import ScaleNormalScore
from modulesProject.utils import ScaleMinMax
from modulesProject.utils import ScaleDataSetLog
from modulesProject.utils import ScaleLogNormalScore

#manipulacion de datos
import pandas as pd
import json
from joblib import dump, load

class useModels(object):

    def __init__(self, dataSet, docModel, pathResponse):

        self.dataSet = dataSet
        self.docModel = docModel
        self.pathResponse = pathResponse

    def scaleDataSet(self):

        #ahora transformamos el set de datos por si existen elementos discretos...
        transformDataSet = transformFrequence.frequenceData(self.dataSet)
        dataSetNewFreq = transformDataSet.dataTransform

        applyNormal = ScaleNormalScore.applyNormalScale(dataSetNewFreq)
        self.data = applyNormal.dataTransform

    def applyModel(self):

        try:
            #load model
            model = load(self.docModel)
            responseClf = model.predict(self.data)

            self.dataSet['responseModel'] = responseClf
            self.dataSet.to_csv(self.pathResponse+"responseModel.csv", index=False)
        except:
            pass
