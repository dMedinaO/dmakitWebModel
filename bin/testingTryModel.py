from modulesProject.models_export import useModels
import pandas as pd

dataSet = pd.read_csv("/home/dmedina/Escritorio/iris.csv")
model = "/var/www/html/dmakitWeb/dataStorage/1574208448/1574544282/modelExport1574544282.joblib"
pathResponse = "/home/dmedina/Escritorio/"
tryModel = useModels.useModels(dataSet, model, pathResponse)
tryModel.scaleDataSet()
tryModel.applyModel()
