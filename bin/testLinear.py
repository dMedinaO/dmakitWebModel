import pandas as pd
import sys

from modulesProject.linear_regression import execLinearModel

dataSet = pd.read_csv("/home/dmedina/Escritorio/testingLM/iris.csv")

execObject = execLinearModel.execProcess(dataSet, "1", "1", "/home/dmedina/Escritorio/testingLM/", 6, "petal.width", 1)
execObject.execAlgorithmByOptions()
