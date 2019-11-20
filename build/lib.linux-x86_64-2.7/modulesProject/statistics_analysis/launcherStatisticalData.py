'''
script que permite poder ejecutar las diversas operaciones asociadas a los procesos de analisis estadisticos
que son requeridos durante la ejecucion del proceso...

En general, el proceso consta de:

1. Recuperar la opcion
2. Obtener las caracteristicas y sus tipos
3. Aplicar el proceso segun el tipo que corresponda
4. Generar los archivos de salida
5. Cambiar status de job con respecto a la ejecucion del proceso

'''
from modulesProject.statistics_analysis import getFeatures
from modulesProject.statistics_analysis import getDataByType
from modulesProject.statistics_analysis import processStatiticsSummary

import json
import pandas as pd

#definicion de la clase
class launcherStatisticalProcess(object):

    def __init__(self, user, job, dataSet, idDataSet, pathResponse, optionProcess):

        self.user = user
        self.job = job
        self.dataSet = dataSet
        self.idDataSet = idDataSet
        self.pathResponse = pathResponse
        self.optionProcess = int(optionProcess)#el metodo a ejecutar...

        #process feature...
        self.handlerFeature = getFeatures.processFeatureInDataSet(self.dataSet, self.idDataSet)
        self.handlerFeature.processDataValues()

    #metodo que permite evaluar la opcion a ejecutar...
    def checkExec(self):

        if self.optionProcess == 0:#show data continue
            print "show data continue"

        elif self.optionProcess == 1:#distribution data
            print "distribucion acumulada" #esto es una imagen
            print "histogramas"#esto es un key -> array data, por cada tipo de dato continuo
            print "prueba de normalidad"#esto es un grafico
            print "test de shapiro"#esto es un key -> data

        elif self.optionProcess == 2:#boxplot

            #instancia a objeto que tiene metodos que permiten obtener la dispersion de la data
            dataObject = getDataByType.dataByType(self.handlerFeature)

            dictDispersion = {}
            try:
                dictDispersion = dataObject.getValuesContinues()#obtengo la respuesta en forma de diccionario, hago una llamada a un metodo
                dictDispersion.update({"exec": "OK"})#validacion para servidor
                #print json.dumps(dictDispersion)
            except:
                dictDispersion = {"exec": "ERROR"}
                #print json.dumps(dictDispersion)

            #escribimos el archivo de respuesta
            #create file with response...
            with open(self.pathResponse+self.user+"/"+self.job+"/responseDispersion"+str(self.job)+".json", 'w') as fp:
                json.dump(dictDispersion, fp)

        elif self.optionProcess == 3:#frecuence

            try:
                dataObject = getDataByType.dataByType(self.handlerFeature)
                dictDiscrete = dataObject.getValuesDiscrete()
                dictDispersion.update({"exec": "OK"})#validacion para servidor
                print json.dumps(dictDiscrete)
            except:
                dictResponse = {"exec": "ERROR"}
                print json.dumps(dictDispersion)

        elif self.optionProcess == 4:#parallel
            print "parallel"#esto es una mezcla

        elif self.optionProcess == 5:#sploms
            print "sploms"#esto es una mezcla

        else:
            #instanciamos al objeto...
            dictResponse = {}
            statisticProcess = processStatiticsSummary.statisticsValues(self.handlerFeature)
            #try:
            matrixResponse = statisticProcess.getValuesContinues()
            dictResponse.update({"exec": "OK"})

            #genero el data frame con la informacion y lo procesamos
            header = ['Feature', 'Average', 'Standar Deviation', 'Variance', 'Max Value', 'Min Value'];
            df = pd.DataFrame(matrixResponse, columns=header)
            nameFile = self.pathResponse+self.user+"/"+self.job+"/statisticSummary_"+self.job+".csv"
            df.to_csv(nameFile, index=False)
            #except:
            #    dictResponse.update({"exec": "ERROR"})

            with open(self.pathResponse+self.user+"/"+self.job+"/responseStatisticProcess"+str(self.job)+".json", 'w') as fp:
                json.dump(dictResponse, fp)
