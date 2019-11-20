'''
script que permite ejecutar el servicio de clustering,
input:
    dataSet
    job
    user
    pathResponse
response:
    csv error process
    csv result process
    histogram calinski
    histogram siluetas
'''

from modulesProject.clustering_analysis import callService
from modulesProject.dataBase_module import ConnectDataBase
from modulesProject.dataBase_module import HandlerQuery

import sys
import pandas as pd

#recibimos los datos de entrada...
dataSet = pd.read_csv(sys.argv[1])
job = sys.argv[2]
user = sys.argv[3]
pathResponse = sys.argv[4]
optionNormalize = int(sys.argv[5])

#instancia al objeto
callServiceObject = callService.serviceClustering(dataSet, job, user, pathResponse, optionNormalize)
callServiceObject.execProcess()

#cambiamos el estado al job
connectDB = ConnectDataBase.ConnectDataBase()
handler = HandlerQuery.HandlerQuery()

#hacemos la consulta
query = "update job set job.statusJob = 'FINISH', job.modifiedJob= NOW() where job.idjob=%s" % job

connectDB.initConnectionDB()
handler.insertToTable(query, connectDB)
connectDB.closeConnectionDB()
