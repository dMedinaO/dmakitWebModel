'''
script que permite ejecutar el clustering el cual ha sido seleccionado via web, recibe los parametros y genera los resultados pertinentes,
ademas trabaja con formato json para poder generar la lectura desde el javascript en el lado web y hacer la carga de los elementos de una
manera mas sencilla
'''

from modulesProject.clustering_analysis import execAlgorithm
from modulesProject.dataBase_module import ConnectDataBase
from modulesProject.dataBase_module import HandlerQuery

import pandas as pd
import sys

#recibimos los datos de entrada...
dataSet = pd.read_csv(sys.argv[1])
user = sys.argv[2]
job = sys.argv[3]
pathResponse = sys.argv[4]
algorithm = sys.argv[5]
paramsValue = sys.argv[6]
optionNormalize = int(sys.argv[7])

algorithmValue = 0

if algorithm == "AgglomerativeClustering":
    algorithmValue = 3
    data = paramsValue.split('-=-')
    affinity = data[1].split('-')[0]
    linkage = data[2].split('-')[0]
    k = int(data[3])
    #affinity-=-euclidean-linkage-=-ward-k-=-2
    params = [linkage, affinity, k]

if algorithm == "Birch":
    algorithmValue = 2
    data = paramsValue.split('-=-')
    params = [int(data[1].split('-')[0])]

if algorithm == "K-Means":
    algorithmValue = 1
    data = paramsValue.split('-=-')
    params = [int(data[1].split('-')[0])]

if algorithm == "MeanShift":
    algorithmValue = 5
    params = "-"

if algorithm == "DBSCAN":
    algorithmValue = 4
    params = "-"

if algorithm == "AffinityPropagation":
    algorithmValue = 6
    params = "-"

#hacemos la instancia del obeto...
execProcess = execAlgorithm.execAlgorithm(dataSet, user, job, pathResponse, algorithmValue, params, optionNormalize)
execProcess.execAlgorithmByOptions()#hacemos la ejecucion del algoritmo con respecto a la data que se entrego

#cambiamos el estado al job
connectDB = ConnectDataBase.ConnectDataBase()
handler = HandlerQuery.HandlerQuery()

#hacemos la consulta
query = "update job set job.statusJob = 'FINISH', job.modifiedJob= NOW() where job.idjob=%s" % job

connectDB.initConnectionDB()
handler.insertToTable(query, connectDB)
connectDB.closeConnectionDB()
