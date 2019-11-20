'''
script que permite generar la ejecucion de un algorithm de aprendizaje supervisado, contemplando la data que es recolectada desde el navegador
ejecuta el proceso y genera los resultados correspondientes con respecto a la data de interes:

matriz de confusion
curva de aprendizaje
curva precision v/s recall
curva roc
summary process con los resultados de las performance obtenidas
'''

from modulesProject.supervised_learning_predicction import execModelPrediction
from modulesProject.dataBase_module import ConnectDataBase
from modulesProject.dataBase_module import HandlerQuery

import pandas as pd
import sys

#recibimos los datos de entrada...
dataSet = pd.read_csv(sys.argv[1])
user = sys.argv[2]
job = sys.argv[3]
pathResponse = sys.argv[4]
algorithm = int(sys.argv[5])
params = sys.argv[6].split("-")
featureClass = sys.argv[7]
optionNormalize = int(sys.argv[8])

print params
#hacemos la instancia del obeto...
execProcess = execModelPrediction.execAlgorithm(dataSet, user, job, pathResponse, algorithm, params, featureClass, optionNormalize)
execProcess.execAlgorithmByOptions()#hacemos la ejecucion del algoritmo con respecto a la data que se entrego

#cambiamos el estado al job
connectDB = ConnectDataBase.ConnectDataBase()
handler = HandlerQuery.HandlerQuery()

#hacemos la consulta
query = "update job set job.statusJob = 'FINISH', job.modifiedJob= NOW() where job.idjob=%s" % job

connectDB.initConnectionDB()
handler.insertToTable(query, connectDB)
connectDB.closeConnectionDB()
