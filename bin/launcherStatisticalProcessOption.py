'''
script que permite hacer los procesos relacionados al manejo estadistico
'''

from modulesProject.statistics_analysis import launcherStatisticalData
from modulesProject.dataBase_module import ConnectDataBase
from modulesProject.dataBase_module import HandlerQuery

import sys

user = sys.argv[1]#test with 1
job = sys.argv[2]#test with 1
dataSet = sys.argv[3]#test with testingFeature.csv
idDataSet = sys.argv[2] #test with 1
pathResponse = sys.argv[4] #cualquiera que desees
optionProcess = sys.argv[5] # las opciones de job posibles, ver checkExec de launcherStatisticalData

#instancia al objeto...
launcherStatisticalDataObject = launcherStatisticalData.launcherStatisticalProcess(user, job, dataSet, idDataSet, pathResponse, optionProcess)
launcherStatisticalDataObject.checkExec()

#cambiamos el estado al job
connectDB = ConnectDataBase.ConnectDataBase()
handler = HandlerQuery.HandlerQuery()

#hacemos la consulta
query = "update job set job.statusJob = 'FINISH', job.modifiedJob= NOW() where job.idjob=%s" % job

connectDB.initConnectionDB()
handler.insertToTable(query, connectDB)
connectDB.closeConnectionDB()
